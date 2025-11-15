from experta import *

from facts import ProjectFact, RecommendationFact

class LanguageRules:
    """Правила выбора библиотек по языку программирования"""

    # === PYTHON ПРАВИЛА ===

    @Rule(ProjectFact(language='Python', need_db=True), salience=1000)
    def python_db(self):
        self.declare(RecommendationFact(library='SQLAlchemy', reason='Python + Database ORM', priority='high'))
        self.declare(RecommendationFact(library='Psycopg2', reason='Python + PostgreSQL driver', priority='medium'))
        self.declare(RecommendationFact(library='PyMySQL', reason='Python + MySQL driver', priority='medium'))

    @Rule(ProjectFact(language='Python', need_web=True), salience=1000)
    def python_web(self):
        self.declare(RecommendationFact(library='Django', reason='Python + Full-stack Web Framework', priority='high'))
        self.declare(RecommendationFact(library='Flask', reason='Python + Micro Web Framework', priority='medium'))
        self.declare(RecommendationFact(library='FastAPI', reason='Python + Modern API Framework', priority='high'))

    @Rule(ProjectFact(language='Python', need_web=True, high_performance=True), salience=1000)
    def python_web_performance(self):
        self.declare(
            RecommendationFact(library='FastAPI', reason='Python + High-performance Web Framework', priority='high'))

    @Rule(ProjectFact(language='Python', need_data_science=True), salience=1000)
    def python_data_science(self):
        self.declare(RecommendationFact(library='Pandas', reason='Python + Data Analysis', priority='high'))
        self.declare(RecommendationFact(library='NumPy', reason='Python + Numerical Computing', priority='high'))
        self.declare(RecommendationFact(library='SciPy', reason='Python + Scientific Computing', priority='medium'))

    @Rule(ProjectFact(language='Python', need_ml=True), salience=1000)
    def python_ml(self):
        self.declare(RecommendationFact(library='Scikit-learn', reason='Python + Machine Learning', priority='high'))
        self.declare(RecommendationFact(library='XGBoost', reason='Python + Gradient Boosting', priority='medium'))

    @Rule(ProjectFact(language='Python', need_ml=True, need_deep_learning=True), salience=1000)
    def python_deep_learning(self):
        self.declare(
            RecommendationFact(library='TensorFlow', reason='Python + Deep Learning Framework', priority='high'))
        self.declare(RecommendationFact(library='PyTorch', reason='Python + Deep Learning Research', priority='high'))
        self.declare(RecommendationFact(library='Keras', reason='Python + High-level Deep Learning', priority='medium'))

    @Rule(ProjectFact(language='Python', need_visualization=True), salience=1000)
    def python_visualization(self):
        self.declare(RecommendationFact(library='Matplotlib', reason='Python + Basic Plotting', priority='medium'))
        self.declare(
            RecommendationFact(library='Seaborn', reason='Python + Statistical Visualization', priority='medium'))
        self.declare(RecommendationFact(library='Plotly', reason='Python + Interactive Visualization', priority='high'))

    @Rule(ProjectFact(language='Python', need_async=True), salience=1000)
    def python_async(self):
        self.declare(RecommendationFact(library='asyncio', reason='Python + Asynchronous Programming', priority='high'))
        self.declare(RecommendationFact(library='Celery', reason='Python + Distributed Task Queue', priority='medium'))

    @Rule(ProjectFact(language='Python', need_scraping=True), salience=1000)
    def python_scraping(self):
        self.declare(RecommendationFact(library='BeautifulSoup', reason='Python + HTML Parsing', priority='medium'))
        self.declare(RecommendationFact(library='Scrapy', reason='Python + Web Scraping Framework', priority='high'))

    @Rule(ProjectFact(language='Python', need_gui=True), salience=1000)
    def python_gui(self):
        self.declare(RecommendationFact(library='PyQt', reason='Python + Advanced GUI', priority='high'))
        self.declare(RecommendationFact(library='Tkinter', reason='Python + Simple GUI', priority='low'))

    @Rule(ProjectFact(language='Python', need_image_processing=True), salience=1000)
    def python_image_processing(self):
        self.declare(RecommendationFact(library='Pillow', reason='Python + Image Processing', priority='medium'))
        self.declare(RecommendationFact(library='OpenCV', reason='Python + Computer Vision', priority='high'))

    @Rule(ProjectFact(language='Python', need_api=True), salience=1000)
    def python_api(self):
        self.declare(
            RecommendationFact(library='Django REST Framework', reason='Python + REST API for Django', priority='high'))
        self.declare(RecommendationFact(library='Requests', reason='Python + HTTP Client', priority='high'))

    @Rule(ProjectFact(language='Python', need_big_data=True), salience=1000)
    def python_big_data(self):
        self.declare(RecommendationFact(library='Dask', reason='Python + Parallel Computing', priority='high'))
        self.declare(RecommendationFact(library='PySpark', reason='Python + Spark Integration', priority='medium'))

    @Rule(ProjectFact(language='Python', need_workflow=True), salience=1000)
    def python_workflow(self):
        self.declare(RecommendationFact(library='Airflow', reason='Python + Workflow Management', priority='high'))

    @Rule(ProjectFact(language='Python', need_dashboard=True), salience=1000)
    def python_dashboard(self):
        self.declare(RecommendationFact(library='Streamlit', reason='Python + Data Dashboard', priority='high'))

    # === JAVA ПРАВИЛА ===

    @Rule(ProjectFact(language='Java', need_db=True), salience=1000)
    def java_db(self):
        self.declare(RecommendationFact(library='Hibernate', reason='Java + Database ORM', priority='high'))
        self.declare(RecommendationFact(library='JPA', reason='Java + Persistence API', priority='medium'))

    @Rule(ProjectFact(language='Java', need_web=True), salience=1000)
    def java_web(self):
        self.declare(RecommendationFact(library='Spring Boot', reason='Java + Web Framework', priority='high'))
        self.declare(RecommendationFact(library='Spring Framework', reason='Java + Core Framework', priority='high'))

    @Rule(ProjectFact(language='Java', need_microservices=True), salience=1000)
    def java_microservices(self):
        self.declare(RecommendationFact(library='Spring Cloud', reason='Java + Microservices', priority='high'))

    @Rule(ProjectFact(language='Java', need_security=True), salience=1000)
    def java_security(self):
        self.declare(RecommendationFact(library='Spring Security', reason='Java + Security Framework', priority='high'))

    @Rule(ProjectFact(language='Java', need_json=True), salience=1000)
    def java_json(self):
        self.declare(RecommendationFact(library='Jackson', reason='Java + JSON Processing', priority='high'))

    @Rule(ProjectFact(language='Java', need_build=True), salience=1000)
    def java_build(self):
        self.declare(RecommendationFact(library='Maven', reason='Java + Build Tool', priority='high'))
        self.declare(RecommendationFact(library='Gradle', reason='Java + Modern Build Tool', priority='medium'))

    @Rule(ProjectFact(language='Java', need_utils=True), salience=1000)
    def java_utils(self):
        self.declare(RecommendationFact(library='Apache Commons', reason='Java + Utilities', priority='medium'))
        self.declare(RecommendationFact(library='Guava', reason='Java + Google Utilities', priority='medium'))

    @Rule(ProjectFact(language='Java', need_big_data=True), salience=1000)
    def java_big_data(self):
        self.declare(RecommendationFact(library='Apache Spark', reason='Java + Big Data Processing', priority='high'))
        self.declare(RecommendationFact(library='Kafka', reason='Java + Message Streaming', priority='high'))

    @Rule(ProjectFact(language='Java', need_mobile=True), salience=1000)
    def java_mobile(self):
        self.declare(RecommendationFact(library='Android SDK', reason='Java + Mobile Development', priority='high'))

    # === C# ПРАВИЛА ===

    @Rule(ProjectFact(language='C#', need_db=True), salience=1000)
    def csharp_db(self):
        self.declare(RecommendationFact(library='Entity Framework', reason='C# + Database ORM', priority='high'))
        self.declare(RecommendationFact(library='Dapper', reason='C# + Micro ORM', priority='medium'))

    @Rule(ProjectFact(language='C#', need_web=True), salience=1000)
    def csharp_web(self):
        self.declare(RecommendationFact(library='ASP.NET Core', reason='C# + Web Framework', priority='high'))

    @Rule(ProjectFact(language='C#', need_gui=True), salience=1000)
    def csharp_gui(self):
        self.declare(RecommendationFact(library='Windows Forms', reason='C# + Desktop GUI', priority='medium'))
        self.declare(RecommendationFact(library='WPF', reason='C# + Modern Desktop GUI', priority='high'))

    @Rule(ProjectFact(language='C#', need_games=True), salience=1000)
    def csharp_games(self):
        self.declare(RecommendationFact(library='Unity', reason='C# + Game Development', priority='high'))

    @Rule(ProjectFact(language='C#', need_ml=True), salience=1000)
    def csharp_ml(self):
        self.declare(RecommendationFact(library='ML.NET', reason='C# + Machine Learning', priority='high'))

    @Rule(ProjectFact(language='C#', need_realtime=True), salience=1000)
    def csharp_realtime(self):
        self.declare(RecommendationFact(library='SignalR', reason='C# + Real-time Communication', priority='high'))

    @Rule(ProjectFact(language='C#', need_json=True), salience=1000)
    def csharp_json(self):
        self.declare(RecommendationFact(library='Newtonsoft.Json', reason='C# + JSON Processing', priority='high'))
        self.declare(RecommendationFact(library='System.Text.Json', reason='C# + Modern JSON', priority='medium'))

    @Rule(ProjectFact(language='C#', need_mapping=True), salience=1000)
    def csharp_mapping(self):
        self.declare(RecommendationFact(library='AutoMapper', reason='C# + Object Mapping', priority='medium'))

    @Rule(ProjectFact(language='C#', need_resilience=True), salience=1000)
    def csharp_resilience(self):
        self.declare(RecommendationFact(library='Polly', reason='C# + Resilience Patterns', priority='medium'))

    # === JAVASCRIPT ПРАВИЛА ===

    @Rule(ProjectFact(language='JavaScript', need_web=True), salience=1000)
    def javascript_web(self):
        self.declare(RecommendationFact(library='Express.js', reason='JavaScript + Backend Framework', priority='high'))
        self.declare(RecommendationFact(library='Node.js', reason='JavaScript + Runtime', priority='high'))

    @Rule(ProjectFact(language='JavaScript', need_frontend=True), salience=1000)
    def javascript_frontend(self):
        self.declare(RecommendationFact(library='React', reason='JavaScript + Frontend Library', priority='high'))
        self.declare(RecommendationFact(library='Vue.js', reason='JavaScript + Progressive Framework', priority='high'))
        self.declare(RecommendationFact(library='Angular', reason='JavaScript + Full Framework', priority='high'))

    @Rule(ProjectFact(language='JavaScript', need_mobile=True), salience=1000)
    def javascript_mobile(self):
        self.declare(
            RecommendationFact(library='React Native', reason='JavaScript + Cross-platform Mobile', priority='high'))

    @Rule(ProjectFact(language='JavaScript', need_realtime=True), salience=1000)
    def javascript_realtime(self):
        self.declare(
            RecommendationFact(library='Socket.io', reason='JavaScript + Real-time Communication', priority='high'))

    @Rule(ProjectFact(language='JavaScript', need_ssr=True), salience=1000)
    def javascript_ssr(self):
        self.declare(RecommendationFact(library='Next.js', reason='JavaScript + React SSR', priority='high'))
        self.declare(RecommendationFact(library='Nuxt.js', reason='JavaScript + Vue SSR', priority='high'))

    @Rule(ProjectFact(language='JavaScript', need_visualization=True), salience=1000)
    def javascript_visualization(self):
        self.declare(RecommendationFact(library='D3.js', reason='JavaScript + Data Visualization', priority='high'))
        self.declare(RecommendationFact(library='Chart.js', reason='JavaScript + Simple Charts', priority='medium'))

    @Rule(ProjectFact(language='JavaScript', need_3d=True), salience=1000)
    def javascript_3d(self):
        self.declare(RecommendationFact(library='Three.js', reason='JavaScript + 3D Graphics', priority='high'))

    @Rule(ProjectFact(language='JavaScript', need_state=True), salience=1000)
    def javascript_state(self):
        self.declare(RecommendationFact(library='Redux', reason='JavaScript + State Management', priority='medium'))

    @Rule(ProjectFact(language='JavaScript', need_db=True), salience=1000)
    def javascript_db(self):
        self.declare(RecommendationFact(library='Mongoose', reason='JavaScript + MongoDB ODM', priority='high'))
        self.declare(RecommendationFact(library='Sequelize', reason='JavaScript + SQL ORM', priority='high'))

    @Rule(ProjectFact(language='JavaScript', need_auth=True), salience=1000)
    def javascript_auth(self):
        self.declare(RecommendationFact(library='Passport.js', reason='JavaScript + Authentication', priority='high'))
        self.declare(
            RecommendationFact(library='JWT (jsonwebtoken)', reason='JavaScript + Token Auth', priority='high'))

    @Rule(ProjectFact(language='JavaScript', need_utils=True), salience=1000)
    def javascript_utils(self):
        self.declare(RecommendationFact(library='Lodash', reason='JavaScript + Utilities', priority='medium'))
        self.declare(RecommendationFact(library='Axios', reason='JavaScript + HTTP Client', priority='high'))

    @Rule(ProjectFact(language='JavaScript', need_dates=True), salience=1000)
    def javascript_dates(self):
        self.declare(
            RecommendationFact(library='Moment.js', reason='JavaScript + Date Manipulation', priority='medium'))
        self.declare(RecommendationFact(library='Date-fns', reason='JavaScript + Modern Date', priority='high'))

    @Rule(ProjectFact(language='JavaScript', need_build=True), salience=1000)
    def javascript_build(self):
        self.declare(RecommendationFact(library='Webpack', reason='JavaScript + Module Bundler', priority='high'))
        self.declare(RecommendationFact(library='Babel', reason='JavaScript + Compiler', priority='high'))

    @Rule(ProjectFact(language='JavaScript', need_types=True), salience=1000)
    def javascript_types(self):
        self.declare(RecommendationFact(library='TypeScript', reason='JavaScript + Type Safety', priority='high'))