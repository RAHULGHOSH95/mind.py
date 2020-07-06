from todo import Mind
def main():

    try:
        mind = Mind.load()
    except:
        mind = Mind(tasks=[])

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
