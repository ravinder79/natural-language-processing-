from requests import get
from bs4 import BeautifulSoup
import os
import re



def get_blog_articles(urls):
    d ={}
    for url in urls:
        d.update(acquire_codeup_blog(url))
    return d



def acquire_codeup_blog(url):
    d1 ={}
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article = soup.find('div', class_='jupiterx-post-content')
    d1[soup.title.string] = article.text

    return d1


def get_news_articles(urls):
    list = []
    for url in urls:
        list.append(get_news_items(url))
    return list

def get_news_items(url):
    url = url
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    bodies = soup.find_all(attrs={"itemprop": "articleBody"})
    category = re.search(r'([^\/]+$)', url)[0]
    
    #get list of headlines, content and categories
    for i in range(0, len(headlines)):
        headlines[i] = headlines[i].text
    
    for i in range(0, len(bodies)):
        bodies[i] = bodies[i].text
    
    category = [category]* len(headlines)
    
    #create a list of dictionaries:
    list = []
    for i in range (0, len(headlines)):
        list.append({'title': headlines[i], 'content': bodies[i], 'category': category[i]})
    return list