'''
Created on Mar 26, 2018

@author: Q
'''

from bs4 import BeautifulSoup
import re 
import requests

def get_Soup(url):
    response = requests.get(url)
    html = response.content
    return BeautifulSoup(html, "html.parser")

def list_mmh_games():
    soup = get_Soup("http://makemehost.com/games.php")

    tomato = soup.find_all('tr')[1:20]
    out = []
    for e in tomato:
        out.append(e.select('td')[3].__getattribute__('text'))
    return out

def check_mmh(gameName, conditionalText):
    for e in list_mmh_games():
        #To-Do: add conditional text
        regex = re.compile()
        if regex.search(gameName):
            return True
    return False

def set_alarm():
    #To-Do: Alarm
    return

def check_ent(gameName, conditionalText):
    #https://stackoverflow.com/questions/25062365/python-parsing-html-table-generated-by-javascript
    #To-Dp: Use Selenium to scrape the .js table
    
    return

def main():

    return 

main()