from time import perf_counter

start_time = perf_counter()

TASK_NAME = 'MagicalOrbs'
TASK_NUM = '7'

with open(f'{TASK_NAME}/{TASK_NUM}.txt', 'r') as f:
    DATA = f.read().split('\n')

TEST_CASES = int(DATA.pop(0))

def apply_modulo(ans):
    return str(ans % (10**9 + 7))

output = []

for i in range(TEST_CASES):
    total_orbs = DATA[i*2]
    powers = [ int(p) for p in DATA[i*2 + 1].split(' ') ]
    powers.sort(reverse=True)

    final_orb = 0
    for p in powers:
        final_orb = final_orb*2 + p

    output.append(apply_modulo(final_orb))


with open('output.txt', 'w') as f:
    f.write('\n'.join(output))

print('\n'.join(output))
print(f'Completed in Task {TASK_NUM} in {round(perf_counter() - start_time, 5)}s.')