from experta import *

from facts import ProjectFact, RecommendationFact


class TestingRules:
    """Правила для тестирования"""

    @Rule(ProjectFact(language='Python'))
    def recommend_python_testing(self):
        self.declare(RecommendationFact(
            library='pytest',
            reason='Python Testing Framework',
            priority='high'
        ))
        self.declare(RecommendationFact(
            library='unittest',
            reason='Python Standard Testing',
            priority='medium'
        ))

    @Rule(ProjectFact(language='Java'))
    def recommend_java_testing(self):
        self.declare(RecommendationFact(
            library='JUnit',
            reason='Java Unit Testing',
            priority='high'
        ))
        self.declare(RecommendationFact(
            library='Mockito',
            reason='Java Mocking Framework',
            priority='high'
        ))

    @Rule(ProjectFact(language='C#'))
    def recommend_csharp_testing(self):
        self.declare(RecommendationFact(
            library='xUnit',
            reason='C# Testing Framework',
            priority='high'
        ))
        self.declare(RecommendationFact(
            library='Moq',
            reason='C# Mocking Library',
            priority='high'
        ))

    @Rule(ProjectFact(language='JavaScript'))
    def recommend_javascript_testing(self):
        self.declare(RecommendationFact(
            library='Jest',
            reason='JavaScript Testing',
            priority='high'
        ))
        self.declare(RecommendationFact(
            library='Mocha',
            reason='JavaScript Test Framework',
            priority='medium'
        ))
        self.declare(RecommendationFact(
            library='Chai',
            reason='JavaScript Assertion Library',
            priority='medium'
        ))

    @Rule(ProjectFact(need_unit_testing=True))
    def recommend_unit_testing(self):
        self.declare(RecommendationFact(
            library='Unit Test Framework',
            reason='Code Quality Assurance',
            priority='high'
        ))

    @Rule(ProjectFact(need_integration_testing=True))
    def recommend_integration_testing(self):
        self.declare(RecommendationFact(
            library='Integration Test Tools',
            reason='System Integration Testing',
            priority='medium'
        ))

    @Rule(ProjectFact(need_performance_testing=True))
    def recommend_performance_testing(self):
        self.declare(RecommendationFact(
            library='JMeter',
            reason='Performance Testing',
            priority='medium'
        ))

    @Rule(ProjectFact(need_security_testing=True))
    def recommend_security_testing(self):
        self.declare(RecommendationFact(
            library='OWASP ZAP',
            reason='Security Vulnerability Testing',
            priority='high'
        ))

    @Rule(ProjectFact(need_ui_testing=True))
    def recommend_ui_testing(self):
        self.declare(RecommendationFact(
            library='Selenium',
            reason='Web UI Testing',
            priority='high'
        ))

    @Rule(ProjectFact(need_mobile_testing=True))
    def recommend_mobile_testing(self):
        self.declare(RecommendationFact(
            library='Appium',
            reason='Mobile App Testing',
            priority='high'
        ))