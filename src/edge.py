import pygame
import math

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

            angle = math.atan2(
                end_pos_with_offset[1] - start_pos_with_offset[1],
                end_pos_with_offset[0] - start_pos_with_offset[0]
            )
            
            
            head_length = 15
            head_width = 10
            arrow_head = [
                (
                    end_pos_with_offset[0] - head_length * math.cos(angle) + head_width * math.sin(angle),
                    end_pos_with_offset[1] - head_length * math.sin(angle) - head_width * math.cos(angle)
                ),
                end_pos_with_offset,
                (
                    end_pos_with_offset[0] - head_length * math.cos(angle) - head_width * math.sin(angle),
                    end_pos_with_offset[1] - head_length * math.sin(angle) + head_width * math.cos(angle)
                )
            ]

            pygame.draw.polygon(screen, self.color, arrow_head)
