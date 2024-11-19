# this code is super messy because I edited it a lot and
# made tons of changes to debug/try to speed it up, so
# some parts are now kinda unecessary such as most of 
# the get_transformation_parts function

from time import perf_counter

start_time = perf_counter()

TASK_NAME = 'XORTheString'
TASK_NUM = 7

with open(f'{TASK_NAME}/{TASK_NUM}.txt', 'r') as f:
    info, STRING = f.read().split('\n')

LENGTH, K = [ int(i) for i in info.split(' ')]

def get_range_len(start, stop, step):
    return (stop - start - 1) // step + 1

def get_transformation_parts(k):
    odd = k % 2

    start = {
        '00': '0',
        '11': '0' if odd else '1',
        '01': '1',
        '10': str(odd)
    }

    end = {
        '00': '0',
        '11': '0' if odd else '1',
        '01': str(odd),
        '10': '1'
    }

    parts = {}

    for part, beautiful_indexes in start.items():
        parts[part] = {
            # 'beautiful_indexes': beautiful_indexes,
            'start': start[part],
            'end': end[part]
        }

    return parts

def get_sublists_containing_index(index):
    original_length = len(STRING)
    before = index + 1
    after = original_length - index - 1

    return ((before * after))

transformation_parts = get_transformation_parts(K)

b_indexes = []
beautiful_transformed_indexes = {}

for index in range(len(STRING) - 1):
    left = STRING[index]
    right = STRING[index + 1]

    if K == 0 and left == right:
        b_indexes.append(index)
        continue

    transformed_middle = transformation_parts[left+right]
    beautiful_transformed_indexes[index] = left+right

    if left == transformed_middle['start']:
        b_indexes.append(index)

total_beauty = 0

c, t = 0, len(b_indexes)
for b_index in b_indexes:
    total_beauty += get_sublists_containing_index(b_index)

final_length = pow(2, K, 998244353) - 1 # doesn't work for all tasks :(
odd = K % 2

multipliers = {
    '00': final_length,
    '11': get_range_len(2-odd, final_length, 3),
    '01': get_range_len(0, final_length, 3),
    '10': get_range_len(1+odd, final_length, 3)
}

for b_index, pattern in beautiful_transformed_indexes.items():
    total_beauty += multipliers[pattern] * get_sublists_containing_index(b_index)

print(total_beauty % 998244353)
print(f'Completed in Task {TASK_NUM} in {round(perf_counter() - start_time, 5)}s.')
