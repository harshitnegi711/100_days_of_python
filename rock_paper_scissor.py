rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
i=[rock,paper,scissors]
x=int(input("enter 0 for rock , 1 for paper and 2 for scissors : "))
y=int(random.randint(0,2))
if x==0 and y==1:
    print("You lose")
elif x==0 and y==2:
    print("You wins")
elif x==1 and y==0:
    print("You wins")
elif x==1 and y==2:
    print("You lose")
elif x==2 and y==0:
    print("You lose")
elif x==2 and y==1:
    print("You wins")
else:
    print("draw")
print("your choice is {} \n {}".format(x,i[x]))
print("computer choice is {} \n {}".format(y,i[y]))
