import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # создаем пустой списк для записи количества попыток
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    # заполняем список количеством попыток для угадывания
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # считаем среднее значение
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0 # инициализируем число попыток
    predict = np.random.randint(1, 101) # угадываем число
    
    interval_min = 1 # инициализируем начало интервала
    interval_max = 100 # инициализируем конец интервала
    
    # пока не угадали
    while number != predict:
        count += 1 # инкрементируем счетчик попыток

        # если загаданное меньше предсказанного
        if number < predict:
            interval_max = predict # конец интервала - предсказанное число
            predict = (interval_max - interval_min) // 2 # предсказанное - середина
         
        # если загаданное больше предсказанного   
        elif number > predict:
            interval_min = predict + 1 # начало интервала - следующее после предсказанного
            predict = (interval_max + interval_min) // 2 # предсказанное - середина интервала

    return count
    # Ваш код заканчивается здесь


if __name__ == "__main__":
    # RUN
    print('Run benchmarking for game_core_v3: ', end='')
    score_game(game_core_v3)


