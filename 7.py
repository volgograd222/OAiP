while True:
    c = int( input('c = ') )
    s = ''
    for i in range(c-1, c+3):
        s += chr( ord('A') + i % 26 )
    print(s)

