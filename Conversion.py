#for conversion of Binary To Decimal
def binary_To_Decimal(Bin):
    deciValue = 0
    initial = 1
    for i in range(len(Bin)-1,-1,-1):
        deciValue = deciValue + initial*Bin[i]
        initial = initial*2
    return deciValue # It returns decimal value from the given Binary digit


#for conversion of Decimal to Binary
def decimal_To_Binary(q):
    temp = []
    Bin = ""
    while q > 0:
        if q%2 != 0:
            temp.append(1) # It adds 1 to the temp list
        else:
            temp.append(0) # It adds 0 to the temp list
        q = int(q/2) # It Converts float type value into integer if q/2 contains decimal value
    for i in range(len(temp)-1,-1,-1):
        Bin += str(temp[i])
    if len(Bin) < 8:
        for i in range(len(Bin),8):
            Bin = "0" + Bin # It adds 0 if the total length of the numbers is less than 8 digits   
    return Bin # It returns Binary digit of the given decimal value
