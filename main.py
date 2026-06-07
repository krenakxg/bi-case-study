from functions.data_cleaning import data_cleaning
from functions.data_modeling import data_modeling


def main():
    

    input_file = r'analysis/BI Fullstack case study dataset.csv'
    df = data_cleaning(input_file)
    data_modeling(df)
    
    
if __name__ == "__main__":
    main()
