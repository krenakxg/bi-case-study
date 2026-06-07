"# BI Case Study


### Data Model
#### Dimension tables
- **dim_issue_types** - Combustion issue types 
- **dim_resting_result** - Resting results after each engine operation 
- **dim_engine_attr** - Attribtues (e.g. ID)/physical charateristics (e.g. piston material) related to the specific engine.
- **dim_dates** - Date table
#### Fact table
- **fct_engine_operations** - Metrics related to each specific engine operation


## How to run

```bash
# Install dependencies
pip install -r requirements.txt
# Run pipeline
python main.py
```

This will:
1. Load and clean raw engine operation data
2. Create dimension and fact tables (Star Schema)
3. Export to Tableau Hyper format for dashboard development
