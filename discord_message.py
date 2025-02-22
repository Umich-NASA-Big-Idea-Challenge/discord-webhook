from discord import SyncWebhook

class Message:

    def sync(self):
        self.webhook = SyncWebhook.from_url(self.URL)

    def setURL(self, URL):
        self.URL = URL
        self.sync()        

    def send(self, input):
        self.webhook.send(str(input))

    def userInput(self):
        message = input("Message to send: ")
        self.send(message)


