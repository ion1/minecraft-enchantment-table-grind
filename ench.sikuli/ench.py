Settings.MoveMouseDelay = 0.05

class Ench:
    def __init__(self):
        self.region = Screen(0).selectRegion()

    def run(self):
        self.selectTitle()

        while True:
            self.refreshEnchs()
            try:
                self.selectEnch()
                break
            except FindFailed:
                pass

    def refreshEnchs(self):
        self.selectTitle()
        doubleClick(self.region.wait(Pattern("Enchant-title.png").exact().targetOffset(2,90), 1))

    def selectEnch(self):
        self.selectTitle()
        hover(self.region.wait(Pattern("num.png").exact(), 0.1))

    def selectTitle(self):
        click(self.region.wait(Pattern("Enchant-title.png").exact(), FOREVER))

Ench().run()
