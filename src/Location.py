import pygame
from replace_num_to_Location import building_code_to_node_index, node_index_to_building_code
class Location:
    def __init__(self, building_code, x, y, is_show, offset_x = 0, offset_y = 0):
        self.building_code = building_code
        self.x = x
        self.y = y
        # self.font = pygame.font.Font("font/Roboto/Roboto-Regular.ttf", 30)
        self.is_show = is_show
        self.offset = (offset_x, offset_y)
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.node_index = building_code_to_node_index[building_code]

    def draw(self, screen):
        if self.is_show:
            adjusted_x = self.x + self.offset_x
            adjusted_y = self.y + self.offset_y

            pygame.draw.circle(screen, (255, 0, 0), (adjusted_x, adjusted_y), 5)
            # text = self.font.render(self.building_code, True, (0, 0, 0))
            # screen.blit(text, (adjusted_x + 10, adjusted_y))

    def is_clicked(self, mouse_pos):
        return (self.x - mouse_pos[0]) ** 2 + (self.y - mouse_pos[1]) ** 2 < 25
