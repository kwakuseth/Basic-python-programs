#Creating the Caesar Cipher Program
import subprocess
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"

def num_shift(a):
    return a%10

def shift_amount(i):
    return i%26

def encrypt(text, required_shift):
    output_string = ""
    text = text.lower()
    for char in text:
        if char not in alphabet:
            if char not in numbers:
                output_string = output_string + char
            elif char in numbers:
                char_index = numbers.find(char)
                output_string += numbers[num_shift(char_index + required_shift)]
        else:
            char_index = alphabet.find(char)
            output_string += alphabet[shift_amount(char_index + required_shift)]
    return output_string


print("""This program can be used to encrypt both text and numbers thereby hiding details from other users.
It allows you to feed it with documents and other text files apart from feeding them directly in the console.""")
password=int(input('Please enter your pin: '))
while password>9999:
    print('Pin must be four digits long')
    password=int(input('Please re-enter your pin: '))
conf_password=input('Confirm pin: ')
while int(conf_password) != password:
    print('Access denied')
    conf_password=input('Re-enter your pin: ')
else:
    print('Access granted')
input('\nPress any key to continue')
#get_file = subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')
#new = open("F:/Python/Python codes/this.txt", "a")
#print("I'm adding these two lines from a python console.\nYou may wonder how. Let's get interactive on 0555024099.", file=new)
#new.close()


#string = input("Enter text to encrypt: ")
encrypted = encrypt(get_file,5)
print(string.swapcase()+" encrypted will return "+"'"+encrypted+"'")
print()
input("Press enter to see the original number: ")
decrypted = encrypt(encrypted,-5)
print("This is the original text",decrypted)
#decrypted = encrypt(encrypted,-5)