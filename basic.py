from ast import parse
from sys import *

tokens = []

def open_file(filename):
    data = open(filename, "r").read()
    return data

def lex(filecontents):
    tok = ""
    state = 0
    string = ""
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        if tok == " ":
            if state == 0:
                tok = ""
            else:
                tok = " "  
        elif tok == "printc":
            tokens.append("printc")
            tok = ""
        elif tok == "\n":
            tok = ""
        elif tok == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("STRING: " + string + "\"")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""
    return tokens
    # print(tokens)

def parse(toks):
    i = 0
    while(i < len(toks)):
        if toks[i] + " " + toks[i+1][0:6] == "> ":
            print(toks[i+1][6:])
            i+=2
           
        

def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)

run()