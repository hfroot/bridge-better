# MVP

A 'single-room' app to allow 3 players to play a single tournament virtually in real time.

## Flow

### Set up

Player logs in with a pre-agreed unique code.

When all three players have logged in, no more players can join.

The players are given a Direction.

The players are dealt hands.

### Bid

1. The 3 players bid. If no players bid, re-deal hands.
2. The highest bid after three no-bids becomes the Contract.
  a) If the denomination of a bid is a suit, then the suit becomes the trump suit
  b) If the highest bid is held by the dummy, then the person who feels like they can pair with it becomes the Declarer, this person must have made a bid in the last round. If there is a dispute play rock paper scissors like all reasonable humans do. If no person volunteers, then the human player who holds the next highest bid becomes the Declarer.
3. The dummy becomes the Declarer's partner.

### Play

1. The player to the right of the dummy plays the first card of the first hand.
2. The dummy's hand is revealed to the table.
3. The Declarer plays the dummy's card.
4. The player to the left of the dummy plays.
5. The Declarer plays.
6. The trick is given to the player who played the highest card.
7. The trick-winning player starts the next hand, the rest of the cards are played clockwise.
8. Continue playing tricks until all 13 have been won.

### Score

1. Identify whether the Declarer has made the Contract.

## Tests

### Set up

A user should be able to log in with a code word. A user should not be able to log in with an incorrect code word.

A user should not be able to log in if three Players already exist.

When a user logs in, a Player should be created with: Nickname, Direction.

The first Player to log in should become the Dealer.

There should only ever be one Dealer.

If a user logs out, activity is suspended until a new user logs in, who should gain the logged out user's Direction (and nickname? What about later in the game?)

When three Players are logged in, the Dealer can trigger the dealing of the cards into Hands for each Player.

The Dummy is created at this point, and given a Direction.

The Direction of each Player should be unique.

When cards are dealt, each Player should get no more or less than 13 cards.

Each card should be valid and unique.

A Player should be able to sort their Hand from lowest to highest, with suit value included.

Each Hand should have between 0 and 37 HCP.

Each Hand should have between 0 and 9 Hand Distribution Points. (Let's only count shorts.)

Check the point calculation of particular Hands? E.g. a 'normal' Hand, a Hand with no points, a Hand with strange points (see problem suits: http://pi.math.cornell.edu/~belk/counting.htm), a Hand which plans to Bid Notrump (which should only count HCP, not HDP.)

### Bid

The Dealer should be the first person given the opportunity to make a Call.

When it is one Player's turn to Call, no other Player should be able to Call. (What about doubling?)

A Player should only be able to make a valid Call.

The Dummy should Open the bidding if, and only if, it has more than 12 HCP.

