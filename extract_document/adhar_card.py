import re

# extract labels from aadhar image
def get_aadhar_text(temp):
    imp = {}

    # reverse list to parse through it starting from the aadhar number
    temp = temp[:: -1]
    # parse through the list
    for idx in range(len(temp)):

        try:
            # if string similar to aadhar number is found, use it as a hook to find other details
            if re.search(r"[0-9]{4}\s[0-9]{4}\s[0-9]{4}", temp[idx]):
                try:
                    imp['Aadhar No'] = re.findall(r"[0-9]{4}\s[0-9]{4}\s[0-9]{4}", temp[idx])[0]
                except Exception as _:
                    imp['Aadhar No'] = "Not Found"
                if temp[idx + 1].endswith("Female") or temp[idx + 1].endswith("FEMALE"):
                    imp["Gender"] = "Female"
                elif temp[idx + 1].endswith("Male") or temp[idx + 1].endswith("MALE"):
                    imp["Gender"] = "Male"
                elif temp[idx + 2].endswith("Female") or temp[idx + 2].endswith("FEMALE"):
                    imp["Gender"] = "Female"
                elif temp[idx + 2].endswith("Male") or temp[idx + 2].endswith("MALE"):
                    imp["Gender"] = "Male"
                elif temp[idx + 3].endswith("Female") or temp[idx + 3].endswith("FEMALE"):
                    imp["Gender"] = "Female"
                elif temp[idx + 3].endswith("Male") or temp[idx + 3].endswith("MALE"):
                    imp["Gender"] = "Male"

            elif re.search(r"[0-9]{2}\-|/[0-9]{2}\-|/[0-9]{4}", temp[idx]):
                # if string similar to date is found, use it as a hook to find other details
                try:
                    imp["Date of Birth"] = re.findall(r"[0-9]{2}\-[0-9]{2}\-[0-9]{4}", temp[idx])[0]
                except Exception as _:
                    imp["Date of Birth"] = re.findall(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", temp[idx])[0]
                imp["Name"] = temp[idx + 1]

            elif "Year of Birth" in temp[idx]:
                # handle variation of 'Year of Birth' in place of DOB
                try:
                    imp["Year of Birth"] = re.findall(r"[0-9]{4}", temp[idx])[0]
                except Exception as _:
                    imp["Year of Birth"] = "Not Found"
                imp["Name"] = temp[idx + 1]

            elif re.search(r"[0-9]{4}", temp[idx]):
                # handle exception if Year of Birth is not found but string similar to year is found
                try:
                    imp["Year of Birth"] = re.findall(r"[0-9]{4}", temp[idx])[0]
                except Exception as _:
                    imp["Year of Birth"] = "Not Found"
                imp["Name"] = temp[idx + 1]

            elif len(temp[idx].split(' ')) > 2:
                # following text will be name, ignore line if it includes GOVERNMENT OF INDIA
                if 'GOVERNMENT' in temp[idx] or 'OF' in temp[idx] or 'INDIA' in temp[idx]:
                    continue
                else:
                    imp["Name"] = temp[idx]
        except Exception as _:
            pass
    return imp
