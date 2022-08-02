# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, state, field, base_speed):
        self.state = state
        self.field = field
        self.base_speed = base_speed


    def move(self, direction):
        actual_speed = self._get_speed()
        if direction == 'UP':
            self.field.set.unit()


        elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
        elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
        elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed

    def _get_speed(self):
        if self.state == 'fly':
            return self.base_speed * 1,2
        elif self.state == 'crawl':
            return self.base_speed * 0,5
        else:
            raise ValueError('Неверное состояние игрока')


#     ...
