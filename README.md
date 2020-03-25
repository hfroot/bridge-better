# BridgeBetter

BridgeBetter inpsired by a version of the game of Bridge modified for three players. BridgeBetter aims to automate the fourth, unseen, hand's bid such that we can achieve higher-scoring games, with fewer surprises hidden in the fourth hand.

# Our modified version

There are many three person Bridge modifications. Ours works as follows:

 * Each player plays for themselves, unlike traditional Bridge where the game is scored in teams of two
 * Four hands are dealt, one for each player and a fourth that will act as the dummy for the round
 * After each round of bidding, in which at least one of the three players has increased the existing bid, three cards are turned over in the 'dummy hand' to provide a guess as to the strength of the hand
 * If all players no bid in one round, no more cards are turned over in the dummy hand, and none of the players have any further chance to bid. The game is commenced based on the highest bid placed, or if no bid has been placed, the round is abandoned and the cards are re dealt.

## Pitfalls

The bidding flow and game play following bidding has been positive using this approach. The weakness is in the accuracy of the final bid - an ideal bid would maximise points 'above the line' for the player leading the bid.

This approach to hinting at the strength of the dummy results in both too little information and too much:
 * when the players have weak hands, but the dummy has a strong hand, very few cards are turned over in the dummy, and the game may be played for on a much lower bid than it should be
 * when the players have strong hands and most, or even all, of the dummy hand is revealed during the bidding process, this makes bidding too easy for the leading bidder(s)

## Aims

As a result the primary aim is to optimise for bid accuracy, without scrapping the need for players to be skilled in bidding. Along the way of building this logic, might as well support full remote gameplay, especially during the pandemic. This includes:

 * a player can initiate a round of cards
 * players will not see each others' hands
 * players can place bids online
 * the dummy hand will place bids in response to their own cards and the other players' bids. NB: the dummy should not base decisions based on access to the hands of all players, such that the same logic could be applied in a physical game of cards in the future
 * a bid can be accepted and the gameplay initiated
 * players can play the round
 * scores for the round can be stored persistently
 * scores for games can be stored persistently
 * track a leaderboard

## Future extensions

The BridgeBetter would support physical games of cards.

 * Image processing to scan cards dealt to the dummy
 * Physical equipment/set up for scanning the cards
 * Voice recognition to process player bids
 * Speech generation to place bids
 * Admin screen to monitor and modify data coming in to BridgeBetter

# Technical details

Prototype of the application will be created as a web app, since all parties are not on a shared phone operating system, so native applications would hinder testing and development.

Libraries, tools, and frameworks will only be imported when required. All code in this repo should have been read by a developer of the project, and the app should be lightweight.

Testing is nice.
