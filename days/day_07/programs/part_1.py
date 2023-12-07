from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    hand_strength = [
        [1, 1, 1, 1, 1],    # High card
        [2, 1, 1, 1],       # One pair
        [2, 2, 1],          # Two pair
        [3, 1, 1],          # Three of a kind
        [3, 2],             # Full house
        [4, 1],             # Four of a kind
        [5]                 # Five of a kind
    ]

    card_strength = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    # function that converts a card into a numerical value to allow a comparison between integers
    def convert_card(self, cards):
        conversion_base = len(self.card_strength)

        # Define hand strength

        # The hand is first converted to an array of occurrences of its cards, ordered by most to least common
        # Example: 32T3K -> [2, 1, 1, 1], T55J5 -> [3, 1, 1]
        card_set = set(list(cards))
        card_set_frequency = [cards.count(x) for x in card_set]
        card_set_frequency.sort(reverse=True)

        # Hand configurations are placed in order of strength in the array hand_strength
        # This means that the configuration's index is bigger for stronger hands.
        converted_number = self.hand_strength.index(card_set_frequency)

        for cur_card in list(cards):
            converted_number *= conversion_base

            # Cards are placed in order of value in the array card_strength
            # This means that the card's index is bigger for more valuable cards.
            converted_number += self.card_strength.index(cur_card)

        return converted_number

    def execute_internal(self, filepath):
        hand_list = [x.split(" ") for x in open_file_lines(filepath)]

        for cur_hand in hand_list:
            cards, bid = cur_hand

            cur_hand[0] = self.convert_card(cards)
            cur_hand[1] = int(bid)

        hand_list.sort(key=lambda x: x[0])

        total = 0
        for cur_index, cur_hand in enumerate(hand_list):
            hand_rank = cur_index + 1
            _, cur_bid = cur_hand

            total += hand_rank * cur_bid

        return total


p1 = Part_1()
p1.test(6440)
p1.execute()
