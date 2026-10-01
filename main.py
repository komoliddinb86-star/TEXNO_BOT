from aiogram import Bot,Dispatcher,executor
from dotenv import load_dotenv
from aiogram.types import Message
import os
from keyboards import *
from texno_pars import pars_texno
from configs import *

load_dotenv()


TOKEN=os.getenv('TOKEN')

bot=Bot(TOKEN)

dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_star(message:Message):
    await  message.answer('Salom! Texnomartga xush kelibsiz')
    await  show_category_products(message)

async def show_category_products(message:Message):
    chat_id=message.chat.id
    await bot.send_message(chat_id,'Kategoriyani tanglang',
                           reply_markup=buttons_category())

@dp.message_handler(content_types=['text'])
async def get_products_by_category(message:Message):
    category_text=message.text
    get_products=pars_texno(get_values(category_text))


    for product in get_products:
        images=product.get('images')
        title=product.get('title')
        price=product.get('price')
        cred_price=product.get('cred_price')
        link=product.get('link')

        await  message.answer_photo(photo=images,parse_mode='HTML',caption=f"""
<b>{title}</b>\n\n
<i>{price}</i>\n
<i>{cred_price}</i>""",reply_markup=button_link(link))



executor.start_polling(dp)
