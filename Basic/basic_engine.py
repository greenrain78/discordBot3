class BasicEngine:

    def __init__(self, pointBot, erbsBot):
        self.pointBot = pointBot
        self.erbsBot = erbsBot

    def getState(self) -> str:
        text = f"디코봇 정보\n" \
               f"{self.getStatePoint()}\n" \
               f""
        return text

    def getStatePoint(self) -> str:
        pointList = self.pointBot.engine.pointList
        sleepList = self.pointBot.engine.sleepList

        text = f"포인트 봇 정보\n" \
               f"점수 리스트: {pointList}\n" \
               f"잠수 리스트: {sleepList}\n"

        return text
