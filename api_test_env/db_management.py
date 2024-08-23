import sqlite3
from sqlite3 import Cursor

import pandas as pd
from pandas import DataFrame
# データベースファイルの相対パス
relative_path = 'data/MM.db'

# プロジェクトのルートディレクトリからのフルパスを取得
db_file_path = Path(__file__).parent / relative_path



class DataBaseNotFoundError(Exception):
    """DBに接続出来なかった際に発生するエラーです。"""

    def __init__(self, message: str = 'Connection failed...') -> None:
        super().__init__(message)


def connect_to_db() -> Cursor:
    if db_file_path:
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()
        print(f'Connected to {db_file_path}')
        return cursor
    else:
        raise DataBaseNotFoundError()


def fetch_skill_name(cursor: Cursor) -> list[str]:
    cursor.execute(
        '''
                SELECT
                    skill_name
                FROM 
                    code_skill
                '''
    )
    skill_data = [row[0] for row in cursor.fetchall()]
    return skill_data


def fetch_proficiency_data(cursor: Cursor) -> list[str]:
    cursor.execute(
        '''
                SELECT
                    proficiency_name
                FROM 
                    code_proficiency
                '''
    )
    prof_data = [row[0] for row in cursor.fetchall()]
    return prof_data


def fetch_selected_data(
    cursor: Cursor,
    selected_series: str | list[str],
    selected_skills: str | list[str],
    selected_proficiency: str | list[str],
) -> DataFrame:
    cursor.execute(
        '''
                SELECT
                    proficiency_name
                FROM 
                    code_proficiency
                '''
    )
