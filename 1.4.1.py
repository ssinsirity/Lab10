# 1. Сформувати функцію для введення з клавіатури послідовності чисел і виведення її на екран у зворотному порядку
# (завершаючий символ послідовності – крапка)
# Гевчук Максим КН-А

import timeit
# from memory_profiler import profile


# @profile
def recursion(s):
    # Послідовність перебирається з кінця до початку, склеюючи нову послідовність із символів.
    # Коли передана у функ. послідовність буде пустою, то до нової додається крапка в кінці

    """if s == '':
        return '.'
    else:
        return s[-1] + recursion(s[:-1])"""

    return '.' if s == '' else s[-1] + recursion(s[:-1])


# @profile
def iteration(s):
    # у випадку ітерації послідовність теж перебирається з кінця та склеюються в нову послідовність, а потім
    # в кінці додається крапка

    text = ''
    for i in range(len(s) - 1, -1, -1):
        text += s[i]
    return text + '.'


string = input(f'Введіть послідовність чисел: ')

# виведення результатів
print(f"Результат рекурсії: {recursion(string)}")
print(f"Результат ітерації: {iteration(string)}")
print(f"Час роботи рекурсії: "
      f"{timeit.timeit('recursion(string)', setup='from __main__ import recursion, string', number=1)}")
print(f"Час роботи ітерації: "
      f"{timeit.timeit('iteration(string)', setup='from __main__ import iteration, string', number=1)}")

# В усіх функціях обсяг використаної пам'яті варіюється від 13.3 до 13.9 МіВ
# Час розробки рекурсії переважає за час розробки ітерації
# Різниця часу роботи залежить від кількості дани - якщо їх більше, то і різниця набагато більша (рекурсія працює довже
# ніж ітерація). На початку відношення часу = 2, зі збільшенням к-сті даних збільшується поступово.
# Отож у даному варіанті варто використовувати рекурсію, тому що в неї простіша читабельність, аніж в ітерації, але якщо
# ми працюємо з великими даними, то ітерація буде кращим варіантом.