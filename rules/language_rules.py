from experta import *

from facts import ProjectFact, RecommendationFact

class LanguageRules:
    """Правила выбора библиотек по языку программирования"""

    # Высокий приоритет - правила языка выполняются первыми
    @Rule(ProjectFact(language='Python', need_db=True), salience=1000)
    def python_db(self):
        self.declare(RecommendationFact(
            library='SQLAlchemy',
            reason='Python + Database ORM',
            priority='high'
        ))

    @Rule(ProjectFact(language='Python', need_web=True), salience=1000)
    def python_web(self):
        self.declare(RecommendationFact(
            library='Django',
            reason='Python + Full-stack Web Framework',
            priority='high'
        ))

    @Rule(ProjectFact(language='Python', need_web=True, high_performance=True), salience=1000)
    def python_web_performance(self):
        self.declare(RecommendationFact(
            library='FastAPI',
            reason='Python + High-performance Web Framework',
            priority='high'
        ))

    @Rule(ProjectFact(language='Python', need_gui=True), salience=1000)
    def python_gui(self):
        self.declare(RecommendationFact(
            library='PyQt',
            reason='Python + Desktop GUI',
            priority='medium'
        ))

    @Rule(ProjectFact(language='Python', need_ml=True), salience=1000)
    def python_ml(self):
        self.declare(RecommendationFact(
            library='scikit-learn',
            reason='Python + Machine Learning',
            priority='high'
        ))

    @Rule(ProjectFact(language='Python', need_ml=True, need_deep_learning=True), salience=1000)
    def python_deep_learning(self):
        self.declare(RecommendationFact(
            library='TensorFlow',
            reason='Python + Deep Learning',
            priority='high'
        ))

    @Rule(ProjectFact(language='Python', need_data_analysis=True), salience=1000)
    def python_data_analysis(self):
        self.declare(RecommendationFact(
            library='Pandas',
            reason='Python + Data Analysis',
            priority='high'
        ))

    @Rule(ProjectFact(language='Python', need_visualization=True), salience=1000)
    def python_visualization(self):
        self.declare(RecommendationFact(
            library='Matplotlib',
            reason='Python + Data Visualization',
            priority='medium'
        ))

    # Java правила
    @Rule(ProjectFact(language='Java', need_db=True), salience=1000)
    def java_db(self):
        self.declare(RecommendationFact(
            library='Hibernate',
            reason='Java + Database ORM',
            priority='high'
        ))

    @Rule(ProjectFact(language='Java', need_web=True), salience=1000)
    def java_web(self):
        self.declare(RecommendationFact(
            library='Spring Boot',
            reason='Java + Web Framework',
            priority='high'
        ))

    @Rule(ProjectFact(language='Java', need_mobile=True), salience=1000)
    def java_mobile(self):
        self.declare(RecommendationFact(
            library='Android SDK',
            reason='Java + Mobile Development',
            priority='high'
        ))

    @Rule(ProjectFact(language='Java', need_microservices=True), salience=1000)
    def java_microservices(self):
        self.declare(RecommendationFact(
            library='Spring Cloud',
            reason='Java + Microservices',
            priority='medium'
        ))

    # C# правила
    @Rule(ProjectFact(language='C#', need_db=True), salience=1000)
    def csharp_db(self):
        self.declare(RecommendationFact(
            library='Entity Framework',
            reason='C# + Database ORM',
            priority='high'
        ))

    @Rule(ProjectFact(language='C#', need_web=True), salience=1000)
    def csharp_web(self):
        self.declare(RecommendationFact(
            library='ASP.NET Core',
            reason='C# + Web Framework',
            priority='high'
        ))

    @Rule(ProjectFact(language='C#', need_gui=True), salience=1000)
    def csharp_gui(self):
        self.declare(RecommendationFact(
            library='Windows Forms',
            reason='C# + Desktop GUI',
            priority='medium'
        ))

    @Rule(ProjectFact(language='C#', need_games=True), salience=1000)
    def csharp_games(self):
        self.declare(RecommendationFact(
            library='Unity',
            reason='C# + Game Development',
            priority='high'
        ))

    # JavaScript правила
    @Rule(ProjectFact(language='JavaScript', need_web=True), salience=1000)
    def javascript_web(self):
        self.declare(RecommendationFact(
            library='Express.js',
            reason='JavaScript + Backend Web Framework',
            priority='high'
        ))

    @Rule(ProjectFact(language='JavaScript', need_frontend=True), salience=1000)
    def javascript_frontend(self):
        self.declare(RecommendationFact(
            library='React',
            reason='JavaScript + Frontend Framework',
            priority='high'
        ))

    @Rule(ProjectFact(language='JavaScript', need_mobile=True), salience=1000)
    def javascript_mobile(self):
        self.declare(RecommendationFact(
            library='React Native',
            reason='JavaScript + Cross-platform Mobile',
            priority='high'
        ))

    @Rule(ProjectFact(language='JavaScript', need_real_time=True), salience=1000)
    def javascript_realtime(self):
        self.declare(RecommendationFact(
            library='Socket.io',
            reason='JavaScript + Real-time Communication',
            priority='medium'
        ))

    # Новые языки
    @Rule(ProjectFact(language='Go', need_web=True), salience=1000)
    def go_web(self):
        self.declare(RecommendationFact(
            library='Gin',
            reason='Go + Web Framework',
            priority='high'
        ))

    @Rule(ProjectFact(language='Rust', need_systems=True), salience=1000)
    def rust_systems(self):
        self.declare(RecommendationFact(
            library='Tokio',
            reason='Rust + Systems Programming',
            priority='high'
        ))

    @Rule(ProjectFact(language='Kotlin', need_mobile=True), salience=1000)
    def kotlin_mobile(self):
        self.declare(RecommendationFact(
            library='Android SDK + Kotlin',
            reason='Kotlin + Mobile Development',
            priority='high'
        ))