# FIX для совместимости с Python 3.10+
import collections
import collections.abc

collections.Mapping = collections.abc.Mapping
collections.Sequence = collections.abc.Sequence
collections.Iterable = collections.abc.Iterable

from database import DatabaseManager
from knowledge_base import KnowledgeBase
import tests


def initialize_sample_data(db_manager):
    """Инициализировать базу данных тестовыми данными согласно вашей структуре"""

    # Добавляем тестовые библиотеки


    for lib in tests.sample_libraries:
        db_manager.add_library(lib)

    print("Добавлены тестовые библиотеки")


def main():
    """Основная функция"""
    # FIX для совместимости с Python 3.10+
    import collections
    import collections.abc
    collections.Mapping = collections.abc.Mapping
    collections.Sequence = collections.abc.Sequence
    collections.Iterable = collections.abc.Iterable

    # Инициализация менеджера БД
    db_manager = DatabaseManager('dbIS.db')

    # Тестируем все проекты
    for i, project_data in enumerate(tests.test_projects):
        print(f"\n{'=' * 60}")
        print(f"ТЕСТИРОВАНИЕ ПРОЕКТА {i + 1}: {project_data['project_name']}")
        print(f"{'=' * 60}")

        # Добавляем проект в БД
        project_id = db_manager.add_project(project_data)
        print(f"Создан проект с ID: {project_id}")

        # Создаем и запускаем базу знаний
        kb = KnowledgeBase(db_manager)
        results = kb.analyze_project(project_id)

        # Выводим результаты
        print(f"\nРЕКОМЕНДАЦИИ для проекта '{project_data['project_name']}':")
        for j, rec in enumerate(results['recommendations'], 1):
            print(f"  {j}. {rec['library']} - {rec['reason']} (приоритет: {rec['priority']})")

        print(f"\n ПРЕДУПРЕЖДЕНИЯ:")
        if results['warnings']:
            for j, warning in enumerate(results['warnings'], 1):
                print(f"  {j}. {warning}")
        else:
            print("Нет предупреждений")

        print(f"\nРекомендации сохранены в базу данных для проекта #{project_id}")

    print(f"\nТЕСТИРОВАНИЕ ЗАВЕРШЕНО! Проанализировано {len(tests.test_projects)} проектов.")


if __name__ == "__main__":
    main()