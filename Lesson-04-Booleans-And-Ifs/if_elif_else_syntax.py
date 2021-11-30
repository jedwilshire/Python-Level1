score = 75

if score < 70:
    print('F')    # not run because score < 70 is False
elif score < 80:
    print('C')    # run because score < 80 is True
elif score < 90:
    print('B')    # NOT run because an earlier if or elif branch was True
else:
    print('A')    # not run because an earlier branch was True