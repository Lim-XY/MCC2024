def transform(string, k):
    for _ in range(k):
        new_string = ''
        for index in range(len(string)):
            new_string += string[index]
            if index < len(string) - 1:
                new_string += str(int(string[index]) ^ int(string[index+1]))

        string = new_string

    return string

def get_all_sublists(string):
    length = len(string)
    return [string[i:j+1] for i in range(length) for j in range(i,length)]

def get_beauty(string):
    b = 0
    for index in range(len(string) - 1):
        left = string[index]
        right = string[index + 1]

        if left == right:
            b += 1

    return b

STRING = '010101111101'
K = 4

# 4 - 01101101101101101 // b: 0, 3, 6, 9, 12
# 3 - 011011011 // b: 0, 3, 6

# "10"
# 4 - 10110110110110110 // b: 1, 4, 7, 10, 13
# 3 - 110110110 // b: 2, 5 
total_beauty = 0

print(transform(STRING, K))

for sublist in get_all_sublists(STRING):
    t = transform(sublist, K)
    total_beauty += get_beauty(t)

print(total_beauty)
