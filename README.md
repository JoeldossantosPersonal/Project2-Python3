# Project2-Python3
Project #2 - Computer Programming I

You will be writing an encryption program for an IT company. Your program should give the option to either encrypt or decrypt a file of passwords. The encryption option should take each password in the file, encrypt it, and output the encrypted contents to a new file. The decryption process should reverse a previously encrypted file and output the original message to a new file. File to use for testing: passwords.txt 

Additional Information:
Encryption: To encrypt the file, you should start by reading through the file, character by character, and place each character into a list. Spaces and punctuation are considered characters.  You should then change each character in the list into its ASCII value and subtract its index from the value. For example, with the password: PQERYT, the capital P would be encrypted as 80 (its ASCII code of 80 minus 0, its index number in the list) and the Q would be encrypted as 80 (its ASCII code of 81 minus 1, its index number in the list).  Finally, take the list and concatenate all the values together into one string variable with a period between each value. For example, the password PQERYT, the encrypted output file would contain: 80.80.67.79.85.79.4.  (The 4 is the newline character at the end of the password in the file).

Decryption: To decrypt the file, you should start by reading through the input file. Next, take the string and create a list by using the split() function with the periods as the delimiter. When you create the list, there will be an empty string placed at the end of the list that will need to be removed. Finally, take the new list, add each value by its index and then convert that resulting ASCII number into its appropriate character.

Example: 80.80.67.79.85.79.4. → [80,80,67,79,85,79,4] → PQERYT\n

Your Task: 

You will need to define two functions with the following criteria:

A function named encrypt() with no parameters. Within the function, the user should be prompted to enter the input file name and the output file name. The function will then read in the data from the input file, encrypt the information, and output the results of the encrypted message to the output file.

A function named decrypt() also has no parameters. Within the function, the user should be prompted to enter the input file name and the output file name. The function will then read in the encrypted data from the input file, reverse the encryption process, and output the decrypted message to the output file.
The program should prompt the user to choose whether they want to encrypt or decrypt a file or exit the program.
