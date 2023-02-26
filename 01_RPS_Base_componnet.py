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
    

def choice_checker(question, valid_list, error) :

    valid = False
    while not valid:

        # Ask user for ohoice (and put choice in lowercase)
        response = input(question).lower()

        # interates throught list and if response is an item 
        # in the list (or the first letter of an item) , the 
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return response

        # output error if item not in list
        print(error)
        print()


# Main routine hoes here

# Lists of valid responses
yes_no_list = ["yes, no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# If 'yes', show instructions


# ask user for # of rounds then loop...
rounds_played = 0
choose_instruction ="please choose rock (r), paper (p) or scissor"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: " \
                  "Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of " \
                  "{}".format(rounds_played + 1, rounds)
        
    print(heading)
    choose_instruction = "please choose rock (r), " \ 
                         "paper (p) or scissors (s) " \
                         "or 'xx to exit"
    choose_error = "please choose from rock " \
                    "peper / scissors (or xxx to quit) "

    # Ask user for ohoice and check it's valid
    choose = choice_checker(choose_instruction, rps_list, 
                               choose_error)
 
   # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("comp_choice: ", comp_choice)
    
   #compare choices

    # End game if exit code is typed
    if choose == "xxx":
        break

    #  **** rest of loop / game ****
    print("you chose {}".format(choose))

    rounds_played += 1 

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Ask user if they want to see their game history.
# If 'yes' show game history

# show game statistics