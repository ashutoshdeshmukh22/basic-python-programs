# Using re.search() + strptime()
import re
from datetime import datetime
test_str = "Ashutosh deshmukh at 2022-06-17"
print("The original string is : " + str(test_str))
match_str = re.search(r'\d{4}-\d{2}-\d{2}', test_str)
res = datetime.strptime(match_str.group(), '%Y-%m-%d').date()
print("Computed date : " + str(res))
