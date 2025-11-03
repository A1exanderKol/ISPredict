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
        # Находим и удаляем рекомендацию
        recommendation = self.find_recommendation_fact(lib)
        if recommendation:
            self.retract(recommendation)
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
        # Для финансового и медицинского сектора просто добавляем пометку
        self.declare(RecommendationFact(
            library=lib,
            reason="Высокие требования безопасности",
            priority='high',
            security_required=True
        ))

    @Rule(
        ProjectFact(sector='government'),
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, license=MATCH.license),
        TEST(lambda license: license and 'proprietary' in license.lower()),
        salience=800
    )
    def reject_proprietary_government(self, lib, license):
        recommendation = self.find_recommendation_fact(lib)
        if recommendation:
            self.retract(recommendation)
        self.declare(WarningFact(
            message=f"Библиотека {lib} отклонена: государственные проекты не могут использовать проприетарные библиотеки",
            type='security'
        ))