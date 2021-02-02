import random

from Point import user_DB, point_DB


def check_wrong_args(args, num):
    if len(args) != num:
        text = f"odd 게임의 인자가 잘못 입력되었습니다.\n{len(args)}개가 입력되어 있네요^^\n 정상적으로 입력해 주세요 ^^\n"
        return text
    return False


def update_point(game_name, user, point):
    pt = user_DB.get_point(user)
    result = pt + point
    reason = f"게임({game_name})으로 포인트:{point}만큼 획득하셨습니다."

    user_DB.update_user_point(user, result)
    point_DB.insert(user, point, reason, result)

    text = f"획득 포인트: {point}, 총 포인트: {result}"
    return text


def odd_even(user, point, args):
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
        text = f"정답은 [홀]!!! \n"
        if num == "홀":
            text += f"정답입니다!!\n"
            pt = point
        elif num == "짝":
            text += f"틀렸습니다ㅠㅠ\n"
            pt = -point

    # 짝
    elif rand == 2:
        text = f"정답은 [짝]!!! \n"
        if num == "홀":
            text += f"틀렸습니다ㅠㅠ\n"
            pt = -point
        elif num == "짝":
            text += f"정답입니다!!\n"
            pt = point

    # 점수 처리
    text += update_point("홀짝 게임", user, pt)
    return text


def gameCount_user(user):
    pass
