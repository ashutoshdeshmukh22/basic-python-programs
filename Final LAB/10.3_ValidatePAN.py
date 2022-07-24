import re


def isValidPanCardNo(panCardNo):
    regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
    p = re.compile(regex)
    if(panCardNo == None):
        return False
    if(re.search(p, panCardNo) and
       len(panCardNo) == 10):
        return True
    else:
        return False


str1 = "BNZAA2318J"
print(isValidPanCardNo(str1))
str2 = "23ZAABN18J"
print(isValidPanCardNo(str2))
str3 = "BNZAA2318JM"
print(isValidPanCardNo(str3))
