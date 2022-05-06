# use a single for loop to iterate through the two provided strings, 
# and print all of their matching characters (i.e., the characters
# that are the same index and that are equal to each other), each
# on a separate line.

string1 = "aabbcsdw"
string2 = "abbbcsdd"

for idx in range(len(string1)):
    character1 = string1[idx]
    character2 = string2[idx]

    if character1 == character2:
        print(character1)
