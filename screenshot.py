#!/usr/bin/env python3
from pynput import keyboard
from pynput.mouse import Button, Controller
import pyscreenshot as ImageGrab
import sys
import datetime


class Caster:
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    def __init__(self, action_no, *keys):
        self.combination = {*keys}
        self.currently_pressed = set()
        self.is_pressed = False
        self.action_no = action_no

        listener = keyboard.Listener(on_press=self._on_press, on_release=self._on_release)
        listener.start()

    def _on_press(self, key):
        if key in self.combination:
            self.currently_pressed.add(key)

        if self.currently_pressed == self.combination:
            self.is_pressed = True
            self._action_()
            #print('pressed!')

    def _on_release(self, key):
        try:
            self.currently_pressed.remove(key)

            if self.is_pressed and len(self.currently_pressed) == 0:
                self.is_pressed = False
                #print('released!')

        except KeyError:
            pass

    def _action_(self):
        if(self.action_no == 1):
            self._screen_shot()
        elif(self.action_no == 2):
            self._exit_()
        elif(self.action_no == 3):
            self._setP1_()
        elif(self.action_no == 4):
            self._setP2_()


    def _screen_shot(self):
        if(Caster.x1 == Caster.x2 or Caster.y1 == Caster.y2): #case of fullscreen
            im = ImageGrab.grab()  # X1,Y1,X2,Y2
            print(' --- Full shot! ', end='')
        else:
            im = ImageGrab.grab(bbox=(Caster.x1, Caster.y1, Caster.x2, Caster.y2))  # X1,Y1,X2,Y2
            print(' --- Box shot! ', end='')

        name = str(datetime.datetime.now().strftime("%y_%m_%d_%H-%M-%S"))
        name += '.png'
        print(name, end='')
        print(' ---')
        im.save(name)
        #im.show()

    def _exit_(self):
        sys.exit()

    def _setP1_(self):
        mouse = Controller()
        (x, y) = mouse.position
        Caster.x1 = x
        Caster.y1 = y
        print(' --- P1 set ---')

    def _setP2_(self):
        mouse = Controller()
        (x, y) = mouse.position
        Caster.x2 = x
        Caster.y2 = y
        print(' --- P2 set ---')


if __name__ == '__main__':
    #comb = Caster(1, keyboard.Key.alt, keyboard.Key.ctrl)
    comb1 = Caster(1, keyboard.KeyCode.from_char('c'), keyboard.KeyCode.from_char('s'))
    comb2 = Caster(2, keyboard.KeyCode.from_char('c'), keyboard.KeyCode.from_char('x'))
    comb3 = Caster(3, keyboard.KeyCode.from_char('c'), keyboard.KeyCode.from_char('1'))
    comb4 = Caster(4, keyboard.KeyCode.from_char('c'), keyboard.KeyCode.from_char('2'))
    input()

#https://pl.imgbb.com
