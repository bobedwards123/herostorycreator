from random import randint
from Occupations import occupations
from FirstNames import male_names,female_names
from Dreams import dreams
from Fears import fears
class Character:
    def __init__(self):
        self.occupation = self.getOccupation()
        self.age = self.getAge()
        self.gender = self.getGender()
        self.name = self.getCharacterName(self.gender)
        self.dream = self.getDream()
        self.fear = self.getFear()

    
    def getCharacterName(self, gender):
        # male_names = ["John", "Darcy", "Edward", "George", "Seth"]
        if randint(0,10) > 5:
            randomnumber = randint(0,len(male_names) -1)
        else:
            randomnumber = randint(0,len(female_names) -1)

        return male_names[randomnumber]

    def getOccupation(self):
        randomnumber = randint(0,len(occupations) -1)
        return occupations[randomnumber]
    
    def getAge(self):
        return randint(10,90)
    
    def getFear(self):
        
        randomnumber = randint(0,len(fears) -1)
        return fears[randomnumber]
    
    def getDream(self):
        
        randomnumber = randint(0,len(dreams) -1)
        return dreams[randomnumber] 

    def getCharacterAge(self):
        return randint(10,90)


    def getGender(self):
        return "male"
        
  





 