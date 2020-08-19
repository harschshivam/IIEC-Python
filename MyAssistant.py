# MyAssitant created by Harsch Shivam

import pyttsx3
import os


# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


# intro start

print("Hey User! I'm Your Assistant \n")
pyttsx3.speak("Hey User! I'm Your Assistant")

print("I've been created by a beginner, named Harsch Shivam \n")
pyttsx3.speak("I've been created by a beginner, named Harsch Shivam")

print("So please bare with me because he is still learning\n")
pyttsx3.speak("So please bare with me because he is still learning")

print("Here are a few things that I can help you with :\n")
pyttsx3.speak("Here are a few things that I can help you with :")

# intro end

while True:

    # options

    print("#1 DO YOU WANT ME TO TALK TO YOU? \n")
    print("#2 CAN I HELP YOU WITH BASIC CALCULATIONS? \n")
    print("#3 CAN I OPEN A PROGRAM FOR YOU? \n")
    print("#4 MAY BE YOU WANNA SEE A CAT \n")
    print("#5 OR NOTHING \n")

    # interface

    print("Ask Me (Just Type Here Your Requirement: ", end='')

    query = input()

    if ("1" in query) or ("#1" in query) or ("TALK" in query) or ("talk" in query):
        print("SORRY I DON'T HAVE MUCH TO SAY AS MY CREATOR NEEDS TO LEARN MORE")
        pyttsx3.speak("SORRY I DON'T HAVE MUCH TO SAY AS MY CREATOR NEEDS TO LEARN MORE")

    elif ("2" in query) or ("#2" in query) or ("calculations" in query) or ("calculation" in query) \
            or ("calculate" in query):

        pyttsx3.speak("Select operation")

        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Close Calculator")

        while True:
            # Take input from the user
            pyttsx3.speak("Enter input")
            choice = input("Enter choice(1/2/3/4/5): ")

            # Check if choice is one of the four options
            if choice in ('1', '2', '3', '4', '5'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))

                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))

                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))

                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))

                elif choice == '5':
                    pyttsx3.speak("Alrighty then!")
                    break
            else:
                print("Invalid Input")

    elif ("3" in query) or ("#3" in query) or ("open" in query) or ("program" in query):

        print("WHAT PROGRAM DO YOU WANT ME TO OPEN \n")
        pyttsx3.speak("WHAT PROGRAM DO YOU WANT ME TO OPEN")
        print("1. NOTEPAD OR TEXT EDITOR")
        print("2. CHROME BROWSER")
        print("3. WINDOWS MEDIA PLAYER")
        print("4. WINDOWS EXPLORER")
        print("5. NOTHING")

        while True:
            p = input("Tell me what you want : ")

            if ("1" in p) or ("notepad" in p) or ("editor" in p):
                pyttsx3.speak("Opening Notepad right away!")
                os.system("notepad")

            elif ("2" in p) or ("chrome" in p) or ("chrome.exe" in p):
                pyttsx3.speak("Opening Chrome Browser for you!")
                os.system("chrome")

            elif ("3" in p) or ("media" in p) or ("player" in p):
                pyttsx3.speak("Opening Windows Media Player!")
                os.system("wmplayer")

            elif ("4" in p) or ("explorer" in p):
                pyttsx3.speak("Here's your Window Explorer, enjoy!")
                os.system("explorer")

            elif ("5" in p) or ("nothing" in p) or ("none" in p):
                pyttsx3.speak("Anything else?")
                break

            else:
                pyttsx3.speak("Sorry that's unavailable")
                print(" Unavailable")

    elif ("4" in query) or ("show" in query) or ("cat" in query):

        print(' |\__/,|   (`\  ')
        print(' |_ _  |.--.) ) ')
        print(' ( T   )     / ')
        print('(((^_(((/(((_/ ')

        pyttsx3.speak("Here's my fluffy cat!")
        pyttsx3.speak("meow!")

    elif ("5" in query) or ("nothing" in query) or ("none" in query):
        exit()
        break

    else:
        pyttsx3.speak("Sorry, I don't support it")
        print("Sorry, I don't support it")
