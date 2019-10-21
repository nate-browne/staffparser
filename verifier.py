# Author: Nate Browne

from strings import validate_domain, email_err_str

# Set of valid email domains
domains = set()
domains.add("gmail.com")
domains.add("yahoo.com")
domains.add("outlook.com")
domains.add("ucsd.edu")
domains.add("cs.ucsd.edu")
domains.add("eng.ucsd.edu")


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

  # First, check that the email has the @ sign
  if '@' not in email:
    valid = False

  # Make sure there is something after the @ sign
  check = email.split('@')
  if len(check) == 1 or check[1] == '':
    valid = False
  else:

    # If the domain given isn't in the set, make sure the user really does want
    # to send the email to that domain
    if check[1] not in domains:
      double_check = input(validate_domain.format(check[1]))

      if double_check.upper() != 'Y':
        raise KeyboardInterrupt

  if not valid:
    print(email_err_str.format(email))
    raise KeyboardInterrupt
