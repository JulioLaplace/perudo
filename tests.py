from state import State
from cfr import CFR


def main():
    # current_state = State(10, [1], [], True)
    # current_state.generateActions()
    # print(current_state.nextActions)
    cfr = CFR(1000)
    cfr.train()


if __name__ == "__main__":
    main()
