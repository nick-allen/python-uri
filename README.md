# python-uri
Better URI handling

[![Build Status](https://travis-ci.org/nick-allen/python-uri.svg?branch=master)](https://travis-ci.org/nick-allen/python-uri)
[![Coverage Status](https://coveralls.io/repos/github/nick-allen/python-uri/badge.svg?branch=master)](https://coveralls.io/github/nick-allen/python-uri?branch=master)

## Install

`pip install python-uri`

## Usage

Raw URI string parsing:

```python
from uri import URI

uri = URI('http://localhost:80/path/to/file?query=value#/fragment/path')

uri.scheme == 'http'
uri.host == 'localhost'
uri.port == 80
uri.path == '/path/to/file'
uri.query == 'query=value'
uri.fragment == '/fragment/path'
```

Composition by parts

```python
from uri import URI

uri = URI(scheme='ftp', host='localhost', port=8000, query='key=value')

str(uri) == 'ftp://localhost:8000?key=value'
```

Modification and comparision

```python
from uri import URI

uri1 = URI('https://example.com:80')
uri2 = URI('https://example.com:443/new/path')

uri1 != uri2

uri1.port = 443
uri1.path = '/new/path'

str(uri1) == 'https://example.com:443/new/path'

uri1 == uri2
```


