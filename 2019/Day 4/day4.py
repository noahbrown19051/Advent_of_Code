import itertools
import numpy as np
def check(combo):
    dub = False
    order = True
    double = False
    for i in range(0,(5)):
        if combo[i] == combo[i+1]:
            dub = True
        if combo[i] > combo[i+1]:
            order = False
  
    groups = [combo.count(ch) for ch in set(combo)]

    indeces = np.zeros(10)
    for num in combo:
        indeces[int(num)] += 1
    if 2 in indeces:
        double = True
    
    
    
        
    if dub and order and double:
        return True
    else:
        return False
   

    

def main():
    puz = [2,7,1,9,7,3,7,8,5,9,6,1]
    count = 0
    both = ['271973','785961']
    go_from, go_to = map(int, both)
    for pass_num in range(go_from, go_to + 1):
        
    
        right = check(str(pass_num))
        
        if right:
           
            count += 1
    print(count)       
        
    
    print(check(puz))

main()  
