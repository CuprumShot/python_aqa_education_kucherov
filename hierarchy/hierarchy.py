

class Transport:
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.country = kwargs['country']
            self.company = kwargs['company']
            self.model = kwargs['model']
            self.color = kwargs['color']
            self.year = kwargs['year']
            # self.passengers = kwargs['passengers']
        elif args:
            self.country = args[0]
            self.company = args[1]
            self.model = args[2]
            self.color = args[3]
            self.year = args[4]
            # self.passengers = args[5]

    def __str__(self):
        print(f'\nIt\'s just a {self.company} transport.')

    def transport_description(self):
        print(f'''!!! Little bit of information about !!! 
>>> It was created in {self.country} in {self.year} <<<
>>> The model of one is {self.model} <<<
>>> Also, nice {self.color} color <<<\n''')


class RegularCars(Transport):  # sedan / pickup / etc
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
            self.classification = kwargs['classification']
        elif args:  # бросить исключение насчёт количества элементов
            self.classification = args[5]

    def transport_description(self, *args, **kwargs):
        super().transport_description()
        # Transport.transport_description(self)
        return f'It\'s a {self.classification} car!'

    def __str__(self):
        print(f'It\'s a regular {self.company} car.')


class Engine(RegularCars):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
            self.engine = kwargs['engine']
        elif args:
            self.engine = args[6]

    def transport_description(self, *args, **kwargs):
        super().transport_description()
        # Transport.transport_description(self)
        return f'This car has a {self.engine} engine!'

    def __str__(self):
        print(f'The {self.company} company has cars with great engine.')


class SpecialCars(Transport):  # police / ambulance / etc
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
            self.purpose = kwargs['purpose']
        elif args:
            # try:  # бросить исключение насчёт количества элементов
            self.purpose = args[5]

    def __str__(self):
        print(f'It\'s a special {self.company} transport.')


class CarOrientation(SpecialCars):  # military / civilian
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
            self.orientation = kwargs['orientation']
        elif args:
            # try:  # бросить исключение насчёт количества элементов
            self.orientation = args[6]

    def __str__(self):
        print(f'It\'s a {self.orientation} orientation transport of {self.company} company.')


class Passengers(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
            self.passengers = kwargs['passengers']
        elif args:
            self.passengers = args[5]

    def transport_description(self, *args, **kwargs):
        super().transport_description()
        # Transport.transport_description(self)
        return f'This car for {self.passengers} passengers!'

    def __add__(self, other):
        total_passengers = self.passengers + other.passengers
        return total_passengers

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __str__(self):
        print(f'This is a very roomy {self.company} transport! It can even hold {self.passengers} people!')


def main():
    bike = Transport('Ukrainian SSR', 'Kharkiv Bicycle Plant', 'Ukraine', 'blue', '1926')
    bike.__str__()
    bike.transport_description()

    honda = RegularCars('Japan', 'Honda', 'Civic', 'red', '2003', 'sedan')
    honda.__str__()
    honda.transport_description()

    bmw = Engine('Germany', 'BMW', 'X5', 'black', '2010', 'crossover', 'Petrol')
    bmw.__str__()
    bmw.transport_description()

    sprinter = SpecialCars('Germany', 'Mercedes', 'Benz', 'white', '2012', 'bus')
    sprinter.__str__()
    sprinter.transport_description()

    ambulance = CarOrientation('France', 'Fiat', 'Ducato', 'yellow', '2010', 'minibus', 'ambulance')
    ambulance.__str__()
    ambulance.transport_description()

    riot = Passengers('USA', 'Lenco Industries', 'Lenco BearCat', 'green', '2017', 10)
    max_riot = Passengers('USA', 'Lenco Industries', 'Lenco BearCat', 'green', '2017', 12)
    riot.__str__()
    riot.transport_description()
    super_riot = max_riot + riot
    print(f'Cool riot car has {super_riot} passengers!!!')


if __name__ == '__main__':
    main()
