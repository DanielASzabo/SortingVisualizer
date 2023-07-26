import random
#import pygame



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
    while not_sorted:
        pass
    pass


def create_array(size, min, max, unique_numbers):
    random_array = []
    if unique_numbers:
        if max-min >= size:
            filled = False
            not_used_numbers = [True]*(max-min+1)
            while not(filled):
                new_random_number = random.randint(min, max)
                #Checks if the new random number that is created already in use
                if not_used_numbers[new_random_number-min]:
                    random_array.append(new_random_number)
                    print(random_array)
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


def run_sorting():
    pass


if __name__ == "__main__":
    print(create_array(15,5,15,True))