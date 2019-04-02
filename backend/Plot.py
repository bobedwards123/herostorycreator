from random import randint

class Plot:
    def __init__(self, protag, initial_friend):
        self.setting = self.getSetting()
        self.time_setting = self.getTimeSetting()
        self.protag = protag
        self.inciting_incident = self.getIncitingIncident()
        self.initial_friend = initial_friend

        
        
    def getSetting(self):
        locations = ['Australia', 'Greece', 'USA', 'France'] 
        randomnumber = randint(0,len(locations) -1)
        return locations[randomnumber]
         

      
    def checkGender(self, character):
        if character.gender == "female":
            return "she"
        else:
            return "he"
    
    def getIncitingIncident(self):
        incidents = [["Car crash", "losing loved ones"],["Plane crash", "losing loved ones"], ["house burning down", "losing important possessions"]]
        randomnumber = randint(0,len(incidents) -1)
        return incidents[randomnumber]

    def getInitialEmotionalReaction(self):
        conflicts = ['dispair', 'dismay', 'sorrow', 'anger', 'hatred', 'loss']
        randomnumber = randint(0,len(conflicts) -1)
        return conflicts[randomnumber]

    
    def getTimeSetting(self):
        return randint(1900,2050)


    def ActOne(self):
        text = """
        This story is set in {} in {}. {} is the protagonist, {} is a {} that has a dream of {} but is scared of {}. 
        """.format(self.setting,self.time_setting, self.protag.name, self.checkGender(self.protag), self.protag.occupation, self.protag.dream, self.protag.fear)

        #inciding incident
        text += """
        One day, a {} happens which changes everything. {}'s fears of {} are amplified in having to deal with {}. This causes the protagonist great {}.
        {}ed by the event, {} is called into the unknown. Suddenly the comforts of normalcy see to fade and our protagonist is lost. 

        """.format(self.inciting_incident[0], self.protag.name, self.protag.fear, self.inciting_incident[1], self.getInitialEmotionalReaction(), self.getInitialEmotionalReaction(), self.protag.name)
        
        #the call to advanture

        text += """
        {} soon discovers that things have changed. The world is no longer as it seemed, the protagonist meets {} who is a {}. {} is different from {} in that {} is not scared of the unknown.

        """.format(self.protag.name, self.initial_friend.name, self.initial_friend.occupation, self.initial_friend.name, self.protag.name, self.checkGender(self.initial_friend))

        
        
        return text