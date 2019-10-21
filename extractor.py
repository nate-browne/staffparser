# Author: Nate Browne

from typing import Dict, List

CSVRow = List[str]
ParsedRowDict = Dict[str, str]

def extract_data(row: CSVRow, data: ParsedRowDict) -> None:
  '''Grabs relevant information from the current csv row. Note that the numbers
are hardcoded in for the Spring 2019 file and need to be updated every quarter
for the new file to make sure the positions still line up.

Args:
  row: First parameter. Current row of the CSV/TSV file being parsed.
  data: Second parameter. Populated with relevant fields of the CSV/TSV

Returns:
  None. Data is updated as an output parameter.
  '''
  data['name'] = row[3]
  data['role'] = row[7]
  data['attending'] = row[10]
  data['total_hours'] = row[11]
  data['12_hours'] = row[12]
  data['15l_hours'] = row[13]
  data['110_hours'] = row[14]
  data['location'] = row[16]
  data['12_grading'] = row[17]
  data['15l_grading'] = row[18]
  data['12_account'] = row[20]
  data['15l_account'] = row[21]
  data['110_account'] = row[22]
  data['12_piazza'] = row[23]
  data['15l_piazza'] = row[24]
  data['110_piazza'] = row[25]
  data['12_autograder'] = row[26]
  data['15l_autograder'] = row[27]
  data['110_autograder'] = row[28]
  data['12_mail_list'] = row[29]
  data['15l_mail_list'] = row[30]
  data['110_mail_list'] = row[31]
  data['12_events'] = row[32]
  data['15l_events'] = row[33]
  data['110_events'] = row[34]
