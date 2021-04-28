alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

 

def encrypt(text,shift):
    etext=""
    for i in text:
        x=alphabet.index(i)
        etext+=alphabet[int(x)+shift]   
       
    print(f"the encrypted text is {etext}")
    y=input("do you want the actual text  yes or no ? ")
    if y=="yes":
        decrypt(etext,shift)
    elif y=="no":
        exit(0)
   
    
def decrypt(text,shift):
    dtext=""
    for i in text:
        x=alphabet.index(i)
        dtext+=alphabet[x-shift]
    
    print(f"the decrypted text is {dtext}")
    
    
if direction=="encode":
    encrypt(text,shift)
elif direction=="decode":
    decrypt(text,shift)
else:
    exit(0)