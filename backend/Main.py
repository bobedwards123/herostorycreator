from Plot import Plot
from Character import Character


# char = Character(input("what is the protagonist's name?"), int(input("what is the protagonist's age?")),input("what is the protagonist's occupation?"), input("what is the protagonist's gender?"))


char = Character()
char2 = Character()

plot = Plot(char, char2)


print(char.name)
print(plot.ActOne())

