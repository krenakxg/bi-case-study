import pandas as pd
import pantab

def data_modeling(df: pd.DataFrame):
    

    #creating dimension tables
        # combustion issue dimension
    dim_issue_types = pd.DataFrame([
        {"issue_type_key": 1, "issue_name": "Typical issue"},
        {"issue_type_key": 2, "issue_name": "Atypical issue"},
        {"issue_type_key": 3, "issue_name": "Non-related"},
        {"issue_type_key": 4, "issue_name": "Non-symptomatic"}
    ])

        # resting analysis dimension
    dim_resting_result = pd.DataFrame([
        {"resting_result_key": 0, "result_status": "Normal"},
        {"resting_result_key": 1, "result_status": "Abnormal"},
        {"resting_result_key": 2, "result_status": "Critical"}
    ])

        # engine attributes
    engine_attr = df[['engine_id', 'pist_m', 'number_tc', 'past_dmg']].drop_duplicates()
    engine_attr = engine_attr.reset_index(drop=True)
    engine_attr['engine_attr_key'] = engine_attr.index + 1
    dim_engine_attr = engine_attr[['engine_attr_key', 'engine_id', 'pist_m', 'number_tc', 'past_dmg']]

        # date table
    dim_dates = pd.DataFrame({'timestamp': df['timestamp'].unique()})
    dim_dates['timestamp_key'] = dim_dates['timestamp'].astype(str)
    dim_dates['full_date'] = dim_dates['timestamp'].dt.date.astype(str)
    dim_dates['year'] = dim_dates['timestamp'].dt.year
    dim_dates['month'] = dim_dates['timestamp'].dt.month
    dim_dates['day'] = dim_dates['timestamp'].dt.day
    dim_dates['day_of_week'] = dim_dates['timestamp'].dt.day_name()
    dim_dates = dim_dates.drop(columns=['timestamp'])

    # creating the fact table
    fct_df = df.merge(engine_attr, on=['engine_id', 'pist_m', 'number_tc', 'past_dmg'], how='left')
    fct_df['timestamp_key'] = fct_df['timestamp'].astype(str)
    fct_df = fct_df.rename(columns={'issue_type': 'issue_type_key','resting_analysis_results': 'resting_result_key'})
    fct_col = ['engine_attr_key', 'timestamp_key', 'issue_type_key', 'resting_result_key',
                    'oph', 'bmep', 'ng_imp', 'rpm_max', 'full_load_issues', 'number_up', 
                    'op_set_1', 'op_set_2', 'op_set_3', 'breakdown']
    fct_engine_ops = fct_df[fct_col].copy()

    fct_engine_ops = fct_engine_ops.reset_index(drop=True)
    fct_engine_ops.insert(0, 'engine_ops_key', fct_engine_ops.index + 1)

    model_dict={
        "dim_issue_types": dim_issue_types,
        "dim_resting_result": dim_resting_result,
        "dim_engine_attr": dim_engine_attr,
        "dim_dates": dim_dates,
        "fact_engine_operations": fct_engine_ops
        }
    
    hyper = 'ENGINE_OPS.hyper'
    pantab.frames_to_hyper(model_dict, hyper)