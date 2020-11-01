
parameter_counts = {1 :3, 2 :3, 3 :1, 4 :1 ,}


def read_opcode(opcode):
    opcode = str(opcode)
    if len(opcode) > 2:
        op = int(opcode[-2:])
        print(op)
        if op == 3:
            return (None, 3)
        elif op == 4:
            return (int(opcode[0]), 4)
        elif op == 2 or op ==1:
            modes = [int(mode) for mode in opcode[-3::-1]]
            while len(modes) < 2:
                modes.append(0)
            return (modes,op)

    return (None, int(opcode))

def do_op(instructions, opcode, parameter_modes, opcode_idx):

    def get_store_at():
        return instructions[opcode_idx + parameter_counts[opcode]]

    def get_parameter(param_number = 1):
        return instructions[opcode_idx + param_number]

    if opcode == 3:

        instructions[get_store_at()] = int(input('Input: '))

    elif opcode == 4:
        if not parameter_modes:
            print(instructions[get_parameter()])
        else:
            if parameter_modes == 1:
                print(get_parameter())
            else:
                print(instructions[get_parameter()])

    elif opcode == 2:
        prod = 1
        if not parameter_modes:
            for i in range(1,parameter_counts[opcode]):
                prod *= get_parameter(i+1)
        else:
            for i in range(0, len(parameter_modes)):
                if parameter_modes[i] == 1:
                    prod *= get_parameter(i+1)
                else:
                    prod *= instructions[get_parameter(i+1)]
        instructions[get_store_at()] = prod

    elif opcode == 1:
        op_sum = 0
        if not parameter_modes:
            for i in range(1, parameter_counts[opcode]):
                op_sum += instructions[get_parameter(i)]
        else:
            for i in range(0,len(parameter_modes)):
                if parameter_modes[i] == 1:
                    op_sum += get_parameter(i+1)
                else:
                    op_sum += instructions[get_parameter(i+1)]
        instructions[get_store_at()] = op_sum


def main():
    with open('input5.txt', 'r') as fInput:
        instructions = [ int(value) for value in fInput.read().strip().split(',')]

    opcode_idx = 0
    go = True

    while go:
        opcode = instructions[opcode_idx]

        if opcode == 99:
            go = False
        parameter_modes, opcode = read_opcode(opcode)

        do_op(instructions, opcode, parameter_modes, opcode_idx)

        opcode_idx += parameter_counts[opcode] + 1

if __name__ == '__main__':
    main()
