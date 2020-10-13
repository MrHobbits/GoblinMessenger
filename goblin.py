#!/usr/bin/python3
from math import sqrt
from os import system as cmd
import random

PROGRAM_AUTHOR = "Ryan 'Mr Hobbits' (www.mrhobbits.com)"
CURRENT_VERSION = "0.2"


# clear the screen straight away...
clearTheScreen = cmd('clear')


def createBlankGrid(size):
    # this function creates a blank grid of periods
    # technically, it is just a liner length of periods set to
    # whatever <size> is set to. But it must be a 'square' when
    # given to the rotate and other functions.

    # determine if the size would result in a 'square'
  
    if size >= 5 and size % 2 == 0:
        maxSize = size * size
        newGrid = '.' * maxSize

        return(newGrid)

    else:
        print("invalid length, needs to be 6 or higher")
        return(0)
 

# function to rotate a liner array
def rotateGrid(arrayGrid):

    # get the size of the 'ball' dynamically, so we dont have to fuck with it manually
    size = int(sqrt(len(arrayGrid)))
    newBall = ""
    startPos = len(arrayGrid) - size

    # loop through the linear array and swap the values around
    # based upon the concept that our 'ball' will always be an
    # array that has a whole number as it's length
    while startPos != len(arrayGrid):

        for n in range(startPos,0-size,-size):

            # if the value of n is less than 0 discard the value
            if n >=0:
                newBall += arrayGrid[n]
        
        # increment the starting position
        startPos += 1


    return(newBall)

# def findDots(arrayWithDots):
#     dots = []

#     for i in range(0,len(arrayWithDots)):
#         if arrayWithDots[i] == '.':
#             #print('location {} is a dot'.format(i))
#             dots.append(i) 

#     return(dots)

def printGrid(arrayGrid):
    # this function takes in a linear grid and prints it
    # out as if it were supposed to be in a square shape
    size = int(sqrt(len(arrayGrid)))

    for i in range(size, len(arrayGrid)+size, size):
         print(arrayGrid[i-size:i])

def encodeText(arrayGrid):
    # this function asks from the user what they want to say
    # and will output what they input. The caveat here is that
    # the length of what they say can't be longer than the size
    # if the grid that was created.

    print('Enter your text to encode, it must be less than {} characters'.format(len(arrayGrid)))
    print('    ','-' * len(arrayGrid))

    satisfied = False

    while not satisfied:
        userText = input("msg: ")
        if len(userText) > len(arrayGrid):
            print('Your message is too long.')
        else:
            satisfied = True

    return (userText)


def getSeed(arrayGrid):
    # this function will attempt to pick locations on the grid that
    # when the grid is 'rotated' the same locations will not contain
    # a value in the location picked. e.g.
    
    test_array = arrayGrid
    # list_of_dots = findDots(test_array)

    while '.' in test_array:
        # find a good location that doesn't have an 'x' or 'o'
        # we might be able to speed this up if we can figure out how to
        # first collect all the locations a dot is (maybe in an array?)
        # and then randomly pick one of those locations and fill it then
        # remove it

        #list_of_dots = findDots(test_array)
        list_of_dots = list(test_array)

        good_spot = False
        while not good_spot:

            # pick a random position anywhere along the array
            # randPos = random.randrange(0,len(test_array), 1)
            randPos = random.randrange(0,len(list_of_dots), 1)

            # did we pick a good spot?
            if test_array[randPos] == '.':
                good_spot = True
        
        # grab the array into something we can change
        test_array = list(test_array)

        # mark our good spot with an X
        test_array[randPos] = "x"

        # compress the list, rotate it, and check it
        
        # FIRST ROTATION
        test_array = ''.join(test_array)
        test_array = rotateGrid(test_array)

        test_array = list(test_array)
        if test_array[randPos] == '.':
            test_array[randPos] = 'o'

        # SECOND ROTATION
        test_array = ''.join(test_array)
        test_array = rotateGrid(test_array)

        test_array = list(test_array)
        if test_array[randPos] == '.':
            test_array[randPos] = 'o'

        # THIRD ROTATION
        test_array = ''.join(test_array)
        test_array = rotateGrid(test_array)

        test_array = list(test_array)
        if test_array[randPos] == '.':
            test_array[randPos] = 'o'

        # rotate it one last time, lets see what we got!
        test_array = ''.join(test_array)
        
        # Print the grid, should be full of x's and o's!
        # printGrid(test_array)
    

    the_seed = []

    for i in range(0, len(test_array), 1):
        if test_array[i] == "x":
            the_seed.append(i)

    
    # print("The seed is: {}".format(the_seed))

    return(the_seed)

def bufferMessage(the_message, max_size):
    # this will attempt to buffer the message to the max size
    # with a bunch of random shit
    garbage = "abcde fghij klmno pqrst uvwxy z0123 45678 9ABCD EFGHI JKLMN OPQRS TUVWX YZ "

    temp_msg = the_message

    while len(temp_msg) < max_size:
        temp_msg = temp_msg + garbage[random.randrange(0,len(garbage))]

    return(temp_msg)

def convertSeed(seed_to_convert):
    # this function converts the seed from letters and symbols into a list
    
    # create a blank list
    ord_seed = []

    # loop through the seed the user provided and convert it back
    # into a list
    for i in range(0,len(seed_to_convert)):
        ord_seed.append(ord(seed_to_convert[i])-36)
    
    seed_to_convert = ord_seed
    # can probably just return ord_seed... thoughts for later cleanup
    return(seed_to_convert)

def pullMessage(the_message,the_seed):
    # this function will take the supplied seed and message
    # and write each letter into our grid, and eventually
    # will fill the whole grid with the message
    
    TEST_MSG = "3-BsmgVuPitst-s5sej--eGtJtsact-iashe"
    TEST_SEED = ".FC27-'B6*"

    # temporary assignment so we can test things.    
    # the_message = TEST_MSG
    # the_seed = TEST_SEED

    # we need to validate the length of the message by deterining the square root
    if not sqrt(len(the_message)) == the_seed[-1]:
        print('Invalid message, pixel_boundary mismatch')
        return('Invalid')

    # turn the grid into a list, which is easier to make into a grid
    # and rotate around
    the_grid = list(the_message)

    out_message = ""

    # while the length of the decoded message is less than what the user
    # gave to us, loop through it!
    while len(out_message) < len(the_message):
        the_grid = list(the_grid)
        for i in the_seed[:-1]:

            # letter validation
            if the_grid[i] == "-":
                the_letter = " "
            else:
                the_letter = the_grid[i]
    
            out_message += the_letter

        the_grid = rotateGrid(''.join(the_grid))

    return(out_message)


def writeMessage(the_message, the_array, the_seed):
    # this function will take the supplied seed and message
    # and write each letter into our grid, and eventually
    # will fill the whole grid with the message
    
    if len(the_message) < len(the_array):
        the_message = bufferMessage(the_message,len(the_array))

    # TEMP OVERRIDE
    #the_message = "hello there ryan how are you? great!"
    the_grid = list(the_array)

    while len(the_message) > 0:
        try:

            the_grid = list(the_grid)
            for i in range(0,len(the_seed),1):

                # letter validation
                if the_message[i] == " ":
                    the_letter = "-"
                else:
                    the_letter = the_message[i]

                the_grid[the_seed[i]] = the_letter
        except IndexError:
            print('Index Error (change this to something creative)')            
            return(0)

        the_grid = rotateGrid(''.join(the_grid))

        the_message = the_message[len(the_seed):]

    return(''.join(the_grid))


def scrambleGrid(the_seed):
    # this function will scramble the grid_seed to prevent easy deconstruction

    hold_seed = the_seed
    scrambled_grid = []

    while len(hold_seed) > 0:
        randy = random.randrange(0,len(hold_seed))
        spot = hold_seed[randy]
        scrambled_grid.append(spot)

        del hold_seed[randy]
        
    return(scrambled_grid)

def displayMenu():
    # this displays the main menu when the program starts.

    choice = 0

    while choice not in range(1, 4):
        # os.system('clear')
        choice = int(input("1. Encode a message\n2. Decode a message\n3. Quit\nYour Choice: "))
        
        if choice not in range(1,4):
            print('You must choose a valid option.')


    return(choice)

def message_encode():
        
    # TODO: Maybe ask the user what size of grid they want?
    #       Grid can be any size to be honest, but 6 is a decent size.

    
    # ask the user if they have a key or not
    custom_seed = ''
    while custom_seed.lower() not in ["n", "y"]:
        custom_seed = input('Do you want to use a pre-shared seed (y/n)')
        
    if custom_seed.lower() == "y":
        # ask the user for their pre-shared seed
        grid_seed = input('Enter your pre-shared seed here: ')

        # the last integer of our seed is the size of the array
        # grab the last integer from the decoded seed.
        grid_size = convertSeed(grid_seed)[-1]

        # the seed needs to have the last number removed.
        grid_seed = grid_seed[:-1]

        # because they supplied a custom key, we need to convert it
        grid_seed = convertSeed(grid_seed)

        # we need a blank grid, create one
        grid = createBlankGrid(grid_size)
        
    else:
        # the user did not pick to use a pre-made seed.
        # Default value: 6
        grid_size = 8

        # we need a blank grid, create one
        grid = createBlankGrid(grid_size)
        
        # have the program figure out a random seed, and then scramble it
        # this might be changed to be optional later, maybe...
        grid_seed = getSeed(grid)
        grid_seed = scrambleGrid(grid_seed)
            
        
    the_message = encodeText(grid)

    out_message = writeMessage(the_message, grid, grid_seed)
    if out_message == 0:
        print('There was an error encoding your message')
        return(0)

    # clear the screen
    clearTheScreen = cmd('clear')
    
    # Provide the output to the user
    print('\nYour encoded message is as follows:')
    print(out_message)
                
    # And add the size of the array
    grid_seed.append(grid_size)

    # Convert the array into a string of ASCII characters so humans
    # can remember it (or share it easily)
    ascii_seed = ""
    for i in grid_seed:
        # convert each letter of the array into ASCII
        ascii_seed += chr(i+36)

    # If the user did not supply a seed, show it to them
    # if they did... show which seed they used.
    if custom_seed.lower() == "n":
        print('\nYour seed is as follows')
        print(ascii_seed) # human rememberable
    else:
        print('Remember, your pre-shared seed is:')
        print(ascii_seed) # human rememberable

    return()


def main():
    # main function, this is where the magic happens
    # TODO:
    # - [DONE] create function that picks locations based on a passphrase
    #   that will always result in the same locations being picked
    #   so that we can decode the message too.
    #
    # - [DONE] encode function
    # - [DONE] decode function
    #
    # - [TODO] file output?
    
    # - [DONE] Need to add an option where I can have a constant seed (pre-shared)
    #          that we can use to encode all the messages that way we dont have to
    #          keep sharing the keys back and forth
    
    # - [DONE] main menu system
    # - [DONE] add a function that will turn the seed into letters. As it is
    #          right now the seed may be hard to use or understand (and pass secretly)
    #          but if we know that the maximum number in the seed (for now) is 36
    #          we can figure out what the letters in the ascii table are and just
    #          add X to the seed number then convert it into the letter version
    # - [DONE] add a function that will turn the letter seed back into integers
    #   so we can use them to decode! CHR(90) = Z CHR(48) = 0
    #
    # - [FOOD FOR THOUGHTS] 
    #          [IDEA ONE] We might want to try to add a small amount of minor
    #          "encryption" where we append to the end of the seed an integer that
    #          indicates we have shifted the message letters to the left (odd) or
    #          to the right (even) by X amount. I **think** that this will prevent
    #          any sort of brute force attempts to just simply unscramble the message
    #          that may have been passed, as the value will always be random
    #
    #          [IDEA TWO] Would be interesting to allow the user to input a message of
    #          any size and rather than try to output a super long string of characters
    #          we would just chunk it into whatever size grid we decide to use.
    #          The output of this method would be several sentances of X length that
    #          would have to be saved to a file (and input from file) which would be
    #          something that would have to be able to be passed via email.

    action = displayMenu()

    if action == 1:
        # encode a message
        message_encode()

    elif action == 2:
        # decode a message
        in_message = ""
        in_seed = ""

        print("""
        To decode your message we will need to know two things.
        The first, what your encoded message is.
        The second, is your seed. Your seed needs to be entered
        exactly as you received it, for example:
        .FC2-'B4*
        
        If it is NOT entered exactly as it should be you will never
        decode your message.
        """)

        # get the user's encoded message
        in_message = input('Please enter your encoded message below\n: ')

        # get the user's seed
        in_seed = input('Please enter your seed\n: ')###########.split()

        
        # show me what the seed looks like now
        print(in_seed)
        in_seed = convertSeed(in_seed)
        out_message = pullMessage(in_message, in_seed)

        if out_message != "Invalid":
            print('Decoded message is as follows:\n{}'.format(out_message))
        


    elif action == 3:
        # quit the program
        print('The Goblin King thanks you for your service.')

    return True

# start the program
if __name__ == '__main__':
    main()

