import argparse
import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
import boto3

def download_data_from_s3(s3_uri, local_path):
    """Download a file from S3 to a local directory."""
    bucket_name, key = s3_uri.replace("s3://", "").split("/", 1)
    s3 = boto3.client('s3')
    os.makedirs(local_path, exist_ok=True)
    local_file_path = os.path.join(local_path, key.split("/")[-1])
    s3.download_file(bucket_name, key, local_file_path)
    return local_file_path

if __name__ == '__main__':
    # Parse input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--max_depth', type=int, default=5)
    parser.add_argument('--criterion', type=str, default='gini')
    parser.add_argument('--min_samples_split', type=int, default=2)
    parser.add_argument('--min_samples_leaf', type=int, default=1)
    parser.add_argument('--train_data', type=str, default='')  # S3 path for training data
    parser.add_argument('--val_data', type=str, default='')    # S3 path for validation data
    args = parser.parse_args()

    # Download training and validation data from S3
    train_file = download_data_from_s3(args.train_data, '/opt/ml/input/data/train')
    val_file = download_data_from_s3(args.val_data, '/opt/ml/input/data/val')

    # Load the data into Pandas DataFrames
    train_data = pd.read_csv(train_file)
    val_data = pd.read_csv(val_file)

    # Split features and target
    X_train = train_data.drop('isFraud', axis=1)  # Replace 'target' with your target column name
    y_train = train_data['isFraud']

    X_val = val_data.drop('isFraud', axis=1)
    y_val = val_data['isFraud']

    # Train Decision Tree model
    model = DecisionTreeClassifier(
        max_depth=args.max_depth,
        criterion=args.criterion,
        min_samples_split=args.min_samples_split,
        min_samples_leaf=args.min_samples_leaf,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Validate the model
    predictions = model.predict(X_val)
    accuracy = accuracy_score(y_val, predictions)
    print(f'Validation Accuracy: {accuracy}')

    # Save the model
    model_dir = '/opt/ml/model'  # SageMaker default model output directory
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(model, os.path.join(model_dir, 'model.joblib'))
