import streamlit as st
import numpy as np

from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def get_dataset(dataset_name):
    data = None

    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == "Wine":
        data = datasets.load_wine()
    elif dataset_name == "Breast Cancer":
        data = datasets.load_breast_cancer()

    X = data.data
    y = data.target

    return X, y


def add_parameter_ui(clf_name):
    params = dict()

    if clf_name == "SVM":
        C = st.sidebar.slider("C", 0.01, 10.0)
        params["C"] = C
    elif clf_name == "KNN":
        K = st.sidebar.slider("K", 1, 15)
        params["K"] = K
    elif clf_name == "Random Forest":
        max_depth = st.sidebar.slider("max_depth", 2, 15)
        params["max_depth"] = max_depth
        n_estimators = st.sidebar.slider("n_estimators", 1, 100)
        params["n_estimators"] = n_estimators

    return params


def get_classifier(clf_name, params):
    clf = None

    if clf_name == "SVM":
        clf = SVC(C=params["C"])
    elif clf_name == "KNN":
        clf = KNeighborsClassifier(n_neighbors=params["K"])
    elif clf_name == "Random Forest":
        clf = RandomForestClassifier(
            n_estimators=params["n_estimators"],
            max_depth=params["max_depth"],
            random_state=1234,
        )

    return clf


def main():
    st.subheader("Explore Different Classifiers & Datasets")

    DATASET = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine"))
    CLASSIFIER = st.sidebar.selectbox("Select Classifier", ("KNN", "SVM", "Random Forest"))

    # data
    X, y = get_dataset(DATASET)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

    # define the model
    params = add_parameter_ui(CLASSIFIER)
    clf = get_classifier(CLASSIFIER, params)

    # fit
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # validation
    acc = accuracy_score(y_test, y_pred)
    st.success(f"Accuracy = {acc}")

    # project the data onto the 2 primary principal components
    pca = PCA(2)
    X_projected = pca.fit_transform(X)
    x1 = X_projected[:, 0]
    x2 = X_projected[:, 1]

    # show
    fig = plt.figure()
    plt.scatter(x1, x2, c=y, alpha=0.8, cmap="viridis")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.colorbar()
    st.pyplot()

    # json
    if st.checkbox("JSON"):
        st.json({'Dataset': DATASET, 'Shape': X.shape, 'Number of Classes': len(np.unique(y)), 'Classifier': (CLASSIFIER, params), 'Accuracy': acc})


if __name__ == "__main__":
    main()
