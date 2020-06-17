def name_to_number(name):
    # delete the following pass statement and fill in your code below
    
    #dic = {"rock":0, "Spock":1, "paper":2, "lizard":3, "scissors":4]
    num = [x for x in range(5)]
    nam = ["rock", "Spock", "paper", "lizard", "scissors"]
    dic = dict(zip(nam,num))
    # convert name to number using if/elif/else
    # don't forget to return the result!
    return dic[name]

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    
    num = [x for x in range(5)]
    nam = ["rock", "Spock", "paper", "lizard", "scissors"]
    dic = dict(zip(num,nam))
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    return dic[number]

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
    print '\n'
    # print out the message for the player's choice
    print 'Player chooses ' + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    import random
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print 'Computer chooses ' + comp_choice
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    
    if diff == 3 or diff == 4:
        print 'Player wins!'
    elif diff == 1 or diff == 2:
        print 'Computer wins!'
    else:
        print "Player and computer tie!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
