from time import perf_counter

start_time = perf_counter()

TASK_NAME = 'SimpleGame'
TASK_NUM = 3

with open(f'{TASK_NAME}/{TASK_NUM}.txt', 'r') as f:
    PAIRS = f.read().split('\n')

PAIRS = [ list(map(int, pair.split(' '))) for pair in PAIRS[1:] ]

best_options = sorted(PAIRS, key=lambda k: sum(k), reverse=True)

score = {
    0: 0, # X (Evirir)
    1: 0  # Y (Rhae)
}

for i, pair in enumerate(best_options):
    player = i % 2
    score[player] += pair[player]

print(score[0] - score[1])

print(f'Completed in Task {TASK_NUM} in {round(perf_counter() - start_time, 5)}s.')