class Task:
    def __init__(self, title, description, priority="medium"):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "pending"
        self.subtasks = []
    
    def complete(self):
        self.status = "completed"
        print(f"Задача '{self.title}' выполнена!")
    
    def add_subtask(self, subtask_title):
        self.subtasks.append({"title": subtask_title, "done": False})
        print(f"Подзадача '{subtask_title}' добавлена")
    
    def __str__(self):
        return f"[{self.priority.upper()}] {self.title} - {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_counter = 0
    
    def create_task(self, title, description, priority="medium"):
        self.task_counter += 1
        task = Task(title, description, priority)
        self.tasks.append(task)
        print(f"Создана новая задача #{self.task_counter}: {title}")
        return task
    
    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст")
            return
        print("=== Список задач ===")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
    
    def get_pending_tasks(self):
        return [t for t in self.tasks if t.status == "pending"]
    
    def get_completed_tasks(self):
        return [t for t in self.tasks if t.status == "completed"]
    
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Задача '{removed.title}' удалена")
        else:
            print("Неверный индекс задачи")
    
    def search_tasks(self, keyword):
        results = [t for t in self.tasks if keyword.lower() in t.title.lower()]
        return results


if __name__ == "__main__":
    manager = TaskManager()
    
    manager.create_task("Изучить Git Flow", "Пройти лабораторную работу", "high")
    manager.create_task("Написать отчет", "Оформить документацию", "medium")
    manager.create_task("Отдохнуть", "Сделать перерыв", "low")
    
    manager.list_tasks()
