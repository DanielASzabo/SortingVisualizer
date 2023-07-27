import random
import pygame

import sorting_algorithms
from pygameobjects import *
from sorting_algorithms import *

def create_array(size: int, min: int, max: int, unique_numbers: bool):
    random_array = []
    if unique_numbers:
        if max - min >= size:
            filled = False
            not_used_numbers = [True] * (max - min + 1)
            while not filled:
                new_random_number = random.randint(min, max)
                # Checks if the new random number that is created already in use
                if not_used_numbers[new_random_number - min]:
                    random_array.append(new_random_number)
                    not_used_numbers[new_random_number - min] = False
                    if len(random_array) == size:
                        filled = True

        else:
            print("Error")
            print("There are not enough nuber to fill this size creating with duplicates")
            for i in range(size):
                random_array.append(random.randint(min, max))
    else:
        print("here")
        for i in range(size):
            random_array.append(random.randint(min, max))
    return random_array


def update_screen(array):
    not_sorted = True
    while not_sorted:
        pass
    pass


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 600


def run_sorting():
    pass


def draw_screen():
    pass


if __name__ == "__main__":

    min_number = 40
    max_number = 10000
    array_size = 60
    no_duplicates = True
    win = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    while True:
        random_array = create_array(array_size, min_number, max_number, no_duplicates)
        pillars = create_pillars(random_array, DISPLAY_WIDTH, DISPLAY_HEIGHT, GREEN)
        sorting_algorithms.bubble_soring_pillars(pillars, GREEN, (0, 0, 0), win)

    run = True
    while run:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for pillar in pillars:
            pillar.draw(win)
        pygame.display.update()

        clock.tick(3)
    pygame.quit()
