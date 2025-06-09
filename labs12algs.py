from collections import defaultdict

def group_anagrams(words):
    anagram_groups = defaultdict(list)

    for idx, word in enumerate(words):
        signature = ''.join(sorted(word))
        anagram_groups[signature].append(idx)
    result = list(anagram_groups.values())

    for group in result:
        group.sort()
    result.sort(key=lambda g: g[0])

    return result

if __name__ == "__main__":
    n = int(input())
    words = input().split()

    result = group_anagrams(words)

    for group in result:
        print(' '.join(map(str, group)))
