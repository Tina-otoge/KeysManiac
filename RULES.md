# Judges

PERFECT = 1 point
NICE = 0.5 point
OK = 0.2 point
MISS = 0 point
SUPER = 1 point (bonus)

# Types of notes

- Simple Note:
	- Press a key
	- There can be multiple simple notes at the same time, this is called "chord"

- Long Note:
	- Press and hold a key
	- Both the pressing time and releasing time are judged, both count as a note

- Trick Note:
	- A simple note that spawns other notes

- Simple Mine:
	- A simple note that will cause a miss if you hit it
	- Not hitting it gives a SUPER

- Long Mine:
	- A long note that will cause a miss if you hit anytime during its duration
	- Not hitting it gives a SUPER

- Ghost Note:
	- An invisible note
	- Pressing any key will hit it
	- Always gives a SUPER

# Scoring

Max score = Amount of notes
Bonus score = Amount of mines avoided and ghost notes hit (amount of SUPERs)
Accuracy = (`score` x 100) / `Max score`
