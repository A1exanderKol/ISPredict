from experta import *

from facts import ProjectFact, RecommendationFact, LibraryFact, WarningFact


class PerformanceRules:
    """Правила производительности и оптимизации"""

    @Rule(
        ProjectFact(project_type='mobile'),
        RecommendationFact(library=MATCH.lib),
        salience=700
    )
    def warn_mobile_performance(self, lib):
        self.declare(WarningFact(
            message=f"Для мобильного приложения рекомендуется проверить размер библиотеки {lib}",
            type='performance'
        ))

    @Rule(
        ProjectFact(project_type='big_data'),
        ProjectFact(language='Python'),
        salience=700
    )
    def recommend_big_data_python(self):
        self.declare(RecommendationFact(
            library='Dask',
            reason='Big Data processing for Python',
            priority='medium'
        ))

    @Rule(
        ProjectFact(project_type='big_data'),
        ProjectFact(language='Java'),
        salience=700
    )
    def recommend_big_data_java(self):
        self.declare(RecommendationFact(
            library='Apache Spark',
            reason='Big Data processing for Java/Scala',
            priority='medium'
        ))

    @Rule(
        ProjectFact(high_performance=True),
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, reputation=MATCH.rep),
        TEST(lambda rep: rep < 7),
        salience=700
    )
    def warn_low_performance_library(self, lib, rep):
        self.declare(WarningFact(
            message=f"Библиотека {lib} имеет низкую репутацию ({rep}/10) для высокопроизводительного проекта",
            type='performance'
        ))