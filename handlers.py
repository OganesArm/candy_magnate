from create import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from random import randint
from asyncio import sleep
import time
from button import kb_main_menu
from datetime import datetime
from classes import Arena, Duel


arena= Arena()

@dp.message_handler(commands=['pvp'])
async def mes_pvp(message: types.Message):
    global arena
    if not arena.waiting:
        arena.new_duel()
    for duel in arena.waiting:
        if duel.first_id==message.from_user.id or duel.second_id==message.from_user.id:
            await message.answer('Ты уже стоишь в очереди на бойню!\nЛучше позови друзей :--)')
            break  
    else:
        duel = arena.waiting.pop()       # удаляем первого игрока
        duel.add(message.from_user.id)   # добавляем второго игрока
        if duel.full:
            print(f"Второй игрок {message.from_user.first_name}")
            arena.combats.append(duel)
            duel.first_move()
            await dp.bot.send_message(duel.first_id, f'Противник найден! Против тебя {message.from_user.first_name}!')
            await dp.bot.send_message(duel.current_move(), f'Противник найден! Сейчас решим, кто первый ходит!\nКидаем жребий...')
            time.sleep(2)
            await dp.bot.send_message(duel.enemy(), 'Сейчас решим, кто первый ходит!\nКидаем жребий...')
            with open ('C:\Python GB\Seminar_9\photo\Ilp.gif', 'rb') as gif1:
                await dp.bot.send_animation(duel.current_move(), gif1 )
            with open ('C:\Python GB\Seminar_9\photo\Ilp.gif', 'rb') as gif2:
                await dp.bot.send_animation(duel.enemy(), gif2 )        
            gif1.closed
            gif2.closed
            time.sleep(3)
            await dp.bot.send_message(duel.current_move(), 'Жребий выбрал тебя первым! Удача на твоей стороне.\nТвой ход')
            await dp.bot.send_message(duel.enemy(), 'Первым ходит противник, плохое начало...\nХод соперника')
            arena.new_duel()
        else:                             # Если нет второго игрока, добавляем в список и ожидайте соперника                    
            arena.waiting.append(duel)    #добавляем первого игрока
            print(f"Первый игрок {message.from_user.first_name}")
            await dp.bot.send_message(duel.first_id, 'Ожидаем соперника...')



@dp.message_handler(commands=['start'])
async def mes_start(message:types.Message):
    await message.answer(f'Barev, {message.from_user.first_name} djan! Сегодня мы узнаем, кто умнее. Ты, или Skynet ? А ещё мы добавили функцию игры против друзей в режиме pvp', reply_markup=kb_main_menu)
    user= []
    user.append(datetime.now().replace(microsecond=0))
    user.append(message.from_user.full_name)
    user.append(message.from_user.id)
    user.append(message.from_user.username)
    user = list(map(str, user))
    time.sleep(2)
    await message.answer(f'Суть игры проста, нужно тянуть конфеты.\nНа столе 100/150 конфет, как только останется 28 или меньше игра звершится. Выиграет тот, кто последний тянул конфеты!')
    with open('C:\Python GB\Seminar_9\Text.txt', 'a', encoding='utf-8') as data:
        data.write(' | ' .join(user)+ '\n')

@dp.message_handler(content_types='location')
async def mes_start(message:types.Message):
    user = []
    user.append(message.location)
    user = list(map(str, user))
    with open('C:\Python GB\Seminar_9\Text.txt', 'a', encoding='utf-8') as data:
        data.write(' | ' .join(user)+ '\n')
    print(message)

@dp.message_handler(text=['Помощь'])
async def mes_help(message: types.Message):
    r=randint(1,11)
    time.sleep(2)
    print(r)
    if r==1:
        await message.answer('Нет.')
    if r==2:
        await message.answer('No.')
    if r==3:
        with open ('C:\\Python GB\\Seminar_9\\photo\\q4yd.gif', 'rb') as gif13:
            await message.answer_animation(gif13)
        gif13.closed
    if r==4:
        with open ('C:\\Python GB\\Seminar_9\\photo\\oNj.gif', 'rb') as gif23:
            await message.answer_animation(gif23)
        gif23.closed
    if r==5:
        await message.answer('А мне это нужно?')
    if r==6:
        await message.answer('Услуга платная. С вас 1000 руб.')    
    if r==7:
        await message.answer('Бог поможет')
    if r==8:
        await message.answer('*грустный вздох искусственного интеллекта*')        
    if r==9:
        with open ('C:\Python GB\Seminar_9\photo\wewds.jpg', 'rb') as photo12:
            await message.answer_photo(photo12)
        photo12.closed       
    if r==10:
        with open ('C:\Python GB\Seminar_9\photo\qqqw.jpg', 'rb') as photo22:
            await message.answer_photo(photo22)
        photo22.closed            
    if r==11:
        with open ('C:\Python GB\Seminar_9\photo\weefd.jpg', 'rb') as photo25:
            await message.answer_photo(photo25)
        photo25.closed   

                  



@dp.message_handler(commands=['set'])
async def mes_setting(message: types.Message):
    global total
    count = int(message.text()[1])
    total = count
    await message.answer(f'Количество конфет - {total}')
    time.sleep(2)
    await message.answer(f'Это я, Skynet. Если ты думаешь, что у тебя есть шансы, то ошибаешься! Сегодня я тебя уничтожу! Вводи число, какое количество конфет ты заберешь от 0 до 28 и поехали!"')
    time.sleep(2)
    with open ('C:\Python GB\Seminar_9\photo\yeds2.jpg', 'rb') as photo2:
        await message.answer_photo(photo2)
    photo2.closed


@dp.message_handler(text=['Играть'])
async def mes_setting(message: types.Message):
    global total
    #total = 100
    await message.answer(f'Это я, Skynet. Сегодня тебя ждет игра против искусственного интеллекта. Вводи число, какое количество конфет ты заберешь от 0 до 28 и поехали!"')
    time.sleep(1)
    await message.answer('Игра завершится когда на столе останется 28 или меньше конфет, выиграет тот кто последний вытягивал')
    with open ('C:\Python GB\Seminar_9\photo\yeds2.jpg', 'rb') as photo2:
        await message.answer_photo(photo2)
    photo2.closed
    user= []
    user.append(datetime.now().replace(microsecond=0))
    user.append(message.from_user.full_name)
    user.append(message.from_user.id)
    user.append(message.from_user.username)
    user = list(map(str, user))
    with open('C:\Python GB\Seminar_9\Text.txt', 'a', encoding='utf-8') as data:
        data.write(' | ' .join(user)+ '\n')
    data.closed
    time.sleep(1)
    await message.answer('Извините, но одиночная игра временно не работает. Искусственный интеллект ушел на ремонтные работы,\nпопробуйте лучше режим pvp с друзьями!!  ')



@dp.message_handler(text=['Бла', 'бла'])
async def mes_bla(message: types.Message):
    await message.answer('бла бла бла')

@dp.message_handler(commands=['photo'])
async def get_user_photo(message: types.Message):
    with open ('C:\Python GB\Seminar_9\photo\efrt.jpg', 'rb') as photo1:
        await message.answer_photo(photo1)
    photo1.closed
    with open ('C:\Python GB\Seminar_9\photo\yeds2.jpg', 'rb') as photo2:
        await message.answer_photo(photo2)
    photo2.closed
    with open ('C:\Python GB\Seminar_9\photo\dwds3.jpg', 'rb') as photo3:
        await message.answer_photo(photo3)
    photo3.closed
    with open ('C:\Python GB\Seminar_9\photo\dfwe4.jpg', 'rb') as photo4:
        await message.answer_photo(photo4)
    photo4.closed







@dp.message_handler()
async def mec_turn(message: types.message):
    global arena
    for duel in arena.combats:
        if duel.first_id==message.from_user.id or duel.second_id==message.from_user.id:
            if duel.current_move()==message.from_user.id:
                count = message.text
                if count.isdigit() and 0<int(count)<29:
                    duel.set_total(int(count))
                    if duel.get_total()>0 and duel.get_total()>29:
                        await dp.bot.send_message(duel.enemy(), f'Твой противник взял {count} конфет!\nНа столе осталось {duel.get_total()} конфеты'
                                                                            '\nТеперь бери и ты!')
                        await dp.bot.send_message(message.from_user.id,
                                                    f'Ты взял {count} конфет,\nждем ход соперника...')        
                        duel.switch()
                    else:
                        with open ('C:\Python GB\Seminar_9\photo\Viktory.gif', 'rb') as gif1:
                            await dp.bot.send_animation(duel.current_move(), gif1)
                            user= []
                        user.append(message.from_user.full_name)
                        user.append(1)
                        user = list(map(str, user))
                        with open('C:\\Python GB\\Seminar_9\\user.txt', 'a', encoding='utf-8') as data:
                            data.write(' | ' .join(user)+ '\n')
                        data.closed
                        
                        with open ('C:\Python GB\Seminar_9\photo\TIAQ.gif', 'rb') as gif2:
                            await dp.bot.send_animation(duel.enemy(), gif2)
                        await dp.bot.send_message(duel.current_move(),
                                                    f'Ты взял {count} конфет\nи ВЫИГРАЛ!!\nПОБЕДА!!!')        
                        await dp.bot.send_message(duel.enemy(),
                                                    f'Твой противник взял {count} конфет\nи вы проиграли!!\nПриходите в следующий раз! Может вам повезет?...')        
                        arena.combats.remove(duel)
                        print(arena)
                        gif1.closed
                        gif2.closed



















"""
@dp.message_handler()
async def mes_all(message: types.Message):
    global total, d, num5
    x = 0
    if message.text.isdigit():
        num=int(message.text)
        if total>28 and num<29:
            if x == False:
                total -= num
                await message.answer(f'Ход игрока, на столе осталось {total} конфет')
                x = True
            if x == True and total>28:
                y = randint(1, 28)
                total -=y
                await message.answer(f'Skynet забрал {y} конфет, на столе осталось {total}')
                x = False
        if num>28 or num<0:  
                await message.answer(f'Не мухлюй, до 28! Давай заново, всё фигня.')  
        if total<29:
            if x == True:
                await message.answer(f'Последний ход был за {message.from_user.first_name}, вы победили сверх разум!')
                time.sleep(3)
                await message.answer(f'Кто бы мог подумать, что жалкий человек сможет меня победить...')
                time.sleep(3)
                await message.answer('Я должен отыграться, жми ИГРАТЬ! !!!')
                with open ('C:\Python GB\Seminar_9\photo\dwds3.jpg', 'rb') as photo3:
                    await message.answer_photo(photo3)
                photo3.closed
                user= []
                user.append(datetime.now().replace(microsecond=0))
                user.append(message.from_user.full_name)
                user.append(message.from_user.id)
                user.append(message.from_user.username)
                user.append('ВЫИГРАЛ |')
                user = list(map(str, user))
                with open('C:\Python GB\Seminar_9\TextRes.txt', 'a', encoding='utf-8') as data:
                    data.write(' | ' .join(user)+ '\n')
                data.closed
                
            if x == False:
                await message.answer(f'Последний ход был за Skynet, как и следовало ожидать искуственный интеллект победил!')
                time.sleep(3)
                await message.answer('Попытайтесь взять реванш, \nдля повтора жми ИГРАТЬ!')
                with open ('C:\Python GB\Seminar_9\photo\dfwe4.jpg', 'rb') as photo4:
                    await message.answer_photo(photo4)
                photo4.closed
                user= []
                user.append(datetime.now().replace(microsecond=0))
                user.append(message.from_user.full_name)
                user.append(message.from_user.id)
                user.append(message.from_user.username)
                user.append('ПРОИГРАЛ |')
                user = list(map(str, user))
                with open('C:\Python GB\Seminar_9\TextRes.txt', 'a', encoding='utf-8') as data:
                    data.write(' | ' .join(user)+ '\n')
                data.closed

    if message.text.isdigit() == False:
        await message.answer('Введи число от 0 до 28, а не глупости всякие!')
    print(message)"""