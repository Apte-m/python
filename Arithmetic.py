a,b = map(int, input().split())


print(2 * (a + b ))

number = 46275

# Получение количества десятков и единиц
units = number % 10
tens = (number // 10) % 10

# Возведение количества десятков в степень количества единиц
result = tens ** units

# Умножение результата на количество сотен
result *= ((number // 100) % 10)

# Деление результата на разность количества десятков тысячи и количества тысяч
result /= ((number // 10000) % 10) - (number // 1000) % 10

print(result)

  

 