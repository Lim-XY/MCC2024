from time import perf_counter
import math

start_time = perf_counter()

TASK_NAME = 'ExplodingArrow'
TASK_NUM = 8

with open(f'{TASK_NAME}/{TASK_NUM}.txt', 'r') as f:
    info, TARGETS = f.read().split('\n')

TARGETS = [ int(hp) for hp in TARGETS.split(' ') ]
TOTAL_TARGETS, MULTIPLIER, TOTAL_ARROWS = [ int(i) for i in info.split(' ') ]

def test_power(power):
    first_target_index = 0
    arrows_left = TOTAL_ARROWS

    targets = TARGETS.copy()

    first_target_index = 0
    base_dmg = MULTIPLIER*power

    while first_target_index < len(targets):
        first_target_hp = targets[first_target_index]
        if first_target_hp <= 0:
            first_target_index += 1
            continue

        arrows_to_kill_1st_target = -(first_target_hp // -base_dmg)

        if arrows_to_kill_1st_target > arrows_left:
            return False

        for j in range(first_target_index, len(targets)):
            distance = j - first_target_index
            damage = (MULTIPLIER*power) - (distance**2)

            if damage <= 0:
                break
            targets[first_target_index + distance] -= damage*arrows_to_kill_1st_target
            if targets[first_target_index + distance] < 0:
                targets[first_target_index + distance] = 0

        arrows_left -= arrows_to_kill_1st_target
        if arrows_left == 0:
            break

    # print(targets)
    return max(targets) <= 0

# these values don't really work btw I just add some random multiply and divide for different tasks
min_multiplier = int(max(TARGETS) / MULTIPLIER / TOTAL_ARROWS) // 4
max_multiplier = ((max(TARGETS) + len(TARGETS)**2) * TOTAL_ARROWS)

print(min_multiplier, max_multiplier)

lowest_working, highest_fail = None, None
min_power, max_power = min_multiplier, max_multiplier
final_ans = None
prev_power_test = None

counter = 0

while 1:
    if max_power == min_power:
        break

    power = (min_power + max_power) // 2
    can_destroy = test_power(power)

    counter += 1
    if counter % 5 == 0:
        print(f'[{min_power}~{max_power}] Testing {power} --> {can_destroy}')

    if power == prev_power_test:
        break
    prev_power_test = power

    if can_destroy: # try lower
        if lowest_working is None or power < lowest_working:
            lowest_working = power
        max_power = power - 1
    else: # needs to be higher
        if highest_fail is None or power > highest_fail:
            highest_fail = power
        min_power = power + 1

reduce = 1
if test_power(lowest_working - 1):
    print('Lowest working is not the answer')
    while reduce < lowest_working:
        if not test_power(lowest_working - reduce):
            break
        reduce += 1

print(lowest_working - reduce + 1)
    
print(f'Completed in Task {TASK_NUM} in {round(perf_counter() - start_time, 5)}s.')
