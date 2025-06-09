from collections import defaultdict, Counter

def build_index(documents):
    index = defaultdict(list)
    for i, doc in enumerate(documents):
        word_counts = Counter(doc.split())
        for word, count in word_counts.items():
            index[word].append((i, count))
    return index

def search(index, documents, queries):
    results = []
    for query in queries:
        relevance = defaultdict(int)
        for word in set(query.split()):
            for doc_id, count in index.get(word, []):
                relevance[doc_id] += count
        ranked = sorted(relevance.items(), key=lambda x: (-x[1], x[0]))
        top_docs = [str(doc_id) for doc_id, _ in ranked[:5]]
        results.append(' '.join(top_docs))
    return results

if __name__ == "__main__":
    n = int(input())
    documents = [input().strip() for _ in range(n)]
    m = int(input())
    queries = [input().strip() for _ in range(m)]

    index = build_index(documents)
    results = search(index, documents, queries)

    for line in results:
        print(line)

