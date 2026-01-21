from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8309177863:AAEX_Nmn6Rb7XaZUJ514WMK7kX14qzEB0SQ"

def main_menu():
    keyboard = [
        [InlineKeyboardButton("1", callback_data="1"),
         InlineKeyboardButton("2", callback_data="2"),
         InlineKeyboardButton("3", callback_data="3"),
         InlineKeyboardButton("4", callback_data="4"),
         InlineKeyboardButton("5", callback_data="5")]
    ]
    return InlineKeyboardMarkup(keyboard)

def second_menu(prefix):
    keyboard = [
        [InlineKeyboardButton(f"{prefix}.1", callback_data=f"{prefix}.1"),
         InlineKeyboardButton(f"{prefix}.2", callback_data=f"{prefix}.2"),
         InlineKeyboardButton(f"{prefix}.3", callback_data=f"{prefix}.3"),
         InlineKeyboardButton(f"{prefix}.4", callback_data=f"{prefix}.4"),
         InlineKeyboardButton(f"{prefix}.5", callback_data=f"{prefix}.5")]
    ]
    return InlineKeyboardMarkup(keyboard)

def third_menu(prefix):
    keyboard = [
        [InlineKeyboardButton(f"{prefix}.1", callback_data=f"{prefix}.1"),
         InlineKeyboardButton(f"{prefix}.2", callback_data=f"{prefix}.2"),
         InlineKeyboardButton(f"{prefix}.3", callback_data=f"{prefix}.3"),
         InlineKeyboardButton(f"{prefix}.4", callback_data=f"{prefix}.4"),
         InlineKeyboardButton(f"{prefix}.5", callback_data=f"{prefix}.5")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Выбери кнопку:", reply_markup=main_menu())

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if "." not in data:
        await query.edit_message_text(f"Выбрал {data}", reply_markup=second_menu(data))
    elif data.count(".") == 1:
        await query.edit_message_text(f"Выбрал {data}", reply_markup=third_menu(data))
    else:
        await query.edit_message_text(f"Финальный пункт: {data}")

if name == "main":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()
