import random
low = 1
high = 50
# low = int(input("Enter the lowest number in the range: "))
# high = int(input("Enter the highest number in the range: "))

currect_answer = random.randrange(low, high+1)

for i in range(5):
    i = int(input("guess the number between {}and {}: ".format(low, high)))
    if i< currect_answer:
        print("Correct answer is greater!")
    elif i> currect_answer:
        print("Correct answer is smaller! ")
    else:
        print("Congatulations! your answer is correct")
        break
else:
    print(" you lose! Will show!")