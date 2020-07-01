from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
import requests
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
option.add_argument("headless")

def get_src(link):

    browser = webdriver.Chrome(options=option)
    browser.get(link)
    # Wait 20 seconds for page to load
    timeout = 20
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='btn download-btn player']")))
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()

    titles_href = browser.find_elements_by_xpath("//a[@class='btn download-btn player']")[0]

    titles_href.click()
    time.sleep(3)

    titles_href = browser.find_elements_by_xpath("//a[@class='btn download-btn']")[0]
    titles_href.click()
    time.sleep(6)
    titles_href = browser.find_elements_by_xpath("//a[@class='btn download-btn']")[0]
    vid_src = titles_href.get_attribute('href')
    browser.close()
    browser.quit()
    return (vid_src)

def get_link(link):

    browser = webdriver.Chrome(options=option)
    browser.get(link)
    # Wait 20 seconds for page to load
    timeout = 20
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='push_button blue']")))
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()
    time.sleep(1)
    titles_href = browser.find_elements_by_xpath("//a[@class='push_button blue']")[0]
    vid_src = titles_href.get_attribute('href')
    print (vid_src)
    browser.close()
    browser.quit()
    vid_src = get_src(vid_src)
    return (vid_src)

def get_shows(url):
    content = requests.get(url)

    soup = BeautifulSoup(content.text, 'html.parser')

    shows = soup.find_all("div", {"class": "block-right-home-inside"})

    titles = []
    thumbnails_src = []
    hrefs = []

    for show in shows:
        title = show.find("div", {"class": "block-right-home-inside-text"}).get_text()
        img = show.find("div", {"class": "img33x50"}).img.get('src')
        link = show.find("div", {"class": "block-right-home-inside-text"}).a.get('href')
        hrefs.append(link)
        titles.append(title)
        thumbnails_src.append(img)

    return (titles, hrefs, thumbnails_src)

def search_shows(url, term):
    term = list(term)
    search_term = ""
    for i in range(len(term)):
        if term[i]==" ":
            term[i]="+"
        search_term+=term[i]
    url += search_term
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    shows = soup.find_all("tr")
    titles = []
    hrefs = []
    for show in shows:
        title = show.td.find("a", href=True).get_text()
        href = show.td.find("a", href=True).get('href')
        if href[0] != 'h':
            href = "https://wtv.unblockit.id" + href
        titles.append(title)
        hrefs.append(href)
    return (titles, hrefs)

def get_seasons(url):
    content = requests.get(url)

    soup = BeautifulSoup(content.text, 'html.parser')

    seasons = soup.find_all("h2", {"class": "lists"})

    hrefs = []

    for season in seasons:
        href = season.a.get('href')
        hrefs.append(href)

    return (hrefs)

def get_eps(url):
    content = requests.get(url)

    soup = BeautifulSoup(content.text, 'html.parser')

    episodes = soup.find_all("li", {"itemprop": "episode"})
    hrefs = []

    for ep in episodes:
        href = ep.a.get('href')
        sub_content = requests.get(href)
        sub_soup = BeautifulSoup(sub_content.text, 'html.parser')
        try:
            href = sub_soup.find_all("a", {"title": "mixdrop.co"})[0].get('href')
        except Exception:
            pass
        hrefs.append(href)
    return (hrefs)