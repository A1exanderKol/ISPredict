from experta import *

from facts import ProjectFact, RecommendationFact


class IntegrationRules:
    """Правила интеграции"""

    @Rule(
        ProjectFact(needs_rest_api=True),
        ProjectFact(language='Python'),
        salience=600
    )
    def recommend_rest_python(self):
        self.declare(RecommendationFact(
            library='Requests',
            reason='REST API client for Python',
            priority='medium'
        ))

    @Rule(
        ProjectFact(needs_rest_api=True),
        ProjectFact(language='Java'),
        salience=600
    )
    def recommend_rest_java(self):
        self.declare(RecommendationFact(
            library='Retrofit',
            reason='REST API client for Java',
            priority='medium'
        ))

    @Rule(
        ProjectFact(needs_rest_api=True),
        ProjectFact(language='JavaScript'),
        salience=600
    )
    def recommend_rest_javascript(self):
        self.declare(RecommendationFact(
            library='Axios',
            reason='REST API client for JavaScript',
            priority='medium'
        ))

    @Rule(
        ProjectFact(needs_database=True),
        ProjectFact(language='Python'),
        salience=600
    )
    def recommend_db_driver_python(self):
        self.declare(RecommendationFact(
            library='psycopg2',
            reason='PostgreSQL driver for Python',
            priority='medium'
        ))