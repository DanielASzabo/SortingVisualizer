import pygame


class Pillar:
    def __init__(self, x_pos, y_pos, width, lenght, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.length = lenght
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x_pos, self.y_pos, self.width, self.length))


def create_pillars(array, size_of_screen_x, size_of_screen_y, color):
    array_size = len(array)
    pillar_width = size_of_screen_x / (array_size + array_size / 2)
    pillars = []
    for i in range(array_size):
        x_pos = pillar_width * i + i * (pillar_width / 2)
        pillar_len = array[i] * (size_of_screen_y / max(array))
        y_pos = size_of_screen_y - pillar_len
        pillars.append(Pillar(x_pos, y_pos, pillar_width, pillar_len, color))
    return pillars
