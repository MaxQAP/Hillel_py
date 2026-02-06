#my_list = [”7,3,2,4”, ”10,23,abc,3,4,20” ”python7,2,3”]

def sum_numbers(input_list):
    try:
        parts = input_list.split(",")
        #total = sum(float(part.strip()) for part in parts) - для виведення чисел з дробами
        total = sum(int(part.strip()) for part in parts)
        return total
    except ValueError:
        return "Не можу зробити"

data = [
    "7,32,2,4",
    "10,23,abc,3,4,20",
    "python7,2,3",
    "1, 0.6",
    "2",
    "1000, 777, 333, 61152",
    "My name is "
]

#data = [
    #"1,2,3,4",
    #"1,2,3,4,50",
    #"qwerty1,2,3"
#]
for item in data:
    result = sum_numbers(item)
    print(result)