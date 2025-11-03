from experta import *

from facts import ProjectFact, RecommendationFact, LibraryFact, WarningFact


class ParadigmRules:
    """Правила поддержки парадигм программирования"""

    @Rule(
        ProjectFact(paradigm='OOP'),
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, supports_oop=False),
        salience=500
    )
    def reject_non_oop(self, lib):
        recommendation = self.find_recommendation_fact(lib)
        if recommendation:
            self.retract(recommendation)
        self.declare(WarningFact(
            message=f"Библиотека {lib} отклонена: не поддерживает ООП парадигму",
            type='paradigm'
        ))

    @Rule(
        ProjectFact(paradigm='functional'),
        ProjectFact(language='JavaScript'),
        salience=500
    )
    def recommend_functional_js(self):
        self.declare(RecommendationFact(
            library='Ramda.js',
            reason='Functional programming utilities for JavaScript',
            priority='medium'
        ))

    @Rule(
        ProjectFact(paradigm='functional'),
        ProjectFact(language='Python'),
        salience=500
    )
    def recommend_functional_python(self):
        self.declare(RecommendationFact(
            library='toolz',
            reason='Functional programming utilities for Python',
            priority='medium'
        ))

    @Rule(
        ProjectFact(concurrent=True),
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, supports_concurrency=False),
        salience=500
    )
    def reject_non_concurrent(self, lib):
        recommendation = self.find_recommendation_fact(lib)
        if recommendation:
            self.retract(recommendation)
        self.declare(WarningFact(
            message=f"Библиотека {lib} отклонена: не поддерживает параллельные вычисления",
            type='paradigm'
        ))