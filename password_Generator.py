#Password generator

#Create random 15 digit password

import string
import random
import pyperclip

alphabet = string.ascii_letters
password_Holder = []
num_holder = ""

#Creates numbers 0-9

for i in range(10):
    num_holder += str(i)

num_Alphabet = alphabet + num_holder

while True: 
    try:
        answer = int(input("How long would you like to make your password? "))
        assert(answer > 0)
        break
        
    except:
        print("Ensure you enter a positive number")

        
for i in range(answer):
   password_Holder.append(random.choice(num_Alphabet))

pyperclip.copy("".join(password_Holder))
