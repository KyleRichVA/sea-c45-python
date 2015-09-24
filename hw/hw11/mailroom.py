"""
Mailroom Script.

This Script provides a database of donators to a user's
charity. The user can recieve a report on the donors and
send pre-created thank you letter to new or previous
donors.
"""

# global values to make the dictonary calls more human readable
TOTAL_DONATED = 0
NUM_DONATIONS = 1

'''
The dictonary of donors which is the main data structure.
Each name of a donor (the key) is related to a list containing their total
donations and number of donations.
example: donors["bill gates"] = [Total Donations, num Donations]
'''

donors = {}


def thank_you():
    """
    prints out a precreated thank you email using a name and donation amount
    given by the user. Creates or modifies a existing donator in the database.
    """

    # starting prompt for Thank You command
    print(u"Please enter a name or choose from the following:")
    print(u"list - Print a list of previous donors")
    print(u"quit - Return to main menu")
    name_input = input(u"> ")
    # return to main menu if quit is entered
    if(name_input.lower() == "quit"):
        return
    name_input = name_input.title()

    print(u"Please enter a donation amount or 'quit':")
    # value validation
    while True:
        try:
            amount_input = input(u"> ")
            # return to main menu if quit is entered
            if(amount_input.lower() == "quit"):
                return
            amount_float = float(amount_input)
            break
        except ValueError:
            print(u"Please type a valid numeric dollar amount. (no symbols)")

    # if the donor is already in the database modify their info
    if(name_input in donors.keys()):
        donors[name_input][TOTAL_DONATED] += amount_float
        donors[name_input][NUM_DONATIONS] += 1
    # otherwise create a new value in the dictonary
    else:
        donors[name_input] = [amount_float, 1]

    # print out the custom thank you letter
    print(u"Dear {},\n".format(name_input))
    print(u"We would like to thank you for your generous donation of {}"
          " dollars to the Richardson Foundation. These funds will go a long"
          " way in the fight aganist Ice Wurm infections\n"
          .format(amount_input))
    print(u"Thank You,\n\nKyle Richardson\n\nThe Richardson Foundation"
          "\n\nPress Enter to Continue...\n")
    input(">")

    # return to starting prompt
    return


def report():
    """
    Prints out a report of all donors to the terminal. Formatted and in order
    by total donated ammount
    """
    # Top of report.
    print(u"Name\t|  Total  | # |  Average")
    print(u"-------------------------------------------------")
    print(u"{}\t|  {}|  {}|  {}".format("Kyle","$200.00","5",str(200/5)))

# TESTING
report()
