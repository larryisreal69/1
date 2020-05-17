import datetime

from bot_handler import BotHandler

class Bot(BotHandler):

    def greet(self,last_update):
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        now = datetime.datetime.now()
        hour = now.hour

        if 6 <= hour < 12:
            self.send_message(last_chat_id, 'Good Morning, {}!'.format(last_chat_name))

        elif 12 <= hour < 17:
            self.send_message(last_chat_id, 'Good Afternoon, {}!'.format(last_chat_name))

        elif 17 <= hour < 23:
            self.send_message(last_chat_id, 'Good Evening, {}!'.format(last_chat_name))

        else:
            self.send_message(last_chat_id, 'Good Night, {}!'.format(last_chat_name))

