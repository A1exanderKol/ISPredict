from experta import Rule

from facts import ProjectFact, RecommendationFact


class DevOpsRules:
    """Правила для DevOps и инфраструктуры"""

    @Rule(ProjectFact(need_ci_cd=True))
    def recommend_ci_cd(self):
        self.declare(RecommendationFact(
            library='Jenkins',
            reason='CI/CD Automation',
            priority='high'
        ))
        self.declare(RecommendationFact(
            library='GitHub Actions',
            reason='Cloud-native CI/CD',
            priority='high'
        ))

    @Rule(ProjectFact(need_containerization=True))
    def recommend_containers(self):
        self.declare(RecommendationFact(
            library='Docker',
            reason='Application Containerization',
            priority='high'
        ))
        self.declare(RecommendationFact(
            library='Podman',
            reason='Daemonless Containers',
            priority='medium'
        ))

    @Rule(ProjectFact(need_orchestration=True))
    def recommend_orchestration(self):
        self.declare(RecommendationFact(
            library='Kubernetes',
            reason='Container Orchestration',
            priority='high'
        ))
        self.declare(RecommendationFact(
            library='Docker Swarm',
            reason='Simple Orchestration',
            priority='low'
        ))

    @Rule(ProjectFact(need_monitoring=True))
    def recommend_monitoring(self):
        self.declare(RecommendationFact(
            library='Prometheus',
            reason='Metrics Collection',
            priority='high'
        ))
        self.declare(RecommendationFact(
            library='Grafana',
            reason='Monitoring Dashboards',
            priority='high'
        ))

    @Rule(ProjectFact(need_logging=True))
    def recommend_logging(self):
        self.declare(RecommendationFact(
            library='ELK Stack',
            reason='Centralized Logging',
            priority='high'
        ))

    @Rule(ProjectFact(need_infrastructure=True))
    def recommend_infrastructure(self):
        self.declare(RecommendationFact(
            library='Terraform',
            reason='Infrastructure as Code',
            priority='high'
        ))
        self.declare(RecommendationFact(
            library='Ansible',
            reason='Configuration Management',
            priority='medium'
        ))

    @Rule(ProjectFact(cloud_platform='aws'))
    def recommend_aws_tools(self):
        self.declare(RecommendationFact(
            library='AWS SDK',
            reason='AWS Cloud Integration',
            priority='high'
        ))
        self.declare(RecommendationFact(
            library='Boto3',
            reason='Python + AWS',
            priority='high'
        ))

    @Rule(ProjectFact(cloud_platform='azure'))
    def recommend_azure_tools(self):
        self.declare(RecommendationFact(
            library='Azure SDK',
            reason='Microsoft Azure Integration',
            priority='high'
        ))

    @Rule(ProjectFact(cloud_platform='gcp'))
    def recommend_gcp_tools(self):
        self.declare(RecommendationFact(
            library='Google Cloud SDK',
            reason='GCP Integration',
            priority='high'
        ))