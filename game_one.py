import telebot
from random import choice

game_choice = {
    1 : 'камень',
    2: 'ножницы',
    3: 'бумага'
}

user_score = 0
bot_score = 0

def reset_score():
    global user_score, bot_score
    user_score = 0
    bot_score = 0
    return 'Игра окончена! Счет сброшен!'

def game(user_choise: int):
    global user_score, bot_score

    computer_choise = choice(list(game_choice))
    if user_choise == computer_choise:
        result = f'Ничья, бот выбрал {game_choice[computer_choise]}'
    elif user_choise == 1 and computer_choise == 2 or \
    user_choise == 2 and computer_choise == 3 or \
    user_choise == 3 and computer_choise == 1:
        user_score += 1  
        result = f'Вы выиграли, бот выбрал {game_choice[computer_choise]}. Счет: {user_score}:{bot_score}'
    elif user_choise == 1 and computer_choise == 3 or \
    user_choise == 2 and computer_choise == 1 or \
    user_choise == 3 and computer_choise == 2:
        bot_score += 1  
        result = f'Вы проиграли, бот выбрал {game_choice[computer_choise]}. Счет: {user_score}:{bot_score}'
    else:
        result = 'Выберите корректный смайл'

    if user_score == 3 or bot_score == 3:
        if user_score > bot_score:
            result += "\nИгра окончена! Вы выиграли!"
        else:
            result += "\nИгра окончена! Вы проиграли!"

        # Сброс счета после окончания игры
        reset_score()
    
    return result
