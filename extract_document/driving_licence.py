import re

# extract labels from licence image
def get_licence_text(details):
    imp = {}

    # loop through all the details found line wise
    for idx in range(len(details)):

        try:
            # if DL No is found save it
            if 'DL No' in details[idx]:
                try:
                    imp["DL NO"] = details[idx].split('DL No')[-1].strip()
                except Exception as _:
                    imp["DL NO"] = "Not Found"

            # if dob is found, use it as a hook and try finding other details relative to it
            elif details[idx].startswith('DOB'):
                # extract only dob from the text
                dob = re.findall(r"([0-9]{2}\-[0-9]{2}\-[0-9]{4})", details[idx].split(' ', 1)[-1])[0]

                imp["Date of Birth"] = dob

                # next line is always name and father's name
                imp["Name"] = details[idx + 1].split(' ', 1)[-1].strip()

                try:
                    # split it from 'of' to get Father's Name
                    imp["Father's Name"] = details[idx + 2].split('of', 1)[1].strip()

                except Exception as _:
                    # handle exception if O is capital in 'of'
                    imp["Father's Name"] = details[idx + 2].split('Of', 1)[1].strip()

                i = 4
                # split next line from Add for address
                address = details[idx + 3].split('Add', 1)[1].strip()

                # keep appending until PIN code is found or address is of more than 4 lines
                while not details[idx + i].startswith('PIN') and i < 8:
                    if details[idx + i].isupper() != True:
                        i += 1
                        continue
                    address += ' ' + details[idx + i]

                    i += 1
                imp["Address"] = address
                try:
                    # get only pin code from the string
                    imp["Pin Code"] = re.findall(r"([0-9]{6})", details[idx + i].split(' ', 1)[1])[0]
                except Exception as _:
                    pass

                break
            # if name is found, use it as a hook and try finding other details relative to it
            elif details[idx].startswith('Name'):
                # extract only dob from the text
                dob = re.findall(r"([0-9]{2}\-[0-9]{2}\-[0-9]{4})", details[idx - 1].split(' ', 1)[1])[0]
                imp["Date of Birth"] = dob

                imp["Name"] = details[idx][4:].strip()

                # next line is always name and father's name
                try:
                    # split it from 'of' to get Father's Name
                    imp["Father's Name"] = details[idx + 2].split('of', 1)[1].strip()

                except Exception as _:
                    # handle exception if O is capital in 'of'
                    imp["Father's Name"] = details[idx + 2].split('Of', 1)[1].strip()

                i = 3
                # split next line from Add for address
                address = details[idx + 2].split('Add', 1)[1].strip()

                # keep appending until PIN code is found or address is of more than 4 lines
                while not details[idx + i].startswith('PIN') and i < 7:
                    if details[idx + i].isupper() != True:
                        i += 1
                        continue
                    address += ' ' + details[idx + i]

                    i += 1
                imp["Address"] = address
                try:
                    # get only pin code from the string
                    imp["Pin Code"] = re.findall(r"([0-9]{6})", details[idx + i].split(' ', 1)[1])[0]
                except Exception as _:
                    pass

                break
        except Exception as _:
            pass
    return imp
