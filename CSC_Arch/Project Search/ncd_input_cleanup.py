"""Utility file to cleanup the input copied from ncdcommunity's github page for better representation."""
import re

f = open("ncd_input.txt", "r")
substring = ""
for x in f:
    # parse the name of the sensor
    if "ncd.io" in x and '"' in x:
        name_subsection = re.search("\"(.*)\"", x).group(1)
        name_subsection = name_subsection[7:]
        print(name_subsection)
        print("DATA")
        continue
    # parse the data size
    if "uint8_t data" in x:
        data_size = int(re.search("\[(.*)\]", x).group(1))
    if '"' in x:
        section = re.search("\"(.*)\"", x).group(1)
        if "ADC value" in x:
            continue
        if section[0] == " ":
            continue
        if section[-1] == ":":
            section = section[0:-1]
        substring += section
        if "println" in x:
            continue
        # if "\\n" in substring:
        #     substring = substring[:-2]
        # if substring == "ADC value":
        #     substring = ""
        #     continue
        print(substring)
        substring = ""

print("")
print("Total Data")
print(data_size)
print("Total transmission")
print("Remainder used for verification and as metadata")
