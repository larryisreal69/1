from bot import Bot

def read_token():
    token_file_path = ".token"
    with open (token_file_path,"r") as token_file:
        token = token_file.readlines()[0]
    return token

def is_update_correct(last_update):
  if last_update is None:
      return False
  if "message" not in last_update.keys():
      return False
  if "update_id" not in last_update.keys():
      return False
  if "text" not in last_update["message"].keys():
      return False
  return True

def main():
    offset = None
    token = read_token()
    bot = Bot(token)
    greetings = ('hello', 'hi', 'greetings', 'sup')

    while True:
        bot.get_updates(offset)

        last_update = bot.get_last_update()
        if not is_update_correct(last_update):
            continue
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
