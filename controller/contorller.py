class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            tasks = self.model.get_tasks()
            self.view.show_tasks(tasks)
            user_input = self.view.get_user_input()
            self.model.add_task(user_input)
