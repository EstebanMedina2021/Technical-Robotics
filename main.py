from atod_clusters import find_clusters

if __name__ == "__main__":
    n, m = map(int, input().split())
    connections = [tuple(map(int, input().split())) for _ in range(m)]

    clusters = find_clusters(n, connections)

    print(len(clusters))
    for cluster in clusters:
        print(cluster - 1)
