from datetime import datetime


class BasicEngine:

    def __init__(self, pointBot, erbsBot):
        self.pointBot = pointBot
        self.erbsBot = erbsBot
        self.startTime = datetime.now()

    def getState(self) -> str:
        text = f"디코봇 정보\n" \
               f"{self.getStatePoint()}\n" \
               f""
        return text

    def getStatePoint(self) -> str:
        pointList = self.pointBot.engine.pointList
        sleepList = self.pointBot.engine.sleepList
        runningTime = datetime.now() - self.startTime

        text = f"포인트 봇 정보\n" \
               f"실행 시간: {self.startTime}\n" \
               f"동작 시간: {runningTime.days}일, {runningTime.seconds}초\n" \
               f"점수 리스트: {pointList}\n" \
               f"잠수 리스트: {sleepList}\n"

        return text
