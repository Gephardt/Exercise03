from arithmetic import *

while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")
     
    if tokens[0] == "q" or tokens[0] == "quit":
       break   
    elif tokens[0] == "+":
        print add(int(tokens[1]),int(tokens[2]))
    elif tokens[0] == "-":
        print subtract(int(tokens[1]),int(tokens[2]))
    elif tokens[0] == "*":
        print multiply(int(tokens[1]),int(tokens[2]))
    elif tokens[0] == "/":    
        print divide(int(tokens[1]),int(tokens[2]))
    elif tokens[0] == "square":
        print square(int(tokens[1]))
    elif tokens[0] == "cube":
        print cube(int(tokens[1]))
    elif tokens[0] == "pow":
        print power(int(tokens[1]), int(tokens[2]))
    else:
        print mod(int(tokens[1]),int(tokens[2]))
  
