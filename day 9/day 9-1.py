def extrapolate_sequence(sequence):
    new_sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
    return new_sequence

def predict_next_value(history):
    sequences = [history]

    # Generate sequences of differences until we reach a sequence of all zeroes
    while not all(value == 0 for value in sequences[-1]):
        sequences.append(extrapolate_sequence(sequences[-1]))

    # Extrapolate the next value by adding the last value of each sequence from bottom to top
    next_value = sum(sequence[-1] for sequence in sequences)
    return next_value

def main(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total = 0

    for line in lines:
        history = list(map(int, line.split()))
        next_value = predict_next_value(history)
        total += next_value

    print(f"The sum of all extrapolated values is: {total}")

if __name__ == "__main__":
    file_path = "input.txt"  # Replace with the actual path to your file
    main(file_path)