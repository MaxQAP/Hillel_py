class diamond:
    def __init__(self,side_a, corner_a):
        self.side_a = side_a
        self.corner_a = corner_a
    def __setattr__(self, name, value):
        if name == 'side_a':
            if not isinstance(value, (int,float)) or value <= 0:
                raise ValueError("Довжина будь якої сторони має бути більше 0")
            super().__setattr__(name, float(value))

        elif name == 'corner_a':
            if not isinstance(value, (int,float)):
                raise ValueError("кут має бути числом")

            corner = float(value)
            if corner <= 0 or corner >= 180:
                raise ValueError("Кут повинен бути в межах менше 180 градусів")

            super().__setattr__("corner_a", corner)
            super().__setattr__('corner_b', 180 - corner)

        elif name == 'corner_b':
            raise AttributeError("Атрибут 'кут_б' тільки для читання. "
                         "Змінюйте кут_а — кут_б обчислюється автоматично")

        else:
            super().__setattr__(name, value)
    def __getattr__(self, name):
        if name == 'corner_b':
            return 180 - self.corner_a
        raise AttributeError (f"Об'єкт {type(self).__name__} не має атрибута '{name}'")
    def __str__(self):
        return (f"Ромб (сторона  = {self.side_a:.2f}, "
                f"A = {self.corner_a:.1f}°, B = {self.corner_b:.1f}°)")
if __name__ == "__main__":
    try:
        r1 = diamond(1, 120)
        #r1 = diamond(5, 200)
        print(r1)


    except (ValueError, AttributeError) as e:
        print("Помилка:", e)