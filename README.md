# BI Case Study


### Data Model
#### Dimension tables
- **dim_issue_types** - Combustion issue types 
- **dim_resting_result** - Resting results after each engine operation 
- **dim_engine_attr** - Attributes (e.g. ID)/physical charachteristics (e.g. piston material) related to the specific engine
- **dim_dates** - Date table
#### Fact table
- **fct_engine_operations** - Metrics related to each specific engine operation

## Additional information on the development process (data quality checks, EDA) can be found in the Jupyter notebook file.

## Steps
### 1. Run the python function
```bash
# Install dependencies
pip install -r requirements.txt
# Run pipeline
python main.py
```
This will:
1. Load and clean raw engine operation data
2. Design the data model
3. Export data model to **.hyper** for Tableau data ingestion
   
### 2. Open Tableau

