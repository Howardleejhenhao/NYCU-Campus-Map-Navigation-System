import pygame
import pygame_gui

class DropdownManager:
    def __init__(self):
        self.dropdowns = []

    def add_dropdown(self, dropdown):
        self.dropdowns.append(dropdown)

    def handle_event(self, event):
        for dropdown in self.dropdowns:
            dropdown.handle_event(event)

    def get_selected_option(self, name):
        for dropdown in self.dropdowns:
            if dropdown.name == name:
                return dropdown.get_selected_option()
        return None

    def hide_all(self):
        for dropdown in self.dropdowns:
            dropdown.hide()

    def show_all(self):
        for dropdown in self.dropdowns:
            dropdown.show()