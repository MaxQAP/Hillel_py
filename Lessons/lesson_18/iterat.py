class ReverseListIterator:

    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.lst[self.index]

words = ["Phyton", "qa", "java", "Dnipro", "internet"]


print("Зворотний порядок :")
for fruit in ReverseListIterator(words):
    print(fruit)


class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        result = self.current
        self.current += 2

        return result

print("Парні числа до 20:")
for num in EvenNumbers(n=20):
    print(num, end=" ")


