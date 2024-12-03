import pygame
from PIL import Image, ImageFilter
import io

class ScrollingBackground:
    def __init__(self, image_path, screen_width, screen_height, scroll_speed, blur_radius=5):
        self.image = self.load_and_blur_image(image_path, screen_width, screen_height, blur_radius)
        self.image2 = pygame.transform.flip(self.image, True, False)  # 水平鏡像翻轉
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.scroll_speed = scroll_speed

        self.x1 = 0
        self.x2 = screen_width

    def load_and_blur_image(self, image_path, width, height, blur_radius):
        img = Image.open(image_path).convert("RGB")
        img = img.resize((width, height))
        
        blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))
        
        img_bytes = io.BytesIO()
        blurred_img.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        return pygame.image.load(img_bytes)

    def update(self):
        self.x1 -= self.scroll_speed
        self.x2 -= self.scroll_speed

        if self.x1 + self.screen_width <= 0:
            self.x1 = self.x2 + self.screen_width

        if self.x2 + self.screen_width <= 0:
            self.x2 = self.x1 + self.screen_width

    def draw(self, screen):
        screen.blit(self.image, (self.x1, 0))
        screen.blit(self.image2, (self.x2, 0))
