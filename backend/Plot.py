from random import randint

class Plot:
    def __init__(self, protag, initial_friend, oracle, enemy):
        
        self.setting = self.getSetting()
        self.time_setting = self.getTimeSetting()

     
        #characters
        self.protag = protag
        self.initial_friend = initial_friend
        self.oracle = oracle
        self.enemy = enemy

        #events
        self.inciting_incident = self.getIncitingIncident()
        

        
        
    def getSetting(self):
        locations = ['Sydney', 'Berlin', 'Minesoda', 'Melbourne', 'San Francisco', 'Paris', 'Zurich'] 
        randomnumber = randint(0,len(locations) -1)
        return locations[randomnumber]
    
    def getTimeSetting(self):
        return randint(1900,2050)
         
    def getIncitingIncident(self):
        incidents = [
            ["Car crash", "losing loved ones"],
            ["Plane crash", "losing loved ones"], 
            ["house burning down", "losing important possessions"], 
            ["An Alien ship arrives", "taking human victims"],
            ["A baby downs", "causing the mother to panic"],
            ["being let go", "causing loss of the ability to pay for expenses and creditors"]
            
            ]
        randomnumber = randint(0,len(incidents) -1)
        return incidents[randomnumber]
      
    
    def checkGender(self, character):
        if character.gender == "female":
            return "she"
        else:
            return "he"
    
    

    def getInitialEmotionalReaction(self):
        conflicts = ['dispair', 'dismay', 'sorrow', 'anger', 'hatred', 'loss']
        randomnumber = randint(0,len(conflicts) -1)
        return conflicts[randomnumber]

    
    

    def getPossessiveGender(self, character):
        if character.gender == "male":
            return "his"
        else:
            return "her"
    
    def getHeGender(self, character):
        if character.gender == "male":
            return "he"
        else:
            return "she" 

    def getHimself(self, character):
        if character.gender == "male":
            return "himself"
        else:
            return "herself" 

    #defining the act 

    def ActOne(self):
        text = """
        This story is set in {} in {}. {} is the protagonist, {} is a {} that has a dream of {} but is scared of {}. 
        """.format(self.setting,self.time_setting, self.protag.name, self.checkGender(self.protag), self.protag.occupation, self.protag.dream, self.protag.fear)

        #inciding incident
        text += """
        One day, a {} happens which changes everything. {}'s fears of {} are amplified in having to deal with {}. This causes the protagonist great {}.
        {}ed by the event, {} is called into the unknown. Suddenly the comforts of normalcy begin to fade and our protagonist is lost. 

        """.format(self.inciting_incident[0], self.protag.name, self.protag.fear, self.inciting_incident[1], self.getInitialEmotionalReaction(), self.getInitialEmotionalReaction(), self.protag.name)
        
        #the call to advanture

        text += """
        {} soon discovers that things have changed. The world is no longer as it seemed, the protagonist meets {} who is a {}. {} is different from {} in that {} is not scared of the unknown.

        The world that {} has entered is not the same as {} place of comfort. Things are different here that that which {} knew back home. 

        """.format(self.protag.name, self.initial_friend.name, self.initial_friend.occupation, self.initial_friend.name, self.protag.name, self.checkGender(self.initial_friend), self.protag.name, self.getPossessiveGender(self.protag), self.getHeGender(self.protag))


        #initiation
        text += """
        As {} goes deeper and deeper into this new place, {} faces greater and greater challenges. {} skills at navigating the new world are limited. {} must work with {} new friend {} to develop them.
        {} must continue to face internal and external challenges, slowing approaching the ultimate challenge. 

        """.format(self.protag.name, self.protag.name, self.getPossessiveGender(self.protag), self.getHeGender(self.protag), self.getPossessiveGender(self.protag), self.initial_friend.name, self.getHeGender(self.protag))

        #plunging to the depths of the ocean, the whales belly
        text += """
        Finally {} faces the ultimate challenge, confronting {} who wants to {}. {}'s skills are much stronger than {}'s but {} has developed them through training. 


        """.format(self.protag.name, self.enemy.name, self.enemy.occupation, self.enemy.dream, self.enemy.name, self.protag.name, self.getHeGender(self.protag))


        #death and rebirth
        text += """
        The challenge is incredibly difficult and causes {} to complely doubt {}. In the end it is almost over but {} gets the strength to continue and ultimately succeeds against {}


        """.format(self.protag.name, self.getHimself(self.protag), self.getHeGender(self.protag), self.enemy.name)


        
        #return Home
        text += """
        Finally {} is able to return home. Having achieved success at overcoming the ultimate challenge, brining home the lessons to {} family and friends
        and sharing {} gifts with the community. 
        """.format(self.protag.name, self.getPossessiveGender(self.protag), self.getPossessiveGender(self.protag))
        
        return text