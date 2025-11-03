test_projects = [
    {
        'project_name': 'Финансовая аналитическая платформа',
        'programming_language': 'Python',
        'architecture': 'MVC',
        'description': 'Веб-платформа для анализа финансовых данных с хранением в базе данных и REST API. Коммерческий проект для банковского сектора с требованиями высокой производительности.',
        'performance_requirements': 'Высокая производительность для анализа в реальном времени',
        'security_requirements': 'Шифрование и безопасная аутентификация',
        'project_status': 'in development',
        'version': '1.0'
    },
    {
        'project_name': 'Мобильное приложение для здоровья',
        'programming_language': 'JavaScript',
        'architecture': 'SPA',
        'description': 'Мобильное приложение для отслеживания показателей здоровья с синхронизацией данных через REST API. Функциональное программирование, медицинский сектор.',
        'performance_requirements': 'Оптимизация для мобильных устройств',
        'security_requirements': 'Защита медицинских данных',
        'project_status': 'active',
        'version': '2.1'
    },

]

sample_libraries = [
        # Python библиотеки
        {
            'library_name': 'SQLAlchemy',
            'version': '2.0.0',
            'compatibility': 'Python',
            'license': 'MIT',
            'category': 'database',
            'known_vulnerabilities': '',
            'reputation': 9,
            'developer': 'SQLAlchemy Team',
            'repo_url': 'https://github.com/sqlalchemy/sqlalchemy'
        },
        {
            'library_name': 'Django',
            'version': '4.2.0',
            'compatibility': 'Python',
            'license': 'BSD',
            'category': 'web framework',
            'known_vulnerabilities': '',
            'reputation': 10,
            'developer': 'Django Software Foundation',
            'repo_url': 'https://github.com/django/django'
        },
        {
            'library_name': 'Flask',
            'version': '2.3.0',
            'compatibility': 'Python',
            'license': 'BSD',
            'category': 'web framework',
            'known_vulnerabilities': '',
            'reputation': 9,
            'developer': 'Pallets Team',
            'repo_url': 'https://github.com/pallets/flask'
        },
        {
            'library_name': 'Requests',
            'version': '2.31.0',
            'compatibility': 'Python',
            'license': 'Apache 2.0',
            'category': 'http client',
            'known_vulnerabilities': '',
            'reputation': 9,
            'developer': 'Python Software Foundation',
            'repo_url': 'https://github.com/psf/requests'
        },
        {
            'library_name': 'Pandas',
            'version': '2.0.0',
            'compatibility': 'Python',
            'license': 'BSD',
            'category': 'data analysis',
            'known_vulnerabilities': '',
            'reputation': 10,
            'developer': 'Pandas Team',
            'repo_url': 'https://github.com/pandas-dev/pandas'
        },
        {
            'library_name': 'NumPy',
            'version': '1.24.0',
            'compatibility': 'Python',
            'license': 'BSD',
            'category': 'scientific computing',
            'known_vulnerabilities': '',
            'reputation': 10,
            'developer': 'NumPy Team',
            'repo_url': 'https://github.com/numpy/numpy'
        },
        {
            'library_name': 'PyTorch',
            'version': '2.0.0',
            'compatibility': 'Python',
            'license': 'BSD',
            'category': 'machine learning',
            'known_vulnerabilities': '',
            'reputation': 9,
            'developer': 'Facebook AI Research',
            'repo_url': 'https://github.com/pytorch/pytorch'
        },
        {
            'library_name': 'FastAPI',
            'version': '0.95.0',
            'compatibility': 'Python',
            'license': 'MIT',
            'category': 'web framework',
            'known_vulnerabilities': '',
            'reputation': 9,
            'developer': 'FastAPI Team',
            'repo_url': 'https://github.com/tiangolo/fastapi'
        },
        {
            'library_name': 'Celery',
            'version': '5.3.0',
            'compatibility': 'Python',
            'license': 'BSD',
            'category': 'task queue',
            'known_vulnerabilities': '',
            'reputation': 8,
            'developer': 'Celery Team',
            'repo_url': 'https://github.com/celery/celery'
        },

        # Java библиотеки
        {
            'library_name': 'Hibernate',
            'version': '6.0.0',
            'compatibility': 'Java',
            'license': 'LGPL',
            'category': 'database',
            'known_vulnerabilities': '',
            'reputation': 8,
            'developer': 'Red Hat',
            'repo_url': 'https://github.com/hibernate/hibernate-orm'
        },
        {
            'library_name': 'Spring Boot',
            'version': '3.0.0',
            'compatibility': 'Java',
            'license': 'Apache 2.0',
            'category': 'web framework',
            'known_vulnerabilities': '',
            'reputation': 9,
            'developer': 'VMware',
            'repo_url': 'https://github.com/spring-projects/spring-boot'
        },
        {
            'library_name': 'Jackson',
            'version': '2.15.0',
            'compatibility': 'Java',
            'license': 'Apache 2.0',
            'category': 'json processing',
            'known_vulnerabilities': '',
            'reputation': 9,
            'developer': 'FasterXML',
            'repo_url': 'https://github.com/FasterXML/jackson'
        },
        {
            'library_name': 'JUnit',
            'version': '5.9.0',
            'compatibility': 'Java',
            'license': 'Eclipse Public License',
            'category': 'testing',
            'known_vulnerabilities': '',
            'reputation': 10,
            'developer': 'JUnit Team',
            'repo_url': 'https://github.com/junit-team/junit5'
        },

        # C# библиотеки
        {
            'library_name': 'Entity Framework',
            'version': '7.0.0',
            'compatibility': 'C#',
            'license': 'Apache 2.0',
            'category': 'database',
            'known_vulnerabilities': '',
            'reputation': 8,
            'developer': 'Microsoft',
            'repo_url': 'https://github.com/dotnet/efcore'
        },
        {
            'library_name': 'ASP.NET Core',
            'version': '7.0.0',
            'compatibility': 'C#',
            'license': 'MIT',
            'category': 'web framework',
            'known_vulnerabilities': '',
            'reputation': 9,
            'developer': 'Microsoft',
            'repo_url': 'https://github.com/dotnet/aspnetcore'
        },
        {
            'library_name': 'Newtonsoft.Json',
            'version': '13.0.0',
            'compatibility': 'C#',
            'license': 'MIT',
            'category': 'json processing',
            'known_vulnerabilities': '',
            'reputation': 9,
            'developer': 'James Newton-King',
            'repo_url': 'https://github.com/JamesNK/Newtonsoft.Json'
        },

        # JavaScript библиотеки
        {
            'library_name': 'Express.js',
            'version': '4.18.0',
            'compatibility': 'JavaScript',
            'license': 'MIT',
            'category': 'web framework',
            'known_vulnerabilities': '',
            'reputation': 9,
            'developer': 'Express.js Team',
            'repo_url': 'https://github.com/expressjs/express'
        },
        {
            'library_name': 'React',
            'version': '18.2.0',
            'compatibility': 'JavaScript',
            'license': 'MIT',
            'category': 'frontend framework',
            'known_vulnerabilities': '',
            'reputation': 10,
            'developer': 'Facebook',
            'repo_url': 'https://github.com/facebook/react'
        },
        {
            'library_name': 'Axios',
            'version': '1.4.0',
            'compatibility': 'JavaScript',
            'license': 'MIT',
            'category': 'http client',
            'known_vulnerabilities': '',
            'reputation': 9,
            'developer': 'Axios Team',
            'repo_url': 'https://github.com/axios/axios'
        },
        {
            'library_name': 'Lodash',
            'version': '4.17.0',
            'compatibility': 'JavaScript',
            'license': 'MIT',
            'category': 'utility library',
            'known_vulnerabilities': '',
            'reputation': 9,
            'developer': 'Lodash Team',
            'repo_url': 'https://github.com/lodash/lodash'
        },
        {
            'library_name': 'Ramda.js',
            'version': '0.28.0',
            'compatibility': 'JavaScript',
            'license': 'MIT',
            'category': 'functional programming',
            'known_vulnerabilities': '',
            'reputation': 8,
            'developer': 'Ramda Team',
            'repo_url': 'https://github.com/ramda/ramda'
        },

        # Библиотеки с проблемами (для тестирования правил)
        {
            'library_name': 'VulnerableLib',
            'version': '1.0.0',
            'compatibility': 'Python',
            'license': 'MIT',
            'category': 'general',
            'known_vulnerabilities': 'CVE-2023-12345, CVE-2023-67890',
            'reputation': 3,
            'developer': 'Unknown',
            'repo_url': ''
        },
        {
            'library_name': 'OutdatedLib',
            'version': '0.5.0',
            'compatibility': 'Python',
            'license': 'GPL',
            'category': 'general',
            'known_vulnerabilities': '',
            'reputation': 4,
            'developer': 'Abandoned Developer',
            'repo_url': ''
        },
        {
            'library_name': 'ProprietaryLib',
            'version': '2.1.0',
            'compatibility': 'Java',
            'license': 'Proprietary',
            'category': 'enterprise',
            'known_vulnerabilities': '',
            'reputation': 7,
            'developer': 'Commercial Corp',
            'repo_url': ''
        }
    ]