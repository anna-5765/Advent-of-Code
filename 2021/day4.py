## Day 4
import numpy as np

## Save input bingo cards to a list using numpy
filepath = '/Users/annaberghoff/Documents/code/AOC2021/day4.txt'
with open(filepath, 'r') as f:
    bingo_text = f.read().split('\n\n')
# print(bingo_text)

## The first entry is the bingo numbers
bingo_numbers = list(map(int, bingo_text[0].split(',')))
# print(bingo_numbers)

## The rest are the bingo cards
bingo_cards = []
for card in bingo_text[1:]:
    rows_strings = card.split('\n')
    rows_ints = [[int(number) for number in row.split()] for row in rows_strings]
    bingo_cards.append(rows_ints)
# print(bingo_cards)

## Track play by creating empty matrix and fill a 1 where the number is called
play_tracker = np.zeros(np.array(bingo_cards).shape, dtype=int)
# print(play_tracker)
# Do I need this back in a list? if so .tolist()

## Play bingo, return the winning card and last number called

def play_bingo(bingo_numbers, bingo_cards, play_tracker):
    for call in bingo_numbers:
        for card_index, card in enumerate(bingo_cards):
            for row_index, row in enumerate(card):
                for col_index, num in enumerate(row):
                    if call == num:
                        # print(card_index, row_index, num_index)
                        play_tracker[card_index][row_index][col_index] = 1
                        win_cond_r = np.sum(play_tracker[card_index, row_index, :])
                        win_cond_c = np.sum(play_tracker[card_index, :, col_index])
                        if win_cond_r== 5 or win_cond_c == 5:
                            return(bingo_cards[card_index], call, play_tracker[card_index])
                        else:
                            continue
                    else:
                        continue
    return None

(win_card, win_call, win_tracker) = play_bingo(bingo_numbers, bingo_cards, play_tracker)
# print(win_card, win_call, win_tracker)

## Guarantee victory against the giant squid (sum of unmarked numbers on winning board * last call)

def calc_score(win_card, win_call, win_tracker):
    unmarked_sum = 0
    for row_index, row in enumerate(win_card):
        for col_index, num in enumerate(row):
            if win_tracker[row_index][col_index] == 0:
                unmarked_sum += num
            else: 
                continue
    
    score = unmarked_sum * win_call
    return(score)

print(calc_score(win_card, win_call, win_tracker))

####### Part 2 #######

# Find the last board that wins

bingo_cards_for_last = bingo_cards
play_tracker_for_last = play_tracker

def play_for_last(bingo_numbers, bingo_cards, play_tracker):
    for call in bingo_numbers:
        for card_index, card in enumerate(bingo_cards):
            for row_index, row in enumerate(card):
                for col_index, num in enumerate(row):
                    if call == num:
                        # print(card_index, row_index, num_index)
                        play_tracker[card_index][row_index][col_index] = 1
                        win_cond_r = np.sum(play_tracker[card_index, row_index, :])
                        win_cond_c = np.sum(play_tracker[card_index, :, col_index])
                        if win_cond_r == 5 or win_cond_c == 5 and len(bingo_cards) > 1:
                            bingo_cards.remove(bingo_cards[card_index])
                            np.delete(play_tracker, card_index)
                        elif (win_cond_r == 5 or win_cond_c == 5) and len(bingo_cards) == 1:
                            return(bingo_cards, call, play_tracker)
                        else:
                            continue
                    else:
                        continue
    return None

(last_card, last_call, last_tracker) = play_for_last(bingo_numbers, bingo_cards_for_last, play_tracker_for_last)

