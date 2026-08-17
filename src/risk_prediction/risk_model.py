import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


class RiskPredictionModel:

    def __init__(self):

        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

        self.accuracy = 0

    def create_training_data(self):

        data = {

            "task_count": [
                5, 10, 15, 20, 25,
                30, 8, 12, 18, 22,
                14, 28, 9, 16, 24
            ],

            "completed_tasks": [
                5, 8, 10, 12, 15,
                18, 7, 9, 11, 13,
                10, 16, 8, 11, 14
            ],

            "delayed_tasks": [
                0, 2, 5, 8, 10,
                12, 1, 3, 6, 9,
                4, 11, 1, 5, 10
            ],

            "team_size": [
                5, 5, 6, 6, 7,
                7, 4, 5, 6, 7,
                5, 8, 4, 6, 7
            ],

            "risk": [
                "Low", "Low", "Medium", "Medium", "High",
                "High", "Low", "Medium", "Medium", "High",
                "Medium", "High", "Low", "Medium", "High"
            ]
        }

        return pd.DataFrame(data)

    def train(self):

        df = self.create_training_data()

        X = df[
            [
                "task_count",
                "completed_tasks",
                "delayed_tasks",
                "team_size"
            ]
        ]

        y = df["risk"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)

        self.accuracy = accuracy_score(
            y_test,
            predictions
        )

        print("Risk Prediction Model trained successfully!")
        print(
            "Model Accuracy:",
            round(self.accuracy * 100, 2),
            "%"
        )

    def predict_risk(
        self,
        task_count,
        completed_tasks,
        delayed_tasks,
        team_size=5
    ):

        input_data = pd.DataFrame(
            [[
                task_count,
                completed_tasks,
                delayed_tasks,
                team_size
            ]],
            columns=[
                "task_count",
                "completed_tasks",
                "delayed_tasks",
                "team_size"
            ]
        )

        prediction = self.model.predict(input_data)

        return prediction[0]

    def predict_from_tasks(
        self,
        tasks,
        team_size=5
    ):

        task_count = len(tasks)

        completed_tasks = sum(
            1
            for task in tasks
            if task["status"].lower() == "completed"
        )

        delayed_tasks = sum(
            1
            for task in tasks
            if task["status"].lower() == "delayed"
        )

        return self.predict_risk(
            task_count=task_count,
            completed_tasks=completed_tasks,
            delayed_tasks=delayed_tasks,
            team_size=team_size
        )


if __name__ == "__main__":

    risk_model = RiskPredictionModel()

    risk_model.train()

    risk = risk_model.predict_risk(
        task_count=20,
        completed_tasks=10,
        delayed_tasks=7,
        team_size=5
    )

    print("Predicted Project Risk:", risk)