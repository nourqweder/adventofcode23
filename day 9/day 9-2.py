def predict_previous_value(history):
    sequences = [history]

    # Generate sequences of differences until we reach a sequence of all zeroes
    while not all(value == 0 for value in sequences[-1]):
        sequences.append(extrapolate_sequence(sequences[-1]))

    # Add a zero at the beginning of the sequence of zeroes
    sequences[-1].insert(0, 0)

    # Fill in the new first values for each previous sequence from bottom to top
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].insert(0, sequences[i][0] - sequences[i+1][0])

    # The first value of the first sequence is the extrapolated previous value
    previous_value = sequences[0][0]
    return previous_value

def extrapolate_sequence(sequence):
    new_sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
    return new_sequence

def main(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total = 0

    for line in lines:
        history = list(map(int, line.split()))
        previous_value = predict_previous_value(history)
        total += previous_value

    print(f"The sum of all extrapolated values is: {total}")

if __name__ == "__main__":
    file_path = "input.txt"  # Replace with the actual path to your file
    main(file_path)