from collections import defaultdict

class Indexer:
    def __init__(self):
        self.index = defaultdict(list)

    def index_page(self, url, text):
        self.index[url] = text

    def search(self, keyword):
        results = []
        for url, text in self.index.items():
            if keyword.lower() in text.lower():
                results.append(url)
        return results[:10]
