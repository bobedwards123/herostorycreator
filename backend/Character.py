class Character:
    def __init__(self, occupation, age,gender, adventure):
        self.val = 1
        self.occupation = occupation
        self.age = age
        self.gender = gender
        self.adventure = adventure

    def getProtagonist(self):
        return "Fred is a {} year old {} who does {} for a living".format(self.age, self.gender, self.occupation, )


    def getIncitingIncident(self):
        incident = "incident"
        
        return incident