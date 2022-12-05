with open('2022/data/day2.txt') as f:
    data = [s.strip().split(' ') for s in f.readlines()]

# A/X: rock 
# B/Y: paper
# C/Z: scizzors

# outcome matrix (me perspective)
# outcomes[opp][me]
# rock (0), paper (1), then scizzors (2)
# win 6, lose 0, draw 3
outcomes = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]

# loop through and calculate each round score
scores = []
for game in data:
    opp = game[0]
    my_play = game[1]

    if my_play == 'X':
        shape_score = 1
    if my_play == 'Y':
        shape_score = 2
    if my_play == 'Z':
        shape_score = 3 

    iopp = ['A', 'B', 'C'].index(opp)
    ime = ['X', 'Y', 'Z'].index(my_play)
    outcome = outcomes[iopp][ime]

    score = shape_score + outcome
    scores.append(score)

print('part1', sum(scores))

# part 2

# x - lose
# y - draw
# z - win

scores = []
for game in data:
    opp = game[0]
    iopp = ['A', 'B', 'C'].index(opp)

    outcome = game[1]

    outcomes_to_oscore = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }

    plays = ['X', 'Y', 'Z']

    relevant_outcome_row = outcomes[iopp]
    outcome_score = outcomes_to_oscore.get(outcome)
    my_play_index = outcomes[iopp].index(outcome_score)
    my_play = plays[my_play_index]

    #print(iopp, opp, relevant_outcome_row, outcome, my_play_index, my_play)

    if my_play == 'X':
        shape_score = 1
    if my_play == 'Y':
        shape_score = 2
    if my_play == 'Z':
        shape_score = 3 

    my_play_index = ['X', 'Y', 'Z'].index(my_play)
    outcome = outcomes[iopp][my_play_index]

    score = shape_score + outcome_score
    scores.append(score)

print('part2', sum(scores))