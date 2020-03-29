# Write your code here :-)
print("How many exercises will you perform per card?")

exercises = int(input())

for i in range (15):
    print (i, i*4)
    i += (i*4)

print((i*4)*exercises)
