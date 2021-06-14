logo='''
 _____                       _____ _            _   _                 _               
|  __ \                     |_   _| |          | \ | |               | |              
| |  \/_   _  ___  ___ ___    | | | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/   \_/ |_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                      
'''


import random
g=random.randint(1,100)
print(logo)
level=input("enter level easy , medium or hard : ")
if level=="easy":
    live=10
elif level =="medium":
    live=5
elif level=="hard":
    live=3
else:
    exit(0)



while live!=0:
    print(live)
    x=int(input("guess a number between 0 to 100 : "))
    if x==g:
        print("you win")
    elif x<g:
        print("too low")
    elif x>g:
        print("too big")

    live-=1
if live == 0:
    print(g)
