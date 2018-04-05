'''
Created on Apr 3, 2018

@author: Q
'''
from BackEnd import BE
import BackEnd
from MainGUI import GUI
import winsound


def sound_alarm():
    #To-Do: Sound Alarm
    winsound.Beep(440, 1000)
    return

def main():
    
    b1 = BE()
    g1 = GUI(b1)
    g1.go()
    
    print("meh")
    '''
    while b1.gamesList:
        for e in b1:
            if(b1)
    '''  
    return

main()