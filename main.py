import matplotlib.pyplot as plt

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

    sorted_occurrences = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)
    occurrencesList = []

    for i in range(len(sorted_occurrences)):
        if i % 2 == 0:
            occurrencesList.append(sorted_occurrences[i])
        else:
            occurrencesList.insert(0, sorted_occurrences[i])

    plt.bar(*zip(*occurrencesList))
    plt.xlabel('Letter')
    plt.ylabel('Count')

    for char, count in occurrencesList:
        plt.text(char, count, str(count), ha='center', va='bottom')

    info_text = (f"Characters: {len(input)}, Words: {len(input.split())}\n"
                 f"Most used: {highestCount}, Least used: {lowestCount}")

    plt.gcf().text(0, 0, info_text, horizontalalignment='left', verticalalignment='bottom', fontsize=10, wrap=True)
    plt.subplots_adjust(bottom=0.135)    

    plt.show()

if __name__ == "__main__":
    main()
