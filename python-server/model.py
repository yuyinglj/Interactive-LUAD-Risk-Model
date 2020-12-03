

"""
Args
    model_type: one of [LR, NN, DT, RF]
    genes: a list of genes to be used as features


     f(genes) = ___ 

     outputs
        - tumor or healthy cell
        - risk (live or die at some timeframe)


    sent to UI
        - prediction per patient
        - metrics
        - Ranked feature importance

"""


import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
from itertools import compress


def prepare_data(genelist, prediction_type, df1, df2):
    # choose the targeted cols(genes)
    new_df = df1[genelist]
    if prediction_type == 'cancer_vs_normal':
        X = new_df
        # extract the labels and expreession data for all patient
        normaltissue_index = new_df[df1['Sample Type'] == 'Solid Tissue Normal'].index.to_numpy()
        # normaltissue_index = normaltissue_index[:100]
        cancertissue_index = new_df[df1['Sample Type'] != 'Solid Tissue Normal'].index.to_numpy()
        # new_X_index = np.append(normaltissue_index,cancertissue_index,axis =0)
        # X = new_df.iloc[new_X_index]
        y = np.zeros((1, len(X)))[0]
        y[normaltissue_index] = 0
        y[cancertissue_index] = 1

        print("There are", len(X), "samples in total.", len(y[normaltissue_index]),
              "normal samples vs", len(y[cancertissue_index]), "cancer samples.", "\n")
    if prediction_type == 'highrisk_vs_lowrisk':
        X = df2[genelist]
        y = np.zeros((1, len(X)))[0]
        # in the file 'risk_expression_data.txt', the first 73 patients are high risk and the other 73 patients are low risk.
        y[:73] = 1
        y[73:] = 0
        print("There are", len(X), "samples in total."
              "73 low risk samples vs", "73 high risk samples.", "\n")
    return X, y

'''
{value:"LR", label: "Linear Regression (LASSO)"},
        {value:"NN", label:"Neural Network"},
        {value: "DT", label:"Decision Tree"},
        {value:"RF", label:"Random Forest"}

'''
def train_model(X, y, classifier_name, genelist):
    if classifier_name == 'Random_Forest':
        clf = RandomForestClassifier()
    if classifier_name == 'Neural_Network':
        clf = MLPClassifier()
    if classifier_name == 'K_nearest_neighbor':
        clf = KNeighborsClassifier(3)
    if classifier_name == 'Naive_Bayes':
        clf = GaussianNB()
    if classifier_name == 'Logistic_Regression':
        clf = LogisticRegression()
    if classifier_name == 'SVM':
        clf = SVC()
    results = cross_validate(clf, X, y, cv=3, scoring=['balanced_accuracy', 'average_precision', 'f1_weighted', 'roc_auc'])

    s1 = np.mean(results['test_balanced_accuracy'])
    s2 = np.mean(results['test_average_precision'])
    s3 = np.mean(results['test_f1_weighted'])
    s4 = np.mean(results['test_roc_auc'])

    # TODO train a whole model here as well on all data and get output labels
    

    # metrics = results['test_score']
    print('The classifier is:', classifier_name, "\n", "The genes you chose are:", "\n", genelist, "\n", "\n",
          "The metrics of the classifer with those specific genes are:", "\n", "\n",
          "balanced_accuracy:", s1, "\n",
          'average_precision:', s2, "\n",
          'f1_weighted:', s3, "\n",
          'roc_auc:', s4)
    return s1, s2, s3, s4


'''
TODO change this to Get feature importance for any model


'''
def get_feature_importance(final_genelist, model_name, X, y):

    if len(final_genelist) > 10:
        print("There are more than 10 features to evaluate, it might take several minutes!")
    if classifier_name == 'Random_Forest':
        clf = RandomForestClassifier()
    if classifier_name == 'Logistic_Regression':
        clf = LogisticRegression()
    if classifier_name == 'SVM':
        clf = SVC(kernel='sigmoid')

    rfecv = RFECV(estimator=clf, step=1, cv=3, scoring='balanced_accuracy')
    rfecv.fit(X, y)

    print("Optimal number of features : %d" % rfecv.n_features_)
    selected_genes = list(compress(final_genelist, rfecv.support_))
    print("The supported genes are:", selected_genes)

    # Plot number of features VS. cross-validation scores
    plt.figure()
    plt.xlabel("Number of features selected")
    plt.ylabel("Cross validation score (nb of correct classifications)")
    plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
    plt.show()
    return selected_genes


'''

TODO: yuying create survival analysis curve https://drive.google.com/file/d/1CZZ__yCDHblV_K3DeU5SiK0ty72IAaFr/view

df_2["days_to_initial_pathologic_diagnosis"] -- all 0's

df_2["death_days_to"] -- at what time step did death happen (or never happen if [Not Applicable])

use these to creat Kaplan meier curve with below data
    df["death_days_to", "model_output"] 
    model output is either 1/0

'''
def get_survival_curve():
    ...


'''
classifier_name: 'Random_Forest', 'Logistic_Regression' and 'SVM'
prediction_type: 'cancer_vs_normal' or 'highrisk_vs_lowrisk'
genelist: list of gene names, e.g. ['AAAS','ERAS','MPO','BTBD2','MYG1']

'''
def run_model_creation(classifier_name, prediction_type, genelist):
    print("In create model.")
    print("\tModel Type: ", classifier_name)
    print("\tOutput variable: ", prediction_type)
    print("\tGenes: ", genelist)

    # TODO move this to the server
    print('###Loading data, it might take 2 minutes!###', "\n")
    df1 = pd.read_csv('filtered_all_data_merged.csv', dtype=object) # in drive
    df2 = pd.read_csv('risk_expression_data.txt', sep='\t') # in drive 
    df2 = df2.iloc[:, 1:].T
    df2 = df2.drop(['DESCRIPTION'])
    new_columns = df2.loc['NAME']
    df2 = pd.DataFrame(data=df2.iloc[1:, 0:].to_numpy(), columns=new_columns)
    print("###Finish loading data, start data preprocessing!###", "\n")

    # preprocessing the data
    X, y = prepare_data(genelist, prediction_type, df1, df2)
    print("###Finish data preprocessing, start classification!###", "\n")

    s1, s2, s3, s4 = train_model(X, y, classifier_name, genelist) # TODO get model and metrics here

    # Second Round Feature Selection
    get_feature_importance(clf, X, y, ...)

    return {"metrics": {"ACC": .70, "F1": .57},  "genes": genelist}

