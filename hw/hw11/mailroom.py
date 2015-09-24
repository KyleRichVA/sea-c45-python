"""
Mailroom Script.

This Script provides a database of donators to a user's
charity. The user can recieve a report on the donors and
send pre-created thank you letter to new or previous
donors.
"""

import string

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
    prints out a precreated thank you email using a name and donation ammmount
    given by the user. Creates or modifies a existing donator in the database.
    """
    pass
