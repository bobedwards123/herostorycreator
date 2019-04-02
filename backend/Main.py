from Plot import Plot
from Character import Character


char = Character(input('what is your name?'), 12, "male", True)

char2 = Character("Writing", 32, "female", False)

print(char.getProtagonist() + " meets " + char2.getProtagonist())