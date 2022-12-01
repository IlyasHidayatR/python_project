#morse convert

#morse code dictionary
morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 
         'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 
         'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 
         'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 
         'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', 
         '1':'.----', '2':'..---', '3':'...--', '4':' ....-', '5':'.....', 
         '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', 
         ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', 
         '(':'-.--.', ')':'-.--.-'}

#function to convert string to morse code
def convertToMorse(string):
    morse_string = ""
    for char in string:
        if char != " ":
            morse_string += morse[char] + " "
        else:
            morse_string += " "
    return morse_string

#function to convert morse code to string
def convertToString(morse_string):
    morse_string += " "
    string = ""
    char = ""
    for letter in morse_string:
        if letter != " ":
            i = 0
            char += letter
        else:
            i += 1
            if i == 2:
                string += " "
            else:
                string += list(morse.keys())[list(morse.values()).index(char)]
                char = ""
    return string

#main function
def main():
    while True:
        print("1. Convert string to morse code")
        print("2. Convert morse code to string")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            string = input("Enter string: ")
            print(convertToMorse(string.upper()))
        elif choice == 2:
            morse_string = input("Enter morse code: ")
            print(convertToString(morse_string))
        elif choice == 3:
            break
        else:
            print("Invalid choice")

#call main function
if __name__ == "__main__":
    main()