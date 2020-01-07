# Author: Nate Browne

import smtplib as s
from typing import List
from getpass import getpass

smtp_servers = dict()
smtp_servers['G'] = 'smtp.gmail.com'  # Gmail/UCSD email
smtp_servers['Y'] = 'smtp.mail.yahoo.com'  # Yahoo mail
smtp_servers['O'] = 'smtp.office365.com'  # Microsoft outlook

errstr = "Email login failed. Double check your provided username and password"


def send_mail(course_string: str, recipient: str = "ggillespie@ucsd.edu"):
    '''Module for sending the course string email to a given recipient. Default
    recipient is Gary; the main script allows for an alternate recipient to
    receive the email if desired.

    Args:
        course_string: First argument. Fully constructed custom email string,
        one per tutor.
        recipient: Second argument. Email address to send the email to.

    Returns:
        None.
    '''

    TLS = 587
    message = "Subject: Verification emails for the tutors\n\n"
    message += "Hi Gary!\n\nHere are the emails as requested.\n\nCheers\n\n"
    to_send = message + course_string

    # Grab email client of choice
    print("\n")
    print("Please enter your email server of choice.")
    choice = input("Choices are (o)utlook, (y)ahoo, (g)mail/UCSD mail: ")
    choice = choice.upper()

    if choice not in smtp_servers.keys():
        print("Invalid email server given: ", choice)
        raise KeyboardInterrupt

    # Grab credentials
    print("Please enter your email address.")
    sender = input("It must match the mail server you specified: ")
    print("Please input the password for the email address you inputted.")
    passwd = getpass("Don't worry; your password isn't saved anywhere: ")

    print(f"\nSending email to {recipient} from {sender}")

    # Send message
    try:
        with s.SMTP(smtp_servers[choice], TLS) as server:
            server.ehlo()
            server.starttls()
            server.login(sender, passwd)
            server.sendmail(sender, recipient, to_send)
    except s.SMTPAuthenticationError:
        print(errstr)
        raise EOFError


def send_to_all(mailstrs: List[str], emails: List[str]) -> None:
    TLS = 587
    message = "Subject: Role Verification email\n\n"

    print("\n")
    print("Please enter your email server of choice.")
    choice = input("Choices are (o)utlook, (y)ahoo, (g)mail/UCSD mail: ")
    choice = choice.upper()

    if choice not in smtp_servers.keys():
        print("Invalid email server given: ", choice)
        raise KeyboardInterrupt

    # Grab credentials
    print("Please enter your email address.")
    sender = input("It must match the mail server you specified: ")
    print("Please input the password for the email address you inputted.")
    passwd = getpass("Don't worry; your password isn't saved anywhere: ")

    try:
        with s.SMTP(smtp_servers[choice], TLS) as server:
            server.ehlo()
            server.starttls()
            server.login(sender, passwd)

            for recipient, mailstr in zip(emails, mailstrs):
                to_send = message + mailstr
                print(f"\nSending email to {recipient} from {sender}")
                server.sendmail(sender, recipient, to_send)

    except s.SMTPAuthenticationError:
        print(errstr)
        raise EOFError
