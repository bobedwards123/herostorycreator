class Write:
    def __init__(self, name, text):
        self.name = name
        self.text = text


    def writeFile(self):
        f = open("{}.txt".format(self.name),"w+")
        f.write(self.text)
        f.close


    
