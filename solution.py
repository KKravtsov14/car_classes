class Carbase:
    def __init__(self, car_type, brand, photo_le_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_le_name = photo_le_name
        if carrying != '':
            self.carrying = float(carrying)
        else:
            self.carrying = None

    def get_photo_le_ext(self):
        if self.photo_le_name.count('.') > 0:
            front, end = self.photo_le_name.split('.')
            return end

        else:
            return None

    def __repr__(self):
        return self.car_type


class Car(Carbase):
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, carrying, ):
        super().__init__(car_type, brand, photo_le_name, carrying)
        if passenger_seats_count != '':
            self.passenger_seats_count = int(passenger_seats_count)
        else:
            self.passenger_seats_count = 0

class Truck(Carbase):
    def __init__(self, car_type, brand, photo_le_name, body_whl, carrying):
        super().__init__(car_type, brand, photo_le_name, carrying)
        if body_whl.count('x') == 2:
            body_length, body_width, body_height = map(float, body_whl.split('x'))
        else:
            body_length = 0.0
            body_width = 0.0
            body_height = 0.0

        self.body_length = body_length
        self.body_width = body_width
        self.body_height = body_height

    def get_body_volume(self):
        return self.body_height * self.body_width * self.body_height


class Specmachine(Carbase):
    def __init__(self, car_type, brand, photo_le_name, carrying, extra):
        super().__init__(car_type, brand, photo_le_name, carrying)
        self.extra = extra


def get_car_list(filename):
    car_list = []
    car_list_str = []
    with open(filename, 'r') as inp_f:
        for i in inp_f:
            if i.count(';') == 6:
                car_list_str.append(list(map(str, i.split(';'))))

    for i in range(len(car_list_str)):
        type_list = ['car', 'truck', 'spec_machine']
        if car_list_str[i][0].lower() in type_list:
            if car_list_str[i][0].lower() == type_list[0]:
                car_type = car_list_str[i][0]
                brand = car_list_str[i][1]
                passenger_seats_count = car_list_str[i][2]
                photo_le_name = car_list_str[i][3]
                carrying = car_list_str[i][5]
                car_list.append(Car(car_type, brand, passenger_seats_count, photo_le_name, carrying))

            elif car_list_str[i][0].lower() == type_list[1]:
                car_type = car_list_str[i][0]
                brand = car_list_str[i][1]
                body_whl = car_list_str[i][4]
                photo_le_name = car_list_str[i][3]
                carrying = car_list_str[i][5]
                car_list.append(Truck(car_type, brand, photo_le_name, body_whl, carrying))

            elif car_list_str[i][0].lower() == type_list[2]:
                car_type = car_list_str[i][0]
                brand = car_list_str[i][1]
                extra = car_list_str[i][6]
                photo_le_name = car_list_str[i][3]
                carrying = car_list_str[i][5]
                car_list.append(Specmachine(car_type, brand, photo_le_name, carrying, extra))

    return car_list


def main():
    car_list = get_car_list('solution.txt')
    return car_list


if __name__ == '__main__':
    main()