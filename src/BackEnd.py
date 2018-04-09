'''
Created on Mar 26, 2018

@author: Q
'''

from bs4 import BeautifulSoup
import re 
import requests
from selenium import webdriver
from pandas.io.html import read_html
import winsound
import time
from pyperclip import copy
#from MainGUI import GUI

        
def __get_Soup(url):
    response = requests.get(url)
    html = response.content
    return BeautifulSoup(html, "html.parser")

def __list_mmh_games():
    soup = __get_Soup("http://makemehost.com/games.php")

    tomato = soup.find_all('tr')[1:20]
    out = []
    for e in tomato:
        out.append(e.select('td')[3].__getattribute__('text'))
    for e in out:
        if not e:
            out = list(filter(lambda x:x is not "", out))
    return out

def __regex_compile(gameNames):
    out = "^"
    for e in gameNames:
        out += "(?=.*" + e + ")"
    out += ".*$"
    return out


def __list_ent_games(mode):
    #Parse https://entgaming.net/forum/games_all_fast.php
    soup = __get_Soup("https://entgaming.net/forum/games_all_fast.php")
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

def __check_game(gameNames):
    games = __list_mmh_games() + __list_ent_games(1)
    out = ""
    for e in games:
        reg = __regex_compile(gameNames)
        regex = re.compile(reg, re.I)
        if regex.search(e):
            out = e
    return out

def __check_games(gameList):
    for e in gameList:
        if __check_game(e):
            return __check_game(e)

def __sound_alarm():
    winsound.Beep(440, 1000)
    return

#Public Methods

def thread_actions(gameList):
    out = None
    while not out:
        out = __check_games(gameList)
        if out:
            __sound_alarm()
            copy(out)
            return out
        time.sleep(10)
    return 

def add_gameNames(input, gameList):
    out = input.replace(" ", "")
    out = out.split(',')
    gameList.append(out)
    return 

'''
def main():
    
    g1 = GUI()
    g1.go()
    
    while gamesList:
        if __check_game(gamesList):
            sound_alarm()
        
    return

main()
'''