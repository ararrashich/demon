import telepot, time, subprocess


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if (content_type == 'text'):
        command = msg['text']
        print ('Got command: %s' % command)

        if  '/0' in command:#В кавычках команда которую мы будем писать в телеграмм. 
                            #Можно и слова и по русски но начинать нужно именно с косой палочки
            p = subprocess.Popen(cmd0, shell=True)#А тут собственно выполняется команда которую
                            #мы задали для переменной "cmd0"
            bot.sendMessage(chat_id, "Комп не уйдёт в спящий режим")#А это ответ бота в чат.
					
					
					
					
        if  '/s' in command:
            subprocess.call("cscript sw.vbs")
            bot.sendMessage(chat_id, "ZBS")
			

        if  '/qwer' in command:
            p = subprocess.Popen(cmd1, shell=True)
            bot.sendMessage(chat_id, "Комп уйдёт в спящий режим через одну минуту простоя")

        if  '/sw' in command:
            p = subprocess.Popen(soundpc, shell=True)
            bot.sendMessage(chat_id, "Звук на столе")

        if  '/br' in command:
            p = subprocess.Popen(block, shell=True)
            bot.sendMessage(chat_id, "Звук на телике")


bot = telepot.Bot('727077862:AAFgOLfmrN5bKr58VHYdyBVx_lGqnsBCgkk')#Вместо иксов пишем ваш токен
cmd0 = 'Powercfg -setactive 381b4222-f694-41f0-9685-ff5bb260df2e'
qwe = 'Powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c'
cmd1 = 'SHUTDOWN'
soundpc = ''
block = 'cmd.exe'
swq = 'sw.vbs'


bot.message_loop(handle)





while 1:
    time.sleep(20)
