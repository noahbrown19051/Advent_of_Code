a,b,_ = open('day3input.txt', 'r').read().split('\n')
a,b = [x.split(',') for x in [a,b]]

dx = {'L':-1, 'R': 1, 'U': 0, 'D':0}
dy = {'L':0, 'R':0, 'U': 1, 'D':-1}

def get_points(A):
    x = 0
    y = 0
    length = 0
    ans = {}
    for cmd in A:
        d = cmd[0]
        n = int(cmd[1:])
     #   assert d in ['L', 'R', 'U', 'D']
        for _ in range(n):
            x += dx[d]
            y += dy[d]
            length += 1
            if (x,y) not in ans:
                ans[(x,y)] = length
   
    return ans

pa = get_points(a)

pb = get_points(b)
both = set(pa.keys()) & set(pb.keys())
part1 = min([abs(x)+abs(y) for (x,y) in both])
part2 = min([pa[p] + pb[p] for p in both])

print(part1, part2)
        





##import turtle
##firstpath = turtle.Turtle()
##secondpath = turtle.Turtle()
##class Director:
##    def __init__(self, directions):
##        self.directions = directions
##
##    def draw_first(self):
##        ''' Method that draws first path'''
##        for value in self.directions:
##            distance = value[1:]
##                
##            if value == 'stop':
##                break
##            elif value[0] == 'L':
##                firstpath.setheading(180)
##                firstpath.forward(distance)
##            elif value[0] == 'R':
##                firstpath.setheading(0)
##                firstpath.forward(distance)
##            elif value[0] == 'U':
##                firstpath.setheading(90)
##                firstpath.forward(distance)
##            elif value[0] == 'D':
##                firstpath.setheading(270)
##                firstpath.forward(distance)
##                
##    def draw_second(self):
##        ''' Method that draws second path'''
##        for value in self.directions:
##            if value == 'stop':
##                flag = 'start'
##
##            while flag == 'start':
##                distance = value[1:]
##                if value == 'stop':
##                    break
##                elif value[0] == 'L':
##                    firstpath.setheading(180)
##                    firstpath.forward(distance)
##                elif value[0] == 'R':
##                    firstpath.setheading(0)
##                    firstpath.forward(distance)
##                elif value[0] == 'U':
##                    firstpath.setheading(90)
##                    firstpath.forward(distance)
##                elif value[0] == 'D':
##                    firstpath.setheading(270)
##                    firstpath.forward(distance)
##                
##            
##            
##        print(self.directions)
##        #for value in self.
##       # while '\n' not in 
##    
##def main():
##    
##    directions_file = open('day3input.txt','r')
##    directions = directions_file.read()
##    directions_list = directions.split(',')
##    path = Director(directions_list) # construting Director
##
##    path.draw_first()
##    path.draw_second()
##    directions_file.close()
##
##
##main()
