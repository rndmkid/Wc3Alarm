'''
Created on Mar 30, 2018

@author: Q
'''
from appJar import gui

class MainGUI(object):
    '''
    classdocs
    '''
    app = gui("Wc3Alarm")

    def __init__(self):
        '''
        Constructor
        '''
        self.i = "test"
        self.app.setBg("white")
        self.app.setFont(18)
        self.app.addLabel("title", "Warcraft 3 Alarm")
        self.app.startFrame("Games", 0, 0)
        self.app.addLabel("search", "Searching For:")
        self.app.stopFrame()
        def press(button):
            #To-Do Add/Replace Actions
            self.app.openFrame('Games')
            name = self.app.getEntry("Game Name")
            self.app.addLabel(self.i, name)
            self.i = self.i + "t"
            self.app.stopFrame()
            self.app.setEntry("Game Name", "")
            self.app.setEntry("key", "")
        self.app.addEntry("Game Name")
        self.app.addEntry("key")
        self.app.setEntryDefault("Game Name", "Game Name")
        self.app.setEntryDefault("key", "Keyword, Keyword")
        self.app.addButton("Add New Game", press)
        
        
    def go(self):
        self.app.go()
    
    def getKey(self):
        return self.app.getEntry("key")