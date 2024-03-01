from state import State


def main():
    current_state = State(10, [1, 2, 3, 4, 5], 5, 4, 1)
    current_state.generateActions()


if __name__ == "__main__":
    main()
