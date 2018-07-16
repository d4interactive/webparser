A web content parser using Python lxml


Compatibility
-------------

The library is compatible with Python3. Python2 is currently not supported.


Usage
-----

Convert to Document

Accept the html content document, convert it to the doc element, if we want to convert relative links to absolute links, 
we pass the domain url to the absolute links.

```
from webparser.parser import convert_to_doc

doc = convert_to_doc('HTML content', 'http://yourwebsite.com')

```

