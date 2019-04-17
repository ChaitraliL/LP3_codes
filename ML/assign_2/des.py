import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.tree import export_graphviz
from subprocess import call
import matplotlib.pyplot as plt

def load_dataset():
    path = "/home/chaitrali/Desktop/LP3-421075/ML/assign_2/lipstickdata.csv"
    df = pd.read_csv(path,usecols = ['AGE','INCOME','GENDER','MS','BUYS'])
    return df

def labelEncode(df):
    for column in df.columns:
        if df[column].dtype == type(object):
            le = preprocessing.LabelEncoder()
            df[column] = le.fit_transform(df[column])
            print(le.classes_)
    return df

def split_dataset(df):
    X = df.values[:,0:4]
    Y = df.values[:,-1]
    return train_test_split(X, Y, test_size = 0.2, random_state = 42)

def create_model(x_train, y_train, gini):
    if gini == "True":
        clf = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth = 3, min_samples_leaf = 5)
        clf.fit(x_train, y_train)
    else:
        clf = DecisionTreeClassifier(criterion = "entropy", random_state = 100, max_depth = 3, min_samples_leaf = 5)
        clf.fit(x_train, y_train)
    return clf

def predict(clf, x_test):
    return clf.predict(x_test)

def modelEvaluation(y_test, y_predict):
    print("test data labels:", y_test)
    print("test data predictions:", y_predict)
    print("Confusion Matrix: ", confusion_matrix(y_test, y_predict))
    print ("Accuracy : ", accuracy_score(y_test,y_predict)*100)
    print("Report : ", classification_report(y_test, y_predict))

def visualiseTree(clf):
    export_graphviz(clf, out_file='tree.dot', feature_names = ['AGE','INCOME','GENDER','MS'],
                class_names = ['NO','YES'],
                rounded = True, proportion = False, precision = 2, filled = True)
    call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])

    plt.figure(figsize = (14, 18))
    plt.imshow(plt.imread('tree.png'))
    plt.axis('off')
    plt.show()

    call(['rm','-f','tree.dot','tree.png'])

def main():
    df = load_dataset()
    df = labelEncode(df)

    x_train, x_test, y_train, y_test = split_dataset(df)
    clf = create_model(x_train, y_train, gini = "True")
    impurity = clf.tree_.impurity
    print('impurity: ',impurity)
    y_predict = predict(clf, x_test)
    modelEvaluation(y_test, y_predict)
    visualiseTree(clf)
    y = [['<21','low','female','married']]
    y = pd.DataFrame(data=y)
    y = labelEncode(y)
    print(predict(clf,y))

    # test on whole dataset
    # x = df.values[:,0:4]
    # y = df.values[:,-1]
    # clf = create_model(x, y, gini = "True")
    # y_predict = predict(clf, x)
    # modelEvaluation(y, y_predict)

if __name__ == "__main__":
    main()
