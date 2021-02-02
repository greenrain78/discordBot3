import random


def check_wrong_args(args, num):
    if len(args) != num:
        text = f"odd 게임의 인자가 잘못 입력되었습니다.\n{len(args)}개가 입력되어 있네요^^\n 정상적으로 입력해 주세요 ^^\n"
        return text
    return False


class GameEngine:
    def __init__(self):
        pass

    def odd_even(self, args):
        # 인자 확인
        check = check_wrong_args(args, 1)
        if check:
            return check
        num = args[0]
        if num != "홀" and num != "짝":
            text = f"홀짝 게임에서는 홀 짝 둘중 하나만 선택할 수 있어요.\n 알겠나요?"
            return text

        # 홀짝
        rand = random.randrange(1, 3)
        # 홀
        if rand == 1:
            if num == "홀":
                text = f"정답은 홀!!! \n정답입니다!!"
            elif num == "짝":
                text = f"정답은 홀!!! \n틀렸습니다ㅠㅠ"
        # 짝
        elif rand == 2:
            if num == "홀":
                text = f"정답은 짝!!! \n틀렸습니다ㅠㅠ"
            elif num == "짝":
                text = f"정답은 짝!!! \n정답입니다!!"
        return text

    def gameCount_user(self, user):
        pass
