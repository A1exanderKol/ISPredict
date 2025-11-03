import sqlite3
from datetime import datetime


class DatabaseManager:
    """Менеджер для работы с базой данных"""

    def __init__(self, db_path='dbIS.db'):
        self.db_path = db_path

    def get_project(self, project_id):
        """Получить проект по ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM projects WHERE id_project = ?', (project_id,))
        project = cursor.fetchone()
        conn.close()

        if project:
            columns = [description[0] for description in cursor.description]
            return dict(zip(columns, project))
        return None

    def get_all_libraries(self):
        """Получить все библиотеки"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM libraries')
        libraries = cursor.fetchall()
        conn.close()

        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, lib)) for lib in libraries]

    def get_library_by_name(self, library_name):
        """Получить библиотеку по имени"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM libraries WHERE library_name = ?', (library_name,))
        library = cursor.fetchone()
        conn.close()

        if library:
            columns = [description[0] for description in cursor.description]
            return dict(zip(columns, library))
        return None

    def get_project_libraries(self, project_id):
        """Получить библиотеки проекта"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT l.*, pl.library_status, pl.reason, pl.risk 
            FROM libraries l 
            JOIN project_libraries pl ON l.id_library = pl.id_library 
            WHERE pl.id_project = ?
        ''', (project_id,))
        libraries = cursor.fetchall()
        conn.close()

        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, lib)) for lib in libraries]

    def add_recommendation(self, project_id, library_name, reason, risk_level='low'):
        """Добавить рекомендацию в базу данных"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Найдем ID библиотеки
        cursor.execute('SELECT id_library FROM libraries WHERE library_name = ?', (library_name,))
        result = cursor.fetchone()

        if result:
            library_id = result[0]
            cursor.execute('''
                INSERT INTO project_libraries (id_project, id_library, reason, risk, library_status)
                VALUES (?, ?, ?, ?, 'active')  -- ИЗМЕНИЛИ 'recommended' на 'active'
            ''', (project_id, library_id, reason, risk_level))

        conn.commit()
        conn.close()
        return True

    def add_project(self, project_data):
        """Добавить новый проект"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO projects (
                project_name, programming_language, architecture, description,
                performance_requirements, security_requirements, error_history,
                project_status, version
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            project_data['project_name'],
            project_data['programming_language'],
            project_data.get('architecture', ''),
            project_data.get('description', ''),
            project_data.get('performance_requirements', ''),
            project_data.get('security_requirements', ''),
            project_data.get('error_history', ''),
            project_data.get('project_status', 'in development'),
            project_data.get('version', '1.0')
        ))

        project_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return project_id

    def add_library(self, library_data):
        """Добавить новую библиотеку"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO libraries (
                library_name, version, compatibility, license, category,
                known_vulnerabilities, reputation, developer, repo_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            library_data['library_name'],
            library_data['version'],
            library_data.get('compatibility', ''),
            library_data.get('license', ''),
            library_data.get('category', ''),
            library_data.get('known_vulnerabilities', ''),
            library_data.get('reputation', 5),
            library_data.get('developer', ''),
            library_data.get('repo_url', '')
        ))

        library_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return library_id

    def get_vulnerable_libraries(self):
        """Получить библиотеки с уязвимостями"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT library_name, version, known_vulnerabilities, reputation
            FROM libraries 
            WHERE known_vulnerabilities IS NOT NULL 
            AND LENGTH(TRIM(known_vulnerabilities)) > 0
        ''')
        libraries = cursor.fetchall()
        conn.close()

        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, lib)) for lib in libraries]

    def get_project_library_overview(self):
        """Получить обзор проектов и их библиотек"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                p.project_name,
                p.programming_language,
                l.library_name,
                l.version AS library_version,
                pl.added_date,
                pl.library_status,
                l.reputation,
                l.known_vulnerabilities
            FROM projects p
            JOIN project_libraries pl ON p.id_project = pl.id_project
            JOIN libraries l ON l.id_library = pl.id_library
        ''')
        results = cursor.fetchall()
        conn.close()

        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, row)) for row in results]