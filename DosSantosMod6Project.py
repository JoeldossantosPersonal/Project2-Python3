"""
* Class: 44-141 Computer Programming I
* Author:  Joel Dos Santos Iraha
* Description:   This program should give the option to either encrypt or decrypt a file of passwords.
                The encryption option should take each password in the file, encrypt it, and output the
                encrypted contents to a new file.
* Due: November 18th, 2021
* I pledge that I have completed the programming assignment independently.
* I have not copied the code from a student or any source.
* I have not given my code to any other student and will not share this code with anyone under any circumstances.
"""
def encrypt():                                   #defining function to encrypt file
    enc = input("Enter file to encrypt: ")       #user input for file to encrypt and file to write encrypted code on
    outFile = input("Enter output file: ")      
    read_file = open(enc, "r")                   #open files from user's input ; input for reading, output file to write
    write_file = open(outFile, "w")              
    for i in read_file:                          #for loop to read line by line
        passwords=""                             #variable password to store characters
        count=0
        for x in i:                              #for nested loop to read char. by char. in each line
            char = ord(x)                        #casting characters to ord ascii values
            char = ord(x)-count                  #its ASCII code minus 1, its index number in the list)
            char = str(char)                     #casting  ord characters (int) to str
            passwords+=char+"."                  #adding . in between characters 
            count+=1                             #count++
        write_file.write(passwords+"\n")         #once 2nd for loop done, write password on output file
    read_file.close()          
    write_file.close()
    print("\nEncrypted passwords wrote to", outFile+"\n")      
            


def decrypt():                                   #defining function to decrypt file
    enc = input("Enter file to decrypt: ")       #user input for file to decrypt and file to write decrypted code on
    outFile = input("Enter output file: ")       
    read_file = open(enc, "r")                   #open files from user's input ; input for reading, output file to write
    write_file = open(outFile, "w")              
    for i in read_file:                          #for loop to read line by line 
        passwords=""                             #variable password to store characters
        char = i.split(".")                         #spliting each line separated 
        char.pop()                               #deleting "\n" from last line in the file
        for x in range (len(char)):              #for in range nested loop (stop range lenght of char); 
            c = int(char[x])                     #casting str to int; takes index value x and store in variable c (char instead of c)
            c+=x                                 # now, c = value of index value x plus x 
            c=chr(c)                             #casting c characters (int) to str using chr ascii value
            passwords= passwords + c             #concatenating c to password variable
        write_file.write(passwords)              #once 2nd for loop done, write password on output file
    read_file.close()          
    write_file.close()
    print("\nDecrypted passwords wrote to", outFile+"\n")
           
    
# main program
print("Welcome to the password encryption program!\n")
print("Options: < e for encryption >\n\t < d for decryption >\n\t < q to quit the program >\n")
option = input("Select an option: ")
while (option!="q"):
    if (option == "e"):
        encrypt()
    elif(option == "d"):
        decrypt()
    else:
        print("\nIncorrect option. Please select another option: \n")
    print("Options: < e for encryption >\n\t < d for decryption >\n\t < q to quit the program >\n")
    option = input("Select an option: ")
print("\n ** Thank you for using our program! ** ")

        




        


