import math
##class Fuel:
##    def __init__(self, weight):
##        self.weight = weight
##        
##    def calculate_fuel_mod(self):
##        
##        return self.calculate(self.weight) + 
##
##    def calculate(self, fuel)
##        b4round = int(fuel) / 3
##        rounded = math.floor(b4round)
##        fuel_weight = rounded - 2
##        return fuel_weight
##        
####        fuel_mod = 0
####        fuel = 1
####        while fuel != 0:
##            b4round = int(self.weight) / 3
##            rounded = math.floor(b4round)
##            fuel = rounded - 2
##            fuel_mod += fuel
##        print(fuel)
##        print(fuel_mod)
##        

def calculate_fuel(weights):
    fuel_mod = 0
    for weight in weights:
        weight = str(weight)
        while weight != 0:
            b4round = int(weight) / 3
            rounded = math.floor(b4round)
            weight = rounded - 2
            if weight < 0:
                weight = 0
            fuel_mod += weight
    print(fuel_mod)
            
           
    return fuel_mod
        
def main():
    filename = 'advent1.txt'
    weights = open(filename, 'r')
    
    print(calculate_fuel( weights))

        

    weights.close()


main()
