import Conversion as BCon # It import functions from Conversion
import Addition as BAdd # It import functions from module Addition

def Bin_Adder():
    print("*_____Welcome to Binary Adder_____*")
    execute = False # It is the condition for the main loop to continue
    while execute == False:
        finish = False # It is the condition for the input loop to continue
        while finish == False:
            try:
                j = int(input("Enter the First integer: ")) # asking input from user
               
                z = 0
                if j > 255 or j < 0:
                    print("The Number should be positive and between 0 and 255")
                else:
                    finish = True
            except:
                print("The value you have entered is Incorrect") # Exception  when the user inputs alphabets or symbols
        finish = False
        while finish == False:
            try:
                k = int(input("Enter the Second integer: "))
                if k > 255 or k<0:
                    print("The Number should be positive and between 0 and 255")
                else:
                    finish = True
            except:
                print("The value you have entered is Incorrect") # Exception when the user inputs alphabets or symbols
        BinaryA = BCon.decimal_To_Binary(j) #binary value of j in string
        BinaryB = BCon.decimal_To_Binary(k) #binary value of k in string
        print(f"The binary value of first number: {BinaryA}")
        print(f"The binary value of second number: {BinaryB}")
        Ans = ""
        Ans = BAdd.byte_adder(str(BinaryA),str(BinaryB),z) #Function for adding two 8-digit binary numbers
        print(f"The addition is: {Ans}")
        exe = input("Press Enter to Continue the program ///Enter F to Exit: ") # asking input for the user to continue
        exe = exe.upper() # Changing the input taken from the user to uppercase if the input taken is in lower case
        if exe == "F":
            execute = True
            print("****Terminating the program****")

            
Bin_Adder() # Calling the function Bin_Adder

