from helpers import draw_board

spots = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5',
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}

draw_board(spots)

# Changing the board proof of concept
spots[1] = 'x'
print('second player ', draw_board(spots))
