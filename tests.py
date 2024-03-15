from state import State


def main():
    current_state = State(10, [1], [], True)
    current_state.generateActions()
    print(current_state.nextActions)


if __name__ == "__main__":
    main()
