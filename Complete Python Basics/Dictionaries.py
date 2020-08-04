
# A dictionary is an unordered collection that is changable and indexed
sampleDictionary = {
    # The left side is the key 
    "sample": "vscode",
    "sample2": "jetbrains IDE"

}
print(sampleDictionary)
# Asigns the sampleDictionary key to a varible 
temp = sampleDictionary["sample"]
print(temp)
# Gets the value of sample 2 
temp = sampleDictionary.get("sample2")
print(temp)
# Changes the value of sample to eclipse
sampleDictionary["sample"] = "eclipse"
print(sampleDictionary)

# Prints every single key in dictionary
for x in sampleDictionary:
    print(x)

# Prints all the values in the dictionary
for i in sampleDictionary:
    print(sampleDictionary[i])

# Prints the values using .values 
for h in sampleDictionary.values():
    print(h+ ' example 2')

# Getting both key and values using .items()
for (i,k) in sampleDictionary.items():
    print(i,k)

# Checks if the sample key is in the dictionary
if "sample" in sampleDictionary:
        print('yes')

 # Prints the length of the dictionary
print(len(sampleDictionary))

# Adding items to the dictionary
sampleDictionary["coding language"] = "python"
print(sampleDictionary.values())

# Removing items from the dictionary
sampleDictionary.pop("sample")
print(sampleDictionary)

sampleDictionary["temp"] = "temp1"
print(sampleDictionary)

# popitem() removes most recent inserted item
sampleDictionary.popitem()
print(sampleDictionary)

# del removes the specified key 
del sampleDictionary["sample2"]
print(sampleDictionary)