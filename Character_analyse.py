word = str(input("Write a series of characters: "))

A = len(word)

if A==0 :
    print("You didn't write anything.")

print("Your word contains "+ str(A) + " characters")

print("The first character is: << " + str(word[0]) + " >> and the last character is: << " + str(word[-1]) + " >>")
