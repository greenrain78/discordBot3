import discord
from apscheduler.schedulers.background import BackgroundScheduler
from discord import Embed
from Log.infoLog import logger as log

from Point import point_DB
from Point import user_DB
from Point.script import point_table, reason_script
from Settings import debug


class PointEngine:
    pointList = None
    sleepList = None
    schedule = BackgroundScheduler()

    def __init__(self):
        # init
        point_DB.init()
        user_DB.init()
        self.initUserList()

        # set schedule
        self.schedule.start()

        if not debug:
            self.schedule.add_job(self.dailyReset, 'cron', hour=12, id="dailyReset")
        else:
            self.schedule.add_job(self.dailyReset, 'cron', second=40, id="dailyReset")

    def eventInfo(self) -> Embed:
        title = "디스코드 포인트 이벤트"
        text = '디스코드 포인트를 모아 기프티콘을 받아 가자'
        em = discord.Embed(title=title, description=text)

        title1 = "포인트 획득 방법"
        text1 = f"1. 매일 꾸준히 디스코드 방에 접속하여 출석채크를 한다.\n" \
                f"2. 도박 기능 출시 예정\n"
        em.add_field(name=title1, value=text1, inline=False)

        title2 = "상품 목록"
        text2 = f"커피 기프티콘\n" \
                f"목표 포인트: 10000pt\n" \
                f"남은 수량: 2장\n"
        em.add_field(name=title2, value=text2, inline=False)

        footer = '반응이 좋거나 활성화가 잘되면 상품을 더 늘리겠습니다.'
        em.set_footer(text=footer)
        return em

    def getPoint(self, name: str) -> str:
        if name not in self.sleepList:
            text = f"미등록 사용자 입니다."
            return text
        pt = user_DB.get_point(name)
        if pt == 0:
            text = '데이터 베이스에 사용자 정보가 없습니다.'
        else:
            text = f'유저({name})의 획득 포인트는 {pt}입니다,'
        return text

    def dailyReset(self):
        log.info("daily user reset: %s", self.sleepList)
        for user in self.sleepList:
            self.sleepList[user] = self.sleepList[user] + 1
            user_DB.update_user_sleep(user, self.sleepList[user])

    def initUserList(self):
        # make user list
        tmp_sleepList = user_DB.get_sleepList()
        self.sleepList = {user[0]: user[1] for user in tmp_sleepList}

        tmp_pointList = user_DB.get_pointList()
        self.pointList = {user[0]: user[1] for user in tmp_pointList}

        log.info("bot init sleepList: %s", self.sleepList)
        log.info("bot init pointList: %s", self.pointList)

    def dailyCheck(self, name):
        # 최초 채팅 -> 리스트 추가
        if name not in self.sleepList:
            user_DB.insert_user(name, "new user", point_table['first'], 0)
            point_DB.insert(name, point_table['first'], reason_script['first'], point_table['first'])
            self.initUserList()
            text = f"{name}님이 최초로 채팅을 하셨습니다. ㅊㅋㅊㅋ\n" \
                   f"특별 보너스로 {point_table['first']}포인트 적립되었습니다."
            return text

        # 오늘 처음 채팅 -> 포인트 획득
        if self.sleepList[name] != 0:
            # 개근 여부 확인
            prev_val = user_DB.get_point(name)
            if self.sleepList[name] == 1:
                reason = reason_script["daily"]
                get_point = point_table['daily']
                text = f"{name}이 출석하여 {point_table['daily']}포인트를 획득하셨습니다."
            else:
                reason = reason_script["sleep"]
                get_point = point_table['daily'] + point_table["sleep"] * self.sleepList[name]
                text = f"{name}이 {self.sleepList[name]}일만에 복귀했습니다.\n" \
                       f"특별 보너스 포인트로 {get_point}포인트를 획득하셨습니다."

            point_DB.insert(name, get_point, reason, prev_val + get_point)
            user_DB.update_user_point(name, prev_val + get_point)

            self.sleepList[name] = 0
            user_DB.update_user_awake(name)
            return text
        else:
            # 중복 채팅 -> 무시
            return None
