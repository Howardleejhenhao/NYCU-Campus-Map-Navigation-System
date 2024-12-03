import pygame

class Edge:
    def __init__(self, locations_managers, start_node, end_node, weight = 1, offset_x = 0, offset_y = 0, is_show = 1):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight
        self.color = (255, 0, 0)
        self.thickness = 2
        self.offset = (offset_x, offset_y)
        self.is_show = is_show        
        self.start_node_pos = (0, 0)
        # print(locations_managers)
        for location in locations_managers.locations:
            # print(type(location))
            if location.node_index == start_node:
                self.start_node_pos = (location.x, location.y)
                break
        self.end_node_pos = (0, 0)
        for location in locations_managers.locations:
            if location.node_index == end_node:
                self.end_node_pos = (location.x, location.y)
                break


    def draw(self, screen):
        # print(self.start_node_pos, self.offset)
        if self.is_show:
            start_pos_with_offset = (self.start_node_pos[0] + self.offset[0], self.start_node_pos[1] + self.offset[1])
            end_pos_with_offset = (self.end_node_pos[0] + self.offset[0], self.end_node_pos[1] + self.offset[1])
            pygame.draw.line(screen, self.color, start_pos_with_offset, end_pos_with_offset, self.thickness)
