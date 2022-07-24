import pickle
mydictionary = {1: 'Ashutosh', 2: 'Swanand', 3: 'Vishal'}
file1 = open('mt.dat', 'wb')
pickle.dump(mydictionary, file1)
file1.close()
print("File saved successfully")
file2 = open('mt.dat', 'rb')
mydictionary2 = pickle.load(file2)
file2.close()
print("File retrived successfully")
print(mydictionary2)
