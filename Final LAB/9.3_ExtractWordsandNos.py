import re
test_string = "Ashutosh Deshmukh,    is a @# Full Stack developer and his DOB is 22-04-2000.!!!"
print("The original string is : " + test_string)
res = re.findall(r'\w+', test_string)
print("The list of words is : " + str(res))
