import pygame

class Map:
    def __init__(self, image_path, offset_x = 0, offset_y = 0):
        self.image = pygame.image.load(image_path)
        self.scale = 0.21
        self.offset = (offset_x, offset_y)

    def draw(self, screen):
        scaled_image = pygame.transform.scale(self.image, (
            int(self.image.get_width() * self.scale),
            int(self.image.get_height() * self.scale)
        ))
        screen.blit(scaled_image, self.offset)

    def zoom(self, factor):
        self.scale *= factor
