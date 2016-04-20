
class Grid():
    
    def __init__(self,x,y, start):
        self.x = x
        self.y = y
        self.layout = [[' '] * x] * y
        
        self.current = start
        
        
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
    
    
    def up(self):
        self.current = (self.current[0], self.current[1] - 1)
        
        
    def left(self):
        self.current = (self.current[0] - 1, self.current[1])
        
        
    def down(self):
        self.current = (self.current[0], self.current[1] + 1)
            
            
    def right(self): 
        self.current = (self.current[0] + 1, self.current[1])

    def is_valid(self):
        valid = True
        pos = self.current
        
        if pos[0] >= self.x or pos[0] < 0:
            print('failes')
            valid = False
        
        if pos[1] >= self.y or pos[1] < 0:
            print('failes')
            valid = False
        
        return valid
            
        
        
    def run(self, inpt):
        error = False
        counter = 0
        
        commands = {'u': self.up,
                    'l': self.left,
                    'd': self.down,
                    'r': self.right,
                    'grid': self.__str__,
                    }
        
        for char in inpt:
            if error == False:
                    
                commands[char]()
                                
                if not self.is_valid():
                    error = True
                    
            else:
                break
            
            
        if error == False:
            return (True, self.current)
        else:
            return (False, self.current)
        

def problem(start, end):
    
    print('\nYou start at ' + str(start) + ' and you must reach ' + str(end) + '.\n')
    grid = Grid(3, 3, start)
    print(grid)
    
    prompt = input('> ')
    
    error = False
    if prompt == 'grid':
        print(grid)
        
    else:
        
        options = ['u','l','d','r','grid']
        
        for i in prompt:
            if i not in options:
                error = True
        
        if error == False:
            finish = grid.run(prompt)[1]
            
            grid.current = start
            
        else:
            print('error in input u = up, l = left, d = down, r = right')
    
    if error == False and finish == end:
        return True
        
    else:
        return False
        
    
def uldr():
    
    frage = problem((0,0),(2,2))
    
    while frage == False:
        print('\nBad luck. Try again')
        frage = problem((0,0),(2,2))
        
    print('congrats')
    
    
uldr()