from FSC import Userdata
from textblob import TextBlob
from info_telegram import images
from NewsBot import NEEWS
from inlineTelegram import CricMain
ss = Userdata()

def Football():
    print("Football hai")
    return ("You have entered football zone")
    
def Reminder():
    print("Reminder")
    return ("You have entered Reminder zone")

def Dictionary():
    print("Dictionary")
    return ("You have entered Dictionary zone")

def Weather():
    print("Weather")
    return ("Enter place:")



cmd = {'/start':'','/photo':images,'Football':Football,'Cricket':CricMain,'Reminder':Reminder,'Dictionary':Dictionary, 'Weather':Weather, 'News': NEEWS }#, Football,Cricket,Reminder,News,Dictonary]
Id = []

def iinput(text, idd):
    print("Stage - 3")
    blob = TextBlob(text)
    dd = blob.tags
    ID = open('TelegramID.txt', 'r')
    ID = ID.read()
    Id = ID.split('\n')
    idd = str(idd)
    try:
        if not idd in Id:
            print("out")
            ID = open('TelegramID.txt', 'a')
            ID.write(idd+'\n')
            return ("Hello New User. \nYou can pick any of my services to begin.")
        
        else:
            print("Stage - 4")
            return cmd[text]()
            #print(text)
            #return ("Hello")
                    
    except Exception as e:
        print(e)
                
#print(type(Football))
#iinput('Football',490217645)


    
