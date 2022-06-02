
squares = {x: x ** 2 for x in range(1, 11)}
print(f"squares :{squares}")

players = {
    'sachin': (280, 345, 250, 410, 320),
    'sourav': (310, 225, 180, 265, 385),
    'rahul': (230, 260, 350, 150, 198),
    'sehwag': (175, 375, 450, 340, 230),
    'yuvraj':(120, 180, 280, 250, 150)
}

print("-" * 40)
print(f"players :{players}")

print("-" * 40)
print(f"Sachin :{players['sachin']}")
print(f"Sachin :{sum(players['sachin'])}")

print("-" * 40)
score = {score for score in players}
print(f"score :{score}")

print("-" * 40)
score = {score for score in players.keys()}
print(f"score :{score}")

print("-" * 40)
score = {score for score in players.values()}
print(f"score :{score}")

print("-" * 40)
score = {k: v for k, v in players.items()}
print(f"score :{score}")

print("-" * 40)
score = {k: sum(v) for k, v in players.items()}
print(f"score :{score}")

print("-" * 40)
avg_score = {k: (lambda scores: sum(scores) / len(scores)) (v)
            for k, v in players.items()}
print(f"Average score :{avg_score}")

print("-" * 40)
res = [{x :(lambda par: "Mr." + par) ("Sachin {}".format(x))}
            for x in range(1, 6)]
print(f"res :{res}")

print("-" * 40)
score  = [score for score in players.values()]
print(f"score :{score}")

print("-" * 40)
score = [scr for scores in players.values() for scr in scores]
print(f"score :{score}")

print("-" * 40)
score = [scr for scores in players.values() for scr in scores if scr >= 200]
print(f"score :{score}")

print("-" * 40)
score = {name: [scr for scr in scores if scr >= 200]
            for name, scores in players.items()}
print(f"score :{score}")
