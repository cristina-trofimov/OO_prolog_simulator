from models.input import Input

def main():
    input = Input("declarativeModel.txt")
    input.parse()
    print("")
    input.print_states()
    print("")
    input.print_transitions()
    
    for state in input.states:
        state.add_transitions(input.transitions)
        state.print_transitions()
        


if __name__ == '__main__':
    main()