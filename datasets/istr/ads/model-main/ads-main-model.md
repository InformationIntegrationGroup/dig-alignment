## ads-sample.json

### PyTransforms
#### _cache_uri_
From column: _url_
>``` python
return getCacheBaseUrl()+"page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/processed"
```

#### _snapshot_uri_
From column: _cache_uri_
>``` python
return getCacheBaseUrl()+"page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/raw"
```

#### _posttime_iso_
From column: _posttime_
>``` python
return iso8601date(getValue("posttime"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _cache_uri_ | `uri` | `schema:WebPage1`|
| _posttime_iso_ | `schema:dateCreated` | `schema:WebPage1`|
| _snapshot_uri_ | `memex:snapshotUri` | `schema:WebPage1`|
| _text_ | `schema:text` | `schema:WebPageElement2`|
| _title_ | `schema:text` | `schema:WebPageElement1`|
| _url_ | `schema:url` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `memex:hasBodyPart` | `schema:WebPageElement2`|
| `schema:WebPage1` | `memex:hasTitlePart` | `schema:WebPageElement1`|