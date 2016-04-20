
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
        for lis in range(0, len(self.layout)):
            grid += '----+' + ('---+' * (self.x)) + '\n'
            
            num = str(self.y - lis)
            
            grid += '{0:^4}|'.format(num) + ('   |' * self.x) + '\n'
                
            
        grid += '----+' + ('---+' * (self.x)) + '\n'
        
        row = 'uldr|'
        
        for item in range(0, self.x):
            row += ' ' + alpha[item] + ' |'
            
        grid += row + '\n'
                    
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
                
                print(self.current)
                
                if not self.is_valid():
                    error = True
                    
            else:
                break
            
            
        if error == False:
            return 'cool'
        else:
            return 'summon satan'
        
            
def uldr():
    start = (0,0)
    quit = False
    
    print()
    grid = Grid(3, 3, start)
    print(grid)
    
    while quit == False:
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
                print(grid.run(prompt))
                grid.current = start
                
            else:
                print('error in input u = up, l = left, d = down, r = right')
        


uldr()
        