# Kydienko Daniil

# 1. Создайте класс Vehicle с атрибутами экземпляра max_speed и mileage
# 2. Создайте класс Vehicle без переменных и методов
# 3. Создайте класс Person с атрибутами экземпляра first_name,last_name,middle_name,email,is_active
# и методами get_full_name - возвращает полное имя, get_gmail - возвращает только почту с доменом @gmail.com.
# Создайте 5 экземпляров класса Person с разными параметрами и выведите в консоль все параметры созданных вами классов.

class Vehicle:
    max_speed = 980
    mileage = 29323923

    def wroom_wroom(self):
        print('The car is moving at a speed: ', self.max_speed, ' Mileage in 20 seconds = ', self.mileage)


Vehicle.test = Vehicle()
Vehicle.test.wroom_wroom()


class VVehicle:
    print('E M P T Y')

Vehicle2 = VVehicle()
print(Vehicle2)


class Person:
    last_name = 'Фамилия'
    first_name = 'Имя '
    middle_name = 'Отчествович'
    email = 'no.imagination'
    is_active = 'yes'

    def get_full_name(self):
        print('Приветствую, меня зовут ', self.last_name, self.first_name, self.middle_name)

    def get_gmail(self):
        print(self.email + '@gmail.com')  # вот тут я немного не понял задание поэтому просто добавил gmail


Person1 = Person()
Person2 = Person()
Person3 = Person()
Person4 = Person()
Person5 = Person()

Person1.last_name = 'Коржиков'
Person1.first_name = 'Аппетит'
Person1.middle_name = 'Голодович'
Person1.email = 'must.go.eat_something'

Person2.last_name = 'Воображалович'
Person2.first_name = 'Закончился'
Person2.middle_name = 'Совсемович'
Person2.is_active = 'no'

Person3.last_name = 'Тевс'
Person3.first_name = 'Вадим'
Person3.middle_name = 'Максимович'
Person3.email = 'friend.name'

Person4.last_name = 'Colt'
Person4.first_name = 'Samuel'
Person4.middle_name = ''
Person4.is_active = '~~~'

Person5.last_name = 'Буянов'
Person5.first_name = 'Никита'
Person5.middle_name = 'Таркович'
Person5.email = 'escape.from.tarkov'


Person1.get_full_name()
Person1.get_gmail()
print('~'*15)

Person2.get_full_name()
Person2.get_gmail()
print('~'*15)

Person3.get_full_name()
Person3.get_gmail()
print('~'*15)

Person4.get_full_name()
Person4.get_gmail()
print('~'*15)

Person5.get_full_name()
Person5.get_gmail()
print('~'*15)