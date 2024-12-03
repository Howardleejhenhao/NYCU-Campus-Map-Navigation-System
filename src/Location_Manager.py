import pygame
from Location import Location
from replace_num_to_Location import node_index_to_building_code

class LocationManager:
    def __init__(self, offset_x = 0, offset_y = 0):
        self.locations = []  # 儲存所有的 Location 物件
        self.offset = (offset_x, offset_y)
        self.offset_x = offset_x
        self.offset_y = offset_y

    def add_location(self, building_code, x, y, is_show=True):
        location = Location(building_code, x, y, is_show, offset_x = self.offset_x, offset_y = self.offset_y)
        self.locations.append(location)

    def draw_locations(self, screen):
        for location in self.locations:
            location.draw(screen)

    def toggle_location_visibility(self, building_code):
        for location in self.locations:
            if location.building_code == building_code:
                location.is_show = not location.is_show

    def set_invisible_allpoint(self):
        for location in self.locations:
            location.is_show = 0
    
    def set_single_point_visible(self, building_code):
        for location in self.locations:
            if location.building_code == building_code:
                location.is_show = 1

    def set_group_visible(self, locations):
        self.set_invisible_allpoint()
        for i in locations:
            self.set_single_point_visible(node_index_to_building_code[i])