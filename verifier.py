# Author: Nate Browne

import re
from strings import validate_domain, email_err_str

# Set of valid email domains
domains = {
    'gmail.com',
    'yahoo.com',
    'outlook.com',
    'ucsd.edu',
    'cs.ucsd.edu',
    'eng.ucsd.edu'
}

# Handy regular expression used for email matching
# shoutout to CSE 105 for being able to create this
# monstrosity
r_str = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
regex = re.compile(r_str)


def verify_email(email: str) -> None:
    '''Verifies that the given email address is a valid email address. It
    considers an email to be valid if it is formatted <name>@domain.*.

    This function will raise a KeyboardInterrupt if the email is invalid.

    Args:
        email: First argument. Email to verify

    Returns:
        None.
    '''

    # Initially, assume the email will be valid
    valid = True

    if not regex.match(email):
        valid = False

    # Make sure there is something after the @ sign
    check = email.split('@')

    # If the domain given isn't in the set, make sure the user really does want
    # to send the email to that domain
    if check[1] != '' and check[1] not in domains:
        double_check = input(validate_domain.format(check[1]))

        if double_check.upper() != 'Y':
            raise KeyboardInterrupt

    if not valid:
        print(email_err_str.format(email))
        raise KeyboardInterrupt
