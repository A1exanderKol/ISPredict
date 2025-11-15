from experta import *

from facts import ProjectFact, RecommendationFact


class SpecializedRules:
    """Правила для специализированных технологий и сценариев"""

    # Правила для AI/ML проектов
    @Rule(ProjectFact(need_computer_vision=True))
    def recommend_cv_libraries(self):
        self.declare(RecommendationFact(
            library='OpenCV',
            reason='Computer Vision library',
            priority='high'
        ))

    @Rule(ProjectFact(need_nlp=True))
    def recommend_nlp_libraries(self):
        self.declare(RecommendationFact(
            library='NLTK',
            reason='Natural Language Processing',
            priority='high'
        ))
        self.declare(RecommendationFact(
            library='spaCy',
            reason='Industrial-strength NLP',
            priority='high'
        ))

    # Правила для блокчейн проектов
    @Rule(ProjectFact(need_blockchain=True))
    def recommend_blockchain_libraries(self):
        self.declare(RecommendationFact(
            library='Web3.py',
            reason='Python + Ethereum',
            priority='high'
        ))

    # Правила для IoT проектов
    @Rule(ProjectFact(need_iot=True))
    def recommend_iot_libraries(self):
        self.declare(RecommendationFact(
            library='Paho-MQTT',
            reason='IoT + MQTT Protocol',
            priority='high'
        ))

    # Правила для финансовых технологий
    @Rule(ProjectFact(sector='financial', need_analytics=True))
    def recommend_finance_libraries(self):
        self.declare(RecommendationFact(
            library='QuantLib',
            reason='Financial Instrument Pricing',
            priority='high'
        ))

    # Правила для игровых проектов
    @Rule(ProjectFact(need_game_development=True))
    def recommend_game_libraries(self):
        self.declare(RecommendationFact(
            library='Unity',
            reason='Cross-platform Game Engine',
            priority='high'
        ))
        self.declare(RecommendationFact(
            library='Pygame',
            reason='Python Game Development',
            priority='medium'
        ))

    # Правила для образовательных проектов
    @Rule(ProjectFact(sector='education'))
    def recommend_education_libraries(self):
        self.declare(RecommendationFact(
            library='Interactive Visualization Tools',
            reason='Enhanced Learning Experience',
            priority='medium'
        ))

    # Правила для медицинских проектов
    @Rule(ProjectFact(sector='medical', need_data_analysis=True))
    def recommend_medical_libraries(self):
        self.declare(RecommendationFact(
            library='Medical Image Processing Tools',
            reason='Healthcare Data Analysis',
            priority='high'
        ))

    # Правила для правительственных проектов
    @Rule(ProjectFact(sector='government'))
    def recommend_government_libraries(self):
        self.declare(RecommendationFact(
            library='Security-focused Libraries',
            reason='Government Security Standards',
            priority='high'
        ))

    # Правила для высоконагруженных систем
    @Rule(ProjectFact(high_load=True))
    def recommend_high_load_libraries(self):
        self.declare(RecommendationFact(
            library='Caching Solutions',
            reason='High Performance Caching',
            priority='high'
        ))
        self.declare(RecommendationFact(
            library='Load Balancing Tools',
            reason='Traffic Distribution',
            priority='medium'
        ))

    # Правила для систем реального времени
    @Rule(ProjectFact(real_time_requirements=True))
    def recommend_realtime_libraries(self):
        self.declare(RecommendationFact(
            library='Real-time Processing',
            reason='Low Latency Requirements',
            priority='high'
        ))

    # Правила для legacy систем
    @Rule(ProjectFact(legacy_integration=True))
    def recommend_legacy_libraries(self):
        self.declare(RecommendationFact(
            library='Compatibility Layers',
            reason='Legacy System Integration',
            priority='medium'
        ))

    # Правила для мультиязычных проектов
    @Rule(ProjectFact(multi_language=True))
    def recommend_multilingual_libraries(self):
        self.declare(RecommendationFact(
            library='Internationalization Tools',
            reason='Multi-language Support',
            priority='medium'
        ))