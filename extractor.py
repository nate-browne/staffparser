# Author: Nate Browne

from typing import Dict, List

CSVRow = List[str]
ParsedRowDict = Dict[str, str]


def extract_data(row: CSVRow, data: ParsedRowDict) -> None:
    '''Grabs relevant information from the current csv row. Note that the numbers
    are hardcoded in for the Spring 2019 file and need to be updated every
    quarter for the new file to make sure the positions still line up.

    Args:
        row: First parameter. Current row of the CSV/TSV file being parsed.
        data: Second parameter. Populated with relevant fields of the CSV/TSV

    Returns:
        None. Data is updated as an output parameter.
    '''
    data['name'] = row[3]
    data['role'] = row[9]
    data['attending'] = row[12]
    data['total_hours'] = row[13]
    data['12_hours'] = row[14]
    data['15l_hours'] = row[15]
    # data['110_hours'] = row[14]
    # data['location'] = row[16]
    data['12_grading'] = row[19]
    data['15l_grading'] = row[20]
    data['12_account'] = row[22]
    data['15l_account'] = row[23]
    # data['110_account'] = row[22]
    data['12_piazza'] = row[25]
    data['15l_piazza'] = row[26]
    # data['110_piazza'] = row[25]
    data['12_autograder'] = row[28]
    data['15l_autograder'] = row[29]
    # data['110_autograder'] = row[28]
    data['12_mail_list'] = row[31]
    data['15l_mail_list'] = row[32]
    # data['110_mail_list'] = row[31]
    data['12_events'] = row[34]
    data['15l_events'] = row[35]
    # data['110_events'] = row[34]


def extract_emails(row: CSVRow, mails: List[str]) -> None:
    '''Pulls out the email addresses of the tutors.

    Args:
        row: First parameter. Current row of the CSV/TSV file being parsed.
        mails: Second parameter. Populated with the email address of the
        current row.

    Returns:
        None. mails is updated as an output parameter.
    '''
    mails.append(row[7])
