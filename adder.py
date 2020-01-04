# Author: Nate Browne

from strings import lab_str, auto_str, piazza, mail
from strings import accounts, grading
from strings import grading12
from strings import grading15
# from strings import grading110
from typing import Dict, List

MessageString = List[str]
ParsedRowDict = Dict[str, str]


def add_attendance(dct: ParsedRowDict, out: MessageString) -> None:
    '''Adds the course attendance portion of the email to the MessageString.

    Args:
        dct: the first parameter.
        out: the second parameter.

    Returns:
        None. Out is updated as an output parameter to the function.
    '''
    if dct['attending'] != '':
        tmp = dct['attending']
        course = tmp.split('-')[0]
        tp = tmp.split('-')[1]
        out.append(f"You are attending lecture for {course} for {tp}\n")


def add_hours_portion(dct: ParsedRowDict, out: MessageString) -> None:
    '''Adds the open lab hours portion of the email to the MessageString.

    Args:
        dct: the first parameter.
        out: the second parameter.

    Returns:
        None. Out is updated as an output parameter to the function.
    '''
    if dct['total_hours'] != '':
        hrs = f'You are holding {dct["total_hours"]} open lab hours per week.'
        if 'location' in dct:
            loc = dct['location']
        else:
            loc = 'B250'
        lb = f'\nYou will hold your open lab hours in {loc}.\n\n'
        out.append(hrs + "\n\n")
        if dct['12_hours'] != '':
            out.append(lab_str.format('CSE 12', dct['12_hours']))
        if dct['15l_hours'] != '':
            out.append(lab_str.format('CSE 15L', dct['15l_hours']))
        # if dct['110_hours'] != '':
        #     out.append(lab_str.format('CSE 110', dct['110_hours']))
        out.append(lb)
    else:
        out.append("You are not holding open lab hours.\n\n")


def add_ticket_portion(dct: ParsedRowDict, out: MessageString) -> None:
    '''Adds the Autograder ticket answering portion of the email to the
    MessageString.

    Args:
        dct: the first parameter.
        out: the second parameter.

    Returns:
        None. Out is updated as an output parameter to the function.
    '''
    if dct['12_autograder'] != '':
        out.append(auto_str.format("CSE 12", "yes"))
    else:
        out.append(auto_str.format("CSE 12", "no"))
    if dct['15l_autograder'] != '':
        out.append(auto_str.format("CSE 15L", "yes"))
    else:
        out.append(auto_str.format("CSE 15L", "no"))
    # if dct['110_autograder'] != '':
    #     out.append(auto_str.format("CSE 110", "yes"))
    # else:
    #     out.append(auto_str.format("CSE 110", "no"))


def add_piazza_portion(dct: ParsedRowDict, out: MessageString) -> None:
    '''Adds the Piazza membership portion of the email to the MessageString.

    Args:
        dct: the first parameter.
        out: the second parameter.

    Returns:
        None. Out is updated as an output parameter to the function.
    '''
    if dct['12_piazza'] != '':
        out.append(piazza.format("CSE 12", "yes"))
    else:
        out.append(piazza.format("CSE 12", "no"))
    if dct['15l_piazza'] != '':
        out.append(piazza.format("CSE 15L", "yes"))
    else:
        out.append(piazza.format("CSE 15L", "no"))
    # if dct['110_piazza'] != '':
    #     out.append(piazza.format("CSE 110", "yes"))
    # else:
    #     out.append(piazza.format("CSE 110", "no"))


def add_maillist_portion(dct: ParsedRowDict, out: MessageString) -> None:
    '''Adds the mailing list membership portion of the email to the MessageString.

    Args:
        dct: the first parameter.
        out: the second parameter.

    Returns:
        None. Out is updated as an output parameter to the function.
    '''
    if dct['12_mail_list'] != '':
        out.append(mail.format("CSE 12", "yes"))
    else:
        out.append(mail.format("CSE 12", "no"))
    if dct['15l_mail_list'] != '':
        out.append(mail.format("CSE 15L", "yes"))
    else:
        out.append(mail.format("CSE 15L", "no"))
    # if dct['110_mail_list'] != '':
    #     out.append(mail.format("CSE 110", "yes"))
    # else:
    #     out.append(mail.format("CSE 110", "no"))


def add_accounts_portion(dct: ParsedRowDict, out: MessageString) -> None:
    '''Adds the ieng6 TA account portion of the email to the MessageString.

    Args:
        dct: the first parameter.
        out: the second parameter.

    Returns:
        None. Out is updated as an output parameter to the function.
    '''
    if dct['12_account'] != '':
        out.append(accounts.format("CSE 12", "yes"))
    else:
        out.append(accounts.format("CSE 12", "no"))
    if dct['15l_account'] != '':
        out.append(accounts.format("CSE 15L", "yes"))
    else:
        out.append(accounts.format("CSE 15L", "no"))
    # if dct['110_account'] != '':
    #     out.append(accounts.format("CSE 110", "yes"))
    # else:
    #     out.append(accounts.format("CSE 110", "no"))


def add_grading_portion(dct: ParsedRowDict, out: MessageString) -> None:
    '''Adds the PA grading portion of the email to the MessageString.

    Args:
        dct: the first parameter.
        out: the second parameter.

    Returns:
        None. Out is updated as an output parameter to the function.
    '''
    if dct['12_grading'] != '':
        out.append(grading.format("CSE 12", "yes"))
    else:
        out.append(grading.format("CSE 12", "no"))
    if dct['15l_grading'] != '':
        out.append(grading.format("CSE 15L", "yes"))
    else:
        out.append(grading.format("CSE 15L", "no"))


def add_invites_portion(dct: ParsedRowDict, out: MessageString) -> None:
    '''Adds the event attendance portion of the email to the MessageString. Events
    include quiz grading, exam grading, project grading, etc.

    Args:
        dct: the first parameter.
        out: the second parameter.

    Returns:
        None. Out is updated as an output parameter to the function.
    '''
    if dct['12_events'] != '':
        out.append(grading12.format("yes"))
    else:
        out.append(grading12.format("no"))
    if dct['15l_events'] != '':
        out.append(grading15.format("yes"))
    else:
        out.append(grading15.format("no"))
    # if dct['110_events'] != '':
    #     out.append(grading110.format("yes"))
    # else:
    #     out.append(grading110.format("no"))
