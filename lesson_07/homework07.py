# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f"{number}  * {multiplier} = {result}")
        multiplier += 1


multiplication_table(5)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def multy_numbers (a,b):
    return a + b

sum_1 = multy_numbers(10,143)
print(sum_1)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def helf(numbers):
    return sum(numbers) / len(numbers)
print("Cереднє арифметичне списку 1 - ", helf([1, 2, 3, 4, 5, 12.1]))
print("Cереднє арифметичне списку 2 - ", helf([11,22, 33, 44, 55, 66]))
print("Cереднє арифметичне списку 3 - ", helf([101,202, 303, 404, 505, 606]))



# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(h):
    return h[::-1]

print(reverse_string("Hello"))
print(reverse_string("World"))
print(reverse_string("123456789"))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_words(words):
    if not words:
        return ""
    return max(words, key=len)

words = ["Python", "Javascript", "Qa", "Project", "International"]
print(longest_words(words))



# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
#def find_substring(str1, str2):

 #   return -1

#str1 = "Hello, world!"
#str2 = "world"
#print(find_substring(str1, str2)) # поверне 7

#str1 = "The quick brown fox jumps over the lazy dog"
#str2 = "cat"
#print(find_substring(str1, str2))


def find_substring(str1, str2):
    return str1.find(str2)

print(find_substring("Hello, world!", "world"))
print(find_substring("Hello, world!", "python"))
print(find_substring("aaaaa", "aa"))
print(find_substring("banana", "nan"))
print(find_substring("test", ""))
print(find_substring("", "abc"))



# task 7
def sum_of_even_numbers(numbers):
    """
    Обчислює суму всіх парних чиесел у списку.

    Args: numbers  (list): Список цілих чисел

    Returns: int: Сума всіх парних чисел у списку
    """
    return sum(x for x in numbers if x % 2 == 0)

print("Сумма парних чисел", sum_of_even_numbers([1, 2, 3, 4, 5, 6, 7]))

# task 8

def extract_strings(items):
    """
    Повертає новий список, що містить тільки рядкові елементи (тип str)
    з початкового списку.

    Args:
        items (list): Вхідний список з елементами будь-яких типів

    Returns:
        list: Список, що містить тільки рядки (str) у тому ж порядку
    """
    return [item for item in items if isinstance(item, str)]

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', 2424]

lst2 = extract_strings(lst1)
print(lst2)


# task 9
def has_both_h_and_H(text):
    return 'h' in text.lower() and 'H' in text.upper()



while True:
    word = input("Enter your text: ")
    if has_both_h_and_H(word):
        print("Знайдено шукане значення:")
    else:
        print("Не знайдено шукане значення:")

#task 10
    def get_only_strings(items):
        return [item for item in items if isinstance(item, str)]


    lst1 = ['111', '2124', 33, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'ENGLISH', 2424]

    lst2 = get_only_strings(lst1)
    print(lst2)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""





