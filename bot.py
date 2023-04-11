import time
import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = "" # add your Token here

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

logging.basicConfig(filename="name_rus_to_lat_bot_log",
                    level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

dict = {ord('А') : ord('A'), ord('Б') : ord('B'), 
        ord('В') : ord('V'), ord('Г') : ord('G'), 
        ord('Д') : ord('D'), ord('Е') : ord('E'),  
        ord('Ё') : ord('E'), 
        ord('Ж') : 'ZH', 
        ord('З') : ord('Z'), ord('И') : ord('I'), 
        ord('Й') : ord('I'), ord('К') : ord('K'),  
        ord('Л') : ord('L'), ord('М') : ord('M'), 
        ord('Н') : ord('N'), ord('О') : ord('O'),  
        ord('П') : ord('P'), ord('Р') : ord('R'), 
        ord('С') : ord('S'), ord('Т') : ord('T'), 
        ord('У') : ord('U'), ord('Ф') : ord('F'),
        ord('Х') : 'KH', 
        ord('Ц') : 'TS',
        ord('Ч') : 'CH', 
        ord('Ш') : 'SH', 
        ord('Щ') : 'SHCH', 
        ord('Ъ') : 'IE',  
        ord('Ы') : ord('Y'),  ord('Ь') : None,
        ord('Э') : ord('E'),  
        ord('Ю') : 'IU',  
        ord('Я') : 'IA'}

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_full_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'START: {user_id=} {user_full_name=} {time.asctime()}')
    await message.reply("Привет, введи имя для перевода!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    user_full_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'HELP: {user_id=} {user_full_name=} {time.asctime()}')
    await message.reply("Напиши мне имя на кирилице, и я его переведу в латиницу!")

@dp.message_handler()
async def echo_message(message: types.Message):
    user_full_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'TRANSLATE: {user_id=} {user_full_name=} {time.asctime()}')
    tranlatted_message = message.text.upper().translate(dict)
    await bot.send_message(user_id, tranlatted_message)

if __name__ == '__main__':
    executor.start_polling(dp)

