
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
import svs
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


def prepare_data(genelist, prediction_type,df1,df2):
    # choose the targeted cols(genes)
    new_df = df1[genelist]
    if prediction_type == 'cancer_vs_normal':
        X = new_df
        # extract the labels and expreession data for all patient
        normaltissue_index = new_df[df1['Sample Type']=='Solid Tissue Normal'].index.to_numpy()
        cancertissue_index = new_df[df1['Sample Type']!='Solid Tissue Normal'].index.to_numpy()
        y = np.zeros((1,len(X)))[0]
        y[normaltissue_index]=0
        y[cancertissue_index]=1

        print("There are", len(X), "samples in total.",len(y[normaltissue_index]),
            "normal samples vs", len(y[cancertissue_index]),"cancer samples.","\n")
    if prediction_type == 'highrisk_vs_lowrisk':
        X = df2[genelist]
        y = np.zeros((1,len(X)))[0]
        # in the file 'risk_expression_data.txt', the first 73 patients are high risk and the other 73 patients are low risk.
        y[:73]=1
        y[73:]=0
        print("There are", len(X), "samples in total."
            "73 low risk samples vs","73 high risk samples.","\n")
    return X,y


def Classification_Performace(X,y, classifier_name,genelist):
    if classifier_name == 'Random_Forest':
        clf = RandomForestClassifier()
#     if classifier_name == 'Neural_Network':      ### this one always cannot converge and don't support RFECV
#         clf = MLPClassifier()
#     if classifier_name == 'K_nearest_neighbor':  ### this one do support RFECV
#         clf = KNeighborsClassifier(3)
#     if classifier_name == 'Naive_Bayes':         ### this one do support RFECV
#         clf = GaussianNB()
    if classifier_name == 'Logistic_Regression':
        clf = LogisticRegression()
    if classifier_name == 'SVM': 
        clf = SVC(kernel='sigmoid')
    results = cross_validate(clf, X, y, cv=10,scoring=['balanced_accuracy','average_precision','f1_weighted','roc_auc'])
    s1 = np.mean(results['test_balanced_accuracy'])
    s2 = np.mean(results['test_average_precision'])
    s3 = np.mean(results['test_f1_weighted'])
    s4 = np.mean(results['test_roc_auc'])

  # metrics = results['test_score']
  print('The classifier is:', classifier_name,"\n", "The genes you chose are:","\n",genelist,"\n","\n",
  "The metrics of the classifer with those specific genes are:","\n","\n",
        "balanced_accuracy:", s1,"\n",
        'average_precision:', s2,"\n",
        'f1_weighted:', s3,"\n",
        'roc_auc:', s4  )
  return s1, s2, s3, s4



def second_feature_selection(final_genelist,model_name,X,y):
    if len(final_genelist)>10:
        print("There are more than 10 features to evaluate, it might take several minutes!")
    if classifier_name == 'Random_Forest':
        clf = RandomForestClassifier()
    if classifier_name == 'Logistic_Regression':
        clf = LogisticRegression()
    if classifier_name == 'SVM': 
        clf = SVC(kernel='sigmoid')
    rfecv = RFECV(estimator=clf, step=1, cv=10,scoring='balanced_accuracy')
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



if __name__ == '__main__':
    # First, identify which kind of prediction types the user want
  # the prediction type is either 'cancer_vs_normal' or "highrisk_vs_lowrisk"
    print("Pleas choose the prediction type: 'cancer_vs_normal' or 'highrisk_vs_lowrisk'")
    prediction_type = sys.argv[1]
    
  # The classifier "Random_Forest", 'Logistic_Regression' and 'SVM' are included.
    print("Please choose the classifcation model: 'Random_Forest' or 'Logistic_Regression' or 'SVM'")
    classifier_name = sys.argv[2]
  # After specify the prediction_type and classification model name, choose the genes you want to study from the 
  # correpsondig ranked genes list(get from the result of GSEA)
#     ?????????????????????/ how to pass a list as command line in python
    genelist = sys.argv[3]
#     genelist = ['AAAS','ERAS','MPO','BTBD2','MYG1']
  # genelist = ['MPO', 'BTBD2', 'MYG1', 'AMH', 'PCBP2']
  # genelist = ['GADD45G','SFRP5','ARNT2','CUEDC2','H1-10']

  # load the data
    print('###Loading data, it might take 2 minutes!###',"\n")
    df1 = pd.read_csv('filtered_all_data_merged.csv', dtype = object)
    df2 = pd.read_csv('risk_expression_data.txt',sep = '\t')
    df2 = df2.iloc[:,1:].T
    df2 = df2.drop(['DESCRIPTION'])
    new_columns = df2.loc['NAME']
    df2 = pd.DataFrame(data=df2.iloc[1:,0:].to_numpy(),columns=new_columns )
    print("###Finish loading data, start data preprocessing!###","\n")
    # preprocessing the data
    X,y = prepare_data(genelist,prediction_type,df1,df2 )
    print("###Finish data preprocessing, start classification!###","\n")
    
    s1,s2,s3,s4 = Classification_Performace(X,y, classifier_name,genelist)
    x = ['Balanced accuracy','Average precision','f1 weighted','roc auc']
    fig, ax = plt.subplots()
    ax.plot(x, all_results[0], '-b', label='genelist1')
    # ax.plot(x, all_results[1], '--r', label='genelist2')
    # ax.plot(x, all_results[2], '--y', label='genelist3')
    plt.ylabel(classifier_name +'  metrics')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.show()
    
    final_genelist = sys.argv[4]
    second_feature_selection(final_genelist,classifier_name,X,y)
    
    
    
# def create_model(model_type, genes):
#     print("In create model.")
#     print("\tType: ", model_type)
#     print("\tGenes: ", genes)

#     # TODO: write this method
   

#     # TODO: what do we want to return to the UI?

#     return {"metrics": {"ACC": .70, "F1": .57}, "model": model_type, "genes": genes}
    
