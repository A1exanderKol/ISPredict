from experta import *

from facts import ProjectFact, RecommendationFact


class TestingRules:
    """Правила для тестирования"""

    @Rule(
        ProjectFact(language='Python'),
        salience=650
    )
    def recommend_python_testing(self):
        self.declare(RecommendationFact(
            library='pytest',
            reason='Фреймворк для тестирования Python',
            priority='medium'
        ))

    @Rule(
        ProjectFact(language='Java'),
        salience=650
    )
    def recommend_java_testing(self):
        self.declare(RecommendationFact(
            library='JUnit',
            reason='Фреймворк для тестирования Java',
            priority='medium'
        ))

    @Rule(
        ProjectFact(language='JavaScript'),
        salience=650
    )
    def recommend_js_testing(self):
        self.declare(RecommendationFact(
            library='Jest',
            reason='Фреймворк для тестирования JavaScript',
            priority='medium'
        ))

    @Rule(
        ProjectFact(need_unit_testing=True),
        salience=650
    )
    def recommend_unit_testing(self):
        self.declare(RecommendationFact(
            library='Unit Test Framework',
            reason='Фреймворк для модульного тестирования',
            priority='high'
        ))

    @Rule(
        ProjectFact(need_integration_testing=True),
        salience=650
    )
    def recommend_integration_testing(self):
        self.declare(RecommendationFact(
            library='Integration Test Tools',
            reason='Инструменты для интеграционного тестирования',
            priority='medium'
        ))

    @Rule(
        ProjectFact(need_performance_testing=True),
        salience=650
    )
    def recommend_performance_testing(self):
        self.declare(RecommendationFact(
            library='JMeter',
            reason='Инструмент для нагрузочного тестирования',
            priority='medium'
        ))

    @Rule(
        ProjectFact(need_security_testing=True),
        salience=650
    )
    def recommend_security_testing(self):
        self.declare(RecommendationFact(
            library='OWASP ZAP',
            reason='Инструмент для тестирования безопасности',
            priority='medium'
        ))