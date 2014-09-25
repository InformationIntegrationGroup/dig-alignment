import time
import hashlib

def splitNameField(field):
    if field=="N":
        return []
    if field.startswith("{"):
        field = field[1:]
    if field.endswith("}"):
        field = field[:-1]
    return ",".join([n.strip('"') for n in field.split(",")])

countryCodes = [1, 20, 212, 213, 216, 218, 220, 221, 222, 223, 224,
                225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235,
                236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246,
                247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
                258, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269,
                27, 290, 291, 297, 298, 299, 30, 31, 32, 33, 34, 350,
                351, 352, 353, 354, 355, 356, 357, 358, 36, 370, 371,
                372, 373, 374, 375, 376, 377, 378, 380, 381, 382, 385,
                386, 387, 389, 39, 40, 41, 420, 421, 423, 43, 44, 45,
                46, 47, 48, 49, 500, 501, 502, 503, 504, 505, 506,
                507, 508, 509, 51, 52, 53, 54, 55, 56, 57, 58, 590,
                591, 592, 593, 594, 595, 596, 597, 598, 599, 60, 61,
                62, 63, 64, 65, 66, 670, 672, 673, 674, 675, 676, 677,
                678, 679, 680, 681, 682, 683, 685, 686, 687, 688, 689,
                690, 691, 692, 699, 7, 81, 82, 84, 850, 852, 853, 855,
                856, 86, 872, 880, 886, 90, 91, 92, 93, 94, 95, 960,
                961, 962, 963, 964, 965, 966, 967, 968, 970, 971, 972,
                973, 974, 975, 976, 977, 98, 992, 993, 994, 995, 996,
                998]

testPhoneFields = ["{+12607040695}",
                    "{+41793666000}",
                    "N",
                    "{+12022719775,+19012976450}"]

def splitPhoneField(field):
    if field=="N":
        return None
    if field.startswith("{"):
        field = field[1:]
    if field.endswith("}"):
        field = field[:-1]
    def stripCountryCode(p):
        if not p:
            return None
        if p.startswith("+"):
            for code in countryCodes:
                scode = str(code)
                lcode = len(scode)
                if p[1:1+lcode] == scode:
                    return p[1+lcode:]
        return p
    return ",".join([stripCountryCode(p) for p in field.split(",")])

def splitLocationField(field):
    if field=="N":
        return []
    if field.startswith("{"):
        field = field[1:]
    if field.endswith("}"):
        field = field[:-1]
    return ",".join([l.strip('"') for l in field.split(",")])

def modtimeToEpochTime(modtime):
    # 2014-04-23 22:23:47
    pattern = '%Y-%m-%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(modtime, pattern)))
    return epoch

def sha1(x):
    return hashlib.sha1(x).hexdigest()

def generateUri(modtime, url):
    return "crawl/%s-%s" % (sha1(url), modtimeToEpochTime(modtime))
