#! /bin/python3
import argparse
import math
import time

# set up arguments for running the program
parser = argparse.ArgumentParser(description = "runOnMicroArchitecture")
parser.add_argument("filename",help = "filenameToRun")
args = parser.parse_args()

# is the line commented out
def isCommented(line):
    if line.strip()[0] == '#':
        return True
    else:
        return False
# initialize funtion
def initialize(registers):
    for reg in registers:
        registers[reg] = 0
    print(registers)

# turn binary into decimal
def binToDec(binaryStr):
    '''
    input binary wrapped in quotes
    '''
    ans = int(binaryStr, 2)
    return ans

# dictionary of instruction meanings
dict = {
    '00000001': 'initialize',
    '00000010': 'set register',
    '00000100': 'save',
    '00000101': 'multiply',
    '00000110': 'print'
        }

# # dictionary of registers
registers = {
    'reg0': 0,
    'reg1': 0,
    'reg2': 0,
    'reg3': 0
    }

# execute the code
def executeInstructions(Data):
    instructions = []
    # register = []
    #for line in Data:
    with open(args.filename, 'r') as f:
        line = f.readline()
        print(line)
        while line != "":
            # if the line is not commented out
            if isCommented(line) == True:
                line = f.readline()
            elif isCommented(line) == False:
                line = line.strip()
                temp = line.split(" ")
                # extract the 8 digits I need
                binaryStr = temp[0]
                print(binaryStr)
                # determine what that 8 digits means to me
                if len(instructions) == 0:
                    instructions.append(dict[binaryStr])
                    print(dict[binaryStr])
                    print(instructions)
                    line = f.readline()
                # if there is exactly one instruction in the list
                elif len(instructions) ==1:
                    if instructions[0] == 'initialize':
                        initialize(registers)
                        instructions.pop()
                        print('registers initialized')
                        print(instructions)
                        line = f.readline()
                    elif instructions[0] == 'set register':
                        reg = binToDec(binaryStr)
                        instructions.append(reg)
                        print(instructions)
                        line = f.readline()
                    else:
                        print('we have a problem with instruction[0]')
                        print(instructions)
                        # break
                # if there are exactly 2 instruction in list
                elif len(instructions) == 2:
                    instructions.append(dict[binaryStr])
                    print(instructions)
                    line = f.readline()
                # if there are exactly 3 instructions in list
                elif len(instructions) == 3:
                    if instruction[2] == 'save':
                        instructions.append(binToDec(binaryStr))
                        print(instructions)
                        line = f.readline()
                    elif instruction[2] == 'multiply':
                        instructions.append(binToDec(binaryStr))
                        print(instructions)
                        line = f.readline()
                    elif instruction[2] == 'print':
                        if instructions[1] == 0:
                            print(registers[reg0])
                            # break
                        elif instructions[1] == 1:
                            print(registers[reg1])
                            # break
                        elif instructions[1] == 2:
                            print(registers[reg2])
                            # break
                        elif instructions[1] == 3:
                            print(registers[reg3])
                            instructions.clear()
                            # break
                        else:
                            print('error with finding register for instructions[1]')
                    else:
                        print('error with instruction[2]')
                # if instructions has exactly 4 instructions in list
                elif len(instructions) == 4:
                    if instructions[2] == 'save':
                        if instructions[1] == 0:
                            registers[reg0] = binToDec(binaryStr)
                            instructions.clear()
                            line = f.readline()
                        elif instructions[1] == 1:
                            registers[reg1] = binToDec(binaryStr)
                            instructions.clear()
                            line = f.readline()
                        elif instructions[1] == 2:
                            registers[reg2] = binToDec(binaryStr)
                            instructions.clear()
                            line = f.readline()
                        elif instructions[1] == 3:
                            registers[reg3] = binToDec(binaryStr)
                            instructions.clear()
                            line = f.readline()
                        else:
                            print('register in instructions[1] not found to save to')
                    elif instructions[2] == 'multiply':
                        instructions.append(binToDec(binaryStr))
                        line = f.readline()
                    else:
                        print('error instructions[2] not anticiipated with instructions length 4')
                # if instructions has exactly 5 instructions
                if len(instructions) == 5:
                    if instructions[2] == 'multiply':
                        if instructions[1] == 0:
                            registers[reg0] = instructions[4] * binToDec(binaryStr)
                            instructions.clear()
                            line = f.readline()
                        elif instructions[1] == 1:
                            registers[reg1] = instructions[4] * binToDec(binaryStr)
                            instructions.clear()
                            line = f.readline()
                        elif instructions[1] == 2:
                            registers[reg2] = instructions[4] * binToDec(binaryStr)
                            instructions.clear()
                            line = f.readline()
                        elif instructions[1] == 3:
                            registers[reg3] = instructions[4] * binToDec(binaryStr)
                            instructions.clear()
                            line = f.readline()
                        else:
                            print('register in instructions[1] not found to save to')
                    else:
                        print('the instructions list is too long to not be multiplying')

            # else:
            #     print('the length of instructions is not accounted for')
            #     print(len(instructions))

#Create:
# Array of instructions --> instructions variable in executeInstructions
# CPU to read instructions starting at 0
# Array containing ASCII values --> register

executeInstructions(args.filename)

############################# TESTS #####################################
# print(initialize({1: 'a', 2: 'b', 3: 'c'}))
# print(int('00000001', 2))
# print (binToDec('00000000'))
