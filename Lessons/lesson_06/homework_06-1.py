while True:
    s = input ("Введіть сюди свій текст:")
    count = len(s)
    if not s:
     print("Поле не може бути пустим")
    if count >= 10:
        print("True")
    if count < 10 and count != 0:
        print("False")