def isVowel(st):
    vowels = 'AEIOU'
    if st in vowels:
        return True
    else:
        return False

def count(substr, theStr):
    num = i = 0
    while True:
        j = theStr.find(substr, i)
        if j == -1:
            break
        num += 1
        i = j + 1
    return num

def minion_game(string):
    
    players = {'Kevin':0, 'Stuart': 0}
   
    for i in range(len(s)):
        vowels = 'AEIOU'
        if s[i] in vowels:
            players['Kevin'] += (len(s)-i)
        else:
            players['Stuart'] += (len(s)-i)
    if players['Stuart'] == players['Kevin']:
        print('Draw')
    else:
        maximum = max(players, key=players.get)  # Just use 'min' instead of 'max' for minimum.
        print(maximum, players[maximum])


if __name__ == '__main__':
    s = input()
    minion_game(s)