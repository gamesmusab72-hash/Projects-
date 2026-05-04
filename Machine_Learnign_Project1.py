# This is my second project that I started after finishing the UniAthena Machine learning course and thier algorithms.

# ===============================
# Student Performance Predictor
# Decision Tree vs Naive Bayes
# ===============================

# 1. IMPORTS
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


# 2. LOAD DATA
def load_data():
    data = {
        "study_hours": [2, 5, 1, 7, 3, 6, 4, 8, 2, 5],
        "attendance": [60, 80, 50, 90, 65, 85, 70, 95, 55, 75],
        "sleep_hours": [5, 7, 4, 8, 6, 7, 6, 8, 5, 7],
        "previous_grade": [50, 70, 45, 85, 60, 75, 65, 90, 55, 72],
        "pass": [0, 1, 0, 1, 0, 1, 1, 1, 0, 1]
    }

    df = pd.DataFrame(data)
    return df


# 3. PREPARE DATA
def prepare_data(df):
    X = df.drop("pass", axis=1)
    y = df["pass"]

    return train_test_split(X, y, test_size=0.2, random_state=42)


# 4. TRAIN MODELS
def train_models(X_train, y_train):
    dt_model = DecisionTreeClassifier()
    nb_model = GaussianNB()

    dt_model.fit(X_train, y_train)
    nb_model.fit(X_train, y_train)

    return dt_model, nb_model


# 5. EVALUATE MODELS
def evaluate_models(dt_model, nb_model, X_test, y_test):
    dt_predictions = dt_model.predict(X_test)
    nb_predictions = nb_model.predict(X_test)

    dt_accuracy = accuracy_score(y_test, dt_predictions)
    nb_accuracy = accuracy_score(y_test, nb_predictions)

    print("\n=== Model Performance ===")
    print(f"Decision Tree Accuracy: {dt_accuracy:.2f}")
    print(f"Naive Bayes Accuracy: {nb_accuracy:.2f}")

    return dt_accuracy, nb_accuracy


# 6. VISUALIZE DATA
def visualize_data(df):
    plt.scatter(df["study_hours"], df["previous_grade"])
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Grade")
    plt.title("Study Hours vs Previous Grade")
    plt.show()


# 7. SHOW DECISION TREE
def show_tree(model):
    plt.figure(figsize=(10, 6))
    plot_tree(model, filled=True, feature_names=[
              "study_hours", "attendance", "sleep_hours", "previous_grade"])
    plt.title("Decision Tree Visualization")
    plt.show()


# 8. MAKE PREDICTION
def predict_student(model):
    print("\n=== New Student Prediction ===")

    # Example student
    new_student = [[6, 80, 7, 75]]

    prediction = model.predict(new_student)

    result = "PASS" if prediction[0] == 1 else "FAIL"
    print(f"Prediction for student {new_student}: {result}")


# 9. MAIN FUNCTION
def main():
    print("📊 Student Performance Predictor\n")

    df = load_data()
    print("Dataset:\n", df)

    X_train, X_test, y_train, y_test = prepare_data(df)

    dt_model, nb_model = train_models(X_train, y_train)

    dt_acc, nb_acc = evaluate_models(
        dt_model, nb_model, X_test, y_test)

    visualize_data(df)
    show_tree(dt_model)

    # Use the better model
    best_model = dt_model if dt_acc > nb_acc else nb_model
    predict_student(best_model)


# RUN PROGRAM
if __name__ == "__main__":
    main()