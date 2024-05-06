from experta import Fact
from enum import Enum
from KnowledgeBase.FieldFacts import Field
from KnowledgeBase.PreviousKnowledgeFacts import PreviousKnowledge
from KnowledgeBase.LearningCurveFacts import LearningCurve

# Frontend Beginner
class HtmlFact(Fact):
    pass

class BootstrapFact(Fact):
    pass

class JQueryFact(Fact):
    pass

# Frontend Intermediate
class ReactFact(Fact):
    pass

class VueFact(Fact):
    pass

class AngularFact(Fact):
    pass

# Frontend Advanced
class SvelteFact(Fact):
    pass

class EmberFact(Fact):
    pass

class BackboneFact(Fact):
    pass

# Backend Beginner
class FlaskFact(Fact):
    pass

class NodeFact(Fact):
    pass

class DjangoFact(Fact):
    pass

# Backend Intermediate
class LaravelFact(Fact):
    pass

class RubyFact(Fact):
    pass

class DotNetFact(Fact):
    pass

# Backend Advanced
class ExpressFact(Fact):
    pass

class SymfonyFact(Fact):
    pass

class SpringFact(Fact):
    pass

# Mobile Beginner
class ReactNativeFact(Fact):
    pass

class FlutterFact(Fact):
    pass

# Mobile Intermediate
class NativeScriptFact(Fact):
    pass

class XamarinFact(Fact):
    pass

# Mobile Advanced
class JavaKotlinFact(Fact):
    pass

class SwiftFact(Fact):
    pass

# Testing Beginner
class SeleniumFact(Fact):
    pass

class CypressFact(Fact):
    pass

class PuppeteerFact(Fact):
    pass

# Testing Intermediate
class AppiumFact(Fact):
    pass

class TestNGFact(Fact):
    pass

class JUnitFact(Fact):
    pass

# Testing Advanced
class ProtractorFact(Fact):
    pass

class RobotFact(Fact):
    pass

# DevOps Beginner
class BashScriptingFact(Fact):
    pass

class DockerFact(Fact):
    pass
class AnsibleFact(Fact):
    pass

# DevOps Intermediate
class JenkinsFact(Fact):
    pass

class TerraformFact(Fact):
    pass

class KubernetesFact(Fact):
    pass

# DevOps Advanced
class ChefFact(Fact):
    pass

class PuppetFact(Fact):
    pass

class PrometheusFact(Fact):
    pass

def getSuggestionFromAllKnowledge(field, previous_knowledge, learning_curve):
    if field == Field.Frontend:
        if previous_knowledge == PreviousKnowledge.Beginner:
            if learning_curve == LearningCurve.Shallow:
                return HtmlFact()
            elif learning_curve == LearningCurve.Normal:
                return BootstrapFact()
            else:
                return JQueryFact()
        elif previous_knowledge == PreviousKnowledge.Intermediate:
            if learning_curve == LearningCurve.Shallow:
                return ReactFact()
            elif learning_curve == LearningCurve.Normal:
                return VueFact()
            else:
                return AngularFact()
        elif previous_knowledge == PreviousKnowledge.Advanced:
            if learning_curve == LearningCurve.Shallow:
                return SvelteFact()
            elif learning_curve == LearningCurve.Normal:
                return EmberFact()
            else:
                return BackboneFact()
    elif field == Field.Backend:
        if previous_knowledge == PreviousKnowledge.Beginner:
            if learning_curve == LearningCurve.Shallow:
                return FlaskFact()
            elif learning_curve == LearningCurve.Normal:
                return NodeFact()
            else:
                return DjangoFact()
        elif previous_knowledge == PreviousKnowledge.Intermediate:
            if learning_curve == LearningCurve.Shallow:
                return LaravelFact()
            elif learning_curve == LearningCurve.Normal:
                return RubyFact()
            else:
                return DotNetFact()
        elif previous_knowledge == PreviousKnowledge.Advanced:
            if learning_curve == LearningCurve.Shallow:
                return ExpressFact()
            elif learning_curve == LearningCurve.Normal:
                return SymfonyFact()
            else:
                return SpringFact()
    elif field == Field.Mobile:
        if previous_knowledge == PreviousKnowledge.Beginner:
            if learning_curve == LearningCurve.Shallow or learning_curve == LearningCurve.Normal:
                return ReactNativeFact()
            else:
                return FlutterFact()
        elif previous_knowledge == PreviousKnowledge.Intermediate:
            if learning_curve == LearningCurve.Shallow or learning_curve == LearningCurve.Normal:
                return NativeScriptFact()
            else:
                return XamarinFact()
        elif previous_knowledge == PreviousKnowledge.Advanced:
            if learning_curve == LearningCurve.Shallow:
                return JavaKotlinFact()
            else:
                return SwiftFact()
    elif field == Field.Testing:
        if previous_knowledge == PreviousKnowledge.Beginner:
            if learning_curve == LearningCurve.Shallow:
                return SeleniumFact()
            elif learning_curve == LearningCurve.Normal:
                return CypressFact()
            else:
                return PuppeteerFact()
        elif previous_knowledge == PreviousKnowledge.Intermediate:
            if learning_curve == LearningCurve.Shallow:
                return AppiumFact()
            elif learning_curve == LearningCurve.Normal:
                return TestNGFact()
            else:
                return JUnitFact()
        elif previous_knowledge == PreviousKnowledge.Advanced:
            if learning_curve == LearningCurve.Shallow:
                return ProtractorFact()
            else:
                return RobotFact()
    elif field == Field.DevOps:
        if previous_knowledge == PreviousKnowledge.Beginner:
            if learning_curve == LearningCurve.Shallow:
                return BashScriptingFact()
            elif learning_curve == LearningCurve.Normal:
                return DockerFact()
            else:
                return AnsibleFact()
        elif previous_knowledge == PreviousKnowledge.Intermediate:
            if learning_curve == LearningCurve.Shallow:
                return JenkinsFact()
            elif learning_curve == LearningCurve.Normal:
                return TerraformFact()
            else:
                return KubernetesFact()
        elif previous_knowledge == PreviousKnowledge.Advanced:
            if learning_curve == LearningCurve.Shallow:
                return ChefFact()
            elif learning_curve == LearningCurve.Normal:
                return PuppetFact()
            else:
                return PrometheusFact()
    return None
