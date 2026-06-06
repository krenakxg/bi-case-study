import sqlite3
import pandas as pd


def data_loading(model_dict: dict[str, pd.DataFrame]):


    conn = sqlite3.connect('ENGINE_OPS.db')
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute("DROP TABLE IF EXISTS fact_engine_operations;")
    cursor.execute("DROP TABLE IF EXISTS dim_engine_attr;")
    cursor.execute("DROP TABLE IF EXISTS dim_dates;")
    cursor.execute("DROP TABLE IF EXISTS dim_issue_types;")
    cursor.execute("DROP TABLE IF EXISTS dim_resting_result;")

    cursor.execute("""
    CREATE TABLE dim_engine_attr (
        engine_attr_key INTEGER PRIMARY KEY,
        engine_id TEXT,
        pist_m INTEGER,
        number_tc INTEGER,
        past_dmg INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE dim_dates (
        timestamp_key TEXT PRIMARY KEY,
        full_date TEXT,
        year INTEGER,
        month INTEGER,
        day INTEGER,
        day_of_week TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE dim_issue_types (
        issue_type_key INTEGER PRIMARY KEY,
        issue_name TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE dim_resting_result (
        resting_result_key INTEGER PRIMARY KEY,
        result_status TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE fact_engine_operations (
        operation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        engine_attr_key INTEGER,
        timestamp_key TEXT,
        issue_type_key INTEGER,
        resting_result_key INTEGER,
        oph INTEGER,
        bmep REAL,
        ng_imp INTEGER,
        rpm_max INTEGER,
        full_load_issues INTEGER,
        number_up INTEGER,
        op_set_1 REAL,
        op_set_2 REAL,
        op_set_3 REAL,
        breakdown INTEGER,
        FOREIGN KEY (engine_attr_key) REFERENCES dim_engine_attr(engine_attr_key),
        FOREIGN KEY (timestamp_key) REFERENCES dim_dates(timestamp_key),
        FOREIGN KEY (issue_type_key) REFERENCES dim_issue_types(issue_type_key),
        FOREIGN KEY (resting_result_key) REFERENCES dim_resting_result(resting_result_key)
    );
    """)

    conn.commit()

    for name, table in model_dict.items():
        table.to_sql(name, conn, if_exists="append", index=False)

    conn.commit()
    conn.close()

