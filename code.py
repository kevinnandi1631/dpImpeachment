mpigsVotes = 291

legalthreshold = input("Hey Assembly Speaker, Enter the results: ")
number = int(legalthreshold)

try:
    if number > mpigsVotes:
        print("The DP has been impeached ")

    else:
        print("The impeachment motion fails")

except ValueError:
    print("Please Enter a valid number")