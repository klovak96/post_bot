import requests
import telebot

url = "https://quotes15.p.rapidapi.com/quotes/random/"

querystring = {"language_code":"ru"}

headers = {
	"x-rapidapi-key": "d1a1ed4e83msh0689565852c58bbp1736e2jsn53f5625e3d88",
	"x-rapidapi-host": "quotes15.p.rapidapi.com"
}


TOKEN = '7847696631:AAFczsdzDhyEWzf3Hgzl8jTGSFVaQ1agj5w'
CHANNEL_ID = '@TestPost96'

bot = telebot.TeleBot(TOKEN)


while True:
    try:
        response = requests.get(url, headers=headers, params=querystring)
        new_post = response.json()
        post_content = new_post['content']
        if len(post_content) < 100:
            break
    except:
        continue

def post_to_channel(message):
    bot.send_message(CHANNEL_ID, message)
    print(f"Сообщение отправлено в канал: {message}")

if __name__ == '__main__':
    post_to_channel(post_content)
