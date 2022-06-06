

class TooTiny(Exception):
    pass

class TooYoung(Exception):
    pass

class TooOld(Exception):
    pass

try:
    age = 106

    if age < 10:
        raise TooTiny("Too very young to decide the leader.....")
    elif (age < 18):
        raise TooYoung("Young to decide the leader......")
    elif (age > 100):
        raise TooOld("Too very old to decide the right person......")

except TooTiny as t:
    print(t)

except TooYoung as y:
    print(y)

except TooOld as o:
    print(o)

except Exception as e:
    print(e)

else:
        print("You are eligible to cast your vote.....")
finally:
        print("Voting process completed.....")