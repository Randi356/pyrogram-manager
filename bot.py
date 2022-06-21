# credits by @FFmpegNotInstalled
# code by https://github.com/Randi356/pyrogram-manager

from multiprocessing.connection import Client
from warnings import filters
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions # muted user
# from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Client(
    "my first projects",
    api_id = 
     123456,
    api_hash = "ask123",
    bot_token = "your_token_botftaher"
)

# START_MESSAGE = "Helo bot management"
# START_MESSGE_BUTTONS = [
#    [InlineKeyboardButton('CHANNEL', url='https://t.me/RendyProjects')]
# ]

# start // use input & filters.prviate
@bot.on_message(filters.command('start') & filters.private)
def start(bot, message):
    message.reply_text("selamat datang")
 #    text = START_MESSAGE
 #    reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS) # fixed buttons.append () inpurt str
 #   message.reply(
 #       text=text,
 #       reply_markup=reply_markup,
 #       disable_web_page_preview=True
 #       )

# helping
@bot.on_message(filters.command('help'))
def help(client, message):
    message.reply_text("kontol")

# welcome bot
GROUP = "testinggroupmods"
WELCOME_MESSAGE = "Hello, selamat datang!"
@bot.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcomebot(client, message):
    message.reply_text(WELCOME_MESSAGE)

# send photo
@bot.on_message(filters.command('photo'))
def send_photo(bot, message):
    bot.send_photo(message.chat.id, "") # input jpg

# send video
@bot.on_message(filters.command('video'))
def send_video(bot, message):
    bot.send_video(message.chat.id, "") # input mp4

# get audio id
@bot.on_message(filters.audio & filters.private)
def audio(bot, message):
    message.reply(message.audio.file_id)

@bot.on_message(filters.command('audio'))
def commad3(bot, message):
    bot.send_audio(message.chat.id, "") # input audio

# get stucker id
@bot.on_message(filters.sticker & filters.private)
def get_sticker(bot, message):
    message.reply(message.sticker.file_id)

@bot.on_message(filters.command('sticker'))
def commad4(bot, message):
    bot.send_sticker(message.chat.id, "") # input sticker

# get voice id
@bot.on_message(filters.voice & filters.private)
def get_voice(bot, message):
    message.reply(message.sticker.file_id)

@bot.on_message(filters.command('voice'))
def commad5(bot, message):
    bot.send_sticker(message.chat.id, "")

# blacklist text
@bot.on_message(filters.text)
def delete_text(bot, message):
 #     bot.delete_messages(message.chat.id, message.message_id)
     word_list = ["bokep", "goblok", "kontol"]
     if message.text in word_list:
        bot.delete_messages(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "blacklist kontol")

# group leave
@bot.on_message(filters.cmmand('leave'))
def leave(bot, message):
    bot.send_message(message.chat.id, "Bye! Fucking")
    bot.leave_chat(message.chat.id)

# hacking ban 
@bot.on_message(filters.command('ban') & filters.group)
def ban(bot, message):
    bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} whacking banned!")

# hacking kick
@bot.on_message(filters.command('kick') & filters.group)
def kick(bot, message):
    bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} whacking kicked!")


# hacking mute
@bot.on_message(filters.command('mute') & filters.group)
def mute(bot, message):
    bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions())
    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} whacking muted!")


print("bot running")
bot.run()
