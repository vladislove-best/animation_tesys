import pygame
class Sheep(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.walk_back_animation = False
        self.walk_front_animation = False
        self.walk_right_animation = False
        self.walk_left_animation = False
        self.x_speed = 0
        self.y_speed = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 3 
        self.walk_back_sprites ,walk_front_sprites = [], []
        self.walk_right_animation, walk_left_animation = [], []
        for i in range(4):
            self.walk_back_sprites.append(pygame.image.load('sheep/sheep_walk'+str(i+1)+'.png'))
            self.walk_front_sprites.append(pygame.image.load('sheep/sheep_walk_front'+str(i+1)+'.png'))
            self.walk_right_sprites.append(pygame.image.load('sheep/sheep_walk_right'+str(i+1)+'.png'))
            self.walk_left_sprites.append(pygame.image.load('sheep/sheep_walk_left'+str(i+1)+'.png'))
        self.current_sprite = 0
        self.image = self.walk_front_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
    def walk_back(self):
        self.walk_back_animation = True
        self.y_speed = -self.speed
    def walk_front(self):
        self.walk_front_animation = True
        self.y_speed = self.speed
    def walk_right(self):
        self.walk_right_animation = True
        self.x_speed = self.speed
    def walk_left(self):
        self.walk_left_animation = True
        self.x_speed = -self.speed
    def stop(self):
        self.walk_back_animation = False
        self.walk_front_animation = False
        self.walk_left_animation = False
        self.walk_right_animation = False
        self.y_speed = 0
        self.x_speed = 0