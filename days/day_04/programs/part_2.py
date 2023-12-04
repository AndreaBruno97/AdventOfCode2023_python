from common import *
import re


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        card_list = open_file_lines(filepath)

        total = 0

        # Dictionary of acquired cards:
        #   - the key is the card's number
        #   - the value is the number of cards currently possessed
        current_cards = {1: 0}

        for card in card_list:
            card_without_start = re.sub("Card +", "", card)
            card_num_str, winning_str_list, my_str_list = re.split(r" \| |: ", card_without_start)
            card_num = int(card_num_str)

            number_of_cur_card = 1 + (current_cards.pop(card_num) if (card_num in current_cards) else 0)

            winning_list = [int(x) for x in re.split(r" +", winning_str_list) if x != ""]
            my_list = [int(x) for x in re.split(r" +", my_str_list) if x != ""]

            match_num = len(set(winning_list) & set(my_list))

            # Updating the total with the number of copies of the current card
            total += number_of_cur_card

            # Getting the next match_num cards, each one number_of_cur_card times
            # It symbolizes taking a copy of the next cards for each copy of the current card
            for next_acquired_card in range(card_num+1, card_num+1+match_num):
                if next_acquired_card in current_cards:
                    current_cards[next_acquired_card] += number_of_cur_card
                else:
                    current_cards[next_acquired_card] = number_of_cur_card

        return total


p2 = Part_2()
p2.test(30)
p2.execute()
