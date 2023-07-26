import random
from tkinter import ttk
from tkinter import *


def bubble_soring(array):
    not_sorted = True
    while(not_sorted):
        pass
    pass


def merge_sorting(array):
    not_sorted = True
    while (not_sorted):
        pass
    pass


def binary_sorting(array):
    not_sorted = True
    while (not_sorted):
        pass
    pass


def update_screen(array):
    not_sorted = True
    while (not_sorted):
        pass
    pass


def create_array(size, min, max):
    random_array = []
    for i in range(size):
        random_array.append(random.randint(min, max))
    return random_array


if __name__ == "__main__":
    root = Tk()
    root.geometry("900x700")
    root.title("Sorting Visualizer")
    rand_array = create_array(5, 1, 1)
    print()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    #ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    #ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
    #sorable_array = create_array()
    #bubble_soring(sorable_array)