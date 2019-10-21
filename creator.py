# Author: Nate Browne

from adder import *
from strings import bp
from typing import Dict

ParsedRowDict = Dict[str, str]

def create_course_string(dct: ParsedRowDict, quarter: str) -> str:
  '''This function creates the full course email string for a given tutor.

Params:
  dct: First argument. Dictionary of all of the relevant information for the current tutor.
  quarter: Second argument. The current quarter we are in.

Returns:
  String representing the current user's preferences.
  '''
  out = []
  out.append(("-" * 106) + "\n")
  name = dct['name'].split(',')[1] + ' ' + dct['name'].split(',')[0]

  out.append(bp.format(nm=name, qrtr=quarter))
  out.append("Your primary role for {} is: {}\n".format(quarter, dct['role']))

  # Add in corresponding sections of the email using helper functions from adder
  add_attendance(dct, out)
  add_hours_portion(dct, out)
  add_ticket_portion(dct, out)
  out.append("\n")
  add_piazza_portion(dct, out)
  out.append("\n")
  add_maillist_portion(dct, out)
  out.append("\n")
  add_grading_portion(dct, out)
  out.append("\n")
  add_invites_portion(dct, out)
  out.append("\n")

  return ''.join(out)
