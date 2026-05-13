import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r"C:\Users\Adithyan\Downloads\oops\gender_classification.csv"
data = pd.read_csv(file_path)
print(data.head(5))
print(data.info(7))

#missing value
print("Missing values:\n", data.isnull().sum())

#duplicate
print("\nDuplicate rows:",data.duplicated().sum())

#dropping duplicates
data = data.drop_duplicates()

#rechecking duplicates
print("\nDuplicate rows:", data.duplicated().sum())


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data["gender"] = le.fit_transform(data["gender"])
x = data.drop("gender", axis=1)
y = data["gender"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, classification_report
y_pred_log = log_reg.predict(X_test)
print("\nLogistic Regression Results")
print("Accuracy:", accuracy_score(y_test, y_pred_log))
print(classification_report(y_test, y_pred_log, target_names=["Female","Male"]))

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred_log)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Female", "Male"])
disp.plot()
plt.title("Confusion Matrix - Logistic Regression")
plt.show()
