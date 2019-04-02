from Plot import Plot
from Character import Character
from Write import Write

# char = Character(input("what is the protagonist's name?"), int(input("what is the protagonist's age?")),input("what is the protagonist's occupation?"), input("what is the protagonist's gender?"))

protagonist = Character()
initial_friend = Character()
oracle = Character()
enemy = Character()

plot = Plot(protagonist, initial_friend, oracle, enemy)

title = "Adventures of {} in {}".format(protagonist.name, plot.setting)
plot_output = plot.ActOne()

print(plot_output)
writer = Write(title, plot_output)
writer.writeFile()