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
            type='performance',
            severity='medium'
        ))

    @Rule(
        ProjectFact(project_type='big_data'),
        ProjectFact(language='Python'),
        salience=700
    )
    def recommend_big_data_python(self):
        self.declare(RecommendationFact(
            library='Dask',
            reason='Параллельные вычисления для больших данных в Python',
            priority='high'
        ))

    @Rule(
        ProjectFact(project_type='big_data'),
        ProjectFact(language='Java'),
        salience=700
    )
    def recommend_big_data_java(self):
        self.declare(RecommendationFact(
            library='Apache Spark',
            reason='Обработка больших данных для Java/Scala',
            priority='high'
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
            type='performance',
            severity='medium'
        ))

    @Rule(
        ProjectFact(need_caching=True),
        salience=700
    )
    def recommend_caching(self):
        self.declare(RecommendationFact(
            library='Redis',
            reason='Кэширование данных в памяти',
            priority='medium'
        ))

    @Rule(
        ProjectFact(need_optimization=True),
        ProjectFact(language='Python'),
        salience=700
    )
    def recommend_python_optimization(self):
        self.declare(RecommendationFact(
            library='Cython',
            reason='Оптимизация производительности Python кода',
            priority='medium'
        ))

    @Rule(
        ProjectFact(real_time_requirements=True),
        salience=700
    )
    def recommend_real_time_libraries(self):
        self.declare(RecommendationFact(
            library='Real-time Processing Tools',
            reason='Инструменты для обработки в реальном времени',
            priority='high'
        ))

    @Rule(
        ProjectFact(high_concurrency=True),
        ProjectFact(language='Python'),
        salience=700
    )
    def recommend_concurrency_python(self):
        self.declare(RecommendationFact(
            library='asyncio',
            reason='Асинхронное программирование для Python',
            priority='high'
        ))

    @Rule(
        ProjectFact(memory_constrained=True),
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, memory_footprint='high'),
        salience=700
    )
    def warn_high_memory_library(self, lib):
        self.declare(WarningFact(
            message=f"Библиотека {lib} имеет высокое потребление памяти - не подходит для ограниченных систем",
            type='performance',
            severity='medium'
        ))