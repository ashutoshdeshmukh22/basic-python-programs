vcount = 0
ccount = 0
blank = 0

str = "My Name is Ashutosh"

# Converting entire string to lower case to reduce the comparisons
str = str.lower()
for i in range(0, len(str)):
    # Checks whether a character is a vowel
    if str[i] in ('a', "e", "i", "o", "u"):
        vcount = vcount + 1
    elif (str[i] >= 'a' and str[i] <= 'z'):
        ccount = ccount + 1
    elif str[i] in (' '):
        blank = blank + 1

print("Total number of vowel, consonant and Blanks are")
print("Vowels Count : ", vcount)
print("Conconent Count : ", ccount)
print("Blanks Count : ", blank)
