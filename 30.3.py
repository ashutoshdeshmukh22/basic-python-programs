import re
items = ["example (.com)", "iicmr", "google (.com)", "youtube(.com)"]
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))
