import sklearn
import pandas as pd
import numpy as np
import catboost
import random
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
def get_n_best(arg_sphere, arg_numbest):
  data_bez_con=pd.read_csv('model_dataset.csv')
  data_bez_con.drop(['Unnamed: 0'], axis=1, inplace=True)
  data_bez_con.columns=list(range(0,10))
  cb=catboost.CatBoostClassifier(cat_features=[0,1,7,10])
  cb.load_model('modelcb.cbm')
  ans_d=data_bez_con.copy()
  ans_d[10]=[arg_sphere for i in range(ans_d.shape[0])]
  a=pd.read_csv('data_with_concur.csv')
  a.drop(['Unnamed: 0'], axis=1, inplace=True)
  preds=cb.predict_proba(ans_d)[:,1]
  ress=preds.argsort()[-1*arg_numbest:][::-1]
  answer=[]
  for i in ress:
    answer.append({'lat':sum(list(map(float,data_bez_con.iloc[i][0][1:-1].split(', '))))/2,
     'lng':sum(list(map(float,data_bez_con.iloc[i][1][1:-1].split(', '))))/2,
     'info':f'Оценка: {100*preds[i]}, Количество конкурентов рядом: {a.iloc[i][arg_sphere]}, Среднее количество людей в час: {round(data_bez_con.iloc[i][2],1)}, Средняя ценя аренды за год за кв. м. {data_bez_con.iloc[i][9]}'})
  return answer
