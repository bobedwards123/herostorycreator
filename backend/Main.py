from Plot import Plot
from Character import Character
from Write import Write

# char = Character(input("what is the protagonist's name?"), int(input("what is the protagonist's age?")),input("what is the protagonist's occupation?"), input("what is the protagonist's gender?"))

protagonist = Character()
initial_friend = Character()
oracle = Character()
enemy = Character()
title = "Adventures of {}".format(protagonist.name)
html = input("would you like html or txt?")
if html == "html":
    html = True
else:
    html = False
plot = Plot(protagonist, initial_friend, oracle, enemy, title, html)


plot_output = plot.ActOne()

print(plot_output)
writer = Write(title, plot_output, html)
writer.writeFile()