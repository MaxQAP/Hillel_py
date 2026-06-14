#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
"\"Would you tell me, please, which way I ought to go from here?\"\n"
"\"That depends a good deal on where you want to get to,\" said the Cat.\n"
"\"I don't much care where -\" said Alice.\n"
"\"Then it doesn't matter which way you go,\" said the Cat.\n"
"\"- so long as I get somewhere,\" Alice added as an explanation.\n"
"\"Oh, you're sure to do that,\" said the Cat, \"if you only walk long enough.\""
)
print(alice_in_wonderland)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
print("Одинарні лапки (') зустрічаються  в тексті на позиціях:")

for index, char in enumerate(alice_in_wonderland):
    if char == "'":
        print(f"Позиція {index}: '{char}'")

# task 03 == Виведіть змінну alice_in_wonderland на друк
print("\nПовний текст діалогу:")
print(alice_in_wonderland)




"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
Blacksea = 436402
Azovsea = 37800
Area = Blacksea + Azovsea
print("Загальна площа:", Area, "км²")



# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

first_and_second = 250449
second_and_third = 222950
total = 375291

var1 = total - 222950
var2 = first_and_second - var1
var3 = second_and_third - var2
sum = var1 + var2 + var3
print ("Перший склад - ", var1, "товарів")
print ("Другий склад -", var2, "товарів")
print ( "Третій склад -", var3, "товарів")
print("Всього товірів -", sum, "товарів")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

monthly_payment = 1179
price = monthly_payment * 18
print ("Вартість ком'ютера становить:", price, "грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 7
c = 2789 % 5
d = 7247 % 6
e = 7128 % 5
f = 19224 % 9

print(f"a) 8019/8 остача  {a}")
print(f"b) 9907/7 остача {b}")
print(f"c) 2789/5 остача {c}")
print(f"d) 7247/6 остача {d}")
print(f"e) 7128/5 остача {e}")
print(f"f) 19224/9 остача {f}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big = 4 * 274
pizza_medium = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
sum = pizza_big + pizza_medium + juice + cake + water

print ("Вартість великих піц", pizza_big, "грн")
print ("Вартість середніх піц", pizza_medium, "грн")
print ("Вартість соку", juice, "грн")
print ("Вартість тортів", cake, "грн")
print ("Вартість води",water , "грн")
print ("Загальна вартість замовлення", sum, "грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

sum = 232
pages = sum // 8
print("Ігорю знадобиться", pages, "сторінок")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
gasoline = 1600 // 100 * 9
print("Знадобиться", gasoline, "літрів бензину")
tank = 144 // 48
print("Знадобиться", tank, "рази заїзджати на заправку, з розрахунком перщої заправки перед подорожжю")
tank_2 = ( 144 - 48 ) // 48
print("Саме в дорозі між Харковом та Будапештом знадобиться", tank_2, "рази заїджати на заправку" )