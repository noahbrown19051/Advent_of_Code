
def intcode(codein):
    code = codein
    for i in range(0,len(code)):# Converting strings to ints
        code[i] = int(code[i])
    
    for i in range(0, len(code) + 1,4):
        
        
        if code[i] == 1:     # if the indexed element is 1, at the index = 3rd value
           # put the sum of the value at the first and value at the second
          
           code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
        elif code[i] == 2:
            code[code[i+3]] = code[code[i + 1]] * code[code[i + 2]]
            
        elif int(code[i]) == 99:
            break
       
    print(code)

        
    
def main():
    opcode_file = open('day2data.txt', 'r')
    data_edited = open('day2edit.txt', 'w')
    opcode = opcode_file.read()
    opcode_list = opcode.split(',')
    
    opcode_list[1] = 12
    opcode_list[2] = 2
    #opcode_list = [1,1,1,4,99,5,6,0,99]
    intcode(opcode_list)
    
    opcode_file.close()
    data_edited.close()
    
main()
