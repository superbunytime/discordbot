import json
import random

class MessageFactory:
    def __init__(self):
        with open("messages.json") as file:
            self.messages = json.load(file)
        self.templates = self.messages["templates"]
        self.conjunctions = self.messages["conjunctions"]
        self.words = []
        for key in self.messages["words"]:
            for value in self.messages["words"][key]:
                self.words.append(value)

    def word(self):
        return random.choice(self.words)

    def template(self):
        templateText = random.choice(self.templates)
        wordText = self.word()


        while "****" in templateText:
            templateText = templateText.replace("****", wordText)

        # The above code replaces any occurrence of "****" in a template with
        #  the same phrase. Therefore the one template with two asterisk groups
        #  ends up using the same word (e.g. "samurai, O samurai").
        #
        # If you prefer to have "****, O ****" have different words
        #  (e.g. "enemy, O archer"), replace it with the below code, and add an
        #  asterisk to one of the groups in the line in the JSON.

        #if ", O" in templateText:
            #templateText = templateText.replace("*****", self.word())
        #templateText = templateText.replace("****", wordText)

        return templateText

    def conjunction(self):
        return random.choice(self.conjunctions)

    def message(self):
        # Whether to build from one template, or two joined by a conjunction.
        layout = random.choice(["T", "TCT"])

        messageText = ""

        for s in layout:
            if s == "T":
                messageText += self.template()
            elif s == "C":
                messageText += self.conjunction() + " "

        # Just me being OCD about extra spaces...
        return messageText.replace("  ", " ").replace("  ", " ").replace("  ", " ")

if __name__ == "__main__":
    m = MessageFactory()
    print(m.message())



