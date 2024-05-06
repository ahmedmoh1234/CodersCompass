from experta import Fact, KnowledgeEngine, Rule, NOT, AND, OR

from KnowledgeBase.FieldFacts import *
from KnowledgeBase.PreviousKnowledgeFacts import *
from KnowledgeBase.LearningCurveFacts import *
from KnowledgeBase.FinalSuggestionFacts import *

class Reaction(KnowledgeEngine):

    @Rule(NoFieldFact())
    def no_field(self):
        print("\n++ Welcome to the Software Expert System ++\n\nPlease select one of the following fields you would like to learn:")
        i = 1
        for field in Field:
            print(str(i) + ".", field.value[1])
            i = i + 1
        response = input("Your response: ")
        while response not in ["1", "2", "3", "4", "5"]:
            response = input("Please select a valid field: ")
            i = 1
            for field in Field:
                print(str(i) + ".", field.value[1])
                i = i + 1
        for field in Field:
            if int(response) == field.value[0]:
                self.declare(field.value[2])
                self.declare(NoPreviousKnowledgeFact())

    @Rule(NoPreviousKnowledgeFact())
    def no_knowledge(self):
        print("\nWhat is your knowledge in the chosen field?")
        i = 1
        for knowledge in PreviousKnowledge:
            print(str(i) + ".", knowledge.value[1])
            i = i + 1
        response = input("Your response: ")
        while response not in ["1", "2", "3"]:
            response = input("Please select valid level of knowledge: ")
            i = 1
            for knowledge in PreviousKnowledge:
                print(str(i) + ".", knowledge.value[1])
                i = i + 1
        for knowledge in PreviousKnowledge:
            if int(response) == knowledge.value[0]:
                self.declare(knowledge.value[2])

    @Rule(AND(FieldFrontendFact(), KnowledgeBeginnerFact()))
    def front_end_beginner(self):
        print("\nIt looks like you are a beginner! Here is a few suggestions")
        print("HTML/CSS || Bootstrap || jQuery")
        self.fetch_learning_curve(Field.Frontend, PreviousKnowledge.Beginner)

    @Rule(AND(FieldFrontendFact(), KnowledgeIntermediateFact()))
    def front_end_intermediate(self):
        print("\nIt seems you have some knowledge in frontend development! Here is a few suggestions")
        print("React.js || Vue.js || Angular")
        self.fetch_learning_curve(Field.Frontend, PreviousKnowledge.Intermediate)

    @Rule(AND(FieldFrontendFact(), KnowledgeAdvancedFact()))
    def front_end_advanced(self):
        print("\nBased on your expert level! Here is a few suggestions")
        print("Svelte || Ember.js || Backbone.js")
        self.fetch_learning_curve(Field.Frontend, PreviousKnowledge.Advanced)

    @Rule(AND(FieldBackendFact(), KnowledgeBeginnerFact()))
    def back_end_beginner(self):
        print("\nIt looks like you are a beginner! Here is a few suggestions")
        print("Node.js (with Express.js) || Flask (Python) || Django (Python)")
        self.fetch_learning_curve(Field.Backend, PreviousKnowledge.Beginner)

    @Rule(AND(FieldBackendFact(), KnowledgeIntermediateFact()))
    def back_end_intermediate(self):
        print("\nIt seems you have some knowledge in backend development! Here is a few suggestions")
        print("Ruby on Rails || ASP.NET Core || Laravel (PHP)")
        self.fetch_learning_curve(Field.Backend, PreviousKnowledge.Intermediate)

    @Rule(AND(FieldBackendFact(), KnowledgeAdvancedFact()))
    def back_end_advanced(self):
        print("\nBased on your expert level! Here is a few suggestions")
        print("Spring Boot (Java) || Symfony (PHP) || Express.js with TypeScript")
        self.fetch_learning_curve(Field.Backend, PreviousKnowledge.Advanced)

    @Rule(AND(FieldMobileFact(), KnowledgeBeginnerFact()))
    def mobile_beginner(self):
        print("\nIt looks like you are a beginner! Here is a few suggestions")
        print("React Native || Flutter")
        # //TODO
        self.fetch_learning_curve(Field.Mobile, PreviousKnowledge.Beginner)

    @Rule(AND(FieldMobileFact(), KnowledgeIntermediateFact()))
    def mobile_intermediate(self):
        print("\nIt seems you have some knowledge in mobile development! Here is a few suggestions")
        print("Native Script || Xamarin")
        # //TODO
        self.fetch_learning_curve(Field.Mobile, PreviousKnowledge.Intermediate)

    @Rule(AND(FieldMobileFact(), KnowledgeAdvancedFact()))
    def mobile_advanced(self):
        print("\nBased on your expert level! Here is a few suggestions")
        print("Android: Java-Kotlin iOS: Swift")
        self.fetch_learning_curve(Field.Mobile, PreviousKnowledge.Advanced)

    @Rule(AND(FieldTestingFact(), KnowledgeBeginnerFact()))
    def testing_beginner(self):
        print("\nIt looks like you are a beginner! Here is a few suggestions")
        print("Selenium WebDriver || Cypress || Puppeteer")
        self.fetch_learning_curve(Field.Testing, PreviousKnowledge.Beginner)

    @Rule(AND(FieldTestingFact(), KnowledgeIntermediateFact()))
    def testing_intermediate(self):
        print("\nIt seems you have some knowledge in testing development! Here is a few suggestions")
        print("Appium || TestNG || JUnit")
        self.fetch_learning_curve(Field.Testing, PreviousKnowledge.Intermediate)

    @Rule(AND(FieldTestingFact(), KnowledgeAdvancedFact()))
    def testing_advanced(self):
        print("\nBased on your expert level! Here is a few suggestions")
        print("Protractor || Robot Framework || Cucumber")
        self.fetch_learning_curve(Field.Testing, PreviousKnowledge.Advanced)

    @Rule(AND(FieldDevOpsFact(), KnowledgeBeginnerFact()))
    def devops_beginner(self):
        print("\nIt looks like you are a beginner! Here is a few suggestions")
        print("Bash Scripting || Docker || Ansible")
        self.fetch_learning_curve(Field.DevOps, PreviousKnowledge.Beginner)

    @Rule(AND(FieldDevOpsFact(), KnowledgeIntermediateFact()))
    def devops_intermediate(self):
        print("\nIt seems you have some knowledge in devops engineering! Here is a few suggestions")
        print("Jenkins || Terraform || Kubernetes")
        self.fetch_learning_curve(Field.DevOps, PreviousKnowledge.Intermediate)

    @Rule(AND(FieldDevOpsFact(), KnowledgeAdvancedFact()))
    def devops_advanced(self):
        print("\nBased on your expert level! Here is a few suggestions")
        print("Chef || Pupper || Prometheus")
        self.fetch_learning_curve(Field.DevOps, PreviousKnowledge.Advanced)
    
    def fetch_learning_curve(self, field, knowledge):
        print("\nWhat is your preferred learning curve?")
        i = 1
        for learning_curve in LearningCurve:
            print(str(i) + ".", learning_curve.value[1])
            i = i + 1
        response = input("Your response: ")
        while response not in ["1", "2", "3"]:
            response = input("Please select valid learning curve: ")
            i = 1
            for learning_curve in LearningCurve:
                print(str(i) + ".", learning_curve.value[1])
                i = i + 1
        for learning_curve in LearningCurve:
            if int(response) == learning_curve.value[0]:
                fact = getSuggestionFromAllKnowledge(field, knowledge, learning_curve)
                if fact is not None:
                    self.declare(fact)
                else:
                    print("No suggestions available for this combination")
    
    @Rule(HtmlFact())
    def html_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn HTML/CSS")

    @Rule(BootstrapFact())
    def bootstrap_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Bootstrap")
    
    @Rule(JQueryFact())
    def jquery_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn jQuery")
    
    @Rule(ReactFact())
    def react_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn React.js")
    
    @Rule(VueFact())
    def vue_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Vue.js")
    
    @Rule(AngularFact())
    def angular_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Angular")
    
    @Rule(SvelteFact())
    def svelte_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Svelte")
    
    @Rule(EmberFact())
    def ember_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Ember.js")
    
    @Rule(BackboneFact())
    def backbone_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Backbone.js")
    
    @Rule(FlaskFact())
    def flask_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Flask")
    
    @Rule(NodeFact())
    def node_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Node.js")
    
    @Rule(DjangoFact())
    def django_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Django")
    
    @Rule(LaravelFact())
    def laravel_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Laravel")

    @Rule(RubyFact())
    def ruby_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Ruby on Rails")
    
    @Rule(DotNetFact())
    def dotnet_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn ASP.NET Core")
    
    @Rule(ExpressFact())
    def express_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Express.js with TypeScript")
    
    @Rule(SymfonyFact())
    def symfony_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Symfony")
    
    @Rule(SpringFact())
    def spring_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Spring Boot")

    @Rule(ReactNativeFact())
    def react_native_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn React Native")

    @Rule(FlutterFact())
    def flutter_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Flutter")

    @Rule(NativeScriptFact())
    def native_script_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Native Script")

    @Rule(XamarinFact())
    def xamarin_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Xamarin")
    
    @Rule(JavaKotlinFact())
    def java_kotlin_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Android: Java-Kotlin")
    
    @Rule(SwiftFact())
    def swift_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn iOS: Swift")
    
    @Rule(SeleniumFact())
    def selenium_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Selenium WebDriver")
    
    @Rule(CypressFact())
    def cypress_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Cypress")

    @Rule(PuppeteerFact())
    def puppeteer_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Puppeteer")
    
    @Rule(BashScriptingFact())
    def bash_scripting_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Bash Scripting")
    
    @Rule(DockerFact())
    def docker_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Docker")
    
    @Rule(AnsibleFact())
    def ansible_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Ansible")
    
    @Rule(AppiumFact())
    def appium_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Appium")
    
    @Rule(TestNGFact())
    def testng_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn TestNG")
    
    @Rule(JUnitFact())
    def junit_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn JUnit")

    @Rule(ProtractorFact())
    def protractor_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Protractor")

    @Rule(RobotFact())
    def robot_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Robot Framework")

    @Rule(ChefFact())
    def chef_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Chef")
    
    @Rule(JenkinsFact())
    def jenkins_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Jenkins")

    @Rule(TerraformFact())
    def terraform_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Terraform")
    
    @Rule(KubernetesFact())
    def kubernetes_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Kubernetes")
    
    @Rule(PuppetFact())
    def puppet_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Puppet")

    @Rule(PrometheusFact())
    def prometheus_rule(self):
        print("\nBased on your knowledge and preferences, we suggest you to learn Prometheus")



def main():
    engine = Reaction()
    print(engine.get_rules())
    engine.reset()
    engine.declare(NoFieldFact())
    engine.run()

if __name__ == "__main__":
    main()