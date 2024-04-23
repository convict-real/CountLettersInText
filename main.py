input = input("Enter your text: ")

if input[-1] == " ":
    print("Text should not end with a space.")

list = []

def main():
    occurrences = {}

    for char in "abcdefghijklmnopqrstuvwxyz":
        occurrences[char] = 0

    for char in input.lower():
        if char.isalpha():
            occurrences[char] += 1

    filtered_occurrences = {key: value for key, value in occurrences.items() if value > 0}

    highestCount = max(occurrences, key = occurrences.get)
    lowestCount = min(filtered_occurrences, key = filtered_occurrences.get)

    print(
        f"Characters: {len(input)}, Words: {len(input.split())}\n"
        f"Most used: {highestCount}, Least used: {lowestCount}"
    )

    for char, count in occurrences.items():
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()
    
