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

# custom thank you letter string.
THANK_YOU = '''Dear {},
We would like to thank you for your generous donation of {:,}
dollars to the Richardson Foundation. These funds will go a long
way in the fight aganist Ice Wurm infections.

Thank You,
Kyle Richardson
The Richardson Foundation
'''

'''
The dictonary of donors which is the main data structure.
Each name of a donor (the key) is related to a list containing their total
donations and number of donations.
example: donors["bill gates"] = [Total Donations, num Donations]
'''

donors = {'Big Boss': [250.90, 3], 'Tony Stark': [500.45, 1],
          'Bruce Wayne': [34, 2], 'Scrooge McDuck': [750.34, 2],
          'Kyle Richardson': [3.50, 1]}


def thank_you():
    """
    prints out a precreated thank you email using a name and donation amount
    given by the user. Creates or modifies a existing donator in the database.
    """

    # starting prompt for Thank You command
    while True:
        print(u"Please enter a name or choose from the following:\n")
        print(u"list - Print a list of previous donors\n")
        print(u"quit - Return to main menu\n")
        name_input = input(u"> ")
        # return to main menu if quit is entered
        if(name_input.lower() == "quit"):
            return
        # print out a list of previous donors
        elif(name_input.lower() == "list"):
            print(list(donors.keys()))
        else:
            name_input = name_input.title()
            break

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
    print(THANK_YOU.format(name_input, amount_float))
    # write it out to a txt file.
    out = open("letters.txt", 'a')
    out.write(THANK_YOU.format(name_input, amount_float))
    out.close()
    print(u"Letter printed to 'letters.txt'")
    print(u"Press Enter to Continue...\n")
    command = input(">")
    if(command.lower() == 'quit'):
        quit()
    # return to starting prompt
    return


def report():
    """
    Prints out a report of all donors to the terminal. Formatted and in order
    by total donated ammount
    """
    # create a temporary dictonary list of the donors sorted by donation total
    donor_list = sorted(donors.items(),
                        key=lambda donor: donor[1][TOTAL_DONATED],
                        reverse=True)
    # Top of report.
    print(u"  Name\t|  Total  | # |  Average")
    print(u"-------------------------------------------------")
    # prints out information for each donor.
    for name in donor_list:
        avg = float(name[1][TOTAL_DONATED]) / float(name[1][NUM_DONATIONS])
        print(u"{}\t|  ${:,}|  {:,}|\t${:,}"
              .format(name[0], name[1][TOTAL_DONATED],
                      name[1][NUM_DONATIONS], avg))
    print(u"Type 'Thank All' to send Thank You Letters to all Donors")
    print(u"Press Enter To Continue")
    command = input(">")
    if(command.lower() == 'thank all'):
        for name in donor_list:
            filename = "letters/{}_letter.txt".format(name[0])
            out = open(filename, 'w')
            out.write(THANK_YOU.format(name[0], name[1][TOTAL_DONATED]))
            out.close()
    # if anything else return to starting prompt
    return

# main interaction.
if(__name__ == '__main__'):
    command = ''
    while(command.lower().strip() != 'quit'):
        print(u"Welcome to Mailroom Madness\n")
        print(u"Choose from the following:\n")
        print(u"T - Send a (T)hank You\n")
        print(u"R - Create a (R)eport\n")
        print(u"quit -  Quit the program\n")
        command = input("> ")
        if(command.upper().strip() == 'T'):
            thank_you()
        elif(command.upper().strip() == 'R'):
            report()
        # if input is quit the script should quit naturally.
