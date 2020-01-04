# Author: Nate Browne

import adder as ad
from strings import bp
from typing import Dict

ParsedRowDict = Dict[str, str]


def create_course_string(dct: ParsedRowDict, quarter: str) -> str:
    '''This function creates the full course email string for a given tutor.

    Params:
        dct: First argument. Dictionary of all of the relevant information for
        the current tutor.
        quarter: Second argument. The current quarter we are in.

    Returns:
        String representing the current user's preferences.
    '''
    out = []
    out.append(("-" * 106) + "\n")
    name = dct['name'].split(',')[1] + ' ' + dct['name'].split(',')[0]

    out.append(bp.format(nm=name, qrtr=quarter))
    prm_rl = f'Your role(s) for {quarter} is/are: {dct["role"]}.\n'
    out.append(prm_rl)

    # Add in corresponding sections of the email using helper functions from
    # adder
    ad.add_attendance(dct, out)
    ad.add_hours_portion(dct, out)
    ad.add_ticket_portion(dct, out)
    out.append("\n")
    ad.add_piazza_portion(dct, out)
    out.append("\n")
    ad.add_maillist_portion(dct, out)
    out.append("\n")
    ad.add_grading_portion(dct, out)
    out.append("\n")
    ad.add_invites_portion(dct, out)
    out.append("\n")

    return ''.join(out)
