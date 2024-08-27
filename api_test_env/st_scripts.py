from typing import Optional

import db_management as dm
import pandas as pd
import streamlit as st

st.title('Might and Magic trainer finder')


@st.cache_data
def fetch_all_data() -> tuple[list[str]]:
    cursor = dm.connect_to_db()
    skill_data = dm.fetch_skill_name(cursor)
    prof_data = dm.fetch_proficiency_data(cursor)
    return skill_data, prof_data


skill_data, prof_data = fetch_all_data()
series_data: list[int] = [6, 7, 8]

selected_series = st.multiselect(
    'Choose "series" you play.', 
    series_data, 
    [6, 7, 8],
)
selected_skills = st.multiselect('Choose "skills" you want to see.', skill_data)
selected_proficiency = st.multiselect('Choose "proficiency" you want to see.', prof_data)


def build_query(
    selected_series: int | list[int],
    selected_skills: str | list[str],
    selected_proficiency: str | list[str],
) -> Optional[tuple[str | list[int | str]]]:
    base_query = 'SELECT * FROM trainer_data WHERE '
    params = []

    if selected_series:
        placeholders = ', '.join(['?'] * len(selected_series))
        base_query += f'series IN ({placeholders})'
        params.extend(selected_series)

    if selected_skills:
        placeholders = ', '.join(['?'] * len(selected_skills))
        base_query += f'AND skill_name IN ({placeholders})'
        params.extend(selected_skills)

    if selected_proficiency:
        placeholders = ', '.join(['?'] * len(selected_proficiency))
        base_query += f'AND proficiency_name IN ({placeholders})'
        params.extend(selected_proficiency)

    if not (selected_series or selected_skills or selected_proficiency):
        return None, []

    return base_query, params


query, params = build_query(
    selected_series=selected_series,
    selected_skills=selected_skills,
    selected_proficiency=selected_proficiency,
)

if query:
    cursor = dm.connect_to_db()
    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(results, columns=columns)
        st.table(df)
        # st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.write('Error: Please select valid contents...')
    finally:
        cursor.close()
else:
    st.write('Please select requirements.')
