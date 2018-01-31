"""
Extract key data from HL7 ballot comment amalgamated spreadsheet for condensed presentation

Current target file location: /Users/jrhoads/OneDrive - Philips/HL7_Philips/2018-01WGMNewOrleans/ballotcomments_FHIR_IG_PoCD_R1_I1_2018JAN.xls

"""
import os.path
from tablib import Dataset


def read_spreadsheet(file_name):
    file_exists = os.path.exists(file_name)
    if not file_exists:
        print("file not found: ", file_name)
    data = Dataset().load(open(file_name, "rb").read())
    print(data[0])


if __name__ == "__main__":
    target_file = "/Users/jrhoads/OneDrive - Philips/HL7_Philips/2018-01WGMNewOrleans/ballotcomments_FHIR_IG_PoCD_R1_I1_2018JAN.xls"
    read_spreadsheet(target_file)
