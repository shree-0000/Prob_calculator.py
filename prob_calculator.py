from copy import copy, deepcopy 
from random import randrange

class Hat:
    def __init__(self, **colors) -> None:
        #run validiations
        assert len(colors)>0, "Please input atleast one colored ball"

        self.contents = []
        for color, no in colors.colors():
            self.contents += [color]*no

    def draw(self, draw_no) -> list:
        return_list = []
        if draw_no >= len(self.contents):
            return_list = self.contents
        else:
            for i in range(draw_no):
                return_list.append(self.contents.pop(randrange(len(self.contents))))
        return return_list


def experiment(hat: object, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
    
    M = 0
    for i in range(num_experiments):
        expected_balls_copy = copy(expected_balls)
        hat_obj_copy = deepcopy(hat)
        drawn_balls_list = hat_obj_copy.draw(num_balls_drawn)
        for color in drawn_balls_list: 
            if color in expected_balls_copy:
                expected_balls_copy[color] -= 1
        if max(expected_balls_copy.values()) == 0:
            M += 1

    return M/num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=3,
                  num_experiments=20000)
print(f"Probability : {probability}")