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
        occupations = [
        "   Accessory designer",
        "    Advertising designer",
        "    Animator",
        "    Architect",
        "    Art administrator",

        "    Artisan",
        "    Arts administration",

        "    Baker",
        "    Ceramics artist",
        "    Chief creative officer",

        "    Colorist",
        "    Concept Artist",
        "    Curator",
        "    Dancer",
        "    Design director",
        "    Design strategist",

        "    Essayist",
        "    Event planner",
        "    Fashion designer",
        "    Fine artist",

        "    Floral designer",

        "    Graphic designer",
        "    Hairstylist",
        "    Illustrator",
        "    Tattoo artist",
        "    Interior designer",
        "    Jewellery designer",
        "    Lyricist",
        "    Make-up artist",

        "    Marine designer",
        "    Media designer",
        "    Music",
        "    Party planner",
        "    Penciller",
        "    Photographer",
        "    Photojournalist",
        "    Potter",
        "    Production designer",
        "    Sculptor",
        "    Set decorator",
        "    Set dresser",
        "    Web designer",
        "    Wedding planner",
        "    Writer"
        
        
        ]
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
  





 