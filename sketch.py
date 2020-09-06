import random

SUITS = ["clubs", "diamonds", "hearts", "spades"]
VALUES_DISPLAY = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
VALUE_OFFSET = 2 # how much you need to add to the display index to get the point value of the relevant card
PLAYERS = ['Alex', 'Bob', 'Cara', 'Dummy']
VALUE_THRESHOLD = 10 # humans only bother counting Jacks and higher when evaluating hands
SHORT_THRESHOLD = 3 # anything lower than this is a 'short' run in a suit
LONG_THRESHOLD = 4 # anything above this is a 'long' run in a suit
BID_LEVELS = ["One", "Two", "Three", "Four", "Five", "Six", "Seven"]
BID_DENOMINATIONS = ["club", "diamond", "heart", "spade", "no trump"]

def deal():
    deck = []
    for suit in SUITS:
        for value, name in enumerate(VALUES_DISPLAY):
            deck.append({
                'value': value+VALUE_OFFSET,
                'suit': suit
            })
    cardsPerPlayer = len(deck)/len(PLAYERS)
    hands = {}
    for player in PLAYERS:
        hands[player] = []
        c = 0
        while c < cardsPerPlayer:
            card = random.choice(deck)
            hands[player].append(card)
            deck.remove(card)
            c+=1
    return hands

def printHand(hand, player=None):
    print(player)
    for card in hand:
        print(card)

def printHands(hands):
    for player, hand in hands.items():
        printHand(hand, player=player)

def printPoints(message, points, suit=None):
    if suit:
        message += "for "+suit+" "
    else:
        message += "in total "
    print(message + str(points))

# points from cards
def highCardPoints(hand, suit=None):
    points = 0
    for card in hand:
        # optionally only count points in one suit
        if not suit or suit == card['suit']:
            if card['value'] > VALUE_THRESHOLD:
                points += card['value'] - VALUE_THRESHOLD
    printPoints("Straight points ", points, suit=suit)
    return points

# points from cards and long/shorts
def hcpAndDistributionPoints(hand, suit=None):
    points = highCardPoints(hand, suit=suit)
    counts = {}
    for card in hand:
        # optionally only count points in one suit
        if not suit or suit == card['suit']:
            # TODO: see if python has a more concise way of calculating this
            count = 0
            if card['suit'] in counts:
                count = counts[card['suit']]
            count += 1
            counts[card['suit']] = count
    for countSuit in SUITS:
        if not suit or suit == countSuit:
            if counts[countSuit] < SHORT_THRESHOLD:
                points += SHORT_THRESHOLD - counts[countSuit]
            elif counts[countSuit] > LONG_THRESHOLD:
                points += counts[countSuit] - LONG_THRESHOLD
    printPoints("Extended points ", points, suit=suit)

def sortValue(elem):
    return elem['valueWithSuitOffset']

def sortCards(hands, player):
    # TODO: check out pythons in built sorting algos
    # TODO: have different sort options, now just ascending
    hand = hands[player]
    for card in hand:
        card['valueWithSuitOffset'] = SUITS.index(card['suit']) * 100 + card['value']
    # TODO: for the sake of exercise, evaluate different sorting algorithms, implement a few here.
    hand.sort(key=sortValue)
    for s in hand:
        del s['valueWithSuitOffset']
    return hand

def handProfile(hand):
    profile = {}
    for suit in SUITS:
        profile[suit] = {
            'points': 0,
            'count': 0
        }
    for card in hand:
        suit = card['suit']
        if card['value'] > VALUE_THRESHOLD:
            profile[suit]['points'] += card['value'] - VALUE_THRESHOLD
        profile[suit]['count'] += 1
    return profile

def makeOpeningBid(hand):
    profile = handProfile(hand)
    printHand(hand)
    print(profile)
    points = highCardPoints(hand)
    if points > 12:
        mostPoints = 0
        for suit in SUITS:
            suitPoints = profile[suit]['points']
            if suitPoints > mostPoints:
                mostPoints = suitPoints
                strongestSuit = suit
        return "1 "+strongestSuit
    else:
        return "No bid"

def main():
    hands = deal()
    for player in PLAYERS:
        hands[player] = sortCards(hands, player)
    for player, hand in hands.items():
        print("***"+player+"***")
        bid = makeOpeningBid(hand)
        print(player + " bids " + bid)

main()
# Ideas for tests
# check that no card appears twice in the deck/across hands
# check that the number of cards in deck+hands = deck at beginning
# check that no card has a value higher than 14 or lower than 2
# check that points totals across hands do not exceed limit (4+8+12+16=40 straight points)
# cards before and after reordering contain the same set of cards