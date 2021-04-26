stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''



print(logo)
word=["apple","mango","grapes"]
import random
w=random.choice(word)
lives=6
#print(w)
#guess=input("guess a letter : ").lower()
#print(guess)
empty=[]
for _ in range(len(w)):
    empty += "_"
    
end_of_game=False

while not end_of_game:
    
    guess=input("guess a letter : ").lower()
    
    if guess in empty:
        print("you have already gussed it.")
    
    for letter in range(len(w)):
        
        if w[letter]==guess:
            
            empty[letter]=guess
    if guess not in w:
        print(f"{guess} is not in the word, you lose a life")
        lives-=1
        if lives==0:
            end_of_game=True
            print("you lose")
        
    print(f"{' '.join(empty)}")

    if "_" not in empty:
        end_of_game= True
        print("you win")
    
    print(stages[lives])
    