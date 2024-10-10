# https://www.youtube.com/watch?v=2gABYM5M0ww&t=424s
# https://dafluffypotato.com/assets/pg_tutorial (02_images_iput_collisions)

import os

import pygame

BASE_IMG_PATH = 'sprites/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + img_name))
    return images