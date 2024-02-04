import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    filters.command("tnt")
    
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/679986673c48326b4ddb2.jpg",
        caption=f"""**⩹━★⊷━⌞  𝗡𝗢𝗢𝗥 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nانا بوت الذكاء الاصطناعي الخاص بسورس cr \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━★⊷━⌞  𝗡𝗢𝗢𝗥 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة الإستخدام", callback_data="O_F_4"), 
                 ],[
                    InlineKeyboardButton(
                        "مــطور السـورس ", url=f"https://t.me/O_F_4"),
                    InlineKeyboardButton(
                        "قـناه الكـود ", url=f"https://t.me/noordot"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞  السورس • قناه ⌝⚡", url=f"https://t.me/NO_VP8"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("O_F_4"))
async def cr_O_F_4(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━★⊷⌯⌞  𝗡𝗢𝗢𝗥 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⌯⊶★━⩺**
★¦ اهلا بك عزيزي في قسم الأوامر
★¦ لتتمكن من تشغيل الذكاء الاصطناعي فقط اكتب
★¦ /gpt - لـلـسـؤال آي سـؤال بالـذكـاء الاسـطـناعي

**⩹━★⊷⌯⌞  𝗡𝗢𝗢𝗥 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="back"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("طريقة الإستخدام", callback_data="tommm")],
            [InlineKeyboardButton("مــطور السـورس ", url=f"https://t.me/O_F_4"),
             InlineKeyboardButton("قـناه الكـود ", url=f"https://t.me/noordot")],
            [InlineKeyboardButton("★⌞  السورس • قناه ⌝⚡", url=f"https://t.me/NO_VP8")],
        ]
    ))

