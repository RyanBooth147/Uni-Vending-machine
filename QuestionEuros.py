import SelectionEuros # imports seletion to enable this question to lead to different options 
import UnrecognisedEuros # imports unrecognised to allow if unrecognised inputs

def question(): # as the answer will be a whole number the interger "int" is used to describe the input 
     answer = int(input(""" 

   Would you like anything else?

             1. Yes
             2. No
             3. Exit

             """)) # this uses three " to enable the formatting to match the rest of the code
     if answer == 1: # if the user inputs excatly the number 1 it will lead to the selection 
          SelectionEuros.selection()
     elif answer == 2: # if the user inputs exactly the number 2 it will lead to the payment section
          SelectionEuros.pay()
     elif answer == 3: # if the user inputs exactly the number 3 it will allow the user to quit the application
          input ("""
   Press the enter key to exit""") # allows the user to quit the application by pressing the enter key
          quit ()
     else: # if the user inputs anything else it will lead to the unrecoginsed section 
          UnrecognisedEuros.main()
