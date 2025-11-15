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
        self.retract_recommendation(lib)
        self.declare(WarningFact(
            message=f"Библиотека {lib} отклонена: GPL лицензия не подходит для коммерческого проекта",
            type='license',
            severity='high'
        ))

    @Rule(
        RecommendationFact(library=MATCH.lib),
        ProjectFact(license_type='commercial'),
        LibraryFact(name=MATCH.lib, license='AGPL'),
        salience=900
    )
    def reject_agpl_commercial(self, lib):
        self.retract_recommendation(lib)
        self.declare(WarningFact(
            message=f"Библиотека {lib} отклонена: AGPL лицензия требует открытия исходного кода",
            type='license',
            severity='high'
        ))

    @Rule(
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, license=L('MIT') | L('BSD') | L('Apache 2.0') | L('ISC')),
        salience=900
    )
    def allow_permissive_licenses(self, lib):
        # Вместо модификации создаем новую рекомендацию
        self.declare(RecommendationFact(
            library=lib,
            reason="Разрешительная лицензия",
            priority='high',
            license_approved=True
        ))

    @Rule(
        RecommendationFact(library=MATCH.lib),
        ProjectFact(sector='government'),
        LibraryFact(name=MATCH.lib, license=MATCH.license),
        TEST(lambda license: license and 'proprietary' in license.lower()),
        salience=900
    )
    def reject_proprietary_government(self, lib, license):
        self.retract_recommendation(lib)
        self.declare(WarningFact(
            message=f"Библиотека {lib} отклонена: государственные проекты требуют открытого ПО",
            type='license',
            severity='high'
        ))

    @Rule(
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, license=MATCH.license),
        TEST(lambda license: license and 'copyleft' in license.lower()),
        salience=900
    )
    def warn_copyleft(self, lib, license):
        self.declare(WarningFact(
            message=f"Библиотека {lib} имеет copyleft лицензию ({license}) - могут быть ограничения",
            type='license',
            severity='medium'
        ))

    @Rule(
        ProjectFact(license_type='open_source'),
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, license=MATCH.license),
        TEST(lambda license: license and any(
            open_license in license for open_license in ['MIT', 'BSD', 'Apache', 'GPL'])),
        salience=900
    )
    def prefer_osi_approved(self, lib):
        # Просто создаем новую рекомендацию с высоким приоритетом
        self.declare(RecommendationFact(
            library=lib,
            reason="OSI approved open source license",
            priority='high',
            license_approved=True
        ))