import QuestionDollars # this imports the Question file to allow it to be accessed but this section of code
import UnrecognisedDollars # this imports the Unrecognised file to allow for unrecognised input to be detected
import random # thsi inputs the native python module "random" to allow for the code to assign random numbers
list = [] # this will act as a blank list to enable the code to add to and display a list
total = 0 # this is the current "total" that will be used to calculate money 
change = 0 # this is the current "change" which will allow the code to calulate how much change is owed to the user
snickers_total = (random.randint(0,9)) # this uses the random module to assign a random total to the amount of "Snickers" in the machine 
marsbar_total = (random.randint(0,9)) # by using a random total the user experiance will be as similar to real life as able 
bounty_total = (random.randint(0,9))
coke_total = (random.randint(0,9))
fanta_total = (random.randint(0,9))
water_total = (random.randint(0,9))

def selection():
   global total # "global" allows for selection to access the current assigned vaule 
   global list
   global snickers_total
   global marsbar_total
   global bounty_total
   global coke_total
   global fanta_total
   global water_total
   # selection uses integer "int" as the user input should be a whole number
   selection = int(input("""
   Please make your choice

            1. Snickers - $1.20
            2. Mars Bar - $1.33
            3. Bounty   - $1.21
            4. Coke     - $2.42
            5. Fanta    - $2.48
            6. Water    - $1.81
            7. Cancel 

            """)) # displays the options that are contained in the vending machine 
   if selection == 1: # if the user inputs exactly the number 1 
             snickers_total = snickers_total-1 # will minus one from snickers_total and save that as the new snickers_total 
             if snickers_total == 2: # if snickers_total is exactly 2 it will inform the user that there is only one left (after they take this one)
                  print("""
   There is only one Snickers left in stock""") # informs the user there is only one left 
             elif snickers_total == 1: # if the new snickers_total is exactly 1 it will inform the user that they have taken the last one
                  print ("""
   Snickers is now out of stock""") # informs the user that there is no more left
             elif snickers_total <= 0: # if snickers_total is 0 or less (to factor in negative totals) it will inform the user that there are no more in stock 
                  print ("""
   Sorry, Snickers is out of stock""")
                  QuestionDollars.question() # this directs the code to the question file to ensure that no further changes are made to the current saved totals
             list.append('Snickers') # adds "Snickers" to the current list displaying purchases 
             total = total+1.20 # adds 0.99 (signifying 99p) to the current total and saves it as the new current total 
             print ("""
   For""",list,"your current total is $", ("%.2f" % total)) # this prints an current recipt for the user showing the updated list with thier purchaes and the current total price of all items to two decimal places to show currency
             QuestionDollars.question() # this will direct the code to the question file to ask if the user wants to add anything else to thier current order
   elif selection == 2: # if the user inputs exacly the number 2 then the above process is the same however each instance of Snickers or snickers_total is replaced with the corresponding selection
             marsbar_total = marsbar_total-1
             if marsbar_total == 2:
                  print("""
   There is only one Mars Bar left in stock""")
             elif marsbar_total == 1:
                  print("""
   Mars Bar is now out of stock""")
             elif marsbar_total <= 0:
                  print ("""
   Sorry, Mars Bar is out of stock""")
                  QuestionDollars.question()
             list.append('Mars Bar')
             total = total+1.33
             print ("""
   For""",list,"your current total is $",("%.2f" % total))
             QuestionDollars.question()
   elif selection == 3: # if the user inputs exacly the number 2 then the above process is the same however each instance of Snickers or snickers_total is replaced with the corresponding selection
             bounty_total = bounty_total-1
             if bounty_total == 2:
                  print("""
   There is only one Bounty left in stock""")
             elif bounty_total == 1:
                  print ("""
   Bounty is now out of stock""")
             elif bounty_total <= 0:
                  print ("""
   Sorry, Bounty is out of stock""")
                  QuestionDollars.question()
             list.append('Bounty')
             total = total+1.21
             print ("""
   For""",list,"your current total is $",("%.2f" % total))
             QuestionDollars.question()
   elif selection == 4: # if the user inputs exacly the number 2 then the above process is the same however each instance of Snickers or snickers_total is replaced with the corresponding selection
             coke_total = coke_total-1
             if coke_total == 2:
                  print("""
   There is only one Coke left in stock""")
             elif coke_total ==1:
                  print("""
   Coke is now out of stock""")
             elif coke_total <= 0:
                  print ("""
   Sorry, Coke is out of stock""")
                  QuestionDollars.question()
             list.append('Coke')
             total = total+2.42
             print ("""
   For""",list,"your current total is $",("%.2f" % total))
             QuestionDollars.question()
   elif selection == 5: # if the user inputs exacly the number 2 then the above process is the same however each instance of Snickers or snickers_total is replaced with the corresponding selection
             fanta_total = fanta_total-1
             if fanta_total == 2:
                  print("""
   There is only one Fanta left in stock""")
             elif fanta_total == 1:
                  print("""
   Fanta is now out of stock""")
             elif fanta_total <= 0:
                  print ("""
   Sorry, Fanta is out of stock""")
                  QuestionDollars.question()
             list.append('Fanta')
             total = total+2.48
             print ("""
   For""",list,"your current total is $",("%.2f" % total))
             QuestionDollars.question()
   elif selection == 6: # if the user inputs exacly the number 2 then the above process is the same however each instance of Snickers or snickers_total is replaced with the corresponding selection
             water_total = water_total-1
             if water_total == 2:
                  print("""
   There is only one Water left in stock""")
             elif water_total ==1:
                  print("""
   Water is now out of stock""")
             elif water_total <= 0:
                  print ("""
   Sorry, Water is out of stock""")
                  QuestionDollars.question()
             list.append('Water')
             total = total+1.81
             print ("""
   For""",list,"your current total is $",("%.2f" % total))
             QuestionDollars.question()
   elif selection == 7: # If the user inputs exacly the number 7 then it allows the user to quit the application 
                input ("""
   Press the enter key to exit""") # allows the user to exit the application by pressing the enter key
                quit ()
   else: # if the user inputs anything other than a number between 1 and 7 then it will lead to the unrecognised input section of code
      UnrecognisedDollars.main()


def pay(): 
   global total # "global" allows for selection to access the current assigned vaule
   global change
   proceed = int(input("""
   Proceed to transaction?
   
             1. Yes
             2. No
             3. Exit

             """))
   if proceed == 1: # if user inputs exactly the number 1 then it will start the payment process   
         print ("""
   For""",list,"Your total is $",("%.2f" % total),"""
   Input 0.00 to quit""") # this will show the user thier current list of items and the cost to two decimal places to represent currency
         while True: # allows for the process to repeat until full payment has been made
            payment = float(input("""
   Please insert payment $""")) # as the number may not be a whole number such as currency a float is used in place of an integer (int)
            change = change+payment # stores the value "change" as the amount of money that has currently been inserted by the user to be able to return it if needed 
            if payment == total: # if the payment that is inserted the exactly the same as the current total
                 print("""
   Thank you, have a nice day!""") # will thank the user for inputting the correct amount of money and as no further action is required 
                 input ("""
   Press the enter key to exit""") # allows the user to press the enter key to end the transaction
                 quit ()
            elif payment > total: # if the user inserts more money than the current total
                 total=payment-total # caluclates the overpayment and saves it as the new total
                 print("""
   Your change is $""",("%.2f" % total)) # informs the user how much change they are given to two decimal places to represent currency 
                 print("""
   Thank you, have a nice day!""")
                 input ("""
   Press the enter key to exit""")
                 quit ()
            elif payment == 0.00: # if the user inputs exactly 0.00 signifying no money 
               cancel = int(input("""
   Would you like to quit?

            1. Yes
            2. No
            
            """))# provides the user an option to quit if they have insufficient funds 
               if cancel == 1: # if the user inputs exacly the number 1
                  print("""
   Here is your money back $""", ("%.2f" % change)) # provides the user a current total of the money they have already input (to two decimal places to represent currency) 
                  input ("""
   Press the enter key to exit""")
                  quit ()
               elif cancel == 2: # if the user inputs exactly the number 2
                  print ("""
   for""",list,"Your total is $",("%.2f" % total),"""
   Input 0.00 to quit""") # repeats the current list and total to repeat the question as "while True" is still active 
               else: # if the user inputs anything that is not a 1 or a 2
                  UnrecognisedDollars.main() # re-directs to the unrecognised sections 
            else: # if the user input is not equal to or more than the total (or 0.00)
                  total=total-payment # calculates how much money is still owed
                  if total >= 0.01: # if the current total is more then or equal to 0.01 (signifying 1p)  
                      print("""
   Please insert additional $""",("%.2f" % total),"""
   Input 0.00 to quit""") # informs the customer of the outstanding total and asks for additional input
                  elif total < 0.01: # if the total is less than 0.01 as the calculation can provide results such as 0.00000001
                      print("""
   Thank you, have a nice day!""") # informs the user that the tranaction is complete
                      input ("""
   press the enter key to exit""")
                      quit()
   elif proceed == 2: # if the input to the original if statement is exactly 2 
      QuestionDollars.question() #re-directs to the question section 
   elif proceed == 3: # if the input is exaclty 3 
      input ("""
   Press the enter key to exit""") # allows the user to quit using the enter key
      quit ()
   else: # if the user inputs anything that is not a 1, 2 or 3
      UnrecognisedDollars.main() # re-directs to the unrecognised input section. 
