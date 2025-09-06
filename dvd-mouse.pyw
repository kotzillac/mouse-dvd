import time
import random
import math
from pynput.mouse import Controller
from pynput.keyboard import Key, Listener

class DvDClass:
    def __init__(self):
        self.mouse = Controller()
        self.x, self.y = self.mouse.position
        self.speed = 1000
        self.angle = random.uniform(0, 2 * math.pi)
        self.last_time = time.time()
        self.icon_size = 100
        self.screen_width = 1920
        self.screen_height = 1080
        self.running = True
        self.key_listener = Listener(on_press=self.on_key_press)
        self.key_listener.start()
    
    def on_key_press(self, key):
        try:
            if key == Key.esc:
                print("Нажата клавиша Esc - остановка программы")
                self.running = False
                return False
        except AttributeError:
            pass
    
    def update_position(self):
        current_time = time.time()
        delta_time = current_time - self.last_time
        self.last_time = current_time
        
        dx = math.cos(self.angle) * self.speed * delta_time
        dy = math.sin(self.angle) * self.speed * delta_time
        
        new_x = self.x + dx
        new_y = self.y + dy
        
        bounced = False
        
        if new_x > self.screen_width - self.icon_size/2:
            self.angle = math.pi - self.angle
            new_x = self.screen_width - self.icon_size/2
            bounced = True
        elif new_x < self.icon_size/2:
            self.angle = math.pi - self.angle
            new_x = self.icon_size/2
            bounced = True
        
        if new_y > self.screen_height - self.icon_size/2:
            self.angle = -self.angle
            new_y = self.screen_height - self.icon_size/2
            bounced = True
        elif new_y < self.icon_size/2:
            self.angle = -self.angle
            new_y = self.icon_size/2
            bounced = True
        
        self.x, self.y = new_x, new_y
        return bounced
    
    def run(self):
        print("DVD Mouse Simulator запущен!")
        print("Нажмите ESC для остановки")
        print(f"Размер экрана: {self.screen_width}x{self.screen_height}")
        
        try:
            while self.running:
                self.update_position()
                self.mouse.position = (self.x, self.y)
                time.sleep(0.01)
                
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        finally:
            self.key_listener.stop()
            print("Программа остановлена")

def main():
    try:
        from pynput.mouse import Controller
        from pynput.keyboard import Key, Listener
    except ImportError:
        print("Установите pynput: pip install pynput")
        return
    
    programm = DvDClass()
    programm.run()

if __name__ == "__main__":
    main()