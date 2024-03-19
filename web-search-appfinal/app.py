from flask import Flask, request, render_template
import csv
from webcrawler import WebCrawler
from indexer import Indexer
from ranker import Ranker

app = Flask(__name__)
crawler = None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    global crawler
    keyword = request.args.get('keyword')
    url = request.args.get('url')
    if keyword and url:
        if crawler is None:
            crawler = WebCrawler()
        crawler.crawl(url)
        indexer = Indexer()
        indexer.index = crawler.index
        results = indexer.search(keyword)
        if results:
            ranker = Ranker()
            ranked_results = ranker.rank_results(results, indexer.index, keyword)
            return render_template('results.html', results=ranked_results)
        else:
            return render_template('results.html', message='Result not found for the given keyword and URL.')
    else:
        return render_template('results.html', error='Both keyword and URL parameters are required.'), 400

@app.route('/csvdata', methods=['GET'])
def csv_data():
    # Load data from CSV
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return render_template('csvdata.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
