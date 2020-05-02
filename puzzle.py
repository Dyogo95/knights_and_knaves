from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnight,And(AKnight, AKnave)) # Implies that, if AKnight then the statement must be true.
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Implication(AKnight,And(AKnave, BKnave)), # If And statement is true then Aknight
    Not(And(BKnight, BKnave)),  # B can't be Knight and Knave
    Not(And(AKnight, AKnave)),
    Or(AKnight, AKnave),
    Or(BKnight, BKnave)
#    Or(AKnight,BKnight), # If only one could be Knight
#    Or(AKnave, BKnave)   # If only A or B could be Knave
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Implication(AKnight,And(AKnight,BKnight)),
    Implication(AKnight,And(AKnave, BKnave)),
    Implication(BKnight,Not(And(AKnight, BKnight))),
    Implication(BKnight,Not(And(AKnave,BKnave))),
    Not(And(AKnave, BKnave)),
    Or(BKnight, AKnight),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Not(And(AKnight,AKnave)),
    Implication(AKnight,And(BKnave,AKnight)),
#    Biconditional(BKnight,Or(BKnight, AKnight)),
    Implication(BKnight, Or(AKnave,AKnight)),       # B is knight if A is either knight or knave. B Statement True
    Implication(BKnight, And(BKnight,CKnave)),
    Implication(BKnave, And(CKnight,BKnave)),
    Or(BKnight, CKnave),
    Not(And(BKnight,CKnight)),
    Implication(CKnight, And(CKnight,AKnight)),
    And(CKnave,BKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
