import time
import pyautogui as pa
import random
from datetime import datetime
from random import random as rd

time.sleep(5)


def reset():
    esc_press()
    move_click(364, 131, 1)
    time.sleep(1 + rd())
    move_click(808, 217, 1)
    time.sleep(1 + rd())
    move_click(1163, 783, 1)
    time.sleep(1 + rd())
    move_click(940, 627, 1)
    time.sleep(1 + rd())


def input_reset_code(code):
    # 소환사 이름
    pa.write(code, interval=0.25)
    time.sleep(0.5 + rd())
    pa.press('enter')
    time.sleep(1 + rd())
    move_click(781, 762, 1)
    time.sleep(1 + rd())
    move_click(789, 689, 1)
    time.sleep(5 + rd())
    skip()


def right_aft_reset():
    # npc 말
    move_click(736, 292, 1)

    # 첫 번째 스킬
    button(3)

    # 가고일 왼쪽
    move_click(645, 330, 1)
    time.sleep(1.5 + rd())

    # 가고일 오른쪾
    move_click(983, 350, 1)
    time.sleep(3 + rd())

    # 두 번째 스킬
    button(4)
    time.sleep(1 + rd())

    # 스킬 사용할 아군 클릭
    move_click(1410, 643, 1)
    time.sleep(3 + rd())

    # 가운데 드래곤 클릭
    move_click(832, 361, 1)
    time.sleep(1.5 + rd())
    move_click(832, 361, 1)
    time.sleep(1.5 + rd())
    move_click(832, 361, 1)
    time.sleep(1.5 + rd())
    move_click(832, 361, 1)
    time.sleep(1.5 + rd())

    # 다음 스테이지
    time.sleep(13 + rd())

    # npc 말 + 적 클릭
    for i in range(45):
        move_click(888, 429, 1)
        time.sleep(1 + rd())

    # 스킵
    skip2()
    time.sleep(3 + rd())

    
def hunting():
    # 사냥시작
    while True:
        pa.moveTo(1266 + rd(), 577 + rd())
        pa.click()
        time.sleep(0.1 + rd())

        pa.moveTo(1290 + rd(), 299 + rd())
        pa.click()
        time.sleep(0.1 + rd())

        pa.moveTo(1254 + rd(), 225 + rd())
        pa.click()
        time.sleep(0.1 + rd())

        loc = pa.locateOnScreen('전투취소버튼.PNG')
        if loc is not None:
            # 멘토 누르기
            pa.moveTo(304 + rd(), 907 + rd())
            pa.click()
            time.sleep(0.3 + rd())

            # 전투 시작 버튼 누르기
            pa.moveTo(1556 + rd(), 739 + rd())
            pa.click()
            time.sleep(0.2 + rd())

            # 리더 스킬 확인
            pa.moveTo(787 + rd(), 634 + rd())
            pa.click()
            time.sleep(0.2 + rd())

        if check_img('신규지역확인_bef.png'):# or check_img('신규지역오픈.png'): #or check_img('신규지역확인_bef.png') or check_img('신규지역오픈_bef.png'):
            esc_press()
            break


def esc_press():
    move_click(100, 100, 1)
    time.sleep(0.3 + rd())
    while True:
        pa.press('esc')
        if check_img('esc.PNG'):
            pa.press('esc')
            time.sleep(1)
            break


# 소환용
def summon(n):
    cnt = 0
    while cnt < n:
        # 소환
        # 소환서 소환 클릭
        move_click(549, 915, 1)

        # skip
        skip()

        # 소환결과 확인
        move_click(1470, 830)
        # move_click(1173, 844)

        if check_img('4stars.png') or check_img('5stars.png'):
            pa.press('esc')

        cnt += 1


def move_click(x, y, n=1):
    cnt = 0
    while cnt < n:
        pa.moveTo(x + rd(), y + rd())
        pa.click()
        time.sleep(0.9 + rd())
        cnt += 1


def button(n):
    buttons_x = [1044, 1214, 1387, 1560, 1728]
    buttons_y = 947
    move_click(buttons_x[n - 1], buttons_y, 1)


def skip():
    move_click(1667, 973, 1)
    time.sleep(0.4 + (rd() * 2))


def skip2():
    move_click(1800, 988, 1)
    time.sleep(0.4 + (rd() * 2))


def check_img(filename):
    if pa.locateOnScreen(filename) is None:
        return False
    return True


def move_click_img(filename):
    loc = pa.locateOnScreen(filename)
    if loc is None:
        return False
    (x, y) = pa.center(loc)
    move_click(x, y, 1)
    return True


def bef_scenario():
    #소환사 이름
    move_click(100, 100, 1)
    time.sleep(0.5 + rd())
    tmp_number = random.randrange(1, 10000)
    naming = "bottle" + str(tmp_number) + "ck"
    pa.write(naming, interval=0.25)
    pa.press('enter')

    time.sleep(0.5)

    # 확인 클릭
    move_click(1300, 320, 1)

    # npc 말 대기
    time.sleep(11 + rd())

    # npc 말 15번
    move_click(929, 534, 23)

    # 소환 버튼
    button(3)

    # 소환서 클릭(첫 번째)
    move_click(1450, 305, 1)

    # 소환서 소환 클릭
    move_click(549, 915, 1)

    # 소환 확인 클릭
    move_click(792, 678, 1)
    time.sleep(1 + rd())

    # 스킵
    skip()

    # 소환몹 확인 클릭
    move_click(1483, 830, 1)

    # npc말 4번 클릭
    move_click(1483, 830, 4)

    # 소환 버튼
    button(3)

    # 신비 소환서(2번 째)
    move_click(1450, 456, 1)

    # 소환서 소환 클릭
    move_click(549, 915, 1)

    # 소환 확인 클릭
    move_click(792, 678, 1)
    time.sleep(1 + rd())

    # 스킵
    skip()

    # 소환몹 확인 클릭
    move_click(1483, 830, 1)

    # npc말 4번 클릭
    move_click(1483, 830, 5)

    # 신규 지역 오픈 확인 클릭
    move_click(940, 889, 1)

    # 전투 메뉴 버튼
    button(1)

    # 새로운 사냥터 찾아가기
    while True:
        if move_click_img('new.png'):
            break

    # 가렌숲 외곽 클릭
    move_click(1691, 385, 1)
    time.sleep(1)

    # 내 몹 두마리 클릭
    move_click(158, 729, 1)
    time.sleep(1)
    move_click(323, 729, 1)
    time.sleep(1)

    # 전투 시작
    move_click(1556, 729, 1)
    time.sleep(10)


def start_scenario():
    # 가렌숲 외곽 npc 말 + 왼쪽 맷돼지 + 사냥 속도 조절
    move_click(904, 298, 6)

    # 오른쪽 맷돼지
    move_click(1164, 298, 6)

    # 보물 상자 열기 및 보상 확인창 닫기 + npc 말 닫기
    move_click(1250, 345, 8)

    # 소환 메뉴 누르기
    button(3)

    # 소환서 클릭(첫 번째)
    move_click(1450, 305, 1)

    # 소환서 소환 클릭
    move_click(549, 915, 1)

    # 소환 확인 클릭
    move_click(792, 678, 1)

    # 스킵
    skip()

    # 소환몹 확인 클릭 + npc 말
    move_click(1483, 830, 3)
    time.sleep(2)

    # 속성 설명 닫기
    pa.press('esc')
    time.sleep(0.4 + rd())

    # npc 말
    move_click(1483, 700, 3)

    # 몬스터 버튼
    button(2)
    time.sleep(1 + rd())

    # 룬 버튼
    move_click(1053, 536, 1)
    time.sleep(1 + rd())
    move_click(1286, 617, 1)
    time.sleep(1 + rd())

    # 활력 클릭
    move_click(1260, 617, 1)
    time.sleep(1 + rd())

    # 착용할 룬 클릭
    move_click(1189, 661, 1)
    time.sleep(1 + rd())

    # 각인 클릭
    move_click(687, 775, 1)
    time.sleep(1 + rd())

    # 각인? 예 + npc 말
    move_click(778, 631, 4)
    time.sleep(1 + rd())

    # 1번 룬 클릭
    move_click(1440, 260, 1)
    time.sleep(1 + rd())

    # 강화 누르기
    move_click(700, 370, 1)
    time.sleep(1 + rd())

    # 강화 누르기
    move_click(530, 670, 1)
    time.sleep(3)

    # npc 말
    move_click(530, 670, 8)

    # 상점 버튼
    button(5)

    # 강화 마법진
    move_click(937, 530, 1)

    # 구매
    move_click(800, 799, 1)

    # 구매 하시겠습니까? 예
    move_click(800, 640, 1)

    # 확인 버튼
    button(4)
    time.sleep(10)

    # npc 말
    move_click(800, 640, 2)

    # 강화 버튼
    button(3)

    # 헬하운드 초상화
    move_click(1350, 300, 1)

    # 파란 버섯 초상화
    move_click(1700, 300, 1)

    # 강화 누르기2
    move_click(360, 920, 1)

    # 강화? 예
    move_click(780, 640, 1)
    time.sleep(0.7 + rd())

    # 스킵
    skip()
    time.sleep(1)

    # 핼하운드 확인
    move_click(1470, 830, 1)
    time.sleep(0.2 + rd())
    move_click(1470, 830, 1)

    # npc 말
    move_click(800, 640, 5)

    # 퀘스트 버튼
    move_click(150, 300, 1)

    # 퀘스트 느낌표
    move_click(779, 291)

    # npc 말
    move_click(800, 640, 14)
    time.sleep(2 + rd())

    # 전투 메뉴 버튼
    button(1)

    # 가렌숲 클릭
    move_click(503, 552)

    # 드롭 정보 클릭 및 가렌숲 남쪽
    move_click(1685, 563, 2)

    # 풍방랑 클릭
    move_click(398, 729, 1)

    # 전투 시작
    move_click(1556, 729, 1)
    time.sleep(10)


def start_scenario2():
    # 가렌숲 외곽 npc 말 + 왼쪽 맷돼지 + 사냥 속도 조절
    move_click(904, 298, 6)

    # 오른쪽 맷돼지
    move_click(1164, 298, 6)

    # NPC말 및 주황버섯 왼쪽
    move_click(736, 292, 10)

    # 맷돼지 중앙
    move_click(1037, 292, 17)

    # 오른쪽 주황버섯 및 보상 확인 전
    move_click(1345, 292, 8)

    # 보상 확인창 닫기 + npc 말 닫기
    move_click(1250, 345, 4)

    # 다음 스테이지
    move_click(1261, 563)

    # 전투 시작
    move_click(1550, 720)
    time.sleep(9)

    # 가렌숲 외곽 npc 말 + 왼쪽 맷돼지 + 사냥 속도 조절
    move_click(904, 298, 6)

    # 오른쪽 맷돼지
    move_click(1164, 298, 6)

    # NPC말 및 주황버섯 왼쪽
    move_click(736, 292, 6)

    # 맷돼지 중앙
    move_click(1037, 292, 14)

    # 오른쪽 주황버섯 및 보상 확인 전
    move_click(1345, 292, 6)

    # 보물 상자 열기 및 보상 확인창 닫기 + npc 말 닫기
    move_click(1250, 345, 8)

    # 다음 스테이지
    move_click(1261, 563)

    # 전투 시작
    move_click(1550, 720)
    time.sleep(9)

    #  왼쪽 맷돼지
    move_click(904, 298, 6)

    # 오른쪽 맷돼지
    move_click(1164, 298, 6)

    # 왼쪽 맷돼지
    move_click(904, 298, 6)

    # 오른쪽 맷돼지
    move_click(1164, 298, 6)

    # NPC말 및 주황버섯 왼쪽
    move_click(736, 292, 7)

    # 맷돼지 중앙
    move_click(1037, 292, 16)

    # 오른쪽 주황버섯 및 보상 확인 전
    move_click(1345, 292, 7)

    # 보물 상자 열기 및 보상 확인창 닫기 + npc 말 닫기
    move_click(1250, 345, 8)

    # 이벤트 창 닫기
    pa.press('esc')
    time.sleep(0.8)
    move_click(793, 695)

    # 다음 스테이지
    move_click(1261, 563)

    # 전투 시작
    move_click(1550, 720)
    time.sleep(9)

    # 자동 사냥
    move_click(383, 966)

    # 클릭
    while True:
        move_click(1250, 345, 3)
        move_click(1260, 575)
        move_click(1550, 720)
        # if move_click_img('다음.png'):
        #     move_click(1550, 720)
        #     time.sleep(9)


        # if move_click_img('신규지역오픈.PNG'):
        if check_img('신규지역확인_bef.png'):
            esc_press()
            time.sleep(1)
            break


def aft_scenario():
    cnt = 0
    while cnt < 20:
        move_click(100, 100, 1)
        time.sleep(0.4 + rd())
        pa.press('esc')
        cnt += 1

    while check_img('esc.PNG'):
        pa.press('esc')
        time.sleep(0.4 + rd())
    # 소환사의 길 누르기
    move_click(150, 450, 1)
    time.sleep(1 + rd())
    move_click(150, 450, 1)
    time.sleep(1 + rd())

    cnt = 0
    while cnt < 10:
        pa.press('esc')
        time.sleep(0.4 + rd())
        cnt += 1
    while check_img('esc.PNG'):
        pa.press('esc')
        time.sleep(0.4 + rd())
    move_click(150, 450)
    time.sleep(1 + rd())
    move_click(150, 450)
    time.sleep(1 + rd())
    cnt = 0
    while cnt < 10:
        pa.press('esc')
        time.sleep(0.4 + rd())
        cnt += 1
    while check_img('esc.PNG'):
        pa.press('esc')
        time.sleep(0.4 + rd())
    time.sleep(1 + rd())
    move_click(150, 450)
    time.sleep(1 + rd())
    esc_press()
    # 멘토 추가하기
    ########이거하는 중
    ########## 사이사이에 대상 멘티 꽉찬 경우 체크하게 하기
    button(4)
    time.sleep(1 + rd())
    move_click(269, 187)
    move_click(244, 630)

    move_click(1136, 439)
    move_click(689, 337)
    move_click(758, 748)
    time.sleep(2)
    while check_img('대상초과.PNG'):
        move_click(100, 100)
        pa.press('esc')
        time.sleep(1)
        move_click(1136, 439)
        move_click(1317, 197)
        move_click(689, 337)
        move_click(758, 748)
        time.sleep(2)

    move_click(1136, 573)
    move_click(689, 337)
    move_click(758, 748)
    time.sleep(2)
    while check_img('대상초과.PNG'):
        move_click(100, 100)
        pa.press('esc')
        time.sleep(1)
        move_click(1136, 573)
        move_click(1317, 197)
        move_click(689, 337)
        move_click(758, 748)
        time.sleep(2)

    move_click(1136, 703)
    move_click(689, 337)
    move_click(758, 748)
    time.sleep(2)
    while check_img('대상초과.PNG'):
        move_click(100, 100)
        pa.press('esc')
        time.sleep(1)
        move_click(1136, 703)
        move_click(1317, 197)
        move_click(689, 337)
        move_click(758, 748)
        time.sleep(2)

    # move_click(1136, 836)
    # move_click(689, 337)
    # move_click(758, 748)
    # time.sleep(2)
    # while check_img('대상초과.PNG'):
    #     move_click(100, 100)
    #     pa.press('esc')
    #     time.sleep(1)
    #     move_click(1136, 836)
    #     move_click(1317, 197)
    #     move_click(689, 337)
    #     move_click(758, 748)
    #     time.sleep(2)
    #
    # move_click(1136, 963)
    # move_click(689, 337)
    # move_click(758, 748)
    # time.sleep(2)
    # while check_img('대상초과.PNG'):
    #     move_click(100, 100)
    #     pa.press('esc')
    #     time.sleep(1)
    #     move_click(1136, 963)
    #     move_click(1317, 197)
    #     move_click(689, 337)
    #     move_click(758, 748)
    #     time.sleep(2)

    # esc_press()
    # 커뮤니티 메뉴 나가고 소환사의 길 나가기 까지 esc
    cnt = 0
    while cnt < 10:
        pa.press('esc')
        time.sleep(0.4 + rd())
        cnt += 1

    move_click(100, 100, 1)
    time.sleep(1)
    pa.press('esc')
    while check_img('esc.PNG'):
        pa.press('esc')
        time.sleep(0.4 + rd())
    time.sleep(1 + rd())

    move_click(1269, 481)

    # 소환사의 길
    move_click(153, 440)
    time.sleep(1 + rd())

    # npc말 + 보상받기
    move_click(732, 596, 3)

    # 교환권 이동
    move_click(939, 730)
    time.sleep(1 + rd())

    # 프리미엄팩 교환
    move_click(939, 730)
    time.sleep(1 + rd())

    # 1회 무료 버튼
    move_click(797, 846)

    # 구매 확인
    esc_press()

    # 우편함 열기
    move_click(164, 596)
    time.sleep(1 + rd())
    move_click(1275, 257)
    time.sleep(1 + rd())
    move_click(1275, 257)
    time.sleep(1 + rd())
    # 위에서 5개 받기
    move_click(1504, 390, 5)

    # 나가기
    esc_press()

    # 소환진 누르기 및 소환 메뉴 버튼
    time.sleep(1)
    move_click(542, 429)
    button(3)

    # 신비 소환서(2번 째)
    move_click(1450, 456)

    # 소환 11번
    summon(11)

    # 나가기
    esc_press()

    # 나가기
    esc_press()


# 이제 멘토 넣어서 사냥하기
def aft_scenario2():
    # 전투 메뉴 버튼
    button(1)

    # 새로운 사냥터(시즈산)
    move_click(782, 382)

    # 유적 지하1층
    move_click(1694, 387)

    # 듀란드 친추 확인 등 설명 스킵
    pa.moveTo(945 + rd(), 364 + rd())
    cnt = 0
    while cnt < 10:
        pa.click()
        time.sleep(0.1 + rd())
        cnt += 1

    # 멘토 선택 및 앞에서 부터4마리 배치
    # pa.moveTo(304 + rd(), 897 + rd())
    # pa.click()
    # time.sleep(0.2 + rd())
    pa.moveTo(154 + rd(), 721 + rd())
    pa.click()
    time.sleep(0.2 + rd())
    pa.moveTo(310 + rd(), 721 + rd())
    pa.click()
    time.sleep(0.2 + rd())
    pa.moveTo(462 + rd(), 721 + rd())
    pa.click()
    time.sleep(0.2 + rd())
    pa.moveTo(608 + rd(), 721 + rd())
    pa.click()
    time.sleep(0.2 + rd())

    # 전투 시작
    pa.moveTo(1556 + rd(), 735 + rd())
    pa.click()
    time.sleep(0.2 + rd())

    # 리더 스킬 확인
    pa.moveTo(787 + rd(), 634 + rd())
    pa.click()
    time.sleep(0.2 + rd())

    while True:
        pa.moveTo(1266 + rd(), 577 + rd())
        pa.click()
        time.sleep(0.1 + rd())

        pa.moveTo(1290 + rd(), 299 + rd())
        pa.click()
        time.sleep(0.1 + rd())

        pa.moveTo(1254 + rd(), 225 + rd())
        pa.click()
        time.sleep(0.1 + rd())

        loc = pa.locateOnScreen('전투취소버튼.PNG')
        if loc is not None:
            # 멘토 누르기
            # pa.moveTo(304 + rd(), 907 + rd())
            # pa.click()
            # time.sleep(0.3 + rd())

            # 전투 시작 버튼 누르기
            pa.moveTo(1556 + rd(), 739 + rd())
            pa.click()
            time.sleep(0.2 + rd())

            # 리더 스킬 확인
            pa.moveTo(787 + rd(), 634 + rd())
            pa.click()
            time.sleep(0.2 + rd())

        if check_img('신규지역확인.png'):
            esc_press()
            break

    # 다음 카비르유적
    # 전투 메뉴 버튼
    button(1)
    time.sleep(1 + rd())

    # 카비르유적
    move_click(1086, 446)
    time.sleep(0.3 + rd())

    # 유적 지하1층
    move_click(1694, 387)

    move_click(503, 493)

    # 사냥시작
    hunting()

    # 다음 라곤설산
    # 전투 메뉴 버튼
    button(1)
    time.sleep(1 + rd())

    # 라곤설산
    move_click(1166, 155)
    time.sleep(0.3 + rd())

    # 유적 지하1층
    move_click(1694, 387)

    # 사냥시작
    hunting()

    # 다음 테라인숲
    # 전투 메뉴 버튼
    button(1)
    time.sleep(1 + rd())

    # 라곤설산
    move_click(1523, 305)
    time.sleep(0.3 + rd())

    # 유적 지하1층
    move_click(1694, 387)

    # 사냥시작
    hunting()

    # 다음 하이데니
    # 전투 메뉴 버튼
    button(1)
    time.sleep(1 + rd())

    # 하이데니
    move_click(1634, 515)
    time.sleep(0.3 + rd())

    # 유적 지하1층
    move_click(1694, 387)

    # 사냥시작
    hunting()

    # 다음
    # 퀘스트
    move_click(168, 290)
    time.sleep(0.3 + rd())

    move_click(783, 514)
    time.sleep(1 + rd())

    # 유적 지하1층
    move_click(1694, 387)

    # 사냥시작
    hunting()

    # 다음
    # 퀘스트(보르파구스)
    move_click(168, 290)
    time.sleep(0.3 + rd())

    move_click(783, 410)
    time.sleep(1 + rd())

    # 유적 지하1층
    move_click(1694, 387)

    # 사냥시작
    hunting()

    # 다음
    # 퀘스트(화산)
    move_click(168, 290)
    time.sleep(0.3 + rd())

    move_click(783, 410)
    time.sleep(1 + rd())

    # 유적 지하1층
    move_click(1694, 387)

    # 사냥시작
    hunting()



def check_result():
    # 우편함 열기
    esc_press()
    move_click(164, 596)
    time.sleep(1 + rd())
    esc_press()
    move_click(164, 596)
    time.sleep(1 + rd())
    esc_press()
    move_click(164, 596)
    time.sleep(1 + rd())
    move_click(1275, 257)
    time.sleep(1 + rd())
    move_click(1275, 257)
    time.sleep(1 + rd())
    move_click(1495, 515, 1)
    time.sleep(1 + rd())
    esc_press()
    move_click(947, 504, 1)
    time.sleep(1 + rd())
    button(3)
    time.sleep(1 + rd())
    move_click(1454, 312, 1)
    time.sleep(1 + rd())
    move_click(549, 915, 1)
    time.sleep(1 + rd())
    skip()


# 가렌숲 외곽 사냥 시작 전
def main_macro():
    # 가렌숲 외곽 사냥 시작 전
    print(datetime.now())
    right_aft_reset()
    time.sleep(2)
    bef_scenario()
    time.sleep(2)
    start_scenario()
    time.sleep(2)
    start_scenario2()
    time.sleep(2)
    aft_scenario()
    time.sleep(2)
    aft_scenario2()
    print(datetime.now())


def macro1():
    time.sleep(2)
    bef_scenario()


def macro2():
    time.sleep(2)
    start_scenario()


def macro3():
    time.sleep(2)
    start_scenario2()


def macro4():
    time.sleep(2)
    aft_scenario()


def macro5():
    time.sleep(2)
    aft_scenario2()


def macro6():
    time.sleep(2)
    check_result()


def main_macro_without_tuto():
    # 가렌숲 외곽 사냥 시작 전
    print(datetime.now())
    #right_aft_reset()
    time.sleep(2)
    bef_scenario()
    time.sleep(2)
    start_scenario()
    time.sleep(2)
    start_scenario2()
    time.sleep(2)
    aft_scenario()
    time.sleep(2)
    aft_scenario2()
    time.sleep(2)
    check_result()
    print(datetime.now())

# move_click(100, 100, 1)
# hunting()
# right_aft_reset()
# main_macro_without_tuto()
# Fsummon(8)
aft_scenario()