bidders = input('Please enter your name if you want to participate to the auction\n').split()
print('The bidders in this auction are:\n')
for bidder in bidders:
    print(bidder)
print('\n'*100)
bid_num = len(bidders)
secret_bid = {}
for i in range(1, bid_num +1):
    print(f'Bid no. {i}:')
    name = input('Your name: ')
    bid = int(input('Your bid: $'))
    secret_bid[name] = bid
    print('\n'*100)
highest_bid = 0
winner = ''
for bid in secret_bid:
    if secret_bid[bid] > highest_bid:
        highest_bid = secret_bid[bid]
        winner = bid
print(f'The winner is {winner} with a ${highest_bid} bid.')