from aiogram import types, F, Router
from aiogram.types import  *
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from states import FSMGetSearchArgs
from utils import find_olymp
import texts


router = Router()

keyboard = ReplyKeyboardBuilder()
keyboard.row(
    types.KeyboardButton(text="Подобрать олимпиады")
)

subj_menu = [
    [InlineKeyboardButton(text='Информатика',callback_data='информатика')],
    [InlineKeyboardButton(text='Математика',callback_data='математика')],
    [InlineKeyboardButton(text='Физика',callback_data='физика')],
    [InlineKeyboardButton(text='Биология',callback_data='биология')],
    [InlineKeyboardButton(text='Химия',callback_data='химия')]
]

class_menu = [
    [InlineKeyboardButton(text='8', callback_data='8'),
     InlineKeyboardButton(text='9', callback_data='9')],
    [InlineKeyboardButton(text='10', callback_data='10'),
     InlineKeyboardButton(text='11', callback_data='11')],
]

level_menu = [
    [InlineKeyboardButton(text='1 уровень', callback_data='1')],
    [InlineKeyboardButton(text='2 уровень', callback_data='2')],
    [InlineKeyboardButton(text='3 уровень', callback_data='3')],
    [InlineKeyboardButton(text='Любой', callback_data='all')]
]



async def start_handler(msg: Message):
    await msg.answer(texts.greeting, reply_markup=keyboard.as_markup(resize_keyboard=True))


async def main_loop(msg: Message, state: FSMContext):
    if msg.text.lower() == "подобрать олимпиады":
        print("Choose sub")
        menu = InlineKeyboardMarkup(inline_keyboard=subj_menu)
        await state.clear()
        await msg.answer("Выберите направление олимпиады:",reply_markup=menu)
        await state.set_state(FSMGetSearchArgs.subjects)


async def callback_subject(call:types.CallbackQuery,state:FSMContext):
    if call.data in ['1','2','3','all']:
        await callback_levels(call,state)
        return
    if call.data in ['8','9','10','11']:
        await callback_classes(call,state)
        return
    print("Choose sub")

    if call.data == 'информатика':
        await call.answer('Selected it')
        await state.update_data(subject='информатика')
    elif call.data == 'математика':
        await call.answer('Selected math')
        await state.update_data(subject='математика')
    elif call.data == 'физика':
        await state.update_data(subject='физика')
        await call.answer('Selected phys')
    elif call.data == 'химия':
        await state.update_data(subject='химия')
    elif call.data == 'биология':
        await state.update_data(subject='биология')
    menu = InlineKeyboardMarkup(inline_keyboard=class_menu)
    await call.message.edit_text("Выберите класс:",reply_markup=menu)
    await state.set_state(FSMGetSearchArgs.student_class)


async def callback_classes(call:CallbackQuery,state:FSMContext):
    print("Choose class")
    await state.update_data(student_class=call.data)
    menu = InlineKeyboardMarkup(inline_keyboard=level_menu)
    await call.message.delete()
    await call.message.answer("Выберите уровень олимпиады",reply_markup=menu)


async def callback_levels(call:CallbackQuery,state:FSMContext):
    print("Choose lvl")
    await state.update_data(level=call.data)
    data = await state.get_data()
    await call.message.delete()
    await call.answer()
    await state.clear()
    response = "Поиск по параметрам\n\n"
    response += '**Класс:** ' + data['student_class']
    response += '\n**Уровень:** ' + data['level']
    response += '\n**Предмет:** ' + data['subject']
    response += "\n\n**Найдено для вас:**\n\n"
    for i in find_olymp(data['student_class'],data['level'],data['subject']):
        response += i + '\n\n'
    await call.message.answer(response)