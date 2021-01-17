from ERBS.ERBS_api_client import ErbsClient
from discordBot_token import erbs_api_key

api_key = erbs_api_key
version = 'v1'


class ErbsEngine:
    # API Client 생성
    erbsAPI = ErbsClient(api_key=api_key, version=version)

    async def recent(self, name: str):
        print('user name: ', name)
        user_num = await self.erbsAPI.fetch_user_nickname(name)
        print('user_num: ', user_num)
        result = await self.erbsAPI.fetch_user_games(user_num)
        print('result = ', result)
        game = result[0]  # 제일 마지막 판
        text = f'1111유저명: {game["nickname"]}\n' \
               f'등수: {game["gameRank"]}\n' \
               f'───────────────────────────────\n' \
               f'플래이 시작 시간: {game["startDtm"]}\n' \
               f'플래이 타임: {int(game["duration"] / 60)}분 {game["duration"] % 60}초\n' \
               f'플래이어 킬: {game["playerKill"]}\n' \
               f'어시스트: {game["playerAssistant"]}\n' \
               f'동물 킬: {game["monsterKill"]}\n' \
               f'───────────────────────────────\n' \
               f'캐릭터 레벨: {game["characterLevel"]}\n' \
               f'사용 무기: {game["bestWeapon"]}\n' \
               f'무기 숙련도: {game["bestWeaponLevel"]}\n' \
               f'───────────────────────────────\n' \
               f'{game["killDetail"]}({game["killer"]})에게 {game["causeOfDeath"]}으로 죽었습니다. \n' \
               f'플래이어에게 입힌 피해: {game["damageToPlayer"]}\n' \
               f'동물에게 입힌 피해: {game["damageToMonster"]}\n' \
               f'남은 금지 구역: {game["safeAreas"]}\n' \
               f'끝'
        return text
