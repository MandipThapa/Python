#Gates for the addition

#AND-gate
def and_Gate(x,y):
    if x==1 and y==1:
        return 1
    else:
        return 0

#OR-gate
def or_Gate(x,y):
    if x==0 and y==0:
        return 0
    else:
        return 1

#XOR-gate
def xor_Gate(x,y):
    if (x==1 and y==1) or (x==0 and y==0):
        return 0
    else:
        return 1

    
