import discord
from apscheduler.schedulers.background import BackgroundScheduler
from discord import Embed
from Log.infoLog import logger as log

from Point import point_DB
from Point import user_DB
from Point.script import point_table, reason_script
from Settings import debug
from Stock.search_stock import SearchStock


class StockEngine:
    pointList = None
    sleepList = None
    schedule = BackgroundScheduler()

    def __init__(self):
        pass
        # init
        # point_DB.init()
        # user_DB.init()
        # self.initUserList()
        # 
        # # set schedule
        # self.schedule.start()
        # 
        # if not debug:
        #     self.schedule.add_job(self.dailyReset, 'cron', hour=12, id="dailyReset")
        # else:
        #     self.schedule.add_job(self.dailyReset, 'cron', second=40, id="dailyReset")

    def eventInfo(self) -> Embed:
        title = "주식을 하자 주식을 하자"
        text = '합법 도박인 주식이 열렸습니다.'
        em = discord.Embed(title=title, description=text)

        title1 = "주식 투자 방법"
        text1 = f"1. 매일 꾸준히 디스코드 방에 접속하여 출석채크를 한다.\n" \
                f"2. 도박 기능 출시 예정\n"
        em.add_field(name=title1, value=text1, inline=False)

        title2 = "상품 목록"
        text2 = f"커피 기프티콘 2장\n" \
                f"목표 포인트: 10000pt\n" \
                f"남은 수량: 0장\n" \
                f"(상일이가 모든 상품을 수령하였습니다.)\n\n" \
                f"아직 상품이 준비안되었습니다.\n" \
                f"프리 시즌 기간"

        em.add_field(name=title2, value=text2, inline=False)

        footer = '반응이 좋거나 활성화가 잘되면 상품을 더 늘리겠습니다.'
        em.set_footer(text=footer)
        return em

    # def getPoint(self, name: str) -> str:
    #     if name not in self.sleepList:
    #         text = f"미등록 사용자 입니다."
    #         return text
    #     pt = user_DB.get_point(name)
    #     text = f'유저({name})의 획득 포인트는 {pt}입니다,'
    #     return text
    # 
    # def getPointList(self, name: str) -> str:
    #     response = point_DB.select(name)
    #     text = f"사용자: {name}의 점수 리스트\n"
    #     for row in response:
    #         text += f"획득 포인트: {row[2]}, \t " \
    #                 f"획득 일시: {row[4]}, \t" \
    #                 f"총합 포인트: {row[5]}, \t" \
    #                 f"획득 사유: {row[3]}\n"
    #     return text
    # 
    # def dailyReset(self):
    #     log.info("daily user reset: %s", self.sleepList)
    #     for user in self.sleepList:
    #         self.sleepList[user] = self.sleepList[user] + 1
    #         user_DB.update_user_sleep(user, self.sleepList[user])
    # 
    # def initUserList(self):
    #     # make user list
    #     tmp_sleepList = user_DB.get_sleepList()
    #     self.sleepList = {user[0]: user[1] for user in tmp_sleepList}
    # 
    #     tmp_pointList = user_DB.get_pointList()
    #     self.pointList = {user[0]: user[1] for user in tmp_pointList}
    # 
    #     log.debug("bot init sleepList: %s", self.sleepList)
    #     log.debug("bot init pointList: %s", self.pointList)
    # 
    # def dailyCheck(self, name):
    #     # 최초 채팅 -> 리스트 추가
    #     if name not in self.sleepList:
    #         user_DB.insert_user(name, "new user", point_table['first'], 0)
    #         point_DB.insert(name, point_table['first'], reason_script['first'], point_table['first'])
    #         self.initUserList()
    #         text = f"{name}님이 최초로 채팅을 하셨습니다. ㅊㅋㅊㅋ\n" \
    #                f"특별 보너스로 {point_table['first']}포인트 적립되었습니다."
    #         return text
    # 
    #     # 오늘 처음 채팅 -> 포인트 획득
    #     if self.sleepList[name] != 0:
    #         # 개근 여부 확인
    #         prev_val = user_DB.get_point(name)
    #         if self.sleepList[name] == 1:
    #             reason = reason_script["daily"]
    #             get_point = point_table['daily']
    #             text = f"{name}이 출석하여 {point_table['daily']}포인트를 획득하셨습니다."
    #         else:
    #             reason = reason_script["sleep"]
    #             get_point = point_table['daily'] + point_table["sleep"] * self.sleepList[name]
    #             text = f"{name}이 {self.sleepList[name]}일만에 복귀했습니다.\n" \
    #                    f"특별 보너스 포인트로 {get_point}포인트를 획득하셨습니다."
    # 
    #         point_DB.insert(name, get_point, reason, prev_val + get_point)
    #         user_DB.update_user_point(name, prev_val + get_point)
    # 
    #         self.sleepList[name] = 0
    #         user_DB.update_user_awake(name)
    #         return text
    #     else:
    #         # 중복 채팅 -> 무시
    #         return None
    # 
    # def givePoint(self, name: str, point: int) -> str:
    #     if name not in self.sleepList:
    #         text = f"미등록 사용자 입니다."
    #         return text
    # 
    #     pt = user_DB.get_point(name)
    #     result = pt + point
    #     reason = f"관리자에 의해 사용자({name})가 포인트를 {point}만큼 획득하였습니다."
    # 
    #     user_DB.update_user_point(name, result)
    #     point_DB.insert(name, point, reason, result)
    # 
    #     text = f"관리자에 의해 사용자({name})가 포인트를 획득하셨습니다." \
    #            f"획득 포인트: {point}, 총 포인트: {result}"
    #     return text
    def getStock(self, user):
        pass

    def findStock(self, code):
        price = SearchStock.get_price(code)
        text = f"해당 주식의 가격은 {price} 입니다."
        return text
