import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

import json

# gridsearchCV throws lots of warnings so supress bc not critical
import warnings

def warn(*args, **kwargs):
    pass
warnings.warn = warn

'''
data_df has [bcr_patient_barcode, death_days_to, y_is_tumor, GENES...]

NOTE: death_days_to = 1_000_000 means they are censored and didnt die in data

'''
def prepare_data(data_df, genelist, prediction_type, day_threshold=600):
    X = data_df[genelist]

    if prediction_type == 'normal_vs_tumor': # 0 = normal, 1 = tumor
        y = data_df["y_is_tumor"] 

    if prediction_type == 'lowrisk_vs_highrisk': # 0 is low risk, 1 = high risk
        y = (data_df["death_days_to"] < day_threshold).astype(int)
        
    return X, y

'''
TODO: add class_weight to hyperparameter search 

'''
def train_model(X, y, classifier_name, scoring=["f1_weighted", "balanced_accuracy"]):
    X = (X - X.mean()) / X.std()
        
    if classifier_name == 'RF':
        clf = RandomForestClassifier()
    if classifier_name == 'NN':
        clf = MLPClassifier()
    if classifier_name == 'DT':
        clf = DecisionTreeClassifier()
    if classifier_name == 'LR':
        clf = LogisticRegression()
    if classifier_name == "SVM":
        clf = SVC()
        
    params = {
        "RF": {"n_estimators": [10, 100], "criterion": ["gini", "entropy"]},
        "NN": {"hidden_layer_sizes": [(100), (50, 25), (100, 50)], "learning_rate_init": [.01, .001], "max_iter": [100]},
        "DT": {"max_depth": [None, 10]},
        "LR": {"penalty": ["l1", "l2", "elasticnet"], "solver": ["lbfgs", "saga"], "l1_ratio":[.5], "max_iter":[200]},
        "SVM": {"kernel": ["linear", "poly", "rbf",]}
    }
    
    # evaluates with both scoring metrics but selects the best_model with the first
    cv = GridSearchCV(clf, params[classifier_name], scoring=scoring, refit=scoring[0], cv=5)
    cv.fit(X, y)
    
    # best estimator
    best_clf = cv.best_estimator_
    
    # get average metrics
    metric_df = pd.DataFrame(cv.cv_results_)
    metrics = {}
    
    for m in scoring:
        _val = metric_df[metric_df[f"rank_test_{scoring[0]}"] == 1][f"mean_test_{m}"].values[0]
        metrics[m] = _val
        
    return best_clf, metrics


'''
TODO change this to Get feature importance for any model

'''
def get_feature_importance(final_genelist, model_name, X, y):
    ...



'''

TODO: yuying create survival analysis curve https://drive.google.com/file/d/1CZZ__yCDHblV_K3DeU5SiK0ty72IAaFr/view

df_2["days_to_initial_pathologic_diagnosis"] -- all 0's

df_2["death_days_to"] -- at what time step did death happen (or never happen if [Not Applicable])

use these to creat Kaplan meier curve with below data
    df["death_days_to", "model_output"] 
    model output is either 1/0

'''
def get_survival_curve():
    # load the data
    df = pd.read_csv('model_input_data.csv')
    # split the data according to model_output
    df= df.iloc[:,:3]
    df['model_output'] = model_output
    group_0 = df[df['model_output']==0]
    group_1 = df[df['model_output']==1]
    # build event table
    event_table_0 = build_event_table(group_0)
    event_table_1 = build_event_table(group_1)
    # plot the curve
    x = np.arange(0,4962)
    plt.plot(x,event_table0['p'])
    plt.plot(x,event_table1['p'])
    plt.title('The Kaplan-Meier Estimate')
    plt.show()

# function to build_event_table, which will be used by get_survival_curve()
def build_event_table(group_data):
    #the max day is 4961
    event_table = pd.DataFrame(data=np.zeros((4962,2)), columns=['event','at_risk'])
    event_table.index.name = 'days'
    start_at_risk = len(group_data)
    
    for i in range(len(event_table)):
        if i ==0:
            event_table.iloc[i][1]=start_at_risk
        else:
            event_table.iloc[i][1]= event_table.iloc[i-1][1]-event_table.iloc[i-1][0]
            event_num = len(group_data[group_data['death_days_to']==i])
            event_table.iloc[i][0]=event_num
    event_table['difference'] = event_table['at_risk']-event_table['event']
    all_st = []
    all_p = []
    
    for j in range(len(event_table)):
        st = event_table.iloc[j,2]/event_table.iloc[j,1]
        all_st.append(st)
        if j==0:
            p = 1
        else:
            p = p*st
            all_p.append(p)
    event_table['st']=all_st
    event_table['p']=all_p
    return event_table

'''
classifier_name: 'Random_Forest', 'Logistic_Regression' and 'SVM'
prediction_type: 'cancer_vs_normal' or 'highrisk_vs_lowrisk'
genelist: list of gene names, e.g. ['AAAS','ERAS','MPO','BTBD2','MYG1']

'''
def run_model_creation(data_df, classifier_name, prediction_type, genelist, day_thresh):
    print("In create model.")
    print("\tModel Type: ", classifier_name)
    print("\tOutput variable: ", prediction_type)
    print("\tGenes: ", genelist)
    print("\tData looks like: ", data_df.shape)

    X, y = prepare_data(data_df, genelist, prediction_type, day_threshold=day_thresh)

    # scoring = ["f1_weighted", "balanced_accuracy"]
    best_clf, metrics_dict = train_model(X, y, classifier_name) #, scoring) 

    predictions = best_clf.predict(X)

    # feat_importance = get_feature_importance(clf, X, y, ...)

    response = {"metrics": metrics_dict,  "predictions": predictions.tolist()}
    json_res = json.dumps(response)
    print(json_res)
    return json_res

