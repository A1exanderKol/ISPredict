from experta import *

from facts import RecommendationFact, ProjectFact, LibraryFact, WarningFact


class LicenseRules:
    """Правила лицензирования"""

    @Rule(
        RecommendationFact(library=MATCH.lib),
        ProjectFact(license_type='commercial'),
        LibraryFact(name=MATCH.lib, license='GPL'),
        salience=900
    )
    def reject_gpl_commercial(self, lib):
        # Находим и удаляем рекомендацию
        recommendation = self.find_recommendation_fact(lib)
        if recommendation:
            self.retract(recommendation)
        self.declare(WarningFact(
            message=f"Библиотека {lib} отклонена: GPL лицензия не подходит для коммерческого проекта",
            type='license'
        ))

    @Rule(
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, license=L('MIT') | L('Apache 2.0') | L('BSD')),
        salience=900
    )
    def allow_open_source(self, lib):
        self.declare(RecommendationFact(
            library=lib,
            reason=f"Открытая лицензия разрешена",
            priority='medium',
            approved=True
        ))