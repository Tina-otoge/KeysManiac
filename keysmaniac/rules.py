class Judgement:
    NAME = None
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
    NAME = 'Perfect'
    SCORE = 1.0
    TIMING = 0.017

class Nice(NormalJudgement):
    NAME = 'Nice'
    SCORE = 0.5
    TIMING = 0.03

class OK(NormalJudgement):
    NAME = 'OK'
    SCORE = 0.2
    TIMING = 0.05

class Miss(NormalJudgement):
    NAME = 'Miss'
    SCORE = 0.0

class Super(BonusJudgement):
    NAME = 'Super'
    BONUS_SCORE = 1.0
    TIMING = OK.TIMING

NORMAL_WINDOW = [Perfect, Nice, OK]
BONUS_WINDOW = [Super]
JUDGES = [Miss, OK, Nice, Perfect, Super]
BONUS = Super
MISS = Miss
