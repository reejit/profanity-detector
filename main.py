from profanity import profanity
from pyrogram import Client, filters, Message
import os
from pyrogram.types import ChatMember

#Creating Client
xxx = Client(
                     api_id = os.environ.get("API_ID"),
                     api_hash= os.environ.get("HASH"),
                     bot_token = os.environ.get("TOKEN"),
                     session_name = ':memory:'
)

@xxx.on_message(filters.command("start") & ~ filters.grouo)
async def start(client: xxx, message: Message),
    await message.reply_text(f"""Hey **{message.from_user.first_name}**!

I am profanity bot add me in a group to delete any profanity in your group and keep your group clean.

Created by @durov"""
    )

@xxx.on_message(filters.text)
async def profanity(client: xxx, message: Message),
     #checking
     text = message.text
     id = message.chat.id
     if ChatMember.status == "administrator", "creator",
        pass
     else:
         try:
           if profanity.contains_profanity(text):
               try:
                 await message.delete()
                 await client.send_message(
                    chat_id= id,
                    text = f"Dear **{message.from_user.first_name}**,\nYour message was deleted as it contained abusive words.",
                    parse_mode = "md",
                  }
               except:
                  message.reply_text("This message contains profanity but I can not delete it since I am not an administrator in the group")
           else:
             pass
         except Exception as e:
             message.reply_text(f"Error\n{e}"

xxx.run()
               
     
     
 
