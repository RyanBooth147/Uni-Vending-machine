import SelectionGBP # this imports the selection for GBP 
import SelectionDollars # this imports the selection for Dollars
import SelectionEuros # this imports the selection for Euros
import UnrecognisedCurrency # imports the unrecognised section from before the currency selection 

def currency(): # this selection allows for a user to to select the correct currency they wish to use
    currency = int(input("""

    Please select your currency

            1. £ (GBP)
            2. $ (Dollars)
            3. € (Euros)
            4. Quit

            """)) # uses """ to keep formatting and UX
    if currency == 1: # if the user inputs exactly the number 1 it will load the GBP selection 
        SelectionGBP.selection() # accesses the selectionGBP file to continue the code
    elif currency == 2:# if the user inputs exactly the number 2 it will load the Dollars selection
        SelectionDollars.selection()# accesses the selectionDollars file to continue the code
    elif currency == 3: # if the user inputs exactly the number 3 it will load the Euros selection
        SelectionEuros.selection()# accesses the selectionEuros file to continue the code
    elif currency == 4: # if the user inputs exactly the number 4 it will allow the user to quit the application
        input (""" 
    Press the enter key to exit""")
        quit() # allows the user to quit the application when pressing the enter key
    else: # if the user inputs a selection other than the number 1 - 4 it will loop the selection 
        UnrecognisedCurrency.main()
