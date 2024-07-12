import os
import asyncio
import requests
import config
import random
import time
from config import START_IMG_URL
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from strings.filters import command
from MatrixMusic.utils.decorators import AdminActual
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint
#اتار.ي
lnk= "" +config.SUPPORT_CHANNEL

REPLY_MESSAGE = "<b>- اهلا بك عزيزي اليك قائمة اوامر التسلية .\n- اصدار السورس ~ 5.8V .\n- اصدار الكيبورد ~ 5.8V .</b>"

#اتاري
#v..vi.zi.n.n

REPLY_MESSAGE_BUTTONS = [

          [

             ("‹ غنيلي ›"),

             ("‹ شعر ›")
          ],

          [

             ("‹ صور ›"),

             ("‹ انمي ›")

          ],

          [

             ("‹ متحركة ›"),

             ("‹ اقتباسات ›")

          ],

          [

             ("‹ افتارات شباب ›"),

             ("‹ افتار بنات ›")

          ],

          [

             ("‹ هيدرات ›"),

             ("‹ قران ›")

          ],
    
          [

            ("‹ جداريات ›"),

            ("‹ لوكيت ›")
  #ا..تاري
#v..v....i.zi..n.n            
          ],
          [
            ("‹ افتارات سينمائية ›"),

            ("‹ افتارات فنانين ›")
              
          ],
          [
            ("‹ افلام ›"),

            ("‹ قيفات كوكسال ›")
              
          ],
          [
            ("‹ قيفات شباب ›"),

            ("‹ قيفات بنات ›")
              
          ],
          [
            ("‹ قيفات قطط ›"),

            ("‹ قيفات اطفال ›")
              
          ],
          [
            ("‹ قيفات رومانسية ›"),

            ("‹ قيفات كيبوب ›")
          ],
          [
             ("‹ ستوري ›"),

             ("‹ راب ›")
          ],
          [
             ("‹ فيديو ›"),

             ("‹ ريمكس ›")
          ],
          [
             ("‹ فويز ›"),
             ("• اخفاء الكيبورد •")

          ]

]

@app.on_message(filters.regex("^/cmds@ATARI2DBOT$") & filters.group)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("• اخفاء الكيبورد •") & filters.group)
async def down(client, message):
          m = await message.reply("<b>- تم اغلاق الكيبورد .</b>", reply_markup= ReplyKeyboardRemove(selective=True))
