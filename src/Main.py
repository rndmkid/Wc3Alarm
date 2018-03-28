'''
Created on Mar 26, 2018

@author: Q
'''

from bs4 import BeautifulSoup
import re 
import requests
from selenium import webdriver
from pandas.io.html import read_html



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
    for e in out:
        if not e:
            out = list(filter(lambda x:x is not "", out))
    return out

def check_games(gameNames):
    games = list_mmh_games() + list_ent_games(1)
    out = ""
    for e in games:
        reg = regex_compile(gameNames)
        regex = re.compile(reg, re.I)
        if regex.search(e):
            out = e
    return out

def regex_compile(gameNames):
    out = "^"
    for e in gameNames:
        out += "(?=.*" + e + ")"
    out += ".*$"
    return out

def set_alarm():
    #To-Do: Alarm
    return

def sound_alarm():
    #To-Do: Sound Alarm
    return

def list_ent_games(mode):
    #Parse https://entgaming.net/forum/games_all_fast.php
    soup = get_Soup("https://entgaming.net/forum/games_all_fast.php")
    rawText = soup.__getattribute__('text')
    gamesListRaw = re.split("\n|\|", rawText)
    
    out = []
    if mode == 1:
        i = len(gamesListRaw) - 2
        while i > 0:
            if gamesListRaw[i - 1] == '1' and not re.match("\[ENT\].*", gamesListRaw[i]):
                out.append(gamesListRaw[i])
            i -= 6
    return out


def main():
    
    print(check_games(["heroes", "empires"]))
     
    
    return

main()