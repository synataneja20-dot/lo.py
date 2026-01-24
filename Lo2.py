#Write a program to reverse the string entered by the user.
# Input a word or sentance
string = input("Enter your own string: ")


string2 = ('')
# loop for printing in reverse
for i in string:
    string2 = i + string2

print("\n The Original String: ", string)
print("\n The Reversed String: ", string2)