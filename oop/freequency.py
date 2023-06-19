def count_number_appearances(N, M, A):
    frequency = [0] * (M + 1)  # Initialize a frequency array with zeros

    # Count the occurrences of each number in A
    for num in A:
        frequency[num] += 1

    # Print the frequencies of numbers from 1 to M
    for i in range(1, M + 1):
        print(frequency[i])

# Read input values
N, M = map(int, input().split())
A = list(map(int, input().split()))

# Call the function to count number appearances and print the output
count_number_appearances(N, M, A)
