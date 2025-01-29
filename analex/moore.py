class Moore(object):
    """Moore Machine : Finite Automata with Output"""

    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_state, output_table ):
        """
        states: Finite set of states
        input_alphabet: Alphabet of letters for forming input string
        output_alphabet: Alphabet of letters for forming output characters
        transitions: Transition Table
        output_table: Output Table to show what character from output_alphabet is printed when a state from 'states'
        is reached
        """

        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.output_table = output_table
        self.initial_state = initial_state

    def get_output_from_string(self, string):
        """Return Moore Machine's output when a given string is given as input"""

        temp_list = list(string)
        output = ''
        current_state = self.initial_state
        output += self.output_table[current_state]
        for x in temp_list:
            current_state = self.transitions[current_state][x]
            print("Estado corrente:",current_state, '\n')
            output += self.output_table[current_state]

        return output