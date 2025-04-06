class Car:
    manufacturer: str = "Unknown"
    fuel_type: str = "Gasoline"

    def __init__(self, model: str, year: int, color: str, mileage: float, price: float) -> None:
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.price = price

    def __str__(self) -> str:
        return f"{self.year} {self.color} {self.model} - ${self.price}"

    def is_new(self) -> bool:
        return self.year >= 2020

    def drive(self, distance: float) -> None:
        if distance > 0:
            self.mileage += distance
        else:
            print("Distance must be positive.")

    def update_price(self, new_price: float) -> None:
        if new_price >= 0:
            self.price = new_price
        else:
            print("Price cannot be negative.")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Car):
            return self.model == other.model and self.year == other.year
        return False


car1 = Car("Toyota Camry", 2021, "White", 15000, 25000)
car2 = Car("Ford Focus", 2019, "Red", 30000, 15000)
car3 = Car("Toyota Camry", 2021, "Black", 12000, 24000)

print(car1)  # вывод информации об автомобиле
print(car2.is_new())  # проверка, новый ли автомобиль
car3.drive(200)  # добавление пробега
print(car3.mileage)  # вывод пробега после вождения
car2.update_price(14000)  # обновление цены
print(car2.price)  # вывод новой цены
print(car1 == car3)  # проверка эквивалентности двух автомобилей