class Car:
    def __init__(self, height, weight, color, color_wheel,color_glass,color_headlight,color_tail_light, color_bumper):
        self.height = height
        self.weight = weight
        self.color_wheel = color_wheel
        self.color_glass = color_glass
        self.color_headlight = color_headlight
        self.color_tail_light = color_tail_light
        self.color_bumper = color_bumper
        self.color = color
    def say_sound(self):
        print('beep')
    def say_long_sound(self):
        print('beep-beep')

    def get_color(self):
        print(self.color)

    def get_color_wheel(self):
        print(self.color_wheel)

    def get_color_glass(self):
        print(self.color_glass)

    def get_color_headlight(self):
        print(self.color_headlight)

    def get_color_tail_light(self):
        print(self.color_tail_light)

    def get_color_bumper(self):
        print(self.color_bumper)


Lambrgambr = Car(293847938, 2000, 'green', 'yellow', 'black','white','pink','purple',)

print(Lambrgambr.height)
print(Lambrgambr.weight)
print(Lambrgambr.color)
print(Lambrgambr.color_wheel)
print(Lambrgambr.color_glass)
print(Lambrgambr.color_headlight)
print(Lambrgambr.color_tail_light)
print(Lambrgambr.color_bumper)

Lambrgambr.say_sound()
Lambrgambr.say_long_sound()
