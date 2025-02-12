num_in_words = {1:"one",2:"two",3:"three",4:"four",6:"six"}
def convertNumber(number):
    if number in num_in_words:
        return f"{number} is {num_in_words[number]} in words."
    else:
        return f"{number} is not available"
    
def addMember(number,word):
    if number in num_in_words:
        return f"{number} is already available"
    num_in_words[number]=word
    return "New member added successfully"
def display():
    position = 0
    print("_"*100,"DICTIONARY","_"*100)
    for number,word in num_in_words.items():
        position +=1
        print(f"{100*" "} {position}.) {number} in words is {word}")
   
print("What do you want to do today?")


while True:
    print("1. Check numeric value in words\n2. Add a new member\n3. View dictionary\n4. Exit")
    try:
       choice = int(input("Enter your choice: "))
    except ValueError:
        print("Use integers please!")
        continue
    if choice == 1:
        try:
            number = int(input("Enter the number you want to check: "))
        except ValueError:
            print("Invalid input")
        print(convertNumber(number))
    elif choice == 2:
        try:
            number = int(input("Enter new member name: "))
        except ValueError:
            print("Invalid input")
        
        word = input("Enter words of the member: ")
        print(addMember(number,word))
    elif choice == 3:
        display()
        
    elif choice == 4:
        break
    else:
        print("Please try again invalid input.")
    




