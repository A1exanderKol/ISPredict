from experta import Rule

from facts import ProjectFact, RecommendationFact


class DevOpsRules:
    """Правила для DevOps и инфраструктуры"""

    @Rule(
        ProjectFact(need_ci_cd=True),
        salience=750
    )
    def recommend_ci_cd_tools(self):
        self.declare(RecommendationFact(
            library='Jenkins',
            reason='Система непрерывной интеграции и доставки',
            priority='medium'
        ))

    @Rule(
        ProjectFact(need_ci_cd=True),
        ProjectFact(cloud_platform='github'),
        salience=750
    )
    def recommend_github_actions(self):
        self.declare(RecommendationFact(
            library='GitHub Actions',
            reason='CI/CD для проектов на GitHub',
            priority='high'
        ))

    @Rule(
        ProjectFact(need_containerization=True),
        salience=750
    )
    def recommend_docker(self):
        self.declare(RecommendationFact(
            library='Docker',
            reason='Контейнеризация приложения',
            priority='high'
        ))

    @Rule(
        ProjectFact(need_orchestration=True),
        salience=750
    )
    def recommend_kubernetes(self):
        self.declare(RecommendationFact(
            library='Kubernetes',
            reason='Оркестрация контейнеров',
            priority='high'
        ))

    @Rule(
        ProjectFact(need_monitoring=True),
        salience=750
    )
    def recommend_monitoring(self):
        self.declare(RecommendationFact(
            library='Prometheus',
            reason='Мониторинг и оповещения',
            priority='medium'
        ))

    @Rule(
        ProjectFact(need_logging=True),
        salience=750
    )
    def recommend_logging(self):
        self.declare(RecommendationFact(
            library='ELK Stack',
            reason='Централизованное логирование',
            priority='medium'
        ))

    @Rule(
        ProjectFact(need_config_management=True),
        salience=750
    )
    def recommend_config_management(self):
        self.declare(RecommendationFact(
            library='Ansible',
            reason='Управление конфигурациями',
            priority='medium'
        ))

    @Rule(
        ProjectFact(cloud_platform='aws'),
        salience=750
    )
    def recommend_aws_tools(self):
        self.declare(RecommendationFact(
            library='AWS SDK',
            reason='Инструменты для Amazon Web Services',
            priority='medium'
        ))

    @Rule(
        ProjectFact(cloud_platform='azure'),
        salience=750
    )
    def recommend_azure_tools(self):
        self.declare(RecommendationFact(
            library='Azure SDK',
            reason='Инструменты для Microsoft Azure',
            priority='medium'
        ))