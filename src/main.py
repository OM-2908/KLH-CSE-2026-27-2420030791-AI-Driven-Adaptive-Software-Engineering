from task_management.task_manager import TaskManager
from risk_prediction.risk_model import RiskPredictionModel
from scheduling.scheduler import TaskScheduler
from ai.assistant import ProjectAssistant


def main():

    print("=" * 60)
    print("AI-DRIVEN ADAPTIVE SOFTWARE ENGINEERING")
    print("INTELLIGENT PROJECT MANAGEMENT SYSTEM")
    print("=" * 60)

    # -----------------------------------------
    # TASK MANAGEMENT
    # -----------------------------------------

    manager = TaskManager()

    manager.add_task(
        "Develop Login Module",
        priority="High",
        deadline="2026-08-25"
    )

    manager.add_task(
        "Create Database",
        priority="Medium",
        deadline="2026-08-27"
    )

    manager.add_task(
        "Develop Dashboard",
        priority="High",
        deadline="2026-08-28"
    )

    manager.add_task(
        "Testing",
        priority="Medium",
        deadline="2026-08-30"
    )

    manager.update_status(1, "Completed")
    manager.update_status(2, "Delayed")

    tasks = manager.get_tasks()

    # -----------------------------------------
    # DISPLAY TASKS
    # -----------------------------------------

    print("\nTASKS")
    print("-" * 60)

    for task in tasks:
        print(task)

    # -----------------------------------------
    # PROJECT PROGRESS
    # -----------------------------------------

    progress = manager.calculate_progress()

    print(
        "\nProject Progress:",
        round(progress, 2),
        "%"
    )

    # -----------------------------------------
    # RISK PREDICTION
    # -----------------------------------------

    risk_model = RiskPredictionModel()

    risk_model.train()

    risk = risk_model.predict_from_tasks(
        tasks,
        team_size=5
    )

    # -----------------------------------------
    # RISK ANALYSIS
    # -----------------------------------------

    completed = sum(
        1
        for task in tasks
        if task["status"].lower() == "completed"
    )

    delayed = sum(
        1
        for task in tasks
        if task["status"].lower() == "delayed"
    )

    pending = sum(
        1
        for task in tasks
        if task["status"].lower() == "pending"
    )

    print("\nRISK ANALYSIS")
    print("-" * 60)

    print("Total Tasks:", len(tasks))
    print("Completed Tasks:", completed)
    print("Delayed Tasks:", delayed)
    print("Pending Tasks:", pending)
    print("Predicted Project Risk:", risk)

    # -----------------------------------------
    # ADAPTIVE SCHEDULING
    # -----------------------------------------

    scheduler = TaskScheduler()

    prioritized_tasks = scheduler.prioritize_tasks(
        tasks
    )

    print("\nADAPTIVE TASK PRIORITY")
    print("-" * 60)

    for index, task in enumerate(
        prioritized_tasks,
        start=1
    ):

        score = scheduler.calculate_task_score(
            task
        )

        print(
            f"{index}. {task['name']} "
            f"| Priority: {task['priority']} "
            f"| Status: {task['status']} "
            f"| Score: {score}"
        )

    # -----------------------------------------
    # AI ASSISTANT
    # -----------------------------------------

    assistant = ProjectAssistant()

    summary = assistant.generate_summary(
        tasks,
        progress,
        risk
    )

    recommendations = scheduler.get_recommendations(
        tasks,
        risk
    )

    print("\nAI PROJECT ASSISTANT")
    print("-" * 60)

    print(summary["message"])

    print("\nAI RECOMMENDATIONS")

    for recommendation in recommendations:
        print("-", recommendation)


if __name__ == "__main__":
    main()