# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 16:58:23 2021

@author: Samson NZUMGUENG
"""

# importation des données
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.get_dataset_names();
df = sns.load_dataset('titanic');
df.head();
df = df.drop(['alive', 'who', 'embarked', 'class', 'deck'], axis = 1);
df.info();


# visualisation des données
sns.countplot(x='survived', data=df)
df['survived'].value_counts(normalize=True);
sns.countplot(x='pclass', data=df)
sns.countplot(x='sex', data=df)
sns.countplot(x='sibsp', data=df)
sns.countplot(x='age', data=df)
#sns.countplot(x='alone', data=df)
# Samson