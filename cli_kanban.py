import json

class Task:
    def __init__(self, title, status, priority=None, assignee=None, reporter=None):
        self.title = title
        self.status = status
        self.priority = priority
        self.assignee = assignee
        self.reporter = reporter

class Board:
    def __init__(self, project_name):
        self.project_name = project_name
        self.tasks = {'Todo': [], 'In Progress': [], 'Review': [], 'Done': []}

    def add_task(self, task):
        self.tasks[task.status].append(task)

    def remove_task(self, title):
        for status in self.tasks:
            self.tasks[status] = [task for task in self.tasks[status] if task.title != title]

    def move_task(self, title, from_status, to_status):
        self.tasks[from_status] = [task for task in self.tasks[from_status] if task.title != title]
        self.tasks[to_status].append(title)
        

    def display_board(self):
        print(f"\nProject: {self.project_name}")
        for status, tasks in self.tasks.items():
            print(status + ":")
            for task in tasks:
                print(f"  - {task.title} ({task.priority})")

    def save_board(self, filename='data.json'):
        with open(filename, 'w') as f:
            json.dump({'project_name': self.project_name, 'tasks': [task.__dict__ for task in sum(self.tasks.values(), [])]}, f)

    def load_board(self, filename='data.json'):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.project_name = data['project_name']
            self.tasks = {'Todo': [], 'In Progress': [], 'Review': [], 'Done': []}
            for task_data in data['tasks']:
                task = Task(**task_data)
                self.add_task(task)

def main():
    boards = {}

    while True:
        print("\n===== Board Menu =====")
        print("1. Create Board")
        print("2. Select Board")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            project_name = input("Enter project name for new board: ")
            boards[project_name] = Board(project_name)
            print("Board created successfully.")

        elif choice == "2":
            for name in boards:
                print(name)
            project_name = input("Enter project name to select board: ")
            if project_name in boards:
                board = boards[project_name]
                while True:
                    print(f"\n===== {project_name} Board Menu =====")
                    print("1. Add Task")
                    print("2. Remove Task")
                    print("3. Move Task")
                    print("4. Display Board")
                    print("5. Save Board")
                    print("6. Load Board")
                    print("7. Back to Board Menu")

                    board_choice = input("Enter your choice: ")

                    if board_choice == "1":
                        title = input("Enter task title: ")
                        status = input("Enter task status [Todo / In Progress / Review / Done]: ")
                        assignee = input("Enter assignee name: ")
                        reporter = input("Enter reporter name: ")
                        if status!="Done":priority = input("Enter priority [High / Medium / Low]: ")
                        else: priority=None
                        board.add_task(Task(title, status, priority,assignee, reporter))
                    elif board_choice == "2":
                        title = input("Enter title of task to remove: ")
                        board.remove_task(title)
                    elif board_choice == "3":
                        title = input("Enter title of task to move: ")
                        from_status = input("Enter current status of task: ")
                        to_status = input("Enter new status of task: ")
                        board.move_task(title, from_status, to_status)
                    elif board_choice == "4":
                        board.display_board()
                    elif board_choice == "5":
                        filename = input("Enter filename to save: ")
                        board.save_board(filename)
                    elif board_choice == "6":
                        filename = input("Enter filename to load: ")
                        board.load_board(filename)
                    elif board_choice == "7":
                        break
                    else:
                        print("Invalid choice. Enter a number from 1 to 7.")
            else:
                print("Board not found.")

        elif choice == "3":
            print("==========end===========")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 3.")

if __name__ == "__main__":
    main()
