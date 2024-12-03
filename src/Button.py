import pygame_gui
import pygame

class Button:
    def __init__(self, text, position, size, manager):
        self.button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(position, size),
            text=text,
            manager=manager
        )

    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.button:
                # print(f"Button {self.name} clicked!")
                return True
        return False

    def show(self):
        self.button.show()

    def hide(self):
        self.button.hide()