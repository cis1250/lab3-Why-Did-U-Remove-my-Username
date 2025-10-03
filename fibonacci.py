print('User input: ', end='')
amount = input()

while not amount.isdigit() or int(amount) < 0:
    print('Expected output: Please enter a positive integer.')
    print()
    print('User input: ', end='')
    amount = input()

amount = int(amount)
print('Expected output: ', end='')
num_one = 0
num_two = 1
for i in range(amount):
    print(num_one, end='')
    if i < amount - 1:
        print(' ', end='')
    temp = num_one
    num_one = num_two
   num_two = temp + num_two

print() 

print("have a nice day :)")

#pasted from command prompt
