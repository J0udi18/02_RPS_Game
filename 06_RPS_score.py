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
        