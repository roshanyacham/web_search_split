from abc import ABC, abstractmethod

class Crawler(ABC):
    @abstractmethod
    def crawl(self, url):
        pass
    
class Indexer(ABC):
    @abstractmethod
    def index_document(self, doc_id, text):
        pass

    @abstractmethod
    def search(self, query):
        pass  # Implement search logic here

class SimpleCrawler(Crawler):

    def crawl(self, url):
        # Implementation details for crawling a webpage
        pass

    def get_html(self, url):
        # Implementation details for fetching webpage content
        pass

class SimpleIndexer(Indexer):  # Inherits from the abstract Indexer class

    def index_document(self, doc_id, text):
        # Implementation details for indexing document text
        pass

    def search(self, query):
        # Implementation details for searching indexed documents
        pass

class SearchEngine:

    def __init__(self, crawler: Crawler, indexer: Indexer):
        self.crawler = crawler
        self.indexer = indexer

    def perform_search(self, query):
        # Use the crawler and indexer to perform search
        pass
