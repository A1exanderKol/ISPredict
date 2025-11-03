from experta import *
from database import DatabaseManager
from facts import ProjectFact, LibraryFact, RecommendationFact, WarningFact
from rules import *

from experta import *
from database import DatabaseManager
from facts import ProjectFact, LibraryFact, RecommendationFact, WarningFact
from rules import *


class KnowledgeBase(KnowledgeEngine,
                    LanguageRules,
                    LicenseRules,
                    SecurityRules,
                    PerformanceRules,
                    IntegrationRules,
                    ParadigmRules,
                    QualityRules):

    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.recommendations = []
        self.warnings = []

    def find_recommendation_fact(self, library_name):
        """Найти факт рекомендации по имени библиотеки"""
        for fact_id, fact in self.facts.items():
            if (isinstance(fact, RecommendationFact) and
                    hasattr(fact, 'library') and
                    fact['library'] == library_name):
                return fact
        return None

    def find_library_fact(self, library_name):
        """Найти факт библиотеки по имени"""
        for fact_id, fact in self.facts.items():
            if (isinstance(fact, LibraryFact) and
                    hasattr(fact, 'name') and
                    fact['name'] == library_name):
                return fact
        return None

    # ... остальные методы без изменений (analyze_project, _load_project_data, и т.д.)

    def analyze_project(self, project_id):
        """Проанализировать проект и выдать рекомендации"""
        self.reset()
        self.recommendations.clear()
        self.warnings.clear()

        # Загружаем данные проекта из БД
        self._load_project_data(project_id)

        # Загружаем библиотеки из БД
        self._load_libraries_data()

        # Запускаем механизм вывода (прямой вывод)
        print("Запуск механизма вывода...")
        self.run()

        # Собираем результаты
        self._collect_results()

        # Сохраняем рекомендации в БД
        self._save_recommendations(project_id)

        return {
            'recommendations': self.recommendations,
            'warnings': self.warnings
        }

    def _load_project_data(self, project_id):
        """Загрузить данные проекта из БД и преобразовать в факты"""
        project = self.db_manager.get_project(project_id)
        if not project:
            raise ValueError(f"Проект с ID {project_id} не найден")

        # Анализируем описание проекта для определения требований
        description = project['description'] or ''
        requirements = self._analyze_project_requirements(description)

        # Создаем факт проекта
        project_fact_data = {
            'project_id': project['id_project'],
            'project_name': project['project_name'],
            'language': project['programming_language'],
            'architecture': project['architecture'],
            'project_status': project['project_status'],
            **requirements
        }

        self.declare(ProjectFact(**project_fact_data))
        print(f"Загружен проект: {project['project_name']} ({project['programming_language']})")

    def _load_libraries_data(self):
        """Загрузить все библиотеки из БД как факты"""
        libraries = self.db_manager.get_all_libraries()
        for lib in libraries:
            # Определяем характеристики библиотеки согласно вашей структуре БД
            lib_fact_data = {
                'name': lib['library_name'],
                'version': lib['version'],
                'license': lib['license'],
                'category': lib['category'],
                'vulnerabilities': lib['known_vulnerabilities'] or '',
                'reputation': lib['reputation'] or 5,
                'supports_oop': True,  # Большинство библиотек поддерживают ООП
                'supports_functional': 'functional' in (lib.get('category') or '').lower(),
                'supports_concurrency': any(keyword in (lib.get('category') or '').lower()
                                            for keyword in ['concurrent', 'parallel', 'async']),
                'active_community': (lib.get('reputation') or 0) >= 7,
            }

            # Определяем год последнего обновления
            if lib['update_date']:
                try:
                    lib_fact_data['last_update'] = int(lib['update_date'][:4])
                except:
                    lib_fact_data['last_update'] = 2023

            # Примерное преобразование репутации в звезды
            lib_fact_data['stars'] = (lib.get('reputation') or 5) * 1000

            self.declare(LibraryFact(**lib_fact_data))

        print(f"Загружено {len(libraries)} библиотек")

    def _analyze_project_requirements(self, description):
        """Анализировать описание проекта для определения требований"""
        desc_lower = description.lower()

        return {
            'need_db': any(keyword in desc_lower for keyword in
                           ['database', 'db', 'sql', 'data storage', 'база данных']),
            'need_web': any(keyword in desc_lower for keyword in
                            ['web', 'http', 'api', 'rest', 'website', 'веб']),
            'needs_rest_api': any(keyword in desc_lower for keyword in
                                  ['rest', 'api', 'web service', 'json api']),
            'needs_database': any(keyword in desc_lower for keyword in
                                  ['database', 'db', 'sql', 'postgres', 'mysql']),
            'sector': self._detect_sector(desc_lower),
            'project_type': self._detect_project_type(desc_lower),
            'paradigm': self._detect_paradigm(desc_lower),
            'license_type': 'commercial' if any(word in desc_lower
                                                for word in
                                                ['commercial', 'enterprise', 'business']) else 'open_source',
            'high_performance': any(keyword in desc_lower for keyword in
                                    ['high performance', 'real-time', 'low latency']),
            'concurrent': any(keyword in desc_lower for keyword in
                              ['concurrent', 'parallel', 'multithreading', 'async']),
        }

    def _detect_sector(self, description):
        """Определить сектор проекта"""
        if any(word in description for word in ['finance', 'bank', 'payment', 'financial']):
            return 'financial'
        elif any(word in description for word in ['medical', 'health', 'hospital']):
            return 'medical'
        elif any(word in description for word in ['government', 'state', 'public']):
            return 'government'
        return 'general'

    def _detect_project_type(self, description):
        """Определить тип проекта"""
        if any(word in description for word in ['mobile', 'android', 'ios']):
            return 'mobile'
        elif any(word in description for word in ['server', 'backend', 'api']):
            return 'server'
        elif any(word in description for word in ['big data', 'analytics', 'data processing']):
            return 'big_data'
        return 'general'

    def _detect_paradigm(self, description):
        """Определить парадигму программирования"""
        if any(word in description for word in ['functional', 'fp', 'immutable']):
            return 'functional'
        elif any(word in description for word in ['oop', 'object oriented', 'classes']):
            return 'OOP'
        elif any(word in description for word in ['procedural', 'structured']):
            return 'procedural'
        return 'OOP'

    def _collect_results(self):
        """Собрать результаты работы системы"""
        for fact in self.facts.values():
            if isinstance(fact, RecommendationFact):
                self.recommendations.append({
                    'library': fact['library'],
                    'reason': fact['reason'],
                    'priority': fact.get('priority', 'medium')
                })
            elif isinstance(fact, WarningFact):
                self.warnings.append(fact['message'])

    def _save_recommendations(self, project_id):
        """Сохранить рекомендации в базу данных"""
        for recommendation in self.recommendations:
            self.db_manager.add_recommendation(
                project_id,
                recommendation['library'],
                f"{recommendation['reason']} (приоритет: {recommendation['priority']})",
                'low' if recommendation['priority'] == 'low' else 'medium'
            )