def check_sums(orbits):
    
    

   # for planet in planets:
    
    tot_sum = 0
    
    for orbit in orbits:    # for each orbit in the list orbits
        inner = orbit[0]    # inner is the planet being orbited
   #     print(orbit)
        outer = orbit[1]    # outer is the planet orbitting
        count = 0
   #     print('here')
        count += 1
        while inner != 'COM':   # going through until making it to the Center of Mass
            
            for orbit in orbits:
                
                if orbit[1] == inner:
                    inner = orbit[0]
                    count +=1
        
        tot_sum += count
    
    
    return tot_sum
def find_path(orbits,inner):
    # finds list of planets to COM
    path = []
    while inner != "COM":
        for orbit in orbits:
            if orbit[1] == inner:
               
                inner = orbit[0]
                path.append(inner)
    return path

def find_san(orbits):
    for orbit in orbits:    # for each orbit in the list orbits
        inner = orbit[0]    # inner is the planet being orbited
        outer = orbit[1]    # outer is the planet orbitting
        if outer =='YOU':
            you2com = find_path(orbits, 'YOU')
            print(you2com)
    
        elif outer == 'SAN':
            san2com = find_path(orbits, 'SAN')
            print(san2com)
    for toSan in you2com:   # finding first common planet in the paths to the center of mass
        for toYou in san2com:
            if toSan == toYou:
                youToCommon = you2com.index(toSan)
                sanToCommon = san2com.index(toYou)
                print(youToCommon, sanToCommon)
                return youToCommon + sanToCommon
           
        
        
    


def main():
    with open('input6.txt', 'r') as file:
        orbitsf = file.read().split('\n')
    orbits = []
    for orbit in orbitsf:
        orbits.append(orbit.split(')'))
    orbits.pop()
    orbitsb = 'COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L,K)YOU,I)SAN'
    orbitsf = orbitsb.split(',')
   # print(orbitsf)
   # print(orbits)
   # total = check_sums(orbits)
##    orbits = []
##    for orbit in orbitsf:
##        orbits.append(orbit.split(')'))
##    print(orbits)
    youToSan = find_san(orbits)
    print(youToSan)

   
main()
