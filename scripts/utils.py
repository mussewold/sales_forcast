# data_utils.py
import pandas as pd

def load_data(test_file, store_file, sample_submission_file, train_file):
    """Load datasets from the given file paths."""
    test_data = pd.read_csv(test_file)
    store_data = pd.read_csv(store_file)
    sample_submission = pd.read_csv(sample_submission_file)
    train_data = pd.read_csv(train_file)
    return test_data, store_data, sample_submission, train_data

#def merge_data(test_data, store_data, sample_submission, train_data):
    """Merge test and train data with store data and sample submission."""
    merged_test_data = pd.merge(test_data, store_data, on='Store', how='left')
    merged_train_data = pd.merge(train_data, store_data, on='Store', how='left')
    final_test_data = pd.merge(merged_test_data, sample_submission, on='Id', how='left')
    final_merged_data1 = pd.concat([merged_train_data, final_test_data], ignore_index=True)
    return final_merged_data1