import os
from PIL import Image
import Adafruit_SSD1306
import time
import random

class OledFaceController:
    def __init__(self):
        # Directorio base donde se encuentra este archivo
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(base_dir, 'images')

        # Cargar las imágenes desde el directorio de imágenes
        self.eye_images = {
            'open': self.load_image(os.path.join(image_dir, 'face_open.bmp')),
            'half_closed': self.load_image(os.path.join(image_dir, 'face_half_closed.bmp')),
            'closed': self.load_image(os.path.join(image_dir, 'face_closed.bmp')),
            'half_open': self.load_image(os.path.join(image_dir, 'face_half_open.bmp')),
        }

        # Inicializar la pantalla OLED
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)
        self.disp.begin()
        self.disp.clear()
        self.disp.display()

    def load_image(self, path):
        return Image.open(path).convert('1').resize((128, 64))

    def blink_eyes(self, interval_open=2, interval_blink=0.05):
        while True:
            self.display_image(self.eye_images['open'])
            time.sleep(random.uniform(interval_open - 1, interval_open + 1))
            self.display_image(self.eye_images['half_closed'])
            time.sleep(interval_blink)
            self.display_image(self.eye_images['closed'])
            time.sleep(interval_blink)
            self.display_image(self.eye_images['half_open'])
            time.sleep(interval_blink)
            self.display_image(self.eye_images['open'])
            time.sleep(interval_blink)

    def display_image(self, image):
        self.disp.image(image)
        self.disp.display()

    def cleanup(self):
        self.disp.clear()
        self.disp.display()
