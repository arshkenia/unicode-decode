from unicodecode import uniclist

class UnicodeClass(object):
    def __init__(self, text , types ="text" ):
        self.type = types
        self.text = text
        self.unilist = uniclist
    
    def getUnicodeString(self):
        if self.type == "text":
            output = ""
            i = 0
            textstr = ""
            for char in self.text:
                i = i + 1
                for sublist in self.unilist:
                    if char == sublist[1]:
                        output = output + sublist[0]
            return output
        else:
            raise Exception("Not given correct type")
    
    def getUnicodeList(self):
        if self.type == "text":
            output = []
            i = 0
            textstr = ""
            for char in self.text:
                i = i + 1
                for sublist in self.unilist:
                    if char == sublist[1]:
                        output.append(sublist[0])
            return output
        else:
            raise Exception("Not given correct type")

    def getTextString(self):
        if self.type == "unicode":
            output = ""
            i = 0
            unicharacter = ""
            for char in self.text:
                i == i + 1
                unicharacter = unicharacter + char
                if i % 2 == 0:
                    for sublist in self.unilist:
                        if unicharacter == sublist[0]:
                            output = output + sublist[1]
                            unicharacter = ""
            return output

        else:
            raise Exception("Not correct type")

    def getTextList(self):
        if self.type == "unicode":
            output = []
            i = 0
            unicharacter = ""
            for char in self.text:
                i == i + 1
                unicharacter = unicharacter + char
                if i % 2 == 0:
                    for sublist in self.unilist:
                        if unicharacter == sublist[0]:
                            output.append(sublist[1])
                            unicharacter = ""
            return output

        else:
            raise Exception("Not correct type")

                    


            
