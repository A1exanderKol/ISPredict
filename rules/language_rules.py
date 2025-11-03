from experta import *

from facts import ProjectFact, RecommendationFact


class LanguageRules:
    """Правила выбора библиотек по языку программирования"""

    # Высокий приоритет - правила языка выполняются первыми
    @Rule(ProjectFact(language='Python', need_db=True), salience=1000)
    def python_db(self):
        self.declare(RecommendationFact(
            library='SQLAlchemy',
            reason='Python + Database',
            priority='high'
        ))

    @Rule(ProjectFact(language='Python', need_web=True), salience=1000)
    def python_web(self):
        self.declare(RecommendationFact(
            library='Django',
            reason='Python + Web Framework',
            priority='high'
        ))

    @Rule(ProjectFact(language='Java', need_db=True), salience=1000)
    def java_db(self):
        self.declare(RecommendationFact(
            library='Hibernate',
            reason='Java + Database',
            priority='high'
        ))

    @Rule(ProjectFact(language='Java', need_web=True), salience=1000)
    def java_web(self):
        self.declare(RecommendationFact(
            library='Spring Boot',
            reason='Java + Web Framework',
            priority='high'
        ))

    @Rule(ProjectFact(language='C#', need_db=True), salience=1000)
    def csharp_db(self):
        self.declare(RecommendationFact(
            library='Entity Framework',
            reason='C# + Database',
            priority='high'
        ))

    @Rule(ProjectFact(language='C#', need_web=True), salience=1000)
    def csharp_web(self):
        self.declare(RecommendationFact(
            library='ASP.NET Core',
            reason='C# + Web Framework',
            priority='high'
        ))

    @Rule(ProjectFact(language='JavaScript', need_web=True), salience=1000)
    def javascript_web(self):
        self.declare(RecommendationFact(
            library='Express.js',
            reason='JavaScript + Web Framework',
            priority='high'
        ))