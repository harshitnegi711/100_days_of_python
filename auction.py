
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("welcome to the auction")
dir={}
c='y'
while(c!='n'):
    name=input("enter your name : ")
    bit=int(input("enter your bid : "))
    dir[name]=bit
    c=input("is there any more bidders y or n : ")
m=0
winner=''
for i in dir:
    raw=dir[i]
    if(m<raw):
        m=raw
        winner=i
print(f"winner is {winner} with the bid of {m}")





