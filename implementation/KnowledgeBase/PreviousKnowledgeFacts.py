from experta import Fact
from enum import Enum

class NoPreviousKnowledgeFact(Fact):
    pass

class KnowledgeBeginnerFact(Fact):
    pass

class KnowledgeIntermediateFact(Fact):
    pass

class KnowledgeAdvancedFact(Fact):
    pass

class PreviousKnowledge(Enum):
    Beginner = (1, "Beginner", KnowledgeBeginnerFact())
    Intermediate = (2, "Intermediate", KnowledgeIntermediateFact())
    Advanced = (3, "Advanced", KnowledgeAdvancedFact())