select distinct mid(url,27,1+locate('/',url,27)-28) from ads where sources_id=17;