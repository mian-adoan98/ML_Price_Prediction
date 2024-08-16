## BMW Exploratory Data Analysis

# import libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# define class called Dataset
class Dataset: 
  # load dataset
  def load_dataset(file):
    # load bmw data into notebook
    file_name = file
    bmw = pd.read_csv(file)
    return bmw

  # identify bmw data
  def identify_bmw_data(bmw_data):
    bmw.info()
    bmw_cars,bmw_features = bmw.shape
    print(f"------------------------------------------")
    print(f"Numbers of BMW Cars: {bmw_cars}")
    print(f"Numbers of BMW Features: {bmw_features}")

# data preprocessing
class DataPreprocessing: 
  def identify_null_vals(data):
    bmw_null = data.isnull().sum().t_frame()
    bmw_null = bmw_null.reset_value()
    bmw_null = bmw_null.transpose()
    return bmw_null

  def find_dupl_rows(data):
    # find duplicated rows
    dupl_rows = bmw.duplicated().sum()
    return dupl_rows  

  def remove_dupl_rows(data): 
    if find_dupl_rows(data) != 0:
      data = data.drop_duplicated()
      return 

  

