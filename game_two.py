import random

CHAT_DATA = {}

def generate_number():
    return random.randint(1, 10)

def guess_number(message, chat_id, CHAT_DATA):
    if CHAT_DATA[chat_id]["attempt"] <= 3:
        try:
            guess = int(message.text)
            if guess == CHAT_DATA[chat_id]["number"]:
                return f"Поздравляю, ты угадал число! Кол-во попыток: {CHAT_DATA[chat_id]['attempt']}"
            elif guess < CHAT_DATA[chat_id]["number"]:
                CHAT_DATA[chat_id]["attempt"] += 1 
                return "Загаданное число больше."
            else:
                CHAT_DATA[chat_id]["attempt"] += 1 
                return "Загаданное число меньше."
        except ValueError:
            return "Пожалуйста, введи число от 1 до 10."
    else:
        return "Попытки кончились"

