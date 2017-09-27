#! /bin/python3
import argparse
import math
import time

# set up arguments for running the program
parser = argparse.ArgumentParser(description = "runOnMicroArchitecture")
parser.add_argument("filename",help = "filenameToRun")
args = parser.parse_args()
Data = args.filename

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
    '00000010': 'set',
    '00000100': 'save',
    '00000101': 'multiply',
    '00000110': 'print'
        }

# dictionary of registers
registers = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0
    }

# function to pull out binary string
def pullBinaryStr(line):
    line = line.strip()
    temp = line.split(" ")
    # extract the 8 digits I need
    binaryStr = temp[0]
    return binaryStr

# function for SET ---> when called set equal to super register (like Intel)
def setReg(Data):
    # next line gets reg#
    line = Data.readline()
    # is commented
    while isCommented(line) == True:
        line = Data.readline()
    # pull the binary
    regBin = pullBinaryStr(line)
    regNum = binToDec(regBin)
    return regNum

# function for SAVE
def save(Data):
    # next line gets # to save
    line = Data.readline()
    # is Commented?
    while isCommented(line) == True:
        line = Data.readline()
    # pull the binary
    binNum = pullBinaryStr(line)
    saveNum = binToDec(binNum)
    return saveNum

# funtion for MUL
def multiply(Data):
    # next line gets first num to multiply
    line = Data.readline()
    # isCommented
    while isCommented(line) ==True:
        line = Data.readline()
    regBinNum1 = pullBinaryStr(line)
    regNum1 = binToDec(regBinNum1)
    reg1 = registers[regNum1]
    # next line gets second num to multiply
    line = Data.readline()
    # isCommented
    while isCommented(line) ==True:
        line = Data.readline()
    regBinNum2 = pullBinaryStr(line)
    regNum2 = binToDec(regBinNum2)
    reg2 = registers[regNum2]
    return reg1 * reg2

# funtion for PRINT_NUM

# CODE EXECUTE function
def executeCode(Data):
    with open(Data, 'r') as f:
        line = '#'
        while True:

            line = f.readline()
            if not line: break
            while isCommented(line) == True:
                line = f.readline()
            binaryStr = pullBinaryStr(line)
            print(binaryStr)
            # determine what those digits mean
            if dict[binaryStr] == 'initialize':
                initialize(registers)
                # continue;
                # break;
            elif dict[binaryStr] == 'set':
                # save the register to the super secret hidden register (Intel has them, so can I! mwahaha)
                superSecretHiddenRegister = setReg(f)
            elif dict[binaryStr] == 'save':
                registers[superSecretHiddenRegister] = save(f)
            elif dict[binaryStr] == 'multiply':
                registers[superSecretHiddenRegister] = multiply(f)
            elif dict[binaryStr] == 'print':
                print(registers[superSecretHiddenRegister])
            else:
                print('this code is not accounted for')
                print(binaryStr)
                break;

executeCode(Data)
