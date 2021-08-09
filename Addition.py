import LogicalGates as gates # It imports the functions from LogicalGates

def byte_adder(x, y, z):
    result = ""
    #sum value
    for i in range(len(y)-1,-1,-1): #does loop for the 8 times 
        xs = gates.xor_Gate(int(x[i]),int(y[i]))
        add_val = gates.xor_Gate(xs, z)
        result += str(add_val)
        #for carryOver
        fc = gates.and_Gate(int(x[i]),int(y[i]))
        fc2 = gates.and_Gate(xs,z)
        c = gates.or_Gate(fc, fc2)
        z = c
        #this is the value of carry over
    if z == 1:
        result += str(z)
    result = result[::-1] #Reversing the result

    return result
