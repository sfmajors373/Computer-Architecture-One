#! /bin/python3
import argparse

parser = argparse.ArgumentParser(description = "runOnMicroArchitecture")
parser.add_argument("filename",help = "filenameToRun")
args = parser.parse_args()

def printShit(Data):
    with open(args.filename, 'r') as f:
        read_data = f.readline()
        while (f.readline() != ""):
            print(read_data)
            read_data = f.readline()

printShit(args.filename)
