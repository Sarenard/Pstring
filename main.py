from interpeteur import I, Interpretor
from parseur import Parser
from sys import argv as args
try:
    debug = False or args[2] == '-d'
except:
    debug = False
Interpretor(debug_mode=debug).run(Parser(debug_mode=debug).parse(args[1]))