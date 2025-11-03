from experta import *

from facts import ProjectFact, RecommendationFact, LibraryFact, WarningFact


class SecurityRules:
    """Правила безопасности"""

    @Rule(
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, vulnerabilities=MATCH.vulns),
        TEST(lambda vulns: vulns and len(vulns.strip()) > 0),
        salience=800
    )
    def reject_vulnerable_library(self, lib, vulns):
        self.retract(self.get_fact(RecommendationFact, library=lib))
        self.declare(WarningFact(
            message=f"Библиотека {lib} отклонена: обнаружены уязвимости - {vulns}",
            type='security'
        ))

    @Rule(
        ProjectFact(sector=L('financial') | L('medical')),
        RecommendationFact(library=MATCH.lib),
        salience=800
    )
    def require_high_security(self, lib):
        # Для финансового и медицинского сектора требуются библиотеки с высокой репутацией
        self.modify(self.get_fact(RecommendationFact, library=lib),
                    security_required=True)

    @Rule(
        ProjectFact(sector='government'),
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, license=MATCH.license),
        TEST(lambda license: license and 'proprietary' in license.lower()),
        salience=800
    )
    def reject_proprietary_government(self, lib):
        self.retract(self.get_fact(RecommendationFact, library=lib))
        self.declare(WarningFact(
            message=f"Библиотека {lib} отклонена: государственные проекты не могут использовать проприетарные библиотеки",
            type='security'
        ))