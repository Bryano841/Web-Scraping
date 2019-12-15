import numpy as np
import pandas as pd
from splinter import Browser
from selenium import webdriver
from bs4 import BeautifulSoup as bs4
import requests as req
import time

def initBrowser():
   
    return Browser("chrome", headless = False)
    time.sleep(10)

def closeBrowser(browser):
    """ Function: Closes splinter Browser object
        Parameters: (1) Browser object instance
        Returns: None """
    browser.quit()
    time.sleep(10)

def scrap():
   
    marsdata={}
    marsdata["news_data"] = marsNewsData()
    marsdata["featured_image_url"] = marsFeaturedImageURL()
    marsdata["mars_weather"] = marsWeather()
    marsdata["mars_hemispheres"] = marsHemisphereImageURLs()
    marsdata["mars_facts"] = marsFacts()
    return mars_data

def marsNewsData():
 

    news_data = {}
    paragraph = []

    base_url = "https://mars.nasa.gov/"
    news_url = "https://mars.nasa.gov/news/"
    response1 = req.get(news_url)
    time.sleep(5)

    soup = bs(response1.text, 'html.parser')
    soupdiv= soup.find(class_="slide")
    nasa_news = soupdiv.find_all('a')
    nasa_title = nasa_news[1].get_text().strip()
    soup_p = soupdiv.find_all('a', href = True)
    soup_url = soup_p[0]['href']
    paragraph_url = base_url + soup_url
    response2 = req.get(paragraph_url)
    time.sleep(5)

    psoup = bs(response2.text, "html.parser")
    wwparagraphs = psoup.find(class_ = 'article_teaser_body')
    paragraphs = wwparagraphs.find_all('p')

    for paragraph in paragraphs:
        clean_paragraph = paragraph.get_text().strip()
        paragraph.append(clean_paragraph)

        news_data["news_title"] = news_title
        news_data["paragraph_text_1"] = paragraph[0]
        news_data["paragraph_text_2"] = paragraph[1]

        return news_data

        def marsFeaturedImageURL():
            browser = initBrowser()

            jpl_fullsize_url = 'https://photojournal.jpl.nasa.gov/jpeg/'
            jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
            browser.visit(jpl_url)
            time.sleep(5)
            jpl_html = browser.html
            jpl_soup = bs(jpl_html, 'html.parser')
            time.sleep(5)

            featured_image_list = []

            for image in jpl_soup.find_all('div', class_="img"):
                featured_image_list.append(image.find('img').get('src'))

            featured_image = featured_image_list[0]
            temp_list1 = featured_image.split('-')
            temp_list2 = temp_list[0].split('/')
            featured_image_url = jpl_fullsize_url + temp_list2[-1] + '.jpg'

            closeBrowser(browser)

            return featured_image_url

def marsWeather():
    browser = initBrowser()

    tweeturl = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(tweeturl)
    time.sleep(5)

    tweethtml = browser.html
    tweetsoup = bs(tweethtml, 'html.parser')
    time.sleep(5)

    weatherinfo = []
    for weatherinfo in tweetsoup.find_all('p', class_= "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
        weatherinfo.append(weatherinfo.text.strip())

    for value in reversed (weatherinfo):
        if value [:3]=='Sol':
            mars_weather = value

    closeBrowser(browser)

    return mars_weather

def marsFacts():
    facts_url = 'https://space-facts.com/mars/'
    factlist = pd.read_html(facts_url)
    time.sleep(5)
    factsdf = factlist[0]
    factstable = factsdf.to_html(header=False, index=False)

    return factstable

def marsHemisphereImageURLs():
    browser = initBrowser()
    usgsurl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgsurl)
    time.sleep(5)

    usgshtml = browser.html
    usgssoup = bs(usgshtml, 'html.parser')
    time.sleep(5)

    hemisphere_image_urls = []

    products = usgssoup.find('div', class_='result-list')
    time.sleep(5)

    for hemisphere in hemispheres:
        title = hemisphere.find('div', class_='description')

        titletext = title.a.text
        titletext = titletext.replace(' Enhanced', '')
        browser.click_link_by_partial_text(titletext)

        usgshtml = browser.html
        usgssoup = bs(usgshtml, 'html.parser')

        image = usgssoup.find('div', class_='downloads').find('ul').find('li')
        img_url = image.a['href']

        hemisphere_image_urls.append({'title': titletext, 'img_url': img_url})

        browser.click_link_by_partial_text('Back')

    closeBrowser(browser)

    return hemisphere_image_urls
if __name__=="__main__":
    print(scrape())            