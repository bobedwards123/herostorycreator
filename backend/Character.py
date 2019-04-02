from random import randint

class Character:
    def __init__(self):
        self.occupation = self.getOccupation()
        self.age = self.getAge()
        self.gender = self.getGender()
        self.name = self.getCharacterName(self.gender)
        self.dream = self.getDream()
        self.fear = self.getFear()

    
    def getCharacterName(self, gender):
        male_names = ["John", "Darcy", "Edward", "George", "Seth"]
        randomnumber = randint(0,len(male_names) -1)

        return male_names[randomnumber]

    def getOccupation(self):
        occupations = ["waiter", "lawyer", "accountant"]
        randomnumber = randint(0,len(occupations) -1)
        return occupations[randomnumber]
    
    def getAge(self):
        return randint(10,90)
    
    def getFear(self):
        fears = ["the dark", "the unknown", "stepping up", "going outside"]
        randomnumber = randint(0,len(fears) -1)
        return fears[randomnumber]
    
    def getDream(self):
        dreams = ["to fly", "to be a rockstar", "to be a great person"]
        randomnumber = randint(0,len(dreams) -1)
        return dreams[randomnumber] 


    
    def getCharacterAge(self):
        return randint(10,90)


    def getGender(self):
        
        return "male"
  





 