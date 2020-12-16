class Time():
    def __init__(self):
        self.filePlayed = False

    def getTime():
        pass

    def playWavFile(self, file):
        pass

    def wavWasPlayed(self):
        self.filePlayed = True

    def resetWav(self):
        self.filePlayed = False

class Checker():
    def __init__(self):
        self.time = Time()

    def reminder(self, file):
        time = self.time.getTime()

        if time > 17:
            self.time.playWavFile(file)
            self.time.wavWasPlayed()
        else:
            self.time.resetWav()