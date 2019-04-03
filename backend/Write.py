class Write:
    def __init__(self, name, text, html):
        self.name = name
        self.text = text
        self.html = html


    def writeFile(self):
        if self.html == True:

            f = open("{}.html".format(self.name),"w+")
        else:
            f = open("{}.txt".format(self.name),"w+")
        f.write(self.text)
        f.close


    
