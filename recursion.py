def recursive_func(my_list, index=0):
    # Базовый случай: если индекс равен длине массива, вернуться
    if index == len(my_list):
        return
    
    # Действия на каждом шаге рекурсии
    print(my_list[index])
    
    # Рекурсивный вызов функции для следующего элемента
    recursive_func(my_list, index+1)

# Пример использования функции
my_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
recursive_func(my_list)