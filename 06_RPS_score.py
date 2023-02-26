# RPS Component 6 = Scoring System

# Rounds won will be calculated (total - draw - lost)
rounds_played = 0
rounds_lost = 0
rounds_drwan = 0

# Results for trsting purposes
test_results = ["won", "won", "loss", "tie"]

# Play Game
for item in test_results:
    rounds_played += 1

    # Generate computer choice

    results = item

    if result == "tie":
        result = "it's a  tie"
        rounds_drwan += 1
    elif result == "loss":
           rounds_lost += 1

# Qiuck Caloulations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of Game Statements
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {} \t|\t Draw: "
      "{}".format(rounds_won, rounds_lost, rounds_drwan))
print()
print("Thank you for playing")
  