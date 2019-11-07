class Judgement:
    SCORE = None
    BONUS_SCORE = None
    TIMING = None

class NormalJudgement(Judgement):
    BONUS_SCORE = 0
    pass

class BonusJudgement(Judgement):
    SCORE = 0
    pass

class Perfect(NormalJudgement):
    SCORE = 1.0
    TIMING = 0.017

class Nice(NormalJudgement):
    SCORE = 0.5
    TIMING = 0.03

class OK(NormalJudgement):
    SCORE = 0.2
    TIMING = 0.05

class Miss(NormalJudgement):
    SCORE = 0.0

class Super(BonusJudgement):
    BONUS_SCORE = 1.0
    TIMING = OK.TIMING

NORMAL_WINDOW = [Perfect, Nice, OK]
BONUS_WINDOW = [Super]
BONUS = Super
MISS = Miss
