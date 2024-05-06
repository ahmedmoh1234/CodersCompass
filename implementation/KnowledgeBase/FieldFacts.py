from experta import Fact
from enum import Enum

class NoFieldFact(Fact):
    pass

class FieldFrontendFact(Fact):
    pass

class FieldBackendFact(Fact):
    pass

class FieldMobileFact(Fact):
    pass

class FieldTestingFact(Fact):
    pass

class FieldDevOpsFact(Fact):
    pass

class Field(Enum):
    Frontend = (1, "Front-end Development", FieldFrontendFact())
    Backend = (2, "Back-end Development", FieldBackendFact())
    Mobile = (3, "Mobile Development", FieldMobileFact())
    Testing = (4, "Automation Testing", FieldTestingFact())
    DevOps = (5, "DevOps Engineering", FieldDevOpsFact())