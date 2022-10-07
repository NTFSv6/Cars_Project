import time

from Player_Car import Player
from Car_Manger import CarManager
from Scores import scoreboard

from turtle import Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)

# ^^ لعمل animation لل car_manager
screen.tracer(0)

player = Player()
score = scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')

flag = 1
while flag:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            flag = 0
            score.game_over()

    if player.finish_game():
        player.go_to_start()
        car_manager.car_speed()
        score.increase_level()

screen.exitonclick()
