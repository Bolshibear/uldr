import sys as Sys
import os
import time

class Menu():
    
    def __init__(self):
        self.clear()
        
        self._menu = ['[ Play ]', 'Options', 'Exit']
        
        play = False
        self.current = 0
        
        while play == False:
            self.print_line()
            
            prompt = input('> ').lower()
            
            if str(prompt) == 'd': self.move('for')
            elif str(prompt) == 'a': self.move('back')
            
            
    def clear(self):
        if Sys.stdin.isatty():
            os.system('clear') 
        
        
    def print_line(self):
        self.clear()
        _menu = self._menu
        print('\n' * 5)
        line = '{0}{1:6^}     {2:9^}     {3:6^}'.format(' ' * 20,_menu[0],_menu[1],_menu[2])
        print(line)
        print('\n' * 5)
        
    
    def move(self, direc):
        self._menu[self.current] = self._menu[self.current][2:-2]
        if direc == 'for':
            if self.current == 2: self.current = 0
            else: self.current += 1
        if direc == 'back':
            if self.current == 0: self.current = 2
            else: self.current -= 1
        self._menu[self.current] = '[ ' + self._menu[self.current] + ' ]'
        
                                   
        
        
#menu = Menu()

prompt = input()
print(prompt)
print()
prompt = input()
print(prompt)
print()
prompt = input()
print(prompt)