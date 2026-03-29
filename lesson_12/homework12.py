def sum_of_even_numbers(numbers):
        return sum(x for x in numbers if x % 2 == 0)
#print("Сумма парних чисел", sum_of_even_numbers([1, 2, 3, 4, 5, 6, 7]))



def has_h_in_both_cases(word):
    return 'h' in word and 'H' in word


def check_text_length(s):
    count = len(s)
    if not s:
        return "Поле не може бути пустим"
    if count >= 10:
        return "True"
    if count < 10 and count != 0:
        return "False"
    return None