n = int(raw_input("how many numbers do you need?\n"))

output = [1]
output.append(1)

while(len(output) < n - 1):
    output.append(output[-1] + output[-2])

print output
