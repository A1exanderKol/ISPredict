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
        self.retract_recommendation(lib)
        self.declare(WarningFact(
            message=f"Библиотека {lib} отклонена: обнаружены уязвимости - {vulns}",
            type='security',
            severity='critical'
        ))

    @Rule(
        ProjectFact(sector=L('financial') | L('medical') | L('government')),
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, reputation=MATCH.rep),
        TEST(lambda rep: rep < 8),
        salience=800
    )
    def require_high_reputation_sensitive_sectors(self, lib, rep):
        self.retract_recommendation(lib)
        self.declare(WarningFact(
            message=f"Библиотека {lib} отклонена: репутация {rep}/10 недостаточна для чувствительного сектора",
            type='security',
            severity='high'
        ))

    @Rule(
        ProjectFact(requires_encryption=True),
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, category=MATCH.category),
        TEST(lambda category: category and any(
            crypto in category.lower() for crypto in ['crypto', 'encryption', 'security'])),
        salience=800
    )
    def prefer_crypto_libraries(self, lib):
        # Создаем новую рекомендацию с высоким приоритетом
        self.declare(RecommendationFact(
            library=lib,
            reason="Криптографическая библиотека для требований шифрования",
            priority='high'
        ))

    @Rule(
        ProjectFact(handles_pii=True),
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, developer=MATCH.dev),
        TEST(
            lambda dev: dev and any(trusted in dev.lower() for trusted in ['microsoft', 'google', 'apache', 'oracle'])),
        salience=800
    )
    def prefer_trusted_developers_pii(self, lib):
        # Создаем новую рекомендацию с высоким приоритетом
        self.declare(RecommendationFact(
            library=lib,
            reason="Библиотека от доверенного разработчика для работы с PII",
            priority='high'
        ))

    def warn_outdated_internet_facing(self, lib, update):
        self.declare(WarningFact(
            message=f"Библиотека {lib} не обновлялась с {update} года - риск для интерфейсного приложения",
            type='security',
            severity='medium'
        ))

    @Rule(
        ProjectFact(sector='financial'),
        salience=800
    )
    def require_financial_security_standards(self):
        self.declare(RecommendationFact(
            library='OWASP Security Standards',
            reason='Требования безопасности для финансового сектора',
            priority='high'
        ))

    @Rule(
        ProjectFact(compliance_requirements=True),
        salience=800
    )
    def recommend_compliance_tools(self):
        self.declare(RecommendationFact(
            library='Compliance Check Tools',
            reason='Инструменты для проверки соответствия стандартам',
            priority='medium'
        ))