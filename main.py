#!/usr/bin/env python3
# Author: Nate Browne
# Read the README.md file to get information on how to use this program fully.

import csv  # For csv/tsv reading
import pprint  # for debugging

from sys import argv, exit
from os.path import isfile
from mailer import send_mail
from strings import file_err_str
from verifier import verify_email
from extractor import extract_data
from creator import create_course_string


def main(debug: bool = False) -> None:
    '''Main function. Called to run the entire script.

    Args:
        debug: First parameter. Enables diagnostic output. Defaults to False.

    Returns:
        None.
    '''

    # Used to print dictionaries nicely
    pp = pprint.PrettyPrinter(indent=1)

    # Grab info from user
    try:
        quarter = input("Enter the quarter here (Example: Spring 2019): ")
        filename = input("Enter the name of your .tsv file: ")
    except(KeyboardInterrupt, EOFError):
        print('\nExiting...')
        exit(0)

    # Make sure the filename is there
    print("\nVerifying file...")
    if '.tsv' not in filename:
        filename += '.tsv'

    if './' not in filename:
        filename = './' + filename

    if not isfile(filename):
        print(file_err_str.format(filename))
        print()
        exit(1)

    print("File verified. Parsing and generating email...")
    with open(filename, 'r') as infile:

        # Read in the .tsv and skip Gary + TA account
        # This may change depending on the quarter; adjust the number to
        # reflect the number of lines to skip
        reader = csv.reader(infile, delimiter='\t')
        for ind in range(2):
            next(reader)

        # Populate the mails array with one email string per tutor
        mails = []
        printed = False
        for row in reader:
            data = dict()
            extract_data(row, data)

            # Print the first entry
            if debug and not printed:
                pp.pprint(data)
                printed = True

            mails.append(create_course_string(data, quarter))

    if debug:
        # Check the first one to make sure all is good
        print(mails[0])

    # Turn the array into a giant string for emailing
    result = ''.join(mails)
    print(f"Parsed TSV file. Number of tutors: {len(mails)}.")
    print("Verify that this number is what you expect to see.")

    # Send the email
    try:
        opt = input("Send (e)mail or output to (f)ile?: ")
        if opt.upper() == 'E':
            print()
            receiver = input("Send to Gary? (y/n): ")
            if receiver.upper() == 'Y':
                send_mail(result)
            else:
                print()
                print("Enter an email address to send the email to.")
                dest = input("Email address must be well formatted: ")

                # Make sure the user gave us a valid email address
                verify_email(dest)

                send_mail(result, dest)
        else:
            print("Writing to file \"emails.out\"...")
            with open("emails.out", 'w') as outfile:
                outfile.write(result)
    except(KeyboardInterrupt, EOFError):
        print("\nAborted.")
        exit(1)

    print("Complete!")


# Boilerplate to run main
if __name__ == '__main__':

    # Check for debug mode
    if len(argv) - 1 == 1 and (argv[1] == '--debug' or argv[1] == '-d'):
        main(True)
    else:
        main()
