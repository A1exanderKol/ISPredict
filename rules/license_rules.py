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
        self.retract(self.get_fact(RecommendationFact, library=lib))
        self.declare(WarningFact(
            message=f"Библиотека {lib} отклонена: GPL лицензия не подходит для коммерческого проекта",
            type='license'
        ))

    @Rule(
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, license='MIT'),
        salience=900
    )
    def allow_mit(self, lib):
        self.declare(RecommendationFact(
            library=lib,
            reason=f"MIT лицензия разрешена",
            priority='medium',
            approved=True
        ))

    @Rule(
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, license='Apache 2.0'),
        salience=900
    )
    def allow_apache(self, lib):
        self.declare(RecommendationFact(
            library=lib,
            reason=f"Apache 2.0 лицензия разрешена",
            priority='medium',
            approved=True
        ))