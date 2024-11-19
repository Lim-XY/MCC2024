from time import perf_counter

start_time = perf_counter()

TASK_NAME = 'Gifts'
TASK_NUM = 1

with open(f'{TASK_NAME}/{TASK_NUM}.txt', 'r') as f:
    data = f.read().split('\n')

info, TIERS = data[0], list(map(int, data[1].split(' ')))
TOTAL_GUESTS, TOTAL_GIFTS = map(int, info.split(' '))

tiers_map = {}

for index in range(TOTAL_GUESTS):
    tier = TIERS[index]

    if not tier in tiers_map:
        tiers_map[tier] = []

    tiers_map[tier].append(index)

# print(tiers_map)

tiers_in_order = sorted(tiers_map.keys())
remaining_gifts = TOTAL_GIFTS
output = [ '0' for _ in range(TOTAL_GUESTS) ]

for tier in tiers_in_order:
    for guest_index in tiers_map[tier]:
        if remaining_gifts == 0:
            break
        output[guest_index] = '1'
        remaining_gifts -= 1

    if remaining_gifts == 0:
        break


with open('output.txt', 'w') as f:
    f.write(' '.join(output))

print(f'Completed in Task {TASK_NUM} in {round(perf_counter() - start_time, 5)}s.')

