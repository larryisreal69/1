import requests
import datetime

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        try:
            method = 'getUpdates'
            params = {'timeout': timeout, 'offset': offset}
            resp = requests.get(self.api_url + method, params)
            result_json = resp.json()['result']
            return result_json
        except Exception as e:
            print(e)
            print("Error in get_updates, exiting")
            exit(-1)

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        return last_update

class Bot(BotHandler):

    def greet(self,last_update):
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        now = datetime.datetime.now()
        hour = now.hour

        if 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Good Morning, {}!'.format(last_chat_name))

        elif 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Good Afternoon, {}!'.format(last_chat_name))

        elif 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Good Evening, {}!'.format(last_chat_name))

        else:
            greet_bot.send_message(last_chat_id, 'Good Night, {}!'.format(last_chat_name))


def read_token():
    token_file_path = ".token"
    with open (token_file_path,"r") as token_file:
        token = token_file.readlines()[0]
    return token

def main():
    offset = None
    token = read_token()
    bot = Bot(token)
    greetings = ('hello', 'hi', 'greetings', 'sup')

    while True:
        bot.get_updates(offset)

        last_update = bot.get_last_update()
        last_chat_text = last_update['message']['text']
        last_update_id = last_update['update_id']

        if last_chat_text.lower() in greetings:
            bot.greet(last_update)

        offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
