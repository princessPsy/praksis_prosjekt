class View:
    def show_tasks(self, tasks):
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    def get_user_input(self):
        return input("Enter a task: ")
