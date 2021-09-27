
from typing import AsyncGenerator


i = 1

def nameAge():
    while i < 4:
        name = input("Wat is je naam? ")
        if name == "stop":
            break
        age = int(input("Wat is je leeftijd? "))
        print("Hallo " + name + ", je leeftijd is " + str(age))
    
nameAge()
