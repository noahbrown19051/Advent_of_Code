import numpy as np

def intcode(codein):
    code = []
    for value in codein:# Converting strings to ints and creating new list
        code.append(int(value))
    
    for i in range(0, len(code) + 1,4):
        
       # print(code[code[i + 3]])
        if code[i] == 1:     # if the indexed element is 1, at the index = 3rd value
           # put the sum of the value at the first and value at the second
          
           code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
        elif code[i] == 2:
            # puts the product of the value at index in the second position
            #and value at index of third position
            code[code[i+3]] = code[code[i + 1]] * code[code[i + 2]]
            
        elif int(code[i]) == 99:
            break
       
    return code

        
    
def main():
    opcode_file = open('day2data.txt', 'r')
    data_edited = open('day2edit.txt', 'w')
    opcode = opcode_file.read()
    opcode_list = opcode.split(',')
  

    
    for noun in range(0,100): # try noun with value 1-99
        opcode_list[1] = noun
        if noun % 10 == 0:
            print(noun)
        for verb in range(0,100): # try verb with value 1-99
            opcode_list[2] = verb
            
                
         
            changed_code = intcode(opcode_list)
        
            if changed_code[0] == 19690720: # if verb is correct value print the answer
                print('verb: ' + str(verb) + 'noun' + str(noun))
                print(100 * noun + verb)
    
    
    opcode_file.close()
    data_edited.close()
    
main()
