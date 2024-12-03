import pygame_gui
import pygame

class Dropdown:
    def __init__(self, name, options, starting_option, position, size, manager):
        self.name = name
        self.dropdown = pygame_gui.elements.UIDropDownMenu(
            options_list=options,
            starting_option=starting_option,
            relative_rect=pygame.Rect(position, size),
            manager=manager
        )
        self.selected_option = starting_option

    def handle_event(self, event):
        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == self.dropdown:
                self.selected_option = event.text
                # print(f"{self.name} selected: {event.text}")

    def get_selected_option(self):
        return self.selected_option

    def hide(self):
        self.dropdown.hide()

    def show(self):
        self.dropdown.show()