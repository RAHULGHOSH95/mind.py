import os
import json
from pathlib import Path


class Mind:
    path = Path("todo.json")

    def __init__(self, tasks):
        self.tasks = tasks

    def add_task(self, task):
        self.tasks.append(task)

    def save(self):
        with self.path.open("w") as file1:
            file1.write(json.dumps(self.tasks))

    @classmethod
    def load(cls):
        with cls.path.open() as file1:
            tasks = json.loads(file1.read())
        return cls(tasks)

    def eval(self, command):
        if command == "/pop":
            self.tasks.pop()

    def __str__(self):
        os.system("clear")

        lines = []
        i = 0
        for task in self.tasks:
            lines.append(f"[{i}] {task}")
            i += 1

        return "\n".join(lines)


def main():
    mind = Mind.load()
    while True:
        print(mind)
        print(f"[{len(mind.tasks)}] ", end="")
        input_ = input().strip()

        if input_ == "":
            break

        if input_.startswith("/"):
            mind.eval(input_)
            continue

        mind.add_task(input_)

    mind.save()


if __name__ == "__main__":
    main()
