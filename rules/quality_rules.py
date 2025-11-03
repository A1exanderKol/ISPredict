from experta import *

from facts import RecommendationFact, LibraryFact, WarningFact


class QualityRules:
    """Правила качества и поддержки"""

    @Rule(
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, last_update=MATCH.update),
        TEST(lambda update: update is not None and (2024 - update) > 3),
        salience=400
    )
    def reject_outdated(self, lib, update):
        self.retract(self.get_fact(RecommendationFact, library=lib))
        self.declare(WarningFact(
            message=f"Библиотека {lib} отклонена: последнее обновление было в {update} году",
            type='quality'
        ))

    @Rule(
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, stars=MATCH.stars),
        TEST(lambda stars: stars < 100),
        salience=400
    )
    def warn_low_stars(self, lib, stars):
        self.declare(WarningFact(
            message=f"Библиотека {lib} имеет мало звёзд ({stars}), требуется ручная проверка",
            type='quality'
        ))

    @Rule(
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, reputation=MATCH.rep),
        TEST(lambda rep: rep < 5),
        salience=400
    )
    def warn_low_reputation(self, lib, rep):
        self.declare(WarningFact(
            message=f"Библиотека {lib} имеет низкую репутацию ({rep}/10)",
            type='quality'
        ))

    @Rule(
        RecommendationFact(library=MATCH.lib),
        LibraryFact(name=MATCH.lib, active_community=True),
        salience=400
    )
    def boost_active_community(self, lib):
        # Повышаем приоритет для библиотек с активным сообществом
        self.modify(self.get_fact(RecommendationFact, library=lib),
                    community_support=True,
                    priority='high')