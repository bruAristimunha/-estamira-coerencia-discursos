from sklearn.model_selection import cross_val_score

#Methods
from sklearn import naive_bayes
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn import svm

def classification(X, y):
    
    decision_tree_method =  tree.DecisionTreeClassifier(random_state=42)
    svm_method = svm.SVC(random_state=42)
    naive_method = naive_bayes.GaussianNB()
    knn_method = KNeighborsClassifier()

    scores_svm = cross_val_score(svm_method, X, y, cv=10)
    print("Accuracy SVM: %0.2f (+/- %0.2f)" %(scores_svm.mean(), scores_svm.std() * 2))

    scores_naive = cross_val_score(naive_method, X, y, cv=10)
    print("Accuracy Naive: %0.2f (+/- %0.2f)" %(scores_naive.mean(), scores_naive.std() * 2))

    scores_tree = cross_val_score(decision_tree_method, X, y, cv=10)
    print("Accuracy Decision: %0.2f (+/- %0.2f)" %(scores_tree.mean(), scores_tree.std() * 2))

    scores_knn = cross_val_score(knn_method, X, y, cv=10)
    print("Accuracy KNN: %0.2f (+/- %0.2f)" %(scores_knn.mean(), scores_knn.std() * 2))

