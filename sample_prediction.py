"""
Example input file for prediction of euro 2020 match
"""

import stochasticmodel

team1 = stochasticmodel.Team("Germany")
team2 = stochasticmodel.Team("France")


print(
    "Match prediction: "
    + " ".join([team1.name, str(team1.score), "-", str(team2.score), team2.name])
)
