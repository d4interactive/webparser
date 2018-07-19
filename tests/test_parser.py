import unittest

import lxml
import requests

from webparser.parser import convert_to_doc, FeedParser, fuzzy_url_search, has_rss_feed
from webparser.utils import root_path


class TestParser(unittest.TestCase):
    def setUp(self):
        self.english_text = None
        with open(root_path() + "/tests/data/medium_botify.txt", "r") as w:
            self.english_text = w.read()

        self.chinese_text = None
        with open(root_path() + "/tests/data/chinese_text_parsing.txt", "r") as w:
            self.chinese_text = w.read()

        self.url = 'https://medium.com/botify-labs/no-fuss-no-ego-code-reviews-done-right-de69b5cf76e3'

    def test_convert_to_doc_with_text(self):
        res = convert_to_doc(self.english_text)

        if (res.text_content()):
            assert True
        if (isinstance(res, lxml.html.HtmlElement)):
            assert True

    def test_convert_to_doc_with_requests(self):
        res = requests.get(self.url)
        text = convert_to_doc(res.content)
        if text.text_content():
            assert True

    def test_chinese_text(self):
        text = convert_to_doc(self.chinese_text)
        if text.text_content():
            assert True


class TestFeedParser(unittest.TestCase):
    def setUp(self):
        self.viralnova = 'https://viralnova.com/feed'
        self.techcrunch = 'https://techcrunch.com/feed'
        self.feed_url_exists = 'https://techcrunch.com'
        self.no_feed_exists_url = 'https://contentstudio.io'

    def test_viralnova(self):
        feed = FeedParser(self.viralnova)
        res = feed.parse()
        if len(res['feeds']) > 5:
            assert True

    def test_techcrunch(self):
        feed = FeedParser(self.techcrunch)
        res = feed.parse()
        if len(res['feeds']) > 5:
            assert True

    def test_fuzzy_url_search(self):
        status = fuzzy_url_search(self.feed_url_exists, [])
        if (len(status) > 0):
            assert True

        status = fuzzy_url_search(self.no_feed_exists_url, [])
        if len(status) == 0:
            assert True

    def test_has_rss_feed(self):
        res = requests.get(self.feed_url_exists)
        has_feed= has_rss_feed(res.content, self.feed_url_exists)
        print(has_feed)
