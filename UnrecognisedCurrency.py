import Currency # this import the currency file to allow Unrecognised to access it

def main(): # uses the integer input as user should only input a whole number
    choice = int(input("""
   Selection unrecognised, would you like to continue?

            1. Yes
            2. Exit

            """)) # uses three " to keep consistant formatting thoughout the program for a consistent user experience
    if choice == 1:
        Currency.currency() # if the user inputs exactly the number 1 it will lead to the currency section
    elif choice == 2: # if the user inputs exactly the number 2 it will allow them to quit
        input ("""
   Press the enter key to exit""")# allows the user to quit the application using the enter key
        quit ()
    else:
        main() # if the user inputs anything else it will loop the section as this is the section for unrecognised inputs
