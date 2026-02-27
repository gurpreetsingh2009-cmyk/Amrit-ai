class Task:
    def __init__(self, name, execute):
        self.name = name
        self.execute = execute

class MultiTaskSystem:
    def __init__(self):
        self.task_queue = []

    def add_task(self, task):
        self.task_queue.append(task)

    def execute_sequential(self):
        print("Executing tasks sequentially")
        for task in self.task_queue:
            print(f"Running task: {task.name}")
            task.execute()

    def execute_parallel(self):
        print("Executing tasks in parallel")
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(task.execute): task for task in self.task_queue}
            for future in futures:
                print(f"Finished task: {futures[future].name}")

    def clear_tasks(self):
        self.task_queue.clear()

# Example usage:
if __name__ == '__main__':
    import time

    def sample_task():
        time.sleep(1)
        print("Task completed")

    multi_task_system = MultiTaskSystem()
    multi_task_system.add_task(Task('Task 1', sample_task))
    multi_task_system.add_task(Task('Task 2', sample_task))
    multi_task_system.add_task(Task('Task 3', sample_task))

    multi_task_system.execute_sequential()
    print("\nNow executing in parallel:")
    multi_task_system.execute_parallel()