from experta import Fact
from enum import Enum

class ShallowLearningFact(Fact):
    pass

class NormalLearningFact(Fact):
    pass

class SteepLearningFact(Fact):
    pass

class LearningCurve(Enum):
    Shallow = (1, "Shallow", ShallowLearningFact())
    Normal = (2, "Normal", NormalLearningFact())
    Steep = (3, "Steep", SteepLearningFact())