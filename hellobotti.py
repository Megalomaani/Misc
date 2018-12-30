import telepot
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/moro':
        bot.sendMessage(chat_id, "No haista sinä huora vittu!")
    else:
        bot.sendMessage(chat_id, "Haista sinä huora kyrpä!")

bot = telepot.Bot('668854429:AAEsAcxQWL7ej0bSIjQl8bnKeMzG4WfIURM')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
time.sleep(10)
