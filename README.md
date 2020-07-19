# Nine-Men-Morrist-AI
The AI for Nine men's morris game
play the game with command "python  Game/game.py"


when you enter the game

enter difficulty (1~4)

This is for how many steps will AI to predict.
```
# 20      21        22
#   17    18    19 
#      14 15 16
# 8  9 10    11 12  13
#       6     7
#    3     4     5
# 0        1         2
```
In the opening game
```
enter difficulty (1~4)
1
opening game
AI turn
 _     _     _
   _   _   _
     _ _ _
 _ _ _   _ _ _
     _   _
   _   _   _
 W     _     _

Your turn 1 <= this 1 indicate the current board score -10000(black win)~10000(white win)
(now enter the location(0~22) to play the game
```
After 9 round

enter the mid/end game

```
mid game
AI turn
 _     _     _
   B   B   _
     W _ B
 _ _ _   W _ W
     W   _
   _   _   _
 _     _     _

Your turn 949
Choose loc from :  [[16, 17, 18], {9, 15, 19, 20, 21}]  
#{9, 15, 19, 20, 21} this candidate location is only for mid game
#in end game you can choose wherever you want
From 16 (enter the location you want to move from)
to 19 (enter the location you want to move to)
 _     _     _
   B   B   B
     W _ _
 _ _ _   W _ W
     W   _
   _   _   _
 _     _     _

Pick the location to remove
6 (reach the mill and choose to remove W in location 6
 _     _     _
   B   B   B
     W _ _
 _ _ _   W _ W
     _   _
   _   _   _
 _     _     _

AI turn
 _     _     _
   B   B   B
     W _ _
 _ _ _   _ _ W
     _   _
   _   _   _
 W     _     _

Your turn -51
Choose loc from :  [[17, 18, 19], {9, 12, 15, 16, 20, 21, 22}]
From
```

