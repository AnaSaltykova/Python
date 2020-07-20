# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 0, 'bonus': 0}


class Position(Worker):
    def __init__(self, name, surname, position, _income,):
        super().__init__(name, surname, position, _income)
        self.full_name = name + ' ' + surname
        self.total_income = sum(_income.values())

    def get_full_name(self):
        return self.full_name

    def get_total_income(self):
        return self.total_income


b = Position('Gomer', 'Simpson', 'nuclear safety inspector', {'wage': 5000, 'bonus': 1200})
print(b.get_full_name())
print(b.get_total_income())
