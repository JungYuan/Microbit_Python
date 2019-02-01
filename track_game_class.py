import microbit as mBit
from random import randint
import music

class pointers():
    px = 2
    py = 4
    bright = 9
    __agx = 0
    __agy = 0
    def set_on(self, x, y):
        self.px = x
        self.py = y
        mBit.display.set_pixel(self.px, self.py, self.bright)
    def set_off(self, x, y):
        self.px = x
        self.py = y
        mBit.display.set_pixel(self.px, self.py, 0)
    def move(self, mx, my, cyc):
        self.set_off(self.px, self.py)
        self.px += mx
        self.py += my
        if cyc == 1:
            nl = 4
            pl = 0
        else:
            nl = 0
            pl = 4
        if self.px < 0 :
            self.px = nl
        elif self.px > 4:
            self.px = pl
        if self.py < 0 :
            self.py = nl
        elif self.py > 4:
            self.py = pl
        self.set_on(self.px, self.py)
    def gesture_move(self):
        self.__agx += int(mBit.accelerometer.get_x()/200)
        self.__agy += int(mBit.accelerometer.get_y()/200)
        if self.__agx > 200:
            self.__agx = 0
            self.move(1, 0, 0)
        elif self.__agx < (-1*200):
            self.__agx = 0
            self.move(-1, 0, 0)
        if self.__agy > 200:
            self.__agy = 0
            self.move(0, 1, 0)
        elif self.__agy < (-1*200):
            self.__agy = 0
            self.move(0, -1, 0)
    def button_move(self):
        if mBit.button_a.get_presses() > 0:
            self.move(1, 0, 1)
        if mBit.button_b.get_presses() > 0:
            self.move(0, 1, 1)

def new_point(x, y):
    rept = 1
    while rept == 1:
        nx = randint(0, 4)
        ny = randint(0, 4)
        if (nx == x) and (ny == y):
            rept = 1
        else:
            rept = 0
    mBit.display.set_pixel(nx, ny, 5)
    return nx, ny

tracer = pointers()
tracer.bright = 9
target = pointers()
target.bright = 5
score = 0
game_start = 0
while (1 == 1):
    x = 2
    y = 4
    cx = 0
    cy = 0
    mBit.display.scroll(str(score), wait=False, loop=True)
    while game_start == 0:
        if mBit.accelerometer.was_gesture("shake"):
            game_start = 1
        elif mBit.button_a.is_pressed() and mBit.button_b.is_pressed():
            mBit.button_a.get_presses()
            mBit.button_b.get_presses()
            game_start = 2
    music.play(music.PYTHON, wait=False)
    mBit.display.scroll("Start")
    tracer.set_on(x, y)
    score = 0
    correct = True
    t0 = mBit.running_time()
    while (game_start != 0):
        if correct:
            correct = False
            ax, ay = new_point(x, y)
            target.set_on(ax, ay)
        if game_start == 1:
            tracer.gesture_move()
        elif game_start == 2:
            tracer.button_move()
        x = tracer.px
        y = tracer.py
        if mBit.running_time()-t0 > 30000:
            game_start = 0
        if (x == ax) and (y == ay):
            score += 1
            correct = True
            mBit.display.show(mBit.Image.HEART)
            music.play(music.BA_DING, wait=False)
            mBit.display.clear()
            tracer.set_on(x, y)
