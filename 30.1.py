import re
x ="Hello Aug 2000 is the birthday year of Bhushan"
results = re.findall('(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|Next)[\s.]\d{2,4}',x)
print (results)
