
class Grid():
    
    def __init__(self,x,y, start, end, specials):
        self.x = x
        self.y = y
        self.layout = [[' '] * x] * y
        
        self.current = start
        self.start = start
        self.end = end
        
        self.teles = [] # vertices that will teleport you (vertex, dest_state)
        self.fails = [] # vertices that will cause you to fail outright
        self.comps = [] # vertices that are compulsary to include
        
        self.find_specials(specials)
        
    
    def reset(self):
        self.current = self.start
        
        
    def find_specials(self, specials):
        
        for vertex, attributes, dest in specials:
            if 'fail' in attributes:
                self.fails.append(vertex)
                
            if 'tele' in attributes:
                self.teles.append((vertex, dest)) 
                
            if 'comp' in attributes:
                self.comps.append(vertex)      
        
        
    def __str__(self):
        
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', \
                 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', \
                 'y', 'z']
        
        grid = ''
        row = 'uldr|'
        for item in range(0, self.x):
            row += ' ' + str(item) + ' |'
            
        grid += row + '\n'        

        for lis in range(0, len(self.layout)):
            grid += '----+' + ('---+' * (self.x)) + '\n'
            
            num = str(lis)
            
            grid += '{0:^4}|'.format(num) + ('   |' * self.x) + '\n'
                
            
        grid += '----+' + ('---+' * (self.x)) + '\n'
        
        return grid
    
    def intro(self):
        briefing = '\nYou start at {0} and you must reach {1}.\n'.\
            format(str(self.start), str(self.end))
        
        briefing += '\n'    
        
        for vertex  in self.comps:
            briefing += 'You must pass through ' + str(vertex) + '\n'
            
        briefing += '\n'        
        
        for vertex  in self.fails:
            briefing += str(vertex) + ' is blocked.\n'
            
        briefing += '\n'
            
        for vertex, dest in self.teles:
            briefing += 'Going through ' + str(vertex) + ' will teleport you to '\
                + str(dest) + '\n'
        
        return briefing

    
    
    def up(self):
        return (self.current[0] - 1, self.current[1])
        
        
    def left(self):
        return (self.current[0], self.current[1] - 1)
        
        
    def down(self):
        return (self.current[0] + 1, self.current[1])
            
            
    def right(self): 
        return (self.current[0], self.current[1] + 1)

    def is_valid(self, next_vertex):
        '''Checks if a move to next_vertex is available'''
        
        pos = next_vertex
        
        if pos in self.fails:
            print('Used banned vertex')
            return False
        
        elif pos[0] >= self.y or pos[0] < 0:
            return False
        
        elif pos[1] >= self.x or pos[1] < 0:
            return False
        
        else:
            return True
            
        
    def run(self, inpt):
        error = False
        
        commands = {'u': self.up,
                    'l': self.left,
                    'd': self.down,
                    'r': self.right,
                    'grid': self.__str__,
                    }
        
        for char in inpt:
            options = ['u','l','d','r']
            if char not in options:
                print('error in input u = up, l = left, d = down, r = right')
                error = True
                break
            
            if error == False:
                    
                next_vertex = commands[char]()
                                
                if self.is_valid(next_vertex):
                    self.current = next_vertex
                    
                else:
                    error = True
                    
            else:
                break
            
        if error != True:
            return (True, self.current)
        
        else:
            return (False, self.current)
        
        
def problem(start, end, specials):
    
    grid = Grid(3, 3, start, end, specials)
    print(grid.intro())
    print(grid)
    
    prompt = input('> ')
    
    finish = grid.run(prompt)[1]
    grid.reset()
    
    while finish != end:
        prompt = input('> ')
        finish = grid.run(prompt)[1]   
        grid.reset()
        
    if finish == end:
        return True
        
    else:
        return False
        
    
def uldr():
    specials = [((0,1), ['fail'],()), 
                ((1,0), ['comp'],()),
                ((2,0), ['fail'],()),
                ((1,2), ['tele'],(0,0))
                ]
    
    
    frage = problem((0,0),(2,2), specials)
    
    while frage == False:
        print('\nBad luck. Try again')
        frage = problem((0,0),(2,2), specials)
        
    print('Congratulations, you made it through the puzzle.')
    
    
uldr()