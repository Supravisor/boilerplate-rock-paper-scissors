# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], sequences={}):
    play = 5

    if prev_play != '':
        opponent_history.append(prev_play)

    if len(opponent_history) <= play:
        return "P"

    if len(opponent_history) > 6:
        opponent_history.pop(0)

        sequence = "".join(opponent_history)
        sequences[sequence] = sequences.get(sequence, 0) + 1

        sequence = "".join(opponent_history[1:])
