class Grid():
    
    def __init__(self, size, start, end, specials):
        '''
        Implements starting variables and makes them accessable from the class.
        It builds teles, comps anf fails from fins_spcials()'''
        
        self.x = size[0]
        self.y = size[1]
        self.layout = [[' '] * self.x] * self.y
        self.specials = specials
        
        self.current = start
        self.start = start
        self.end = end
        
        self.teles = [] # vertices that will teleport you (vertex, dest_state)
        self.fails = [] # vertices that will cause you to fail outright
        self.comps = [] # vertices that are compulsary to include
        
        self.find_specials()
        
        self.passed = True
        
    
    def reset(self):
        '''
        Resets current vertex to start and the passed bool to True'''
        
        self.current = self.start
        self.passed = True
        
        
    def find_specials(self):
        '''
        Checks specials in self.specials and splits them into 'fail', 'tele'
        and 'comp' and appends them to self.fails, self.teles and self.comps.'''
        
        for vertex, attributes, dest in self.specials:
            if 'fail' in attributes:
                self.fails.append(vertex)
                
            if 'tele' in attributes:
                self.teles.append((vertex, dest)) 
                
            if 'comp' in attributes:
                self.comps.append(vertex)      
        
        
    def __str__(self):
        '''
        Returns a graphical representation of the grid, albeit without special
        vertices'''
        
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
        '''
        Returns the introduction, letting the player know which vertices they
        can't pass through, they must pass through and which ones will teleport
        them to another vertex'''
        
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
        '''Moves self.current up a row'''
        return (self.current[0] - 1, self.current[1])
        
        
    def left(self):
        '''Moves self.current left'''
        return (self.current[0], self.current[1] - 1)
        
        
    def down(self):
        '''Moves self.current down a row'''
        return (self.current[0] + 1, self.current[1])
            
            
    def right(self):
        '''Moves self.current right'''
        return (self.current[0], self.current[1] + 1)
    

    def is_valid(self, next_vertex):
        '''Checks if a move to next_vertex is possible on the grid.'''
        
        pos = next_vertex
        
        if pos[0] >= self.y or pos[0] < 0:
            return False
        
        elif pos[1] >= self.x or pos[1] < 0:
            return False
        
        else:
            return True
            
        
    def run(self, inpt):
        '''
        Runs the user input across the grid and returns if it passed the level
        or not. It checks: a) The input lands on the end vertex
                           b) The input doesn't pass through blocked vertices
                           c) The input passes through the compulsary vertices.
        '''
        
        visited = [self.current]
        
        commands = {'u': self.up,
                    'l': self.left,
                    'd': self.down,
                    'r': self.right,
                    }
        
        for char in inpt:
            
            for i in self.teles:
                if i[0] == self.current:
                    self.current = i[1]  
                    
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