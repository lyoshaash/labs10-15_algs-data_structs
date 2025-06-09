def quick_sort(participants, low, high):
    if low >= high:
        return
    pivot_index = partition(participants, low, high)
    quick_sort(participants, low, pivot_index)
    quick_sort(participants, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while compare(arr[i], pivot):
            i += 1
        j -= 1
        while compare(pivot, arr[j]):
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def compare(a, b):
    if a[1] != b[1]:
        return a[1] > b[1]
    if a[2] != b[2]:
        return a[2] < b[2]
    return a[0] < b[0]

if __name__ == "__main__":
    n = int(input())
    participants = []
    for _ in range(n):
        login, p, f = input().split()
        participants.append((login, int(p), int(f)))

    quick_sort(participants, 0, len(participants) - 1)

    for person in participants:
        print(person[0])
