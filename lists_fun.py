
from random import *


word_list = ["Mac n Cheese", "Pizza", "Penne Vodka", "Empanadas ", "Grilled Cheese", "Icecream"]

#Generates a random integer.
x = randint(0, len(word_list)-1)
print(word_list[x])
