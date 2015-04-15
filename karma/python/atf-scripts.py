# Scripts for modeling ATF data.

def atf_article_uri(url, post_id):
    return get_url_hash(url)+"/"+post_id


test_date = "Wed Feb 11, 2015 10:31 am"

def atf_date_created(date):
    """Put the date in ISO format"""
    return iso8601date(date, "%a %b %d, %Y %I:%M %p")

def atf_joined_date(date):
    """Put the date in ISO format"""
    return iso8601date(date, "%a %b %d, %Y %I:%M %p")

from HTMLParser import HTMLParser

class HTMLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def handle_starttag(self, tag, attrs):
        self.fed.append(" ")
    def handle_endtag(self, tag):
        self.fed.append(" ")
    def handle_startendtag(self, tag, attrs):
        self.fed.append(" ")
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = HTMLStripper()
    s.feed(html)
    return s.get_data()

test_signature = "<span style=\"font-style: italic\">Precision Combat Arms<br />1710 E Trent, Unit 1<br />Spokane, WA 99202<br />509-535-0655<br />M-F 9-5</span></div>"

def signature_clean(text):
    """Strip HTML"""
    return strip_tags(text).strip()


def atf_fc_uri(article_uri):
    """URI of feature collection"""
    return article_uri+"/featurecollection"


def atf_parse_city_state(city_state):
    if "," in city_state:
        return [x.strip() for x in city_state.split(",")]
    else:
        return [city_state, ""]

import re

WEAPONS_PHRASES = ['gun',
                   'rifle',
                   'missile',
                   'mark',
                   'tank',
                   'mk',
                   'torpedo',
                   'naval',
                   'vehicle',
                   'remington',
                   'smith',
                   'pistol',
                   'wesson',
                   'grenade',
                   'howitzer',
                   'mine',
                   'mortar',
                   'colt',
                   'submachine',
                   'canon',
                   'cannon',
                   'mod\xe8le',
                   'ruger',
                   'koch',
                   'heckler',
                   'weapon',
                   'bomb',
                   'armoured',
                   'carbine',
                   'beretta',
                   'missile',
                   'armored',
                   'winchester',
                   'springfield',
                   'revolver',
                   'launcher',
                   'caliber',
                   'assault',
                   'sig',
                   '45',
                   'ordnance',
                   'zastava',
                   'rocket',
                   'anti-tank',
                   'walther',
                   'combat',
                   'benelli',
                   'sniper',
                   'series',
                   'mle',
                   'browning',
                   'schneider',
                   'm1',
                   'carrier',
                   'kanone',
                   'defense',
                   'artillery',
                   'tank',
                   'steyr',
                   'rml',
                   'mowag',
                   'wz.',
                   'mauser',
                   'm3',
                   'vehicle',
                   'vickers',
                   'taurus',
                   'tactical',
                   'sword',
                   'infantry',
                   'panzer',
                   'marlin',
                   'hotchkiss',
                   'fk',
                   'barrett',
                   'weapon',
                   'sauer',
                   'modello',
                   'explosive',
                   'aircraft',
                   'tractor',
                   'skoda',
                   'self-propelled',
                   'rheinmetall',
                   'reconnaissance',
                   'minenwerfer',
                   'm4',
                   'kel-tec',
                   'fighting',
                   'daewoo',
                   'bofors',
                   'rocket',
                   'sd.kfz.',
                   'scout',
                   'pindad',
                   'knife',
                   'carriage',
                   'bliss-leavitt',
                   'arms',
                   'advanced',
                   'storm',
                   'sdkfz',
                   'savage',
                   'saurer',
                   'renault',
                   'nuclear',
                   'missile',
                   'bayonet',
                   'arsenal',
                   'sword',
                   'armoured',
                   'weapons',
                   'weapon-stub',
                   'war',
                   'strike',
                   'spartan',
                   'oerlikon',
                   'obusier',
                   'nebelwerfer',
                   'm\xF6rser',
                   'munition',
                   'military',
                   'marksman',
                   'krupp',
                   'flamethrower',
                   'feldhaubitze',
                   'eagle',
                   'crosman',
                   'cobra',
                   'carrier',
                   'bushmaster',
                   'breda',
                   'army',
                   'amphibious',
                   'afv',
                   'wolf',
                   'vektor',
                   'vehicle',
                   'turret',
                   'tanks',
                   'stridsvagn',
                   'soltam',
                   'siege',
                   'shotgun',
                   'sg',
                   'schwerer',
                   'schwere',
                   'pdw',
                   'panhard',
                   'nambu',
                   'mortier',
                   'magnum',
                   'm8',
                   'm60',
                   'm1918',
                   'm1895',
                   'luftminenwerfer',
                   'leopard',
                   'kbk',
                   'kanon',
                   'imbel',
                   'humber',
                   'hi-point',
                   'guns',
                   'gryazev-shipunov',
                   'explosives',
                   'denel',
                   'battle',
                   'axe',
                   'automag',
                   'attack',
                   'armory',
                   'armalite',
                   'alfa',
                   'pistol',
                   'bomb',
                   'artillery']


def isInt(s):
    try:
        int(s)
        return True
    except:
        pass
    return False

WEAPONS_PHRASES = [w for w in WEAPONS_PHRASES if not isInt(w)]
# restore a few numbers
WEAPONS_PHRASES = WEAPONS_PHRASES + ["45", ".45", "38", "50", "3006", ".22"]
# add a few missing popular items
WEAPONS_PHRASES = WEAPONS_PHRASES + ['uzi', 'ammo', 'ammunition']
WEAPONS_PATTERNS = [re.compile(r"""\b%s\b""" % ph, re.IGNORECASE) for ph in WEAPONS_PHRASES]

test_text = """New In Box Walther UZI .22LR RIFLE 20+1 $349.99"""

def weapons_words(text, patterns=WEAPONS_PATTERNS, phrases=WEAPONS_PHRASES):
    matches = set()
    for (pattern, phrase) in zip(patterns, phrases):
        for match in re.finditer(pattern, text):
            matches.add(phrase)
    matches = list(matches)
    matches.sort()
    return matches

# print weapons_words(test_text)