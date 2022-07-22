from madlib_templates import madlib1, madlib2
import random

if __name__ == "__main__":
    random_madlib = random.choice([madlib1, madlib2])
    random_madlib.madlib()