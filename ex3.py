# Класс Tomato:+
# 1. Создайте класс Tomato+
# 2. Создайте статическое свойство states, которое будет содержать все стадии созревания помидора+
# 3. Создайте метод __init__(), внутри которого будут определены два динамических protected свойства:
# 1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)
class Tomato:

    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}# Стадии созревания помидора

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):# Переход к следующей стадии созревания
        if self._state < 3:
            self._state += 1
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')

    def is_ripe(self):# Проверка, созрел ли томат
        if self._state == 3:
            return True
        return False
# _______________________________________________________
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса Tomato.
# Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая
class TomatoBush:
    def __init__(self, num):# Создаем список из объектов класса Tomato
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):# Переводим все томаты из списка на следующий этап созревания
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):# Проверяем, все ли помидоры созрели
        return all([i.is_ripe() for i in self.tomatoes])

    def give_away_all(self):# Собираем урожай
        self.tomatoes = []

# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.

class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник работает!')
        self._plant.grow_all()

    def harvest(self):
        print('Проверяет созрели ли плоды...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай созрел')
        else:
            print('Еще не все плоды готовы.')

    @staticmethod# Выводит справку по садоводству
    def knowledge_base():
        print('Садовник занимается выращиванием  томатов и сбором урожая.')


# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай
if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()