import pygame


def bubble_soring(array):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                not_sorted = True
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp

#todo change that the window dosent need to be passed down
def bubble_soring_pillars(pillars, pillar_color,selected_color,win):
    for pillar in pillars:
        pillar.color = pillar_color
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(pillars) - 1):
            if pillars[i].length > pillars[i + 1].length:
                not_sorted = True
                container = pillars[i]
                pillars[i] = pillars[i + 1]
                pillars[i + 1] = container
                container = pillars[i].x_pos
                pillars[i].x_pos = pillars[i + 1].x_pos
                pillars[i + 1].x_pos = container
                pillars[i].color = selected_color
                pillars[i + 1].color = selected_color
            else:
                pillars[i].color = selected_color
                pygame.time.delay(1)

            draw_window(pillars,win)
            pillars[i].color = pillar_color
            pillars[i + 1].color = pillar_color


def merge_sorting(array):
    not_sorted = True
    while not_sorted:
        pass
    pass


def binary_sorting(array):
    not_sorted = True
    while not_sorted:
        pass
    pass

#todo need to think out where to put the window drawing

def draw_window(objects,win):
    win.fill((255,255,255))
    pygame.time.delay(2)
    for object in objects:
        object.draw(win)
    pygame.display.update()