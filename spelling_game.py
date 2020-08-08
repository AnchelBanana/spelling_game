message_need_spell = str(input("Enter the word you want: "))
list_spelled = []

'''
A--Alpha;B--Bravo;C--Charlie;D--Delta;E--Echo;F--Foxtrot;
G--Golf;H--Hotel;I--India;J--Juliet;K--Kilo;L--Lima;M--Mike;
N--November;O--Oscar;P--Papa;Q--Quebec;R--Romeo;S--Sierra;T--Tango;
U--Uniform;V--Victor;W--Whiskey;X--X-ray;Y--Yankee;Z--Zulu
'''


def split(message, list):
    for letter in message:
        if letter.capitalize() == "A":
            list.append('alpha')
        if letter.capitalize() == "B":
            list.append('bravo')
        if letter.capitalize() == "C":
            list.append('charlie')
        if letter.capitalize() == "D":
            list.append('delta')
        if letter.capitalize() == "E":
            list.append('echo')
        if letter.capitalize() == "F":
            list.append('foxtrot')
        if letter.capitalize() == "G":
            list.append('golf')
        if letter.capitalize() == "H":
            list.append('hotel')
        if letter.capitalize() == "I":
            list.append('india')
        if letter.capitalize() == "J":
            list.append('juliet')
        if letter.capitalize() == "K":
            list.append('kilo')
        if letter.capitalize() == "L":
            list.append('lima')
        if letter.capitalize() == "M":
            list.append('mike')
        if letter.capitalize() == "N":
            list.append('november')
        if letter.capitalize() == "O":
            list.append('oscar')
        if letter.capitalize() == "P":
            list.append('papa')
        if letter.capitalize() == "Q":
            list.append('quebec')
        if letter.capitalize() == "R":
            list.append('romeo')
        if letter.capitalize() == "S":
            list.append('sierra')
        if letter.capitalize() == "T":
            list.append('tango')
        if letter.capitalize() == "U":
            list.append('uniform')
        if letter.capitalize() == "V":
            list.append('victor')
        if letter.capitalize() == "W":
            list.append('whiskey')
        if letter.capitalize() == "X":
            list.append('xray')
        if letter.capitalize() == "Y":
            list.append('yankee')
        if letter.capitalize() == "Z":
            list.append('zulu')
    return list


split1 = split(message_need_spell, list_spelled)
print(message_need_spell + ' is ')
print(split1)
