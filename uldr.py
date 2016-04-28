from grid import *
import time
import os
import sys


def problem(size, start, end, specials):
    
    grid = Grid(size, start, end, specials)
    print(grid.intro())
    print(grid)
    
    prompt = str(input('\n> '))
    
    if prompt[0:4] == 'quit' or prompt[0:5] == 'close':
        return 'quit'
    
    answer = grid.run(prompt)
    grid.reset()
    
    while answer[0] == False:
        print('\nBad luck. Try again')
        prompt = input('\n> ')
        
        if prompt[0:4] == 'quit' or prompt[0:5] == 'close':
                return 'quit'
            
        answer = grid.run(prompt)  
        grid.reset()
        
    print('\nCongratulations, you made it!\n')
        
    
def level_generator():
    size = (4,3)
    start = (0,0)
    end = (2,3)
    
    specials = [((0,1), ['fail'],()), 
                ((2,1), ['comp'],()),
                ((2,0), ['fail'],()),
                ((1,2), ['tele'],(0,2))
                ]    
    
    return [size, start, end, specials]

def clear_page():
    if sys.stdin.isatty():
        os.system("clear")

    
    
def uldr():
    clear_page()
    
    for i in range(1, 11):
        print('\n---------------- Level {} ----------------\n'.format(i))
        level = level_generator()
        
        frage = problem(level[0], level[1], level[2], level[3])
        
        if frage == 'quit':
            clear_page()
            break
        
        time.sleep(0.7)
        clear_page()
    

        

uldr()