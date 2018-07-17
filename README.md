A web content parser using Python lxml


Compatibility
-------------

The library is compatible with Python3. Python2 is currently not supported.


Usage
-----

Convert to Document

Accept the html content document, convert it to the doc element, if we want to convert relative links to absolute links, 
we pass the domain url to the absolute links.

**convert_to_doc()**

```
from webparser.parser import convert_to_doc

doc = convert_to_doc('HTML content', 'http://yourwebsite.com')

```

**class FeedParser()**

```
from webparser.parser import FeedParser

feed = FeedParser() # optional feed URL can be provided.
parsed_links = feed.parse(url='http://viralnova.com/feed') # url will override constructor feed URL. 
```

**has_rss_feed()**

Check if the website/URL has a RSS feed link present.

 - Check the document with Mimetype of links using XPATH.
 - Fuzzy URL search e.g /feed at the end of the website URL. (Attempted if no links for the RSS URL found)

```
from webparser.parser import has_rss_feed
rss_links = has_rss_feed(doc=html_content, url=website_url)
```

