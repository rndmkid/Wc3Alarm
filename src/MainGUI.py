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
        self.app.addLabel("title", "Warcraft 3 Alarm", 0 , 0)
        
        def restart():
            self.thread = threading.Thread(target=BackEnd.thread_actions, args=(self.gameList,))
            self.thread.start()
        
        self.app.startFrame("Bottom", 4, 0)
        self.app.addButton("Restart",restart, 0, 1)
        self.app.stopFrame()
        
        def press(button):
            try: 
                self.app.openLabelFrame("Searching For:")
            except:
                self.app.startLabelFrame("Searching For:", 1, 0)
                self.app.setSticky("ew")
            name = self.app.getEntry("Game Name")
            self.app.addLabel(self.i, name)
            self.i = self.i + "t"
            self.app.stopLabelFrame()
            BackEnd.add_gameNames(self.app.getEntry("key"), self.gameList)
            self.app.setEntry("Game Name", "")
            self.app.setEntry("key", "")
            self.app.setEntryDefault("Game Name", "Game Name")
            self.app.setEntryDefault("key", "Keyword, Keyword")
            if not self.thread._target:
                self.thread = threading.Thread(target=BackEnd.thread_actions, args=(self.gameList,))
                self.thread.start()
                
            
        self.app.addEntry("Game Name", 2, 0)
        self.app.addEntry("key", 3, 0)
        self.app.setEntryDefault("Game Name", "Game Name")
        self.app.setEntryDefault("key", "Keyword, Keyword")
        self.app.openFrame("Bottom")
        self.app.addButton("Add New Game", press, 0, 0)
        self.app.stopFrame()
        self.app.setStopFunction(self.thread._delete())
    
    def go(self):
        self.app.go()
        return
    
    def stop(self):
        print("Got Here")
        self.thread._stop()
        return

def __getKey(self):
    return self.app.getEntry("key")

def main():
    app = GUI()
    app.go()
    return

main()