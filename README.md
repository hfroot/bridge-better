# BridgeBetter

BridgeBetter is inspired by a version of the card game of Bridge modified for three players. BridgeBetter aims to automate the fourth, unseen, hand's bid such that we can achieve higher-scoring games, with fewer surprises hidden in the fourth hand.

(Side note: the term 'betting' isn't really used in bridge, instead 'bidding' is used, but for the sake of a decent pun this program is called BridgeBetter. Don't @ me plz.)

# Our modified version

There are many three person Bridge modifications. Ours works as follows:

 * Each player plays for themselves, unlike traditional Bridge where the game is scored in teams of two
 * Four hands are dealt, one for each player and a fourth that will act as the dummy for the round
 * After each round of bidding, in which at least one of the three players has increased the existing bid, three cards are turned over in the 'dummy hand' to provide a guess as to the strength of the hand
 * If all three players no bid in one round, no more cards are turned over in the dummy hand, and none of the players have any further chance to bid. The game is commenced based on the highest bid placed, or if no bid has been placed, the round is abandoned and the cards are re dealt.

## Pitfalls

The bidding flow and game play following bidding has been positive using this approach. The weakness is in the accuracy of the final bid - an ideal bid would maximise points 'below the line' for the player leading the bid.

This approach to hinting at the strength of the dummy results in both too little information and too much:
 * when the players have weak hands, but the dummy has a strong hand, very few cards are turned over in the dummy, and the game may be played for on a much lower bid than it could be
 * when the players have strong hands and most, or even all, of the dummy hand is revealed during the bidding process, this makes bidding too easy for the leading bidder(s), and it makes it much easier for the player playing the first card of the first trick

## Aims

As a result the primary aim is to optimise for bid accuracy, without scrapping the need for players to be skilled in bidding. Along the way of building this logic, might as well support full remote gameplay, especially during the pandemic. This includes:

 * a player can initiate a round of cards
 * players will not see each others' hands
 * players can place bids via app
 * the dummy hand will place bids in response to their own cards and the other players' bids. NB: the dummy should not base decisions based on access to the hands of all players, such that the same bidding logic could be applied in a physical game of cards in the future
 * a bid can be accepted and the gameplay initiated
 * players can play the round

### Secondary extensions

 * score tracking
    * scores for the round can be stored persistently
    * scores for games can be stored persistently
    * track a leaderboard
 * persistent user base
 * Compare groups of players in leaderboards in games where the card distribution is duplicated
 * support multiple simultaneous and unrelated games

## Future extensions

There's something quite nice about playing a physical game of cards, so the major second exploration of features would be to allow BridgeBetter to support physical games of cards.

 * Image processing to scan cards dealt to the dummy
 * Physical equipment/set up for scanning the cards
 * Voice recognition to process player bids
     * Admin screen to monitor and modify data coming in to BridgeBetter
 * Speech generation to place bids on the dummy's behalf

At the moment I'd expect this set up to not follow the game play, e.g. it wouldn't be used for tracking how the hand is played or automated scoring.

# Technical details

Messing around with ideas of bidding logic is currently being done in Python because Python is a delight to use for 'sketching'.

TBC: Prototype of the application will be created as a web app, since all parties are not on a shared phone operating system, so native applications would hinder testing and development. Alternatively also looking at developing a mobile app with Flutter which would support both iOS and Android.

Libraries, tools, and frameworks will only be imported when required. All code in this repo should have been read by a developer of the project, and the app should be lightweight.

Testing is nice.

# Parts of the app

## Team creation

## Login

## Display

### Hand
### Bids
### Other players
### Tricks

## Bidding

### Four person version
### Three person version

## Play

## Scoring

## Leaderboard

# Terminology and bidding conventions

Conventions for bidding used as described here: http://pi.math.cornell.edu/~belk/bridge.htm.

Terminology below taken from https://en.wikipedia.org/wiki/Glossary_of_contract_bridge_terms, some have been modified for our three-person Bridge, and some have been rephrased.

Bid: a tuple of number + denomination, given by a player to indicate how many tricks they intend to win, in a game where the trump suit is the given suit.

Call: any bid, pass, double, or redouble in the bidding stage.

Contract: the combination of player + bid. This is determined as the last bid in a round of bidding, and will determine the game's trump suit.

Deck: The 52 cards used in bridge.

Declarer: The player who holds the final contract for a game.

Defeat: To prevent the declarer from achieving the contract.

Defender: The player(s) trying to defeat the contract.

Denomination: The component of a bid that denotes the proposed trump suit or notrump.

Direction: The player's position at the table (North, East, South, West)

Suit distribution: The distribution of one suit's cards across all the hands in a game.

Hand distribution: The count of the four suits in one hand.

Distribution points: The measure of a hand based on the Hand Distribution.

Dummy: The hand that is not given to a player. It goes on to become the Declarer's 'partner'.

Game: A contract, bid and made, worth 100 points or more.

High-card points (HCP): The number of points in a Hand that are purely from face cards.

Play: The stage of a Deal when players attempt to take tricks.

Round: A sequence of four consecutive calls during the bidding stage.

Shuffle: To mix the cards.

Small slam: A contract to win 12 tricks.

Grand slam: A contract to win 13 tricks.

Suit: A ranked division of the deck of cards into (in ascending order) clubs, diamonds, hearts, spades. Suit ranking impacts bidding and scoring, but not play.

Table: A grouping of three players + dummy.

Trick: A set of four cards played in turn, during the play of a hand.

Underbid:

Undertrick:

Vulnerable:

