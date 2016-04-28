class Grid():
    
    def __init__(self, size, start, end, specials):
        self.x = size[0]
        self.y = size[1]
        self.layout = [[' '] * self.x] * self.y
        
        self.current = start
        self.start = start
        self.end = end
        
        self.teles = [] # vertices that will teleport you (vertex, dest_state)
        self.fails = [] # vertices that will cause you to fail outright
        self.comps = [] # vertices that are compulsary to include
        
        self.find_specials(specials)
        
        self.passed = True
        
    
    def reset(self):
        self.current = self.start
        self.passed = True
        
        
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
        x_row = range(0, self.x)
        y_row = range(0, len(self.layout))
        
        for item in x_row:
            row += ' ' + str(item) + ' |'
            
        grid += row + '\n'        

        for lis in y_row:
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
            briefing += 'Going through ' + str(vertex) + ' will teleport \
you to '\
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
        
        if pos[0] >= self.y or pos[0] < 0:
            return False
        
        elif pos[1] >= self.x or pos[1] < 0:
            return False
        
        else:
            return True
            
        
    def run(self, inpt):
        visited = [self.current]
        
        commands = {'u': self.up,
                    'l': self.left,
                    'd': self.down,
                    'r': self.right,
                    }
        
        for char in inpt:
            options = ['u','l','d','r']
            if char not in options:
                print('\nerror in input u = up, l = left, d = down, r = right')
                self.passed = False
                break
            
            if self.passed == True:
                    
                next_vertex = commands[char]()
                                
                if self.is_valid(next_vertex):
                    self.current = next_vertex
                    visited.append(self.current)
                    
                else:
                    self.passed = False
                    
            else:
                break
            
        if self.current != self.end and self.passed == True:
            print('\nYou did not finish on the required end vertex.')
            self.passed = False        
            
        for i in self.comps:
            if i  not in visited and self.passed == True:
                print('\nNot all the compulsary vertices were visited.')
                self.passed = False
                
        for i in self.fails:
            if i in visited and self.passed == True:
                print('\nYou passed through a blocked vertex.')
                self.passed = False
            
        return (self.passed, self.current)