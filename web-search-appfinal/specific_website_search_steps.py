from search_engine import SimpleCrawler, SimpleIndexer, SearchEngine
'''
Scenario: Entering a website URL

Given I have opened the app

When I enter the URL of a website


Then the app should be ready to search within that website

'''

from behave import given, when, then

@given('I have opened the app')

def step_open_app(context):
    #Instantiate the concrete implementations
    my_crawler =SimpleCrawler()
    my_indexer =SimpleIndexer()

    #Instantiate the SearchEngine with the dependencies
    context.app =SearchEngine (crawler=my_crawler, indexer=my_indexer)

@when('I enter the URL of a website')

def step_enter_website_url(context):
    context.app.crawler.crawl('https://crawler-test.com/') # This is a URL

@then('the app should be ready to search within that website')

def step_app_ready_to_search(context): 
    context.app.perform_search('test') # This is a query


# '''
# Scenario: Performing a search query
# Given I have specified a website to search
# When I enter a search query
# Then the app should return results from the specified website
# '''

# @given('I have specified a website to search')
# def step_specify_website(context):
#     pass


# @when('I enter a search query')
# def step_enter_search_query(context):
#     pass

# @then('the app should return results from the specified website')
    
