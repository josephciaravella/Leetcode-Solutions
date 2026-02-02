from collections import Counter
def isNStraightHand(hand, groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False
    
    freq = Counter(hand)
    hand = sorted(hand)

    for card in hand:
        if freq[card] == 0:
            continue

        for i in range(groupSize):
            curr_card = card + i
            if freq[curr_card] > 0:
                freq[curr_card] -= 1
            else: 
                return False

    return True 