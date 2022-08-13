import time
from 매크로 import Macro3
import json
import requests
import telegram
import pyautogui as pa
from datetime import datetime
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

telegram_token = ####토큰#####
telegram_id = 5380801292

bot = telegram.Bot(token=telegram_token)
updater = Updater(token=telegram_token)

recent_text = ''

def get_message(update, context):
    global recent_message
    # update.message.reply_text("got text")
    # update.message.reply_text(update.message.text)
    recent_message = update.message.text
    return recent_message

def send_message(update, context):
    bot.sendMessage(chat_id=telegram_id, text='테스트 메세지')


def check_status(update, context):
    bot.sendMessage(chat_id=telegram_id, text='스크린 캡쳐 명령이 입력되었습니다.')
    im = pa.screenshot('my_screenshot.png')
    bot.send_photo(chat_id=telegram_id, photo=open('my_screenshot.png', 'rb'))


def macro_start(update, context):
    bot.sendMessage(chat_id=telegram_id, text='시작시간 ' + str(datetime.now()))
    Macro3.main_macro_without_tuto()
    bot.sendMessage(chat_id=telegram_id, text='매크로 완료.')
    check_status(update, context)


def macro1(update, context):
    bot.sendMessage(chat_id=telegram_id, text='시작시간 ' + str(datetime.now()))
    Macro3.macro1()
    bot.sendMessage(chat_id=telegram_id, text='macro1 완료.' + str(datetime.now()))
    check_status(update, context)


def macro2(update, context):
    bot.sendMessage(chat_id=telegram_id, text='시작시간 ' + str(datetime.now()))
    Macro3.macro2()
    bot.sendMessage(chat_id=telegram_id, text='macro1 완료.' + str(datetime.now()))
    check_status(update, context)


def macro3(update, context):
    bot.sendMessage(chat_id=telegram_id, text='시작시간 ' + str(datetime.now()))
    Macro3.macro3()
    bot.sendMessage(chat_id=telegram_id, text='macro1 완료.' + str(datetime.now()))
    check_status(update, context)


def macro4(update, context):
    bot.sendMessage(chat_id=telegram_id, text='시작시간 ' + str(datetime.now()))
    Macro3.macro4()
    bot.sendMessage(chat_id=telegram_id, text='macro1 완료.' + str(datetime.now()))
    check_status(update, context)


def macro5(update, context):
    bot.sendMessage(chat_id=telegram_id, text='시작시간 ' + str(datetime.now()))
    Macro3.macro5()
    bot.sendMessage(chat_id=telegram_id, text='macro1 완료.' + str(datetime.now()))
    check_status(update, context)


def macro6(update, context):
    bot.sendMessage(chat_id=telegram_id, text='시작시간 ' + str(datetime.now()))
    Macro3.macro6()
    bot.sendMessage(chat_id=telegram_id, text='macro1 완료.' + str(datetime.now()))
    check_status(update, context)


def reset_start1(update, context):
    bot.sendMessage(chat_id=telegram_id, text='초기화 시작')
    Macro3.reset()
    time.sleep(3)
    check_status(update, context)
    bot.sendMessage(chat_id=telegram_id, text='초기화 코드를 입력한 뒤, "/reset2"를 입력하세요.')


def reset_start2(update, context):
    bot.sendMessage(chat_id=telegram_id, text='초기화2 명령이 입력되었습니다.')
    global recent_text
    Macro3.input_reset_code(recent_text)
    bot.sendMessage(chat_id=telegram_id, text='초기화 완료. 새로 시작하려면 "/macro"를 입력하세요.')


def help(update, context):
    bot.sendMessage(chat_id=telegram_id, text='리스트 : /check, /reset1, /reset2, /macro, /click, /button3, /esc, /help')
    bot.sendMessage(chat_id=telegram_id, text='/check : 현재 화면 캡쳐 및 전송')
    bot.sendMessage(chat_id=telegram_id, text='/reset1 : 리셋 시작(초기화 코드 전송까지)')
    bot.sendMessage(chat_id=telegram_id, text='/reset2 : 초기화코드 입력한 뒤 /reset2 입력하면 초기화 완료')
    bot.sendMessage(chat_id=telegram_id, text='/macro : 소환사명 입력단계부터 시작')
    bot.sendMessage(chat_id=telegram_id, text='/click : [X좌료],[Y좌표] 전송 후 /click 하면 해당 위치 클릭')
    bot.sendMessage(chat_id=telegram_id, text='/button3 : 3번째 버튼 클릭')
    bot.sendMessage(chat_id=telegram_id, text='/esc : esc 입력')


def click(update, context):
    global recent_text
    x, y = map(int, recent_text.split(','))
    bot.sendMessage(chat_id=telegram_id, text='클릭이 입력되었습니다.')
    Macro3.move_click(x, y, 1)
    bot.sendMessage(chat_id=telegram_id, text='클릭 완료')


def button3(update, context):
    bot.sendMessage(chat_id=telegram_id, text='button3이 입략되었습니다.')
    Macro3.button(3)
    bot.sendMessage(chat_id=telegram_id, text='버튼3 클릭 완료')


def esc(update, context):
    bot.sendMessage(chat_id=telegram_id, text='esc가 입략되었습니다.')
    Macro3.esc_press()
    bot.sendMessage(chat_id=telegram_id, text='esc 입력 완료')


def add_handler(cmd, func):
    updater.dispatcher.add_handler(CommandHandler(cmd, func))


def handler(update, context):
    user_text = update.message.text # 사용자가 보낸 메세지를 user_text 변수에 저장합니다.
    # if user_text == "안녕": # 사용자가 보낸 메세지가 "안녕"이면?
    #     bot.send_message(chat_id=id, text="어 그래 안녕") # 답장 보내기
    # elif user_text == "뭐해": # 사용자가 보낸 메세지가 "뭐해"면?
    #     bot.send_message(chat_id=id, text="그냥 있어") # 답장 보내기
    global recent_text
    recent_text = user_text


# 채팅방에서 /send 입력 시 호출
add_handler('send', send_message)
add_handler('check', check_status)
add_handler('reset1', reset_start1)
add_handler('reset2', reset_start2)
add_handler('macro', macro_start)
add_handler('click', click)
add_handler('help', help)
add_handler('button3', button3)
add_handler('esc', esc)


echo_handler = MessageHandler(Filters.text, handler)
updater.dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
