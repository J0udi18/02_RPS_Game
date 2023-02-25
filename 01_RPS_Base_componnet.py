import random

# Funtons go here 
def checker_rounds():
    while Ture:
        response = input("How many rounds: ")

        round_error = "please type either <enter> or an " \
                      "integer that is more than 0\n"
        
        #If infinite mode not ohosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)
                
                # If response is too low, go back to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            # If response is not an integer go back to
            # start of loop
            except ValueError:
                print(round_error)
                continue
        return response
    

# Main routine hoes here

# Lists of valid responses
yes_no_list = ["yes, no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# If 'yes', show instructions


# ask user for # of rounds then loop...


# Ask user if they want to see their game history.
# If 'yes' show game history

# show game statistics