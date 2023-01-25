import sys

message = input()

binary = ''.join(format(ord(c), 'b').zfill(7) for c in message)
output = ''
count = 0

for i in range(len(binary)):
    if i == 0 or binary[i] != binary[i-1]:
        output += '0' if binary[i] == '1' else '00'
        output += ' '
        count = 1
    else:
        count += 1
    if i == len(binary) - 1 or binary[i] != binary[i+1]:
        output += '0' * count
        if i != len(binary) - 1:
            output += ' '

# Write an answer using print
print(output)
