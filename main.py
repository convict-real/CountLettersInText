sentence = "The bird flew over the sky and there were 12 birds."
# sentence = input("Enter your text: ")
list = []

def main():
    occurrences = {}

    for char in "abcdefghijklmnopqrstuvwxyz":
        occurrences[char] = 0

    for char in sentence.lower():
        if char.isalpha():
            occurrences[char] += 1

    filtered_occurrences = {key: value for key, value in occurrences.items() if value > 0}

    highestCount = max(occurrences, key = occurrences.get)
    lowestCount = min(filtered_occurrences, key = filtered_occurrences.get)

    print(
        f"Length: {len(sentence)}"
        f"Most used: {highestCount}, Least used: {lowestCount}"
    )

    for char, count in occurrences.items():
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()
