
class Grid():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.layout = [[' '] * x] * y
        
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
        
        
        
uldr = Grid(3, 1)
print(uldr)