# File: bot_texts.py

# Bahasa default
default_language = 'en'

# Teks dalam berbagai bahasa
texts = {
    'en': {
        'start_message': "Hello {full_name}, Time Sage is a bot that can calculate time.\n\n"
                         "Like knowing the next few hours and converting time between time zones.\n\n"
                         "Use the 'Guide' button to find out how.",
        'guide_button': 'Guide',
        'join_button': 'Join Community 🌍',
        'about_button': 'About ℹ️',
        'select_language_button': 'Select Language 🌐',
        'guide': 'This is how you use the bot...\n\n'
                 'To find out the time a few hours later, use the format:\n'
                 '[hour.minute] [additional hours]\n'
                 'Example: 20.00 3\n\n'
                 'To convert time between time zones, use the format:\n'
                 '[hour.minute] [source timezone] [destination timezone]\n'
                 'Supported time zones: WIB, WITA, WIT, UTC\n'
                 'Example: 20.00 WIB UTC\n\n'
                 'Use the \'Guide\' button if you need this guide again.',
        'about': 'Bot Version 1.0',
        'select_language': 'Select your language:',
        'result': '╓──────────────────╥\n'
                  '│  ⊙ Time entered : {time_str}\n'
                  '│\n'
                  '│  ⊙ Number of hours : {hours}\n'
                  '│\n'
                  '│  ⊙ The result : {result_time}\n'
                  '╙──────────────────╜\n\n'
                  'Then {hours} hours later it will be {result_time}!',
        'timezone_conversion': 'The time {time_str} in {timezone_from} is {converted_time} in {timezone_to}.',
        'error': 'Error: Invalid input format. Please use \'hour.minute hours\' or \'hour.minute source_timezone destination_timezone\'.',
        'timezone_error': 'Error: Invalid time zone. Please use one of the supported time zones.'
    },
    'id': {
        'start_message': "Halo {full_name}, Time Sage adalah bot yang dapat menghitung waktu.\n\n"
                         "Seperti mengetahui beberapa jam ke depan dan mengonversi waktu antar zona waktu.\n\n"
                         "Gunakan tombol 'Panduan' untuk mengetahui caranya.",
        'guide_button': 'Panduan',
        'join_button': 'Bergabung dengan Komunitas 🌍',
        'about_button': 'Tentang ℹ️',
        'select_language_button': 'Pilih Bahasa 🌐',
        'guide': 'Ini cara Anda menggunakan bot...\n\n'
                 'Untuk mengetahui waktu beberapa jam kemudian, gunakan format:\n'
                 '[jam.menit] [jam tambahan]\n'
                 'Contoh: 20.00 3\n\n'
                 'Untuk mengonversi waktu antar zona waktu, gunakan format:\n'
                 '[jam.menit] [zona waktu asal] [zona waktu tujuan]\n'
                 'Zona waktu yang didukung: WIB, WITA, WIT, UTC\n'
                 'Contoh: 20.00 WIB UTC\n\n'
                 'Gunakan tombol \'Panduan\' jika Anda membutuhkan panduan ini lagi.',
        'about': 'Versi Bot 1.0',
        'select_language': 'Pilih bahasa Anda:',
        'result': '╓──────────────────╥\n'
                  '│  ⊙ Waktu yang dimasukkan : {time_str}\n'
                  '│\n'
                  '│  ⊙ Jumlah jam : {hours}\n'
                  '│\n'
                  '│  ⊙ Hasilnya : {result_time}\n'
                  '╙──────────────────╜\n\n'
                  'Kemudian {hours} jam kemudian akan menjadi {result_time}!',
        'timezone_conversion': 'Waktu {time_str} di {timezone_from} adalah {converted_time} di {timezone_to}.',
        'error': 'Kesalahan: Format input tidak valid. Harap gunakan \'jam.menit jam\' atau \'jam.menit zona_waktu_asal zona_waktu_tujuan\'.',
        'timezone_error': 'Kesalahan: Zona waktu tidak valid. Harap gunakan salah satu zona waktu yang didukung.'
    },
    'ru': {
        'start_message': "Привет {full_name}, Time Sage — это бот, который может вычислять время.\n\n"
                         "Например, узнавать, сколько часов будет дальше, и конвертировать время между часовыми поясами.\n\n"
                         "Используйте кнопку 'Руководство', чтобы узнать, как это сделать.",
        'guide_button': 'Руководство',
        'join_button': 'Присоединиться к сообществу 🌍',
        'about_button': 'О боте ℹ️',
        'select_language_button': 'Выберите язык 🌐',
        'guide': 'Вот как использовать бота...\n\n'
                 'Чтобы узнать время через несколько часов, используйте формат:\n'
                 '[час.минуты] [дополнительные часы]\n'
                 'Пример: 20.00 3\n\n'
                 'Чтобы конвертировать время между часовыми поясами, используйте формат:\n'
                 '[час.минуты] [исходный часовой пояс] [целевой часовой пояс]\n'
                 'Поддерживаемые часовые пояса: WIB, WITA, WIT, UTC\n'
                 'Пример: 20.00 WIB UTC\n\n'
                 'Используйте кнопку \'Руководство\', если вам нужна эта инструкция снова.',
        'about': 'Версия бота 1.0',
        'select_language': 'Выберите ваш язык:',
        'result': '╓──────────────────╥\n'
                  '│  ⊙ Введенное время : {time_str}\n'
                  '│\n'
                  '│  ⊙ Количество часов : {hours}\n'
                  '│\n'
                  '│  ⊙ Результат : {result_time}\n'
                  '╙──────────────────╜\n\n'
                  'Через {hours} часов будет {result_time}!',
        'timezone_conversion': 'Время {time_str} в {timezone_from} равно {converted_time} в {timezone_to}.',
        'error': 'Ошибка: Неверный формат ввода. Пожалуйста, используйте \'час.минуты часы\' или \'час.минуты источник_часового_пояса назначение_часового_пояса\'.',
        'timezone_error': 'Ошибка: Неверный часовой пояс. Пожалуйста, используйте один из поддерживаемых часовых поясов.'
    }
}
