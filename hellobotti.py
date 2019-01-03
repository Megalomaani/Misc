import time
import telepot
from telepot.loop import MessageLoop
import subprocess

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/moro':
        bot.sendMessage(chat_id, "No haista sina huora vittu!")
    elif command == '/dickpick':
            bot.sendPhoto(chat_id=chat_id, photo=open('dp.png', 'rb'))
    elif command == '/webkuva':
            subprocess.call(['./takepic.sh'])
            bot.sendPhoto(chat_id=chat_id, photo=open('shpic.jpg', 'rb'))
    else:
        bot.sendMessage(chat_id, "Haista sina huora kyrpa!")

bot = telepot.Bot('668854429:AAEsAcxQWL7ej0bSIjQl8bnKeMzG4WfIURM')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
