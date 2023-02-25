# Version 2 - error message included when calling function


# Functions go here
def choice_checker(question):

       valid = False
       while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question) .lower()

        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "paper":
            return response
        elif response == "s" or response == "scissors":
            return response
        

        elif response == "xxx":
            return response
        else: 
            print(error) 

# Main routine goes here 


# Loop for testing purposes
user_chice = ""
while user_chice != "xxx":

    # Ask user for choice and oheck it's valid
    # user_choice = choice_checker("choose rock / paper / "
                                   "scissors (r/p/s): ", 
                                   "please choose from rock / " 
                                   "peper / scissors "
                                   "(or xxx to quit)"

     # print out ohice for chomparsion purposes
    print("you chose {}".format(user_choice))



