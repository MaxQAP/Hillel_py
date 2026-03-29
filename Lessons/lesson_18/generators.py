def even_numbers(m):
    for num in range(2, m + 1, 2):
    #for num in range(12, n + 1, 4):
        yield num
        #yield num * 2

for num in even_numbers(44):
    print(num, end=' ')

print("\n")


#print(list(even_numbers(44)))