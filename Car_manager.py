import random
import math
from turtle import Turtle

colors = ["blue", "green", "black", "red", "purple"]
LENGTH_OF_THE_TRACK = 520
NUMBER_OF_LANES = LENGTH_OF_THE_TRACK / 20


class CarManager:
    def __init__(self):
        self.cars = []

        self.all_lanes = []
        self.safe_lanes = []
        self.lanes = []

        self.create_lanes()
        self.create_safe_lanes()
        self.final_lanes()
        self.create_cars()
        self.print_safe_lanes()
        self.write_on_safe_lines()

    def create_cars(self):
        for car in range(random.randint(20, 30)):
            car = Turtle()
            car.penup()
            car.setheading(180)
            car.shape("square")
            car.shapesize(stretch_len=3, stretch_wid=1)
            car.color(random.choice(colors))
            car.goto(x=random.randint(-320, 700), y=random.choice(self.lanes))
            self.cars.append(car)

    def create_safe_lanes(self):
        safe_lanes = random.randint(2, 4)
        for new_safe_lane in self.all_lanes[2::int(round(len(self.all_lanes)/safe_lanes))]:
            self.safe_lanes.append(new_safe_lane)

    def create_lanes(self):
        for new_lanes in range(int(NUMBER_OF_LANES)):
            lane_coordinate = -260 + new_lanes * 20
            self.all_lanes.append(lane_coordinate)

    def final_lanes(self):
        """Extract a new list from the differences between the two. Elements in a - elements in b"""
        self.lanes = [item for item in self.all_lanes if item not in self.safe_lanes]

    def random_line(self):
        return random.randint(400, 800), random.choice(self.lanes)

    def loop_cars(self, car):
        car.goto(self.random_line())

    def move_cars(self):
        for car in self.cars:
            if car.xcor() >= -420:
                car.forward(10)
            else:
                pass
                self.loop_cars(car)

    def print_safe_lanes(self):
        printer = Turtle()
        printer.hideturtle()
        printer.penup()
        printer.pensize(2)
        printer.color('green')
        for lane in self.safe_lanes:
            printer.goto(400, lane-10)
            printer.setheading(180)
            printer.pendown()
            printer.forward(800)
            printer.penup()
            printer.goto(400, lane+10)
            printer.setheading(180)
            printer.pendown()
            printer.forward(800)
            printer.penup()

    def write_on_safe_lines(self):
        printer_for_safe_lines = Turtle()
        printer_for_safe_lines.hideturtle()
        printer_for_safe_lines.color("Green")
        printer_for_safe_lines.penup()
        for lane in self.safe_lanes:
            printer_for_safe_lines.goto(x=-350, y=lane-9)
            printer_for_safe_lines.pendown()
            printer_for_safe_lines.write("Safe lane", False, 'center', ('Arial', 11, 'normal'))
            printer_for_safe_lines.penup()

