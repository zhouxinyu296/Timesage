from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CallbackQueryHandler
import datetime
import pytz  # Untuk konversi zona waktu
from bot_texts import texts, default_language

# Zona waktu yang didukung
TIMEZONES = {
    "WIB": "Asia/Jakarta",
    "WITA": "Asia/Makassar",
    "WIT": "Asia/Jayapura",
    "UTC": "UTC"
}

# Fungsi untuk menghitung waktu setelah jam tambahan
def calculate_time(time_str: str, hours: int):
    time_format = "%H.%M"  # Format waktu (jam.menit)
    time_obj = datetime.datetime.strptime(time_str, time_format)
    future_time = time_obj + datetime.timedelta(hours=hours)
    return future_time.strftime(time_format)

# Fungsi untuk mengonversi waktu antar zona waktu
def convert_timezone(time_str: str, timezone_from: str, timezone_to: str):
    time_format = "%H.%M"
    tz_from = pytz.timezone(TIMEZONES.get(timezone_from, "UTC"))
    tz_to = pytz.timezone(TIMEZONES.get(timezone_to, "UTC"))

    # Buat objek waktu dalam zona waktu asal
    naive_time = datetime.datetime.strptime(time_str, time_format)
    localized_time = tz_from.localize(naive_time)

    # Konversi ke zona waktu tujuan
    converted_time = localized_time.astimezone(tz_to)
    return converted_time.strftime(time_format)

# Fungsi untuk menampilkan menu awal dengan tombol
async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, language: str):
    full_name = update.message.from_user.full_name  # Mengambil nama lengkap pengguna
    start_message = texts[language]['start_message'].format(full_name=full_name)
    
    keyboard = [
        [InlineKeyboardButton(texts[language]["select_language_button"], callback_data='select_language')],
        [InlineKeyboardButton(texts[language]["guide_button"], callback_data='guide'),
         InlineKeyboardButton(texts[language]["about_button"], callback_data='about')],
        [InlineKeyboardButton(texts[language]["join_button"], url='https://t.me/timesage_official')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(start_message, reply_markup=reply_markup)

# Fungsi untuk menampilkan panduan
async def show_guide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_language = context.user_data.get('language', default_language)
    keyboard = [
        [InlineKeyboardButton("Back to Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.edit_text(texts[user_language]["guide"], reply_markup=reply_markup)

# Fungsi untuk menampilkan informasi tentang bot
async def show_about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_language = context.user_data.get('language', default_language)
    keyboard = [
        [InlineKeyboardButton("Back to Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.edit_text(texts[user_language]["about"], reply_markup=reply_markup)

# Fungsi untuk menampilkan menu pemilihan bahasa
async def show_language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("English 🇬🇧", callback_data='lang_en')],
        [InlineKeyboardButton("Indonesia 🇮🇩", callback_data='lang_id'),
         InlineKeyboardButton("Русский 🇷🇺", callback_data='lang_ru')],
        [InlineKeyboardButton("Back to Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.edit_text('Select your language:', reply_markup=reply_markup)

# Fungsi untuk memproses tombol callback
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    if data == 'guide':
        await show_guide(query, context)
    elif data == 'about':
        await show_about(query, context)
    elif data == 'select_language':
        await show_language_selection(query, context)
    elif data == 'main_menu':
        # Kembali ke menu utama dengan memperbarui pesan
        user_language = context.user_data.get('language', default_language)
        full_name = query.from_user.full_name
        start_message = texts[user_language]['start_message'].format(full_name=full_name)
        await query.edit_message_text(
            text=start_message,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(texts[user_language]["select_language_button"], callback_data='select_language')],
                [InlineKeyboardButton(texts[user_language]["guide_button"], callback_data='guide'),
                 InlineKeyboardButton(texts[user_language]["about_button"], callback_data='about')],
                [InlineKeyboardButton(texts[user_language]["join_button"], url='https://t.me/timesage_official')]
            ])
        )
    elif data.startswith('lang_'):
        language = data.split('_')[1]
        context.user_data['language'] = language
        # Langsung kembali ke menu utama setelah pemilihan bahasa
        user_language = context.user_data.get('language', default_language)
        full_name = query.from_user.full_name
        start_message = texts[user_language]['start_message'].format(full_name=full_name)
        await query.edit_message_text(
            text=start_message,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(texts[user_language]["select_language_button"], callback_data='select_language')],
                [InlineKeyboardButton(texts[user_language]["guide_button"], callback_data='guide'),
                 InlineKeyboardButton(texts[user_language]["about_button"], callback_data='about')],
                [InlineKeyboardButton(texts[user_language]["join_button"], url='https://t.me/timesage_official')]
            ])
        )

# Fungsi untuk memproses pesan
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_language = context.user_data.get('language', default_language)
        text = update.message.text.strip()

        # Pisahkan berdasarkan spasi
        parts = text.split()

        if len(parts) == 2:
            # Format waktu jam tambahan (e.g., "03.00 5")
            time_str, hours_str = parts
            try:
                hours = int(hours_str)
                result_time = calculate_time(time_str, hours)
                await update.message.reply_text(
                    texts[user_language]["result"].format(
                        time_str=time_str,
                        hours=hours,
                        result_time=result_time
                    )
                )
            except ValueError:
                await update.message.reply_text(texts[user_language]["error"])

        elif len(parts) == 3:
            # Format konversi zona waktu (e.g., "03.00 WIB UTC")
            time_str, timezone_from, timezone_to = parts
            timezone_from = timezone_from.upper()
            timezone_to = timezone_to.upper()

            if timezone_from in TIMEZONES and timezone_to in TIMEZONES:
                converted_time = convert_timezone(time_str, timezone_from, timezone_to)
                await update.message.reply_text(
                    texts[user_language]["timezone_conversion"].format(
                        time_str=time_str,
                        timezone_from=timezone_from,
                        timezone_to=timezone_to,
                        converted_time=converted_time
                    )
                )
            else:
                await update.message.reply_text(texts[user_language]["timezone_error"])
        else:
            await update.message.reply_text(texts[user_language]["error"])

    except Exception as e:
        await update.message.reply_text(texts[user_language]["error"])
        print(f"Error: {e}")

if __name__ == '__main__':
    # Token API Telegram bot
    TOKEN = '7341298046:AAGzndaiqYo3KywfCEWRJibNT4VWfL94srQ'

    # Membangun aplikasi bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Tangani semua pesan yang masuk
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Tangani tombol callback
    application.add_handler(CallbackQueryHandler(button))

    # Tangani perintah 'start' untuk menampilkan menu
    application.add_handler(MessageHandler(filters.COMMAND, lambda update, context: show_menu(update, context, default_language)))

    # Menjalankan bot
    application.run_polling()
