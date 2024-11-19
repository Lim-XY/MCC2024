from time import perf_counter

start_time = perf_counter()

TASK_NAME = 'CornerCover'
TASK_NUM = 5

with open(f'{TASK_NAME}/{TASK_NUM}.txt', 'r') as f:
    INPUT = f.read().split('\n')
TEST_CASES = int(INPUT.pop(0))
output = []

def solve(line):
    n, m, A, B = map(int, line.split(' '))

    # check if AxB and BxA is too big to fit
    if (A > n or B > m) and (B > n or A > m):
        return False
    
    # if A or B are equal to the side lengths, they can cover 2 corners.
    return ((A == n or B == n) or (A == m or B == m))

for i in range(TEST_CASES):
    output.append('YES' if solve(INPUT[i]) else 'NO')

with open('output.txt', 'w') as f:
    f.write('\n'.join(output))

print(f'Completed in {round(perf_counter() - start_time, 5)}s.')