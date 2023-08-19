import asyncio
import logging
from date.date import usercreate,userget
from keyboards.defoult import admincommands,adminusers,admin_interview
from keyboards.usersKeyboards import BoshMenu,interview,endstate,bekorqilish
from keyboards.inline import startpython, startdjango, startdrf, startjobinterview, rek, startphp, startlaravel, \
    startjava
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery


from date.date import interview_category_name,interview_answer
from date.fuzz import suniyintelekt,helpbot,bilmadim


from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")


#API_TOKEN = '6123719033:AAG-t3yeKsHdKIPEn2zvD4Zc-PKJdgP8A5k'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())

python = interview_category_name('python')
django = interview_category_name('django')
drf = interview_category_name('DRF')
jobinterview = interview_category_name('jobinterview')
php = interview_category_name('php')
laravel = interview_category_name('laravel')
java = interview_category_name('java')




class Python(StatesGroup):
    savol1 = State()
    savol2 = State()
    savol3 = State()
    savol4 = State()
    savol5 = State()
    savol6 = State()
    savol7 = State()
    savol8 = State()
    savol9 = State()
    savol10 = State()
    savol11 = State()
    savol12 = State()


class Django(StatesGroup):
    savol1 = State()
    savol2 = State()
    savol3 = State()
    savol4 = State()
    savol5 = State()
    savol6 = State()
    savol7 = State()
    savol8 = State()
    savol9 = State()
    savol10 = State()
    savol11 = State()



class DRF(StatesGroup):
    savol1 = State()
    savol2 = State()
    savol3 = State()
    savol4 = State()
    savol5 = State()
    savol6 = State()
    savol7 = State()
    savol8 = State()
    savol9 = State()
    savol10 = State()




class Job(StatesGroup):
    savol1 = State()
    savol2 = State()
    savol3 = State()
    savol4 = State()
    savol5 = State()
    savol6 = State()
    savol7 = State()
    savol8 = State()
    savol9 = State()
    savol10 = State()
    savol11 = State()
    savol12 = State()
    savol13 = State()
    savol14 = State()
    savol15 = State()
    savol16 = State()
    savol17 = State()
    savol18 = State()
    savol19 = State()



class Php(StatesGroup):
    savol1 = State()
    savol2 = State()
    savol3 = State()
    savol4 = State()
    savol5 = State()
    savol6 = State()
    savol7 = State()
    savol8 = State()



class Laravel(StatesGroup):
    savol1 = State()
    savol2 = State()
    savol3 = State()
    savol4 = State()
    savol5 = State()





class Java(StatesGroup):
    savol1 = State()
    savol2 = State()
    savol3 = State()
    savol4 = State()
    savol5 = State()
    savol6 = State()
    savol7 = State()
    savol8 = State()
    savol9 = State()
    savol10 = State()



class Fikr(StatesGroup):
    habar = State()


class Javob_qaytarish(StatesGroup):
    id = State()
    javob = State()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    username = message.from_user.username
    user_id = message.from_user.id

    usercreate(first_name, username, user_id)
    if message.from_user.id == 1363350178:
        await bot.send_message(chat_id=1363350178, text='Siz adminsiz', reply_markup=admincommands)

    else:
        await message.reply(f"Salom\nKerakli bo'limni tanlang. {message.from_user.first_name}",reply_markup=interview,parse_mode="HTML")
        await bot.send_message(chat_id=1363350178,text=f"{message.from_user.first_name} botga /start bosdi")


@dp.message_handler(commands=['start'],state='*')
async def startstate(message: types.Message):
    await message.answer(f"Savollarga javob berishda davom eting!")



@dp.message_handler(commands=['help'],state='*')
async def helpstate(message: types.Message):
    await message.answer(f"{helpbot()}")




@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(f"{helpbot()}")




@dp.message_handler(text="🚫 Bekor qilish",state=Fikr.habar)
async def habar_end(message: types.Message, state: FSMContext):

    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)

    await state.finish()

    await message.answer("Kerakli bo'limni tanlashingiz mumkun!", reply_markup=interview)



@dp.message_handler(text="🗯️ Fikr bildirish")
async def fikrqoldirish(message: types.Message):
    await message.answer("Taklif va murojaatlaringizni qoldirishingiz mumkin!",reply_markup=bekorqilish)
    await Fikr.habar.set()





@dp.message_handler(state=Fikr.habar)
async def message_user(message: types.Message, state: FSMContext):
    msg = f"{message.from_user.first_name}--@{message.from_user.username}--{message.from_user.id}\n\n"
    msg += f"Habar: -> {message.text}"
    await bot.send_message(chat_id=1363350178,text=msg)
    await state.finish()
    await message.answer("✔️Muvaffaqiyatli yuborildi!",reply_markup=interview)



@dp.message_handler(text="Javob")
async def Javob_berish(message: types.Message):
    await message.answer("javob yozish uchun chat_id kiriting:")
    await Javob_qaytarish.id.set()


@dp.message_handler(state=Javob_qaytarish.id)
async def answer_admin_id(message: types.Message, state: FSMContext):
    id = message.text
    await state.update_data(
        {"chat_id": id}
    )
    await message.answer("javob yozish uchun text kiriting:")
    await Javob_qaytarish.next()


@dp.message_handler(state=Javob_qaytarish.javob)
async def answer_admin_text(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(
        {"text": text}
    )

    data = await state.get_data()
    user_id = data.get("chat_id")
    admin_text = data.get("text")


    try:
        await bot.send_message(chat_id=user_id,text=admin_text)

        await state.finish()
        await bot.send_message(chat_id=1363350178, text="✔️Muvaffaqiyatli yuborildi!")
    except Exception as e:
        await bot.send_message(chat_id=1363350178,text=f"Hato: {e}")
        await state.finish()


@dp.message_handler(text="interviews",chat_id=1363350178)
async def userinterview(message: types.Message):

    await message.answer('interviews',reply_markup=admin_interview)



@dp.message_handler(text="back")
async def userback(message: types.Message):
    if message.from_user.id == 1363350178:
        await message.answer('Bosh menyu', reply_markup=admincommands)
    # else:
    #     await message.answer('Main menu',reply_markup=BoshMenu)


# Interview commands





@dp.message_handler(text="end interview",state='*')
async def stateend(message: types.Message, state: FSMContext):

    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)

    await state.finish()
    if message.from_user.id == 1363350178:
        await message.answer("admin interview",reply_markup=admin_interview)
    else:
        await message.answer("Intervyu tugadi ❌", reply_markup=interview)




# python state

@dp.message_handler(text="Python")
async def pythoninterview(message: types.Message):
    await message.answer("Python interview savollari!\nSavollar soni: 12 ta",reply_markup=startpython)



@dp.callback_query_handler(text="python",state=None)
async def start_question(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Boshladik ✅ Javobni text shakilda yuboring ‼️",reply_markup=endstate)
    await call.message.answer(f"1-Savol ❗️\n{python[0]['question']} ?")
    await call.answer(cache_time=60)
    await Python.savol1.set()


@dp.message_handler(state=Python.savol1)
async def answer1(message: types.Message, state: FSMContext):
    javob1 = message.text
    javoblar = interview_answer(python[0]['question'])
    oxshash = suniyintelekt(javob1,javoblar)

    await bot.send_message(chat_id=1363350178,text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                   f"{python[0]['question']} ?--{oxshash}\n\n{javob1}")


    if len(javob1) > 10 and oxshash > 40:
        await state.update_data(
            {"javob1": javob1,"oxshash1":oxshash}
        )

        await message.answer(f"2-Savol ❗️\n{python[1]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")




@dp.message_handler(state=Python.savol2)
async def answer2(message: types.Message, state: FSMContext):
    javob2 = message.text
    javoblar = interview_answer(python[1]['question'])
    oxshash = suniyintelekt(javob2, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{python[1]['question']} ?--{oxshash}\n\n{javob2}")

    if len(javob2) > 15 and oxshash > 40:
        await state.update_data(
            {"javob2": javob2,"oxshash2":oxshash}
        )

        await message.answer(f"3-Savol ❗️\n{python[2]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol3)
async def answer3(message: types.Message, state: FSMContext):
    javob3 = message.text
    javoblar = interview_answer(python[2]['question'])
    oxshash = suniyintelekt(javob3, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{python[2]['question']} ?--{oxshash}\n\n{javob3}")

    if len(javob3) > 15 and oxshash > 40:
        await state.update_data(
            {"javob3": javob3,"oxshash3":oxshash}
        )

        await message.answer(f"4-Savol ❗️\n{python[3]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol4)
async def answer4(message: types.Message, state: FSMContext):
    javob4 = message.text
    javoblar = interview_answer(python[3]['question'])
    oxshash = suniyintelekt(javob4, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{python[3]['question']} ?--{oxshash}\n\n{javob4}")

    if len(javob4) > 15 and oxshash > 40:
        await state.update_data(
            {"javob4": javob4,"oxshash4":oxshash}
        )

        await message.answer(f"5-Savol ❗️\n{python[4]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol5)
async def answer5(message: types.Message, state: FSMContext):
    javob5 = message.text
    javoblar = interview_answer(python[4]['question'])
    oxshash = suniyintelekt(javob5, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{python[4]['question']} ?--{oxshash}\n\n{javob5}")

    if len(javob5) > 15 and oxshash > 40:
        await state.update_data(
            {"javob5": javob5,"oxshash5":oxshash}
        )

        await message.answer(f"6-Savol ❗️\n{python[5]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol6)
async def answer6(message: types.Message, state: FSMContext):
    javob6 = message.text
    javoblar = interview_answer(python[5]['question'])
    oxshash = suniyintelekt(javob6, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{python[5]['question']} ?--{oxshash}\n\n{javob6}")

    if len(javob6) > 15 and oxshash > 40:
        await state.update_data(
            {"javob6": javob6,"oxshash6":oxshash}
        )

        await message.answer(f"7-Savol ❗️\n{python[6]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol7)
async def answer7(message: types.Message, state: FSMContext):
    javob7 = message.text
    javoblar = interview_answer(python[6]['question'])
    oxshash = suniyintelekt(javob7, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{python[6]['question']} ?--{oxshash}\n\n{javob7}")

    if len(javob7) > 15 and oxshash > 40:
        await state.update_data(
            {"javob7": javob7,"oxshash7":oxshash}
        )

        await message.answer(f"8-Savol ❗️\n{python[7]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Python.savol8)
async def answer8(message: types.Message, state: FSMContext):
    javob8 = message.text
    javoblar = interview_answer(python[7]['question'])
    oxshash = suniyintelekt(javob8, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{python[7]['question']} ?--{oxshash}\n\n{javob8}")

    if len(javob8) > 15 and oxshash > 40:
        await state.update_data(
            {"javob8": javob8,"oxshash8":oxshash}
        )

        await message.answer(f"9-Savol ❗️\n{python[8]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol9)
async def answer9(message: types.Message, state: FSMContext):
    javob9 = message.text
    javoblar = interview_answer(python[8]['question'])
    oxshash = suniyintelekt(javob9, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{python[8]['question']} ?--{oxshash}\n\n{javob9}")

    if len(javob9) > 15 and oxshash > 40:
        await state.update_data(
            {"javob9": javob9,"oxshash9":oxshash}
        )

        await message.answer(f"10-Savol ❗️\n{python[9]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Python.savol10)
async def answer10(message: types.Message, state: FSMContext):
    javob10 = message.text
    javoblar = interview_answer(python[9]['question'])
    oxshash = suniyintelekt(javob10, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{python[9]['question']} ?--{oxshash}\n\n{javob10}")

    if len(javob10) > 15 and oxshash > 40:
        await state.update_data(
            {"javob10": javob10,"oxshash10":oxshash}
        )

        await message.answer(f"11-Savol ❗️\n{python[10]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Python.savol11)
async def answer11(message: types.Message, state: FSMContext):
    javob11 = message.text
    javoblar = interview_answer(python[10]['question'])
    oxshash = suniyintelekt(javob11, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{python[10]['question']} ?--{oxshash}\n\n{javob11}")

    if len(javob11) > 15 and oxshash > 40:
        await state.update_data(
            {"javob11": javob11,"oxshash11":oxshash}
        )

        await message.answer(f"12-Savol ❗️\n{python[11]['question']} ?")

        await Python.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")




@dp.message_handler(state=Python.savol12)
async def answer12(message: types.Message, state: FSMContext):
    javob12 = message.text
    javoblar = interview_answer(python[11]['question'])
    oxshash = suniyintelekt(javob12, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{python[11]['question']} ?--{oxshash}\n\n{javob12}")

    if len(javob12) > 15 and oxshash > 40:
        await state.update_data(
            {"javob12": javob12,"oxshash12":oxshash}
        )

        # Ma`lumotlarni qayta o'qiymiz
        data = await state.get_data()
        javob1 = data.get("javob1")
        oxshash1 = data.get("oxshash1")
        javob2 = data.get("javob2")
        oxshash2 = data.get("oxshash2")
        javob3 = data.get("javob3")
        oxshash3 = data.get("oxshash3")
        javob4 = data.get("javob4")
        oxshash4 = data.get("oxshash4")
        javob5 = data.get("javob5")
        oxshash5 = data.get("oxshash5")
        javob6 = data.get("javob6")
        oxshash6 = data.get("oxshash6")
        javob7 = data.get("javob7")
        oxshash7 = data.get("oxshash7")
        javob8 = data.get("javob8")
        oxshash8 = data.get("oxshash8")
        javob9 = data.get("javob9")
        oxshash9 = data.get("oxshash9")
        javob10 = data.get("javob10")
        oxshash10 = data.get("oxshash10")
        javob11 = data.get("javob11")
        oxshash11 = data.get("oxshash11")
        javob12 = data.get("javob12")
        oxshash12 = data.get("oxshash12")

        sum = oxshash1+oxshash2+oxshash3+oxshash4+oxshash5+oxshash6+oxshash7+oxshash8+oxshash9+oxshash10+oxshash11+oxshash12


        msg1 = f"{message.from_user.first_name} ning natijasi: {sum//12}\n\n"
        msg1 += f"javob1: - {oxshash1}--{javob1}\n\n"
        msg1 += f"javob2: - {oxshash2}--{javob2}\n\n"
        msg1 += f"javob3: - {oxshash3}--{javob3}\n\n"
        msg2 = f"{message.from_user.first_name} ning natijasi: {sum // 12}\n\n"
        msg2 += f"javob4: - {oxshash4}--{javob4}\n\n"
        msg2 += f"javob5: - {oxshash5}--{javob5}\n\n"
        msg2 += f"javob6: - {oxshash6}--{javob6}\n\n"
        msg3 = f"{message.from_user.first_name} ning natijasi: {sum // 12}\n\n"
        msg3 += f"javob7: - {oxshash7}--{javob7}\n\n"
        msg3 += f"javob8: - {oxshash8}--{javob8}\n\n"
        msg3 += f"javob9: - {oxshash9}--{javob9}\n\n"
        msg4 = f"{message.from_user.first_name} ning natijasi: {sum // 12}\n\n"
        msg4 += f"javob10: - {oxshash10}--{javob10}\n\n"
        msg4 += f"javob11: - {oxshash11}--{javob11}\n\n"
        msg4 += f"javob12: - {oxshash12}--{javob12}"


        msg = f"{message.from_user.first_name} ning natijasi: {sum//12}\n\n"
        msg += f"{msg1}\n{msg2}\n{msg3}\n{msg4}"


        if len(msg) < 4000:
            await bot.send_message(chat_id=1363350178,text=msg)
        elif len(msg) > 4000:
            try:
                await bot.send_message(chat_id=1363350178, text=msg1)
                await bot.send_message(chat_id=1363350178, text=msg2)
                await bot.send_message(chat_id=1363350178, text=msg3)
                await bot.send_message(chat_id=1363350178, text=msg4)
            except Exception as e:
                await bot.send_message(chat_id=1363350178, text=f"Xato: {e}")
        else:
            await bot.send_message(chat_id=1363350178, text='Yuborishda hato boldi')


        await message.answer(f"Intervyu yakunlandi ✅ \n\nBarcha savollarga qoniqarli javob berdingiz 👏",reply_markup=interview)

        await state.finish()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


#end python state


# django state
@dp.message_handler(text="Django")
async def djangointerview(message: types.Message):

    await message.answer("Django interview savollari!\nSavollar soni: 11 ta",reply_markup=startdjango)


@dp.callback_query_handler(text="django",state=None)
async def start_question_django(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Boshladik ✅ Javobni text shakilda yuboring ‼️",reply_markup=endstate)
    await call.message.answer(f"1-Savol ❗️\n{django[0]['question']} ?")
    await call.answer(cache_time=60)
    await Django.savol1.set()



@dp.message_handler(state=Django.savol1)
async def django_answer1(message: types.Message, state: FSMContext):
    javob1 = message.text
    javoblar = interview_answer(django[0]['question'])
    oxshash = suniyintelekt(javob1,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{django[0]['question']} ?--{oxshash}\n\n{javob1}")


    if len(javob1) > 15 and oxshash > 30:
        await state.update_data(
            {"javob1": javob1,"oxshash1":oxshash}
        )

        await message.answer(f"2-Savol ❗️\n{django[1]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Django.savol2)
async def django_answer2(message: types.Message, state: FSMContext):
    javob2 = message.text
    javoblar = interview_answer(django[1]['question'])
    oxshash = suniyintelekt(javob2,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{django[1]['question']} ?--{oxshash}\n\n{javob2}")


    if len(javob2) > 15 and oxshash > 30:
        await state.update_data(
            {"javob2": javob2,"oxshash2":oxshash}
        )

        await message.answer(f"3-Savol ❗️\n{django[2]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Django.savol3)
async def django_answer3(message: types.Message, state: FSMContext):
    javob3 = message.text
    javoblar = interview_answer(django[2]['question'])
    oxshash = suniyintelekt(javob3,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{django[2]['question']} ?--{oxshash}\n\n{javob3}")


    if len(javob3) > 15 and oxshash > 30:
        await state.update_data(
            {"javob3": javob3,"oxshash3":oxshash}
        )

        await message.answer(f"4-Savol ❗️\n{django[3]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Django.savol4)
async def django_answer4(message: types.Message, state: FSMContext):
    javob4 = message.text
    javoblar = interview_answer(django[3]['question'])
    oxshash = suniyintelekt(javob4,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{django[3]['question']} ?--{oxshash}\n\n{javob4}")


    if len(javob4) > 15 and oxshash > 30:
        await state.update_data(
            {"javob4": javob4,"oxshash4":oxshash}
        )

        await message.answer(f"5-Savol ❗️\n{django[4]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Django.savol5)
async def django_answer5(message: types.Message, state: FSMContext):
    javob5 = message.text
    javoblar = interview_answer(django[4]['question'])
    oxshash = suniyintelekt(javob5,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{django[4]['question']} ?--{oxshash}\n\n{javob5}")


    if len(javob5) > 15 and oxshash > 30:
        await state.update_data(
            {"javob5": javob5,"oxshash5":oxshash}
        )

        await message.answer(f"6-Savol ❗️\n{django[5]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")

@dp.message_handler(state=Django.savol6)
async def django_answer6(message: types.Message, state: FSMContext):
    javob6 = message.text
    javoblar = interview_answer(django[5]['question'])
    oxshash = suniyintelekt(javob6,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{django[5]['question']} ?--{oxshash}\n\n{javob6}")


    if len(javob6) > 15 and oxshash > 30:
        await state.update_data(
            {"javob6": javob6,"oxshash6":oxshash}
        )

        await message.answer(f"7-Savol ❗️\n{django[6]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")

@dp.message_handler(state=Django.savol7)
async def django_answer7(message: types.Message, state: FSMContext):
    javob7 = message.text
    javoblar = interview_answer(django[6]['question'])
    oxshash = suniyintelekt(javob7,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{django[6]['question']} ?--{oxshash}\n\n{javob7}")


    if len(javob7) > 15 and oxshash > 30:
        await state.update_data(
            {"javob7": javob7,"oxshash7":oxshash}
        )

        await message.answer(f"8-Savol ❗️\n{django[7]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Django.savol8)
async def django_answer8(message: types.Message, state: FSMContext):
    javob8 = message.text
    javoblar = interview_answer(django[7]['question'])
    oxshash = suniyintelekt(javob8,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{django[7]['question']} ?--{oxshash}\n\n{javob8}")


    if len(javob8) > 15 and oxshash > 30:
        await state.update_data(
            {"javob8": javob8,"oxshash8":oxshash}
        )

        await message.answer(f"9-Savol ❗️\n{django[8]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Django.savol9)
async def django_answer9(message: types.Message, state: FSMContext):
    javob9 = message.text
    javoblar = interview_answer(django[8]['question'])
    oxshash = suniyintelekt(javob9,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{django[8]['question']} ?--{oxshash}\n\n{javob9}")


    if len(javob9) > 15 and oxshash > 30:
        await state.update_data(
            {"javob9": javob9,"oxshash9":oxshash}
        )

        await message.answer(f"10-Savol ❗️\n{django[9]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Django.savol10)
async def django_answer10(message: types.Message, state: FSMContext):
    javob10 = message.text
    javoblar = interview_answer(django[9]['question'])
    oxshash = suniyintelekt(javob10,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{django[9]['question']} ?--{oxshash}\n\n{javob10}")


    if len(javob10) > 15 and oxshash > 30:
        await state.update_data(
            {"javob10": javob10,"oxshash10":oxshash}
        )

        await message.answer(f"11-Savol ❗️\n{django[10]['question']} ?")

        await Django.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Django.savol11)
async def django_answer11(message: types.Message, state: FSMContext):
    javob11 = message.text
    javoblar = interview_answer(django[10]['question'])
    oxshash = suniyintelekt(javob11, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{django[10]['question']} ?--{oxshash}\n\n{javob11}")

    if len(javob11) > 15 and oxshash > 30:
        await state.update_data(
            {"javob11": javob11,"oxshash11":oxshash}
        )

        # Ma`lumotlarni qayta o'qiymiz
        data = await state.get_data()
        javob1 = data.get("javob1")
        oxshash1 = data.get("oxshash1")
        javob2 = data.get("javob2")
        oxshash2 = data.get("oxshash2")
        javob3 = data.get("javob3")
        oxshash3 = data.get("oxshash3")
        javob4 = data.get("javob4")
        oxshash4 = data.get("oxshash4")
        javob5 = data.get("javob5")
        oxshash5 = data.get("oxshash5")
        javob6 = data.get("javob6")
        oxshash6 = data.get("oxshash6")
        javob7 = data.get("javob7")
        oxshash7 = data.get("oxshash7")
        javob8 = data.get("javob8")
        oxshash8 = data.get("oxshash8")
        javob9 = data.get("javob9")
        oxshash9 = data.get("oxshash9")
        javob10 = data.get("javob10")
        oxshash10 = data.get("oxshash10")
        javob11 = data.get("javob11")
        oxshash11 = data.get("oxshash11")

        sum = oxshash1 + oxshash2 + oxshash3 + oxshash4 + oxshash5 + oxshash6 + oxshash7 + oxshash8 + oxshash9 + oxshash10 + oxshash11

        msg1 = f"{message.from_user.first_name} ning natijasi: {sum // 11}\n\n"
        msg1 += f"javob1: - {oxshash1}--{javob1}\n\n"
        msg1 += f"javob2: - {oxshash2}--{javob2}\n\n"
        msg1 += f"javob3: - {oxshash3}--{javob3}\n\n"
        msg2 = f"{message.from_user.first_name} ning natijasi: {sum // 11}\n\n"
        msg2 += f"javob4: - {oxshash4}--{javob4}\n\n"
        msg2 += f"javob5: - {oxshash5}--{javob5}\n\n"
        msg2 += f"javob6: - {oxshash6}--{javob6}\n\n"
        msg3 = f"{message.from_user.first_name} ning natijasi: {sum // 11}\n\n"
        msg3 += f"javob7: - {oxshash7}--{javob7}\n\n"
        msg3 += f"javob8: - {oxshash8}--{javob8}\n\n"
        msg3 += f"javob9: - {oxshash9}--{javob9}\n\n"
        msg4 = f"{message.from_user.first_name} ning natijasi: {sum // 11}\n\n"
        msg4 += f"javob10: - {oxshash10}--{javob10}\n\n"
        msg4 += f"javob11: - {oxshash11}--{javob11}\n\n"


        msg = f"{message.from_user.first_name} ning natijasi: {sum // 11}\n\n"
        msg += f"{msg1}\n{msg2}\n{msg3}\n{msg4}"

        if len(msg) < 4000:
            await bot.send_message(chat_id=1363350178, text=msg)
        elif len(msg) > 4000:
            try:
                await bot.send_message(chat_id=1363350178, text=msg1)
                await bot.send_message(chat_id=1363350178, text=msg2)
                await bot.send_message(chat_id=1363350178, text=msg3)
                await bot.send_message(chat_id=1363350178, text=msg4)
            except Exception as e:
                await bot.send_message(chat_id=1363350178, text=f"Xato: {e}")
        else:
            await bot.send_message(chat_id=1363350178, text='Yuborishda hato boldi')

        await message.answer(f"Intervyu yakunlandi ✅ \n\nBarcha savollarga qoniqarli javob berdingiz 👏\nNatija: {sum//11} %", reply_markup=interview)

        await state.finish()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


#end django state



# DRF state

@dp.message_handler(text="DRF")
async def drfinterview(message: types.Message):

    await message.answer("DRF interview savollari!\nSavollar soni: 10 ta",reply_markup=startdrf)


@dp.callback_query_handler(text="drf",state=None)
async def start_question_drf(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Boshladik ✅ Javobni text shakilda yuboring ‼️",reply_markup=endstate)
    await call.message.answer(f"1-Savol ❗️\n{drf[0]['question']} ?")
    await call.answer(cache_time=60)
    await DRF.savol1.set()



@dp.message_handler(state=DRF.savol1)
async def drf_answer1(message: types.Message, state: FSMContext):
    javob1 = message.text
    javoblar = interview_answer(drf[0]['question'])
    oxshash = suniyintelekt(javob1,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{drf[0]['question']} ?--{oxshash}\n\n{javob1}")


    if len(javob1) > 15 and oxshash > 30:
        await state.update_data(
            {"javob1": javob1,"oxshash1":oxshash}
        )

        await message.answer(f"2-Savol ❗️\n{drf[1]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol2)
async def drf_answer2(message: types.Message, state: FSMContext):
    javob2 = message.text
    javoblar = interview_answer(drf[1]['question'])
    oxshash = suniyintelekt(javob2,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{drf[1]['question']} ?--{oxshash}\n\n{javob2}")


    if len(javob2) > 15 and oxshash > 30:
        await state.update_data(
            {"javob2": javob2,"oxshash2":oxshash}
        )

        await message.answer(f"3-Savol ❗️\n{drf[2]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol3)
async def drf_answer3(message: types.Message, state: FSMContext):
    javob3 = message.text
    javoblar = interview_answer(drf[2]['question'])
    oxshash = suniyintelekt(javob3,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{drf[2]['question']} ?--{oxshash}\n\n{javob3}")


    if len(javob3) > 15 and oxshash > 30:
        await state.update_data(
            {"javob3": javob3,"oxshash3":oxshash}
        )

        await message.answer(f"4-Savol ❗️\n{drf[3]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol4)
async def drf_answer4(message: types.Message, state: FSMContext):
    javob4 = message.text
    javoblar = interview_answer(drf[3]['question'])
    oxshash = suniyintelekt(javob4,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{drf[3]['question']} ?--{oxshash}\n\n{javob4}")


    if len(javob4) > 15 and oxshash > 30:
        await state.update_data(
            {"javob4": javob4,"oxshash4":oxshash}
        )

        await message.answer(f"5-Savol ❗️\n{drf[4]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")

@dp.message_handler(state=DRF.savol5)
async def drf_answer5(message: types.Message, state: FSMContext):
    javob5 = message.text
    javoblar = interview_answer(drf[4]['question'])
    oxshash = suniyintelekt(javob5,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{drf[4]['question']} ?--{oxshash}\n\n{javob5}")


    if len(javob5) > 15 and oxshash > 30:
        await state.update_data(
            {"javob5": javob5,"oxshash5":oxshash}
        )

        await message.answer(f"6-Savol ❗️\n{drf[5]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol6)
async def drf_answer6(message: types.Message, state: FSMContext):
    javob6 = message.text
    javoblar = interview_answer(drf[5]['question'])
    oxshash = suniyintelekt(javob6,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{drf[5]['question']} ?--{oxshash}\n\n{javob6}")


    if len(javob6) > 15 and oxshash > 30:
        await state.update_data(
            {"javob6": javob6,"oxshash6":oxshash}
        )

        await message.answer(f"7-Savol ❗️\n{drf[6]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol7)
async def drf_answer7(message: types.Message, state: FSMContext):
    javob7 = message.text
    javoblar = interview_answer(drf[6]['question'])
    oxshash = suniyintelekt(javob7,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{drf[6]['question']} ?--{oxshash}\n\n{javob7}")


    if len(javob7) > 15 and oxshash > 30:
        await state.update_data(
            {"javob7": javob7,"oxshash7":oxshash}
        )

        await message.answer(f"8-Savol ❗️\n{drf[7]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol8)
async def drf_answer8(message: types.Message, state: FSMContext):
    javob8 = message.text
    javoblar = interview_answer(drf[7]['question'])
    oxshash = suniyintelekt(javob8,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{drf[7]['question']} ?--{oxshash}\n\n{javob8}")


    if len(javob8) > 15 and oxshash > 30:
        await state.update_data(
            {"javob8": javob8,"oxshash8":oxshash}
        )

        await message.answer(f"9-Savol ❗️\n{drf[8]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol9)
async def drf_answer9(message: types.Message, state: FSMContext):
    javob9 = message.text
    javoblar = interview_answer(drf[8]['question'])
    oxshash = suniyintelekt(javob9,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{drf[8]['question']} ?--{oxshash}\n\n{javob9}")


    if len(javob9) > 15 and oxshash > 30:
        await state.update_data(
            {"javob9": javob9,"oxshash9":oxshash}
        )

        await message.answer(f"10-Savol ❗️\n{drf[9]['question']} ?")

        await DRF.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=DRF.savol10)
async def drf_answer10(message: types.Message, state: FSMContext):
    javob10 = message.text
    javoblar = interview_answer(drf[9]['question'])
    oxshash = suniyintelekt(javob10, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{drf[9]['question']} ?--{oxshash}\n\n{javob10}")

    if len(javob10) > 15 and oxshash > 30:
        await state.update_data(
            {"javob10": javob10,"oxshash10":oxshash}
        )

        # Ma`lumotlarni qayta o'qiymiz
        data = await state.get_data()
        javob1 = data.get("javob1")
        oxshash1 = data.get("oxshash1")
        javob2 = data.get("javob2")
        oxshash2 = data.get("oxshash2")
        javob3 = data.get("javob3")
        oxshash3 = data.get("oxshash3")
        javob4 = data.get("javob4")
        oxshash4 = data.get("oxshash4")
        javob5 = data.get("javob5")
        oxshash5 = data.get("oxshash5")
        javob6 = data.get("javob6")
        oxshash6 = data.get("oxshash6")
        javob7 = data.get("javob7")
        oxshash7 = data.get("oxshash7")
        javob8 = data.get("javob8")
        oxshash8 = data.get("oxshash8")
        javob9 = data.get("javob9")
        oxshash9 = data.get("oxshash9")
        javob10 = data.get("javob10")
        oxshash10 = data.get("oxshash10")


        sum = oxshash1 + oxshash2 + oxshash3 + oxshash4 + oxshash5 + oxshash6 + oxshash7 + oxshash8 + oxshash9 + oxshash10

        msg1 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg1 += f"<b> javob1: - {oxshash1}</b>--{javob1}\n\n"
        msg1 += f"<b> javob2: - {oxshash2}</b>--{javob2}\n\n"
        msg1 += f"<b> javob3: - {oxshash3}</b>--{javob3}\n\n"
        msg2 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg2 += f"<b>javob4: - {oxshash4}</b>--{javob4}\n\n"
        msg2 += f"<b>javob5: - {oxshash5}</b>--{javob5}\n\n"
        msg2 += f"<b>javob6: - {oxshash6}</b>--{javob6}\n\n"
        msg3 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg3 += f"<b>javob7: - {oxshash7}</b>--{javob7}\n\n"
        msg3 += f"<b>javob8: - {oxshash8}</b>--{javob8}\n\n"
        msg3 += f"<b>javob9: - {oxshash9}</b>--{javob9}\n\n"
        msg4 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg4 += f"<b>javob10: - {oxshash10}</b>--{javob10}\n\n"


        msg = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg += f"{msg1}\n{msg2}\n{msg3}\n{msg4}"

        if len(msg) < 4000:
            await bot.send_message(chat_id=1363350178, text=msg,parse_mode='HTML')
        elif len(msg) > 4000:
            try:
                await bot.send_message(chat_id=1363350178, text=msg1,parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg2,parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg3,parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg4,parse_mode='HTML')
            except Exception as e:
                await bot.send_message(chat_id=1363350178, text=f"Xato: {e}")
        else:
            await bot.send_message(chat_id=1363350178, text='Yuborishda hato boldi')

        await message.answer(f"Intervyu yakunlandi ✅ \n\nBarcha savollarga qoniqarli javob berdingiz 👏\nNatija: {sum//10} %", reply_markup=interview)

        await state.finish()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


# end DRF state

# jobinterview state

@dp.message_handler(text="Job interview")
async def jobinterview_f(message: types.Message):

    await message.answer("Job interview savollari!\nSavollar soni: 18 ta",reply_markup=startjobinterview)


@dp.callback_query_handler(text="jobinterview",state=None)
async def start_question_job(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Boshladik ✅ Javobni text shakilda yuboring ‼️",reply_markup=endstate)
    await call.message.answer(f"1-Savol ❗️\n{jobinterview[0]['question']} ?")
    await call.answer(cache_time=60)
    await Job.savol1.set()



@dp.message_handler(state=Job.savol1)
async def job_answer1(message: types.Message, state: FSMContext):
    javob1 = message.text
    javoblar = interview_answer(jobinterview[0]['question'])
    oxshash = suniyintelekt(javob1,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[0]['question']} ?--{oxshash}\n\n{javob1}")


    if len(javob1) > 15 and oxshash > 30:
        await state.update_data(
            {"javob1": javob1,"oxshash1":oxshash}
        )

        await message.answer(f"2-Savol ❗️\n{jobinterview[1]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol2)
async def job_answer2(message: types.Message, state: FSMContext):
    javob2 = message.text
    javoblar = interview_answer(jobinterview[1]['question'])
    oxshash = suniyintelekt(javob2,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[1]['question']} ?--{oxshash}\n\n{javob2}")


    if len(javob2) > 15 and oxshash > 30:
        await state.update_data(
            {"javob2": javob2,"oxshash2":oxshash}
        )

        await message.answer(f"3-Savol ❗️\n{jobinterview[2]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Job.savol3)
async def job_answer3(message: types.Message, state: FSMContext):
    javob3 = message.text
    javoblar = interview_answer(jobinterview[2]['question'])
    oxshash = suniyintelekt(javob3,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[2]['question']} ?--{oxshash}\n\n{javob3}")


    if len(javob3) > 15 and oxshash > 30:
        await state.update_data(
            {"javob3": javob3,"oxshash3":oxshash}
        )

        await message.answer(f"4-Savol ❗️\n{jobinterview[3]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol4)
async def job_answer4(message: types.Message, state: FSMContext):
    javob4 = message.text
    javoblar = interview_answer(jobinterview[3]['question'])
    oxshash = suniyintelekt(javob4,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[3]['question']} ?--{oxshash}\n\n{javob4}")


    if len(javob4) > 15 and oxshash > 30:
        await state.update_data(
            {"javob4": javob4,"oxshash4":oxshash}
        )

        await message.answer(f"5-Savol ❗️\n{jobinterview[4]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Job.savol5)
async def job_answer5(message: types.Message, state: FSMContext):
    javob5 = message.text
    javoblar = interview_answer(jobinterview[4]['question'])
    oxshash = suniyintelekt(javob5,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[4]['question']} ?--{oxshash}\n\n{javob5}")


    if len(javob5) > 15 and oxshash > 30:
        await state.update_data(
            {"javob5": javob5,"oxshash5":oxshash}
        )

        await message.answer(f"6-Savol ❗️\n{jobinterview[5]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol6)
async def job_answer6(message: types.Message, state: FSMContext):
    javob6 = message.text
    javoblar = interview_answer(jobinterview[5]['question'])
    oxshash = suniyintelekt(javob6,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[5]['question']} ?--{oxshash}\n\n{javob6}")


    if len(javob6) > 15 and oxshash > 30:
        await state.update_data(
            {"javob6": javob6,"oxshash6":oxshash}
        )

        await message.answer(f"7-Savol ❗️\n{jobinterview[6]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")





@dp.message_handler(state=Job.savol7)
async def job_answer7(message: types.Message, state: FSMContext):
    javob7 = message.text
    javoblar = interview_answer(jobinterview[6]['question'])
    oxshash = suniyintelekt(javob7,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[6]['question']} ?--{oxshash}\n\n{javob7}")


    if len(javob7) > 15 and oxshash > 30:
        await state.update_data(
            {"javob7": javob7,"oxshash7":oxshash}
        )

        await message.answer(f"8-Savol ❗️\n{jobinterview[7]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Job.savol8)
async def job_answer8(message: types.Message, state: FSMContext):
    javob8 = message.text
    javoblar = interview_answer(jobinterview[7]['question'])
    oxshash = suniyintelekt(javob8,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[7]['question']} ?--{oxshash}\n\n{javob8}")


    if len(javob8) > 15 and oxshash > 30:
        await state.update_data(
            {"javob8": javob8,"oxshash8":oxshash}
        )

        await message.answer(f"9-Savol ❗️\n{jobinterview[8]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Job.savol9)
async def job_answer9(message: types.Message, state: FSMContext):
    javob9 = message.text
    javoblar = interview_answer(jobinterview[8]['question'])
    oxshash = suniyintelekt(javob9,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[8]['question']} ?--{oxshash}\n\n{javob9}")


    if len(javob9) > 15 and oxshash > 30:
        await state.update_data(
            {"javob9": javob9,"oxshash9":oxshash}
        )

        await message.answer(f"10-Savol ❗️\n{jobinterview[9]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Job.savol10)
async def job_answer10(message: types.Message, state: FSMContext):
    javob10 = message.text
    javoblar = interview_answer(jobinterview[9]['question'])
    oxshash = suniyintelekt(javob10,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[9]['question']} ?--{oxshash}\n\n{javob10}")


    if len(javob10) > 15 and oxshash > 30:
        await state.update_data(
            {"javob10": javob10,"oxshash10":oxshash}
        )

        await message.answer(f"11-Savol ❗️\n{jobinterview[10]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol11)
async def job_answer11(message: types.Message, state: FSMContext):
    javob11 = message.text
    javoblar = interview_answer(jobinterview[10]['question'])
    oxshash = suniyintelekt(javob11,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[10]['question']} ?--{oxshash}\n\n{javob11}")

    if len(javob11) > 15 and oxshash > 30:
        await state.update_data(
            {"javob11": javob11,"oxshash11":oxshash}
        )

        await message.answer(f"12-Savol ❗️\n{jobinterview[11]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol12)
async def job_answer12(message: types.Message, state: FSMContext):
    javob12 = message.text
    javoblar = interview_answer(jobinterview[11]['question'])
    oxshash = suniyintelekt(javob12,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[11]['question']} ?--{oxshash}\n\n{javob12}")


    if len(javob12) > 15 and oxshash > 30:
        await state.update_data(
            {"javob12": javob12,"oxshash12":oxshash}
        )

        await message.answer(f"13-Savol ❗️\n{jobinterview[12]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol13)
async def job_answer13(message: types.Message, state: FSMContext):
    javob13 = message.text
    javoblar = interview_answer(jobinterview[12]['question'])
    oxshash = suniyintelekt(javob13,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[12]['question']} ?--{oxshash}\n\n{javob13}")


    if len(javob13) > 15 and oxshash > 30:
        await state.update_data(
            {"javob13": javob13,"oxshash13":oxshash}
        )

        await message.answer(f"14-Savol ❗️\n{jobinterview[13]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol14)
async def job_answer14(message: types.Message, state: FSMContext):
    javob14 = message.text
    javoblar = interview_answer(jobinterview[13]['question'])
    oxshash = suniyintelekt(javob14, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[13]['question']} ?--{oxshash}\n\n{javob14}")


    if len(javob14) > 15 and oxshash > 30:
        await state.update_data(
            {"javob14": javob14, "oxshash14": oxshash}
        )

        await message.answer(f"15-Savol ❗️\n{jobinterview[14]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Job.savol15)
async def job_answer15(message: types.Message, state: FSMContext):
    javob15 = message.text
    javoblar = interview_answer(jobinterview[14]['question'])
    oxshash = suniyintelekt(javob15, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[14]['question']} ?--{oxshash}\n\n{javob15}")


    if len(javob15) > 15 and oxshash > 30:
        await state.update_data(
            {"javob15": javob15, "oxshash15": oxshash}
        )

        await message.answer(f"16-Savol ❗️\n{jobinterview[15]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol16)
async def job_answer16(message: types.Message, state: FSMContext):
    javob16 = message.text
    javoblar = interview_answer(jobinterview[15]['question'])
    oxshash = suniyintelekt(javob16, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[15]['question']} ?--{oxshash}\n\n{javob16}")


    if len(javob16) > 15 and oxshash > 30:
        await state.update_data(
            {"javob16": javob16, "oxshash16": oxshash}
        )

        await message.answer(f"17-Savol ❗️\n{jobinterview[16]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Job.savol17)
async def job_answer17(message: types.Message, state: FSMContext):
    javob17 = message.text
    javoblar = interview_answer(jobinterview[16]['question'])
    oxshash = suniyintelekt(javob17, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[16]['question']} ?--{oxshash}\n\n{javob17}")


    if len(javob17) > 15 and oxshash > 30:
        await state.update_data(
            {"javob17": javob17, "oxshash17": oxshash}
        )

        await message.answer(f"18-Savol ❗️\n{jobinterview[17]['question']} ?")

        await Job.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")




@dp.message_handler(state=Job.savol18)
async def job_answer18(message: types.Message, state: FSMContext):
    javob18 = message.text
    javoblar = interview_answer(jobinterview[17]['question'])
    oxshash = suniyintelekt(javob18, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{jobinterview[17]['question']} ?--{oxshash}\n\n{javob18}")

    if len(javob18) > 15 and oxshash > 30:
        await state.update_data(
            {"javob18": javob18,"oxshash18":oxshash}
        )
        # Ma`lumotlarni qayta o'qiymiz
        data = await state.get_data()
        javob1 = data.get("javob1")
        oxshash1 = data.get("oxshash1")
        javob2 = data.get("javob2")
        oxshash2 = data.get("oxshash2")
        javob3 = data.get("javob3")
        oxshash3 = data.get("oxshash3")
        javob4 = data.get("javob4")
        oxshash4 = data.get("oxshash4")
        javob5 = data.get("javob5")
        oxshash5 = data.get("oxshash5")
        javob6 = data.get("javob6")
        oxshash6 = data.get("oxshash6")
        javob7 = data.get("javob7")
        oxshash7 = data.get("oxshash7")
        javob8 = data.get("javob8")
        oxshash8 = data.get("oxshash8")
        javob9 = data.get("javob9")
        oxshash9 = data.get("oxshash9")
        javob10 = data.get("javob10")
        oxshash10 = data.get("oxshash10")
        javob11 = data.get("javob11")
        oxshash11 = data.get("oxshash11")
        javob12 = data.get("javob12")
        oxshash12 = data.get("oxshash12")
        javob13 = data.get("javob13")
        oxshash13 = data.get("oxshash13")
        javob14 = data.get("javob14")
        oxshash14 = data.get("oxshash14")
        javob15 = data.get("javob15")
        oxshash15 = data.get("oxshash15")
        javob16 = data.get("javob16")
        oxshash16 = data.get("oxshash16")
        javob17 = data.get("javob17")
        oxshash17 = data.get("oxshash17")
        javob18 = data.get("javob18")
        oxshash18 = data.get("oxshash18")

        sum = oxshash1 + oxshash2 + oxshash3 + oxshash4 + oxshash5 + oxshash6 + oxshash7 + oxshash8 + oxshash9 + oxshash10
        sum += oxshash11 + oxshash12 + oxshash13 + oxshash14 + oxshash15 + oxshash16 + oxshash17 + oxshash18

        msg1 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 18}</b>\n\n"
        msg1 += f"<b> javob1: - {oxshash1}</b>--{javob1}\n\n"
        msg1 += f"<b> javob2: - {oxshash2}</b>--{javob2}\n\n"
        msg1 += f"<b> javob3: - {oxshash3}</b>--{javob3}\n\n"
        msg2 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 18}</b>\n\n"
        msg2 += f"<b>javob4: - {oxshash4}</b>--{javob4}\n\n"
        msg2 += f"<b>javob5: - {oxshash5}</b>--{javob5}\n\n"
        msg2 += f"<b>javob6: - {oxshash6}</b>--{javob6}\n\n"
        msg3 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 18}</b>\n\n"
        msg3 += f"<b>javob7: - {oxshash7}</b>--{javob7}\n\n"
        msg3 += f"<b>javob8: - {oxshash8}</b>--{javob8}\n\n"
        msg3 += f"<b>javob9: - {oxshash9}</b>--{javob9}\n\n"
        msg4 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 18}</b>\n\n"
        msg4 += f"<b>javob10: - {oxshash10}</b>--{javob10}\n\n"
        msg4 += f"<b>javob11: - {oxshash11}</b>--{javob11}\n\n"
        msg4 += f"<b>javob12: - {oxshash12}</b>--{javob12}\n\n"
        msg4 += f"<b>javob13: - {oxshash13}</b>--{javob13}\n\n"
        msg5 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 18}</b>\n\n"
        msg5 += f"<b>javob14: - {oxshash14}</b>--{javob14}\n\n"
        msg5 += f"<b>javob15: - {oxshash15}</b>--{javob15}\n\n"
        msg5 += f"<b>javob16: - {oxshash16}</b>--{javob16}\n\n"
        msg5 += f"<b>javob17: - {oxshash17}</b>--{javob17}\n\n"
        msg5 += f"<b>javob18: - {oxshash18}</b>--{javob18}\n\n"


        msg = f"<b>{message.from_user.first_name} ning natijasi: {sum // 18}</b>\n\n"
        msg += f"{msg1}\n{msg2}\n{msg3}\n{msg4}\n{msg5}"

        if len(msg) < 4000:
            await bot.send_message(chat_id=1363350178, text=msg, parse_mode='HTML')
        elif len(msg) > 4000:
            try:
                await bot.send_message(chat_id=1363350178, text=msg1, parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg2, parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg3, parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg4, parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg5, parse_mode='HTML')
            except Exception as e:
                await bot.send_message(chat_id=1363350178, text=f"Xato: {e}")
        else:
            await bot.send_message(chat_id=1363350178, text='Yuborishda hato boldi')

        await message.answer(
            f"Intervyu yakunlandi ✅ \n\nBarcha savollarga qoniqarli javob berdingiz 👏\nNatija: {sum // 18} %",
            reply_markup=interview)

        await state.finish()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")
# end jobinterview state



# php state

@dp.message_handler(text="PHP")
async def phpinterview(message: types.Message):

    await message.answer("Php interview savollari!\nSavollar soni: 8 ta",reply_markup=startphp)


@dp.callback_query_handler(text="php",state=None)
async def start_question_php(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Boshladik ✅ Javobni text shakilda yuboring ‼️",reply_markup=endstate)
    await call.message.answer(f"1-Savol ❗️\n{php[0]['question']} ?")
    await call.answer(cache_time=60)
    await Php.savol1.set()



@dp.message_handler(state=Php.savol1)
async def php_answer1(message: types.Message, state: FSMContext):
    javob1 = message.text
    javoblar = interview_answer(php[0]['question'])
    oxshash = suniyintelekt(javob1,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{php[0]['question']} ?--{oxshash}\n\n{javob1}")


    if len(javob1) > 15 and oxshash > 30:
        await state.update_data(
            {"javob1": javob1,"oxshash1":oxshash}
        )

        await message.answer(f"2-Savol ❗️\n{php[1]['question']} ?")

        await Php.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Php.savol2)
async def php_answer2(message: types.Message, state: FSMContext):
    javob2 = message.text
    javoblar = interview_answer(php[1]['question'])
    oxshash = suniyintelekt(javob2,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{php[1]['question']} ?--{oxshash}\n\n{javob2}")


    if len(javob2) > 15 and oxshash > 30:
        await state.update_data(
            {"javob2": javob2,"oxshash2":oxshash}
        )

        await message.answer(f"3-Savol ❗️\n{php[2]['question']} ?")

        await Php.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Php.savol3)
async def php_answer3(message: types.Message, state: FSMContext):
    javob3 = message.text
    javoblar = interview_answer(php[2]['question'])
    oxshash = suniyintelekt(javob3,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{php[2]['question']} ?--{oxshash}\n\n{javob3}")


    if len(javob3) > 15 and oxshash > 30:
        await state.update_data(
            {"javob3": javob3,"oxshash3":oxshash}
        )

        await message.answer(f"4-Savol ❗️\n{php[3]['question']} ?")

        await Php.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Php.savol4)
async def php_answer4(message: types.Message, state: FSMContext):
    javob4 = message.text
    javoblar = interview_answer(php[3]['question'])
    oxshash = suniyintelekt(javob4,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{php[3]['question']} ?--{oxshash}\n\n{javob4}")


    if len(javob4) > 15 and oxshash > 30:
        await state.update_data(
            {"javob4": javob4,"oxshash4":oxshash}
        )

        await message.answer(f"5-Savol ❗️\n{php[4]['question']} ?")

        await Php.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")

@dp.message_handler(state=Php.savol5)
async def php_answer5(message: types.Message, state: FSMContext):
    javob5 = message.text
    javoblar = interview_answer(php[4]['question'])
    oxshash = suniyintelekt(javob5,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{php[4]['question']} ?--{oxshash}\n\n{javob5}")


    if len(javob5) > 15 and oxshash > 30:
        await state.update_data(
            {"javob5": javob5,"oxshash5":oxshash}
        )

        await message.answer(f"6-Savol ❗️\n{php[5]['question']} ?")

        await Php.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Php.savol6)
async def php_answer6(message: types.Message, state: FSMContext):
    javob6 = message.text
    javoblar = interview_answer(php[5]['question'])
    oxshash = suniyintelekt(javob6,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{php[5]['question']} ?--{oxshash}\n\n{javob6}")


    if len(javob6) > 15 and oxshash > 30:
        await state.update_data(
            {"javob6": javob6,"oxshash6":oxshash}
        )

        await message.answer(f"7-Savol ❗️\n{php[6]['question']} ?")

        await Php.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Php.savol7)
async def php_answer7(message: types.Message, state: FSMContext):
    javob7 = message.text
    javoblar = interview_answer(php[6]['question'])
    oxshash = suniyintelekt(javob7,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{php[6]['question']} ?--{oxshash}\n\n{javob7}")


    if len(javob7) > 15 and oxshash > 30:
        await state.update_data(
            {"javob7": javob7,"oxshash7":oxshash}
        )

        await message.answer(f"8-Savol ❗️\n{php[7]['question']} ?")

        await Php.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")




@dp.message_handler(state=Php.savol8)
async def php_answer10(message: types.Message, state: FSMContext):
    javob8 = message.text
    javoblar = interview_answer(php[7]['question'])
    oxshash = suniyintelekt(javob8, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{php[7]['question']} ?--{oxshash}\n\n{javob8}")

    if len(javob8) > 15 and oxshash > 30:
        await state.update_data(
            {"javob8": javob8,"oxshash8":oxshash}
        )

        # Ma`lumotlarni qayta o'qiymiz
        data = await state.get_data()
        javob1 = data.get("javob1")
        oxshash1 = data.get("oxshash1")
        javob2 = data.get("javob2")
        oxshash2 = data.get("oxshash2")
        javob3 = data.get("javob3")
        oxshash3 = data.get("oxshash3")
        javob4 = data.get("javob4")
        oxshash4 = data.get("oxshash4")
        javob5 = data.get("javob5")
        oxshash5 = data.get("oxshash5")
        javob6 = data.get("javob6")
        oxshash6 = data.get("oxshash6")
        javob7 = data.get("javob7")
        oxshash7 = data.get("oxshash7")
        javob8 = data.get("javob8")
        oxshash8 = data.get("oxshash8")



        sum = oxshash1 + oxshash2 + oxshash3 + oxshash4 + oxshash5 + oxshash6 + oxshash7 + oxshash8

        msg1 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 8}</b>\n\n"
        msg1 += f"<b> javob1: - {oxshash1}</b>--{javob1}\n\n"
        msg1 += f"<b> javob2: - {oxshash2}</b>--{javob2}\n\n"
        msg1 += f"<b> javob3: - {oxshash3}</b>--{javob3}\n\n"
        msg2 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 8}</b>\n\n"
        msg2 += f"<b>javob4: - {oxshash4}</b>--{javob4}\n\n"
        msg2 += f"<b>javob5: - {oxshash5}</b>--{javob5}\n\n"
        msg2 += f"<b>javob6: - {oxshash6}</b>--{javob6}\n\n"
        msg3 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 8}</b>\n\n"
        msg3 += f"<b>javob7: - {oxshash7}</b>--{javob7}\n\n"
        msg3 += f"<b>javob8: - {oxshash8}</b>--{javob8}\n\n"



        msg = f"<b>{message.from_user.first_name} ning natijasi: {sum // 8}</b>\n\n"
        msg += f"{msg1}\n{msg2}\n{msg3}"

        if len(msg) < 4000:
            await bot.send_message(chat_id=1363350178, text=msg,parse_mode='HTML')
        elif len(msg) > 4000:
            try:
                await bot.send_message(chat_id=1363350178, text=msg1,parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg2,parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg3,parse_mode='HTML')

            except Exception as e:
                await bot.send_message(chat_id=1363350178, text=f"Xato: {e}")
        else:
            await bot.send_message(chat_id=1363350178, text='Yuborishda hato boldi')

        await message.answer(f"Intervyu yakunlandi ✅ \n\nBarcha savollarga qoniqarli javob berdingiz 👏\nNatija: {sum//8} %", reply_markup=interview)

        await state.finish()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



# end php state



# laravel state


@dp.message_handler(text="Laravel")
async def phpinterview(message: types.Message):

    await message.answer("Laravel interview savollari!\nSavollar soni: 5 ta",reply_markup=startlaravel)


@dp.callback_query_handler(text="laravel",state=None)
async def start_question_laravel(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Boshladik ✅ Javobni text shakilda yuboring ‼️",reply_markup=endstate)
    await call.message.answer(f"1-Savol ❗️\n{laravel[0]['question']} ?")
    await call.answer(cache_time=60)
    await Laravel.savol1.set()



@dp.message_handler(state=Laravel.savol1)
async def laravel_answer1(message: types.Message, state: FSMContext):
    javob1 = message.text
    javoblar = interview_answer(laravel[0]['question'])
    oxshash = suniyintelekt(javob1,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{laravel[0]['question']} ?--{oxshash}\n\n{javob1}")


    if len(javob1) > 15 and oxshash > 30:
        await state.update_data(
            {"javob1": javob1,"oxshash1":oxshash}
        )

        await message.answer(f"2-Savol ❗️\n{laravel[1]['question']} ?")

        await Laravel.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Laravel.savol2)
async def laravel_answer2(message: types.Message, state: FSMContext):
    javob2 = message.text
    javoblar = interview_answer(laravel[1]['question'])
    oxshash = suniyintelekt(javob2,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{laravel[1]['question']} ?--{oxshash}\n\n{javob2}")


    if len(javob2) > 15 and oxshash > 30:
        await state.update_data(
            {"javob2": javob2,"oxshash2":oxshash}
        )

        await message.answer(f"3-Savol ❗️\n{laravel[2]['question']} ?")

        await Laravel.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Laravel.savol3)
async def laravel_answer3(message: types.Message, state: FSMContext):
    javob3 = message.text
    javoblar = interview_answer(laravel[2]['question'])
    oxshash = suniyintelekt(javob3,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{laravel[2]['question']} ?--{oxshash}\n\n{javob3}")


    if len(javob3) > 15 and oxshash > 30:
        await state.update_data(
            {"javob3": javob3,"oxshash3":oxshash}
        )

        await message.answer(f"4-Savol ❗️\n{laravel[3]['question']} ?")

        await Laravel.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Laravel.savol4)
async def laravel_answer4(message: types.Message, state: FSMContext):
    javob4 = message.text
    javoblar = interview_answer(laravel[3]['question'])
    oxshash = suniyintelekt(javob4,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{laravel[3]['question']} ?--{oxshash}\n\n{javob4}")


    if len(javob4) > 15 and oxshash > 30:
        await state.update_data(
            {"javob4": javob4,"oxshash4":oxshash}
        )

        await message.answer(f"5-Savol ❗️\n{laravel[4]['question']} ?")

        await Laravel.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Laravel.savol5)
async def laravel_answer5(message: types.Message, state: FSMContext):
    javob5 = message.text
    javoblar = interview_answer(laravel[7]['question'])
    oxshash = suniyintelekt(javob5, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{laravel[7]['question']} ?--{oxshash}\n\n{javob5}")

    if len(javob5) > 15 and oxshash > 30:
        await state.update_data(
            {"javob5": javob5,"oxshash5":oxshash}
        )

        # Ma`lumotlarni qayta o'qiymiz
        data = await state.get_data()
        javob1 = data.get("javob1")
        oxshash1 = data.get("oxshash1")
        javob2 = data.get("javob2")
        oxshash2 = data.get("oxshash2")
        javob3 = data.get("javob3")
        oxshash3 = data.get("oxshash3")
        javob4 = data.get("javob4")
        oxshash4 = data.get("oxshash4")
        javob5 = data.get("javob5")
        oxshash5 = data.get("oxshash5")




        sum = oxshash1 + oxshash2 + oxshash3 + oxshash4 + oxshash5

        msg1 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 5}</b>\n\n"
        msg1 += f"<b> javob1: - {oxshash1}</b>--{javob1}\n\n"
        msg1 += f"<b> javob2: - {oxshash2}</b>--{javob2}\n\n"
        msg1 += f"<b> javob3: - {oxshash3}</b>--{javob3}\n\n"
        msg2 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 5}</b>\n\n"
        msg2 += f"<b>javob4: - {oxshash4}</b>--{javob4}\n\n"
        msg2 += f"<b>javob5: - {oxshash5}</b>--{javob5}\n\n"




        msg = f"<b>{message.from_user.first_name} ning natijasi: {sum // 5}</b>\n\n"
        msg += f"{msg1}\n{msg2}"

        if len(msg) < 4000:
            await bot.send_message(chat_id=1363350178, text=msg,parse_mode='HTML')
        elif len(msg) > 4000:
            try:
                await bot.send_message(chat_id=1363350178, text=msg1,parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg2,parse_mode='HTML')


            except Exception as e:
                await bot.send_message(chat_id=1363350178, text=f"Xato: {e}")
        else:
            await bot.send_message(chat_id=1363350178, text='Yuborishda hato boldi')

        await message.answer(f"Intervyu yakunlandi ✅ \n\nBarcha savollarga qoniqarli javob berdingiz 👏\nNatija: {sum//8} %", reply_markup=interview)

        await state.finish()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")





# end laravel state


# java state



@dp.message_handler(text="Java")
async def javainterview(message: types.Message):

    await message.answer("Java interview savollari!\nSavollar soni: 10 ta",reply_markup=startjava)


@dp.callback_query_handler(text="java",state=None)
async def start_question_java(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Boshladik ✅ Javobni text shakilda yuboring ‼️",reply_markup=endstate)
    await call.message.answer(f"1-Savol ❗️\n{java[0]['question']} ?")
    await call.answer(cache_time=60)
    await Java.savol1.set()



@dp.message_handler(state=Java.savol1)
async def java_answer1(message: types.Message, state: FSMContext):
    javob1 = message.text
    javoblar = interview_answer(java[0]['question'])
    oxshash = suniyintelekt(javob1,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{java[0]['question']} ?--{oxshash}\n\n{javob1}")


    if len(javob1) > 15 and oxshash > 30:
        await state.update_data(
            {"javob1": javob1,"oxshash1":oxshash}
        )

        await message.answer(f"2-Savol ❗️\n{java[1]['question']} ?")

        await Java.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Java.savol2)
async def java_answer2(message: types.Message, state: FSMContext):
    javob2 = message.text
    javoblar = interview_answer(java[1]['question'])
    oxshash = suniyintelekt(javob2,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{java[1]['question']} ?--{oxshash}\n\n{javob2}")


    if len(javob2) > 15 and oxshash > 30:
        await state.update_data(
            {"javob2": javob2,"oxshash2":oxshash}
        )

        await message.answer(f"3-Savol ❗️\n{java[2]['question']} ?")

        await Java.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Java.savol3)
async def java_answer3(message: types.Message, state: FSMContext):
    javob3 = message.text
    javoblar = interview_answer(java[2]['question'])
    oxshash = suniyintelekt(javob3,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{java[2]['question']} ?--{oxshash}\n\n{javob3}")


    if len(javob3) > 15 and oxshash > 30:
        await state.update_data(
            {"javob3": javob3,"oxshash3":oxshash}
        )

        await message.answer(f"4-Savol ❗️\n{java[3]['question']} ?")

        await Java.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



@dp.message_handler(state=Java.savol4)
async def java_answer4(message: types.Message, state: FSMContext):
    javob4 = message.text
    javoblar = interview_answer(java[3]['question'])
    oxshash = suniyintelekt(javob4,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{java[3]['question']} ?--{oxshash}\n\n{javob4}")


    if len(javob4) > 15 and oxshash > 30:
        await state.update_data(
            {"javob4": javob4,"oxshash4":oxshash}
        )

        await message.answer(f"5-Savol ❗️\n{java[4]['question']} ?")

        await Java.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")

@dp.message_handler(state=Java.savol5)
async def java_answer5(message: types.Message, state: FSMContext):
    javob5 = message.text
    javoblar = interview_answer(java[4]['question'])
    oxshash = suniyintelekt(javob5,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{java[4]['question']} ?--{oxshash}\n\n{javob5}")


    if len(javob5) > 15 and oxshash > 30:
        await state.update_data(
            {"javob5": javob5,"oxshash5":oxshash}
        )

        await message.answer(f"6-Savol ❗️\n{java[5]['question']} ?")

        await Java.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Java.savol6)
async def java_answer6(message: types.Message, state: FSMContext):
    javob6 = message.text
    javoblar = interview_answer(java[5]['question'])
    oxshash = suniyintelekt(javob6,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{java[5]['question']} ?--{oxshash}\n\n{javob6}")


    if len(javob6) > 15 and oxshash > 30:
        await state.update_data(
            {"javob6": javob6,"oxshash6":oxshash}
        )

        await message.answer(f"7-Savol ❗️\n{java[6]['question']} ?")

        await Java.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Java.savol7)
async def java_answer7(message: types.Message, state: FSMContext):
    javob7 = message.text
    javoblar = interview_answer(java[6]['question'])
    oxshash = suniyintelekt(javob7,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{java[6]['question']} ?--{oxshash}\n\n{javob7}")


    if len(javob7) > 15 and oxshash > 30:
        await state.update_data(
            {"javob7": javob7,"oxshash7":oxshash}
        )

        await message.answer(f"8-Savol ❗️\n{java[7]['question']} ?")

        await Java.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Java.savol8)
async def java_answer8(message: types.Message, state: FSMContext):
    javob8 = message.text
    javoblar = interview_answer(java[7]['question'])
    oxshash = suniyintelekt(javob8,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{java[7]['question']} ?--{oxshash}\n\n{javob8}")


    if len(javob8) > 15 and oxshash > 30:
        await state.update_data(
            {"javob8": javob8,"oxshash8":oxshash}
        )

        await message.answer(f"9-Savol ❗️\n{java[8]['question']} ?")

        await Java.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Java.savol9)
async def java_answer9(message: types.Message, state: FSMContext):
    javob9 = message.text
    javoblar = interview_answer(java[8]['question'])
    oxshash = suniyintelekt(javob9,javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{java[8]['question']} ?--{oxshash}\n\n{javob9}")


    if len(javob9) > 15 and oxshash > 30:
        await state.update_data(
            {"javob9": javob9,"oxshash9":oxshash}
        )

        await message.answer(f"10-Savol ❗️\n{java[9]['question']} ?")

        await Java.next()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")


@dp.message_handler(state=Java.savol10)
async def java_answer10(message: types.Message, state: FSMContext):
    javob10 = message.text
    javoblar = interview_answer(java[9]['question'])
    oxshash = suniyintelekt(javob10, javoblar)
    await bot.send_message(chat_id=1363350178, text=f"{message.from_user.first_name}--@{message.from_user.username}\n\n"
                                                    f"{java[9]['question']} ?--{oxshash}\n\n{javob10}")

    if len(javob10) > 15 and oxshash > 30:
        await state.update_data(
            {"javob10": javob10,"oxshash10":oxshash}
        )

        # Ma`lumotlarni qayta o'qiymiz
        data = await state.get_data()
        javob1 = data.get("javob1")
        oxshash1 = data.get("oxshash1")
        javob2 = data.get("javob2")
        oxshash2 = data.get("oxshash2")
        javob3 = data.get("javob3")
        oxshash3 = data.get("oxshash3")
        javob4 = data.get("javob4")
        oxshash4 = data.get("oxshash4")
        javob5 = data.get("javob5")
        oxshash5 = data.get("oxshash5")
        javob6 = data.get("javob6")
        oxshash6 = data.get("oxshash6")
        javob7 = data.get("javob7")
        oxshash7 = data.get("oxshash7")
        javob8 = data.get("javob8")
        oxshash8 = data.get("oxshash8")
        javob9 = data.get("javob9")
        oxshash9 = data.get("oxshash9")
        javob10 = data.get("javob10")
        oxshash10 = data.get("oxshash10")


        sum = oxshash1 + oxshash2 + oxshash3 + oxshash4 + oxshash5 + oxshash6 + oxshash7 + oxshash8 + oxshash9 + oxshash10

        msg1 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg1 += f"<b> javob1: - {oxshash1}</b>--{javob1}\n\n"
        msg1 += f"<b> javob2: - {oxshash2}</b>--{javob2}\n\n"
        msg1 += f"<b> javob3: - {oxshash3}</b>--{javob3}\n\n"
        msg2 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg2 += f"<b>javob4: - {oxshash4}</b>--{javob4}\n\n"
        msg2 += f"<b>javob5: - {oxshash5}</b>--{javob5}\n\n"
        msg2 += f"<b>javob6: - {oxshash6}</b>--{javob6}\n\n"
        msg3 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg3 += f"<b>javob7: - {oxshash7}</b>--{javob7}\n\n"
        msg3 += f"<b>javob8: - {oxshash8}</b>--{javob8}\n\n"
        msg3 += f"<b>javob9: - {oxshash9}</b>--{javob9}\n\n"
        msg4 = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg4 += f"<b>javob10: - {oxshash10}</b>--{javob10}\n\n"


        msg = f"<b>{message.from_user.first_name} ning natijasi: {sum // 10}</b>\n\n"
        msg += f"{msg1}\n{msg2}\n{msg3}\n{msg4}"

        if len(msg) < 4000:
            await bot.send_message(chat_id=1363350178, text=msg,parse_mode='HTML')
        elif len(msg) > 4000:
            try:
                await bot.send_message(chat_id=1363350178, text=msg1,parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg2,parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg3,parse_mode='HTML')
                await bot.send_message(chat_id=1363350178, text=msg4,parse_mode='HTML')
            except Exception as e:
                await bot.send_message(chat_id=1363350178, text=f"Xato: {e}")
        else:
            await bot.send_message(chat_id=1363350178, text='Yuborishda hato boldi')

        await message.answer(f"Intervyu yakunlandi ✅ \n\nBarcha savollarga qoniqarli javob berdingiz 👏\nNatija: {sum//10} %", reply_markup=interview)

        await state.finish()
    else:
        await message.answer("To'liqroq javob berishga harakat qiling!")



# end java state



# End interview commands








# Admin commands
ADMINS = [1363350178]

@dp.message_handler(text="admin panel", user_id=1363350178)
async def adminpanel(message: types.Message):

    await message.answer('admin panel',reply_markup=adminusers)




@dp.message_handler(chat_id=1363350178, text='users')
async def users(message: types.Message):
    countuser = userget()
    datauser = userget()[-45:]
    text = f"Interview Questions || Foydalanuvchilar soni: {len(countuser)}\n\n"
    for user in datauser:
        text += f"{user['id']}). || {user['first_name']} || @{user['username']} || {user['language']}\n"
    await message.answer(text)



@dp.message_handler(text="back", user_id=1363350178)
async def back_button(message: types.Message):

    await message.answer('Bosh menyu',reply_markup=admincommands)



@dp.message_handler(text="reklama",user_id=ADMINS)
async def bot_reklama(message: types.Message, state: FSMContext):
    await message.answer("reklama yuboring")
    await state.set_state("reklama")



@dp.message_handler(state='reklama')
async def send_ad_to_all(message: types.Message,state: FSMContext):
    try:
        await bot.send_message(chat_id=ADMINS[0],text=f"Habar to'g'rimi ‼️\n{message.text}",reply_markup=rek)
        try:
            @dp.callback_query_handler(text="ha",state='reklama')
            async def rek_ha(call: CallbackQuery):
                users = userget()
                for user in users:
                    user_id = user['user_id']
                    try:
                        await bot.send_message(chat_id=user_id, text=f"{message.text}")
                    except Exception as e:
                        print(e)
                    await asyncio.sleep(0.05)
                await bot.send_message(chat_id=ADMINS[0],text=f"Reklama yuborildi! ✅")
                await state.finish()
                await call.message.delete()
        except Exception as e:
            print(e)
        @dp.callback_query_handler(text="yuq",state='reklama')
        async def rek_yuq(call: CallbackQuery):
            await bot.send_message(chat_id=ADMINS[0],text="Reklama yuborilmadi! ❌")
            await state.finish()
            await call.message.delete()
    except Exception as e:
        print(e)





# @dp.message_handler(text="rek",user_id=ADMINS)
# async def bot_start(message: types.Message, state: FSMContext):
#     users = userget()
#     for user in users:
#         user_id = user['user_id']
#         try:
#             img = 'https://temur01.pythonanywhere.com/media/images/osmon.jpg'
#             await bot.send_photo(chat_id=user_id, photo=img,caption='test')
#         except Exception as e:
#             print(e)
#         await asyncio.sleep(0.05)




# End admin commands


# @dp.message_handler(text=bilmadim(),state='*')
# async def bilmaslargajavob(message: types.Message):
#
#     await message.answer(f"< {message.text} > Bu javob qabul qilinmaydi!" )



# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
# 
#     await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
