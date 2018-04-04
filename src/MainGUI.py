'''
Created on Mar 30, 2018

@author: Q
'''
from appJar import gui
import BackEnd
import threading



class GUI(object):
    '''
    classdocs
    '''
    app = gui("Wc3Alarm")
    gameList = []
    thread = threading.Thread()

    def __init__(self):
        '''
        Constructor
        '''
        self.i = "test"
        self.gameList = []
        self.app.setBg("white")
        self.app.setFont(18)
        self.app.addLabel("title", "Warcraft 3 Alarm")
        self.app.startFrame("Games", 0, 0)
        self.app.addLabel("search", "Searching For:")
        self.app.stopFrame()
        def press(button):
            self.app.openFrame('Games')
            name = self.app.getEntry("Game Name")
            self.app.addLabel(self.i, name)
            self.i = self.i + "t"
            self.app.stopFrame()
            BackEnd.add_gameNames(self.app.getEntry("key"), self.gameList)
            self.app.setEntry("Game Name", "")
            self.app.setEntry("key", "")
            self.app.setEntryDefault("Game Name", "Game Name")
            self.app.setEntryDefault("key", "Keyword, Keyword")
            if not self.thread:
                self.thread = threading.Thread(target=BackEnd.thread_actions, args=(self.gameList,))
                self.thread.start()
                
            
        self.app.addEntry("Game Name")
        self.app.addEntry("key")
        self.app.setEntryDefault("Game Name", "Game Name")
        self.app.setEntryDefault("key", "Keyword, Keyword")
        self.app.addButton("Add New Game", press)
        self.app.setStopFunction(self.thread._stop())
        
    def go(self):
        self.app.go()
        
    
    
def __getKey(self):
    return self.app.getEntry("key")

def main():
    app = GUI()
    app.go()
    return

main()