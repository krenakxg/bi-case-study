from functions.data_cleaning import data_cleaning
from functions.data_modeling import data_modeling
from functions.data_loading import data_loading


def main():
    

    input_file = r'input/BI Fullstack case study dataset.csv'
    df = data_cleaning(input_file)
    model_dict = data_modeling(df)
    data_loading(model_dict)
    

if __name__ == "__main__":
    main()
