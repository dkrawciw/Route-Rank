# Route Rank

## Introduction

* Find a way to more objectively rank routes in the gym
* Attach statistics (height, weight, wingspan, etc...) to difficulty of routes
* A UI to record comparisons and display overal rankings

## Methodology

The following are the first two algorithms considered:
* [Colley Ranking](https://www.colleyrankings.com/matrate.pdf)
* [Massey Ranking](https://masseyratings.com/theory/massey97.pdf)

These algorithms rank based off of trials where two "things" are compared. These "things" could be teams in sports, insect stings, food from restaurants, etc.

Essentially, trials are recorded between two contenders where there is a "winner" and a "loser". This is done many times over. For colley ranking, there is simply a winner and a loser; whereas with massey ranking, there is also a point differential (how much did the winner win by)?

The idea here is that Colley ranking will be more objective because it is often easier to just say that one climb is harder than another. Massey ranking will be more difficult to capture in because it is unclear what the point differential will be defined as. There are some advantages in Massey ranking though as one can say that one climb is much difficult than another vs a climb that is only slightly more difficult.

Some ideas for how to define the point differential:
* Give them a scale from $1$ to $10$ on how much more difficult the climb is
* Just have the options: "Slightly" or "Significantly" correspond to numerical values

An interesting consideration we have is that Massey ranking's point differential most likely will vary depending on how fatigued the climber is.