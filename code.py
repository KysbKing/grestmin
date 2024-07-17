Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Функция для чтения CSV-файла и поиска пользователя по ID
def find_user_by_id(user_id):
    try:
        df = pd.read_csv('telegram.csv')
        user = df.loc[df['id'] == int(user_id)]
        if not user.empty:
            return user.iloc[0].to_dict()
        else:
            return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

# Обработчик команды /find
def find(update: Update, context: CallbackContext) -> None:
    user_id = context.args[0] if context.args else None
    if user_id:
        user = find_user_by_id(user_id)
        if user:
            user_info = (f"id: {user['id']}\n"
                         f"phone: {user['phone']}\n"
                         f"username: {user['username']}\n"
                         f"first_name: {user['first_name']}\n"
                         f"last_name: {user['last_name']}")
            update.message.reply_text(user_info)
        else:
            update.message.reply_text(f"User with id {user_id} not found.")
    else:
        update.message.reply_text("Please provide a user ID.")

def main() -> None:
    # Вставьте сюда токен вашего бота
    updater = Updater(7422393988:AAG4VeTdo4EaO5fxxulhO8nm6Ygom09_048)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("find", find))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
