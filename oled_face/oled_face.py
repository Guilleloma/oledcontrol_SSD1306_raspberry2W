import os
import time
import random
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image

class OledFaceController:
    def __init__(self, rst=None, i2c_address=0x3C, images_path='oled_face/images'):
        self.rst = rst
        self.i2c_address = i2c_address
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=self.rst)
        self.disp.begin()
        self.disp.clear()
        self.disp.display()
        
        # Ruta de la carpeta de imágenes
        self.images_path = images_path

        # Cargar las imágenes
        self.images = {
            'open': self.load_image('face_open.bmp'),
            'half_closed': self.load_image('face_half_closed.bmp'),
            'closed': self.load_image('face_closed.bmp'),
            'half_open': self.load_image('face_half_open.bmp')
        }

    def load_image(self, filename):
        """Carga una imagen desde el directorio de imágenes."""
        path = os.path.join(self.images_path, filename)
        return Image.open(path).convert('1').resize((128, 64))

    def display_image(self, image_name):
        if image_name in self.images:
            self.disp.image(self.images[image_name])
            self.disp.display()
        else:
            print(f"Image '{image_name}' not found.")

    def clear_display(self):
        self.disp.clear()
        self.disp.display()

    def blink_eyes(self, interval_open=2, interval_blink=0.1):
        while True:
            self.display_image('open')
            time.sleep(random.uniform(interval_open - 1, interval_open + 1))
            self.display_image('half_closed')
            time.sleep(interval_blink)
            self.display_image('closed')
            time.sleep(interval_blink)
            self.display_image('half_open')
            time.sleep(interval_blink)
            self.display_image('open')
            time.sleep(interval_blink)

    def cleanup(self):
        self.clear_display()