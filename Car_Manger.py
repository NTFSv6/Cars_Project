from turtle import Turtle
import random

color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

Start_Move_Distance = 5

Move_Increment = 3

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speedd = Start_Move_Distance

    def create_cars(self):

        # ^^ يختار رقم عشوئي ما بين الرقمين الذي يتم كتابتهم
        chance = random.randint(1, 7)
        if chance == 1:
            new_car = Turtle('square')
            # ? للتحكم في حجم ال turtle
            new_car.shapesize(stretch_wid=0.7, stretch_len=1.7)
            new_car.penup()
            new_car.color(random.choice(color_list))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speedd)

    def car_speed(self):
        self.car_speedd += Move_Increment
