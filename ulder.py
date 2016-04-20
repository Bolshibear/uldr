
class Grid():
    
    def __init__(self,x,y, start):
        self.x = x
        self.y = y
        self.layout = [[' '] * x] * y
        
        current_pos = start
        
        
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
    
    
    def run(self, inpt):
        print('running')
        
    
def control(grid, inpt):
    
    error = False
    
    options = ['u','l','d','r']
    
    for i in inpt:
        if i not in options:
            error = True
    
    if error == False:
        return grid.run(inpt)
        
    else:
        print('error in input u = up, l = left, d = down, r = right')
    
    
        
            
def uldr():
    
    quit = False
    
    print()
    grid = Grid(3,1,(0,0))
    print(grid)
    
    while quit == False:
        prompt = input('> ')
        
        control(grid, prompt)


uldr()
        