from collections import defaultdict, deque

def minimumClicksToReachEnd(start, end, links):
    graph = defaultdict(list)

    for page, linked_pages in enumerate(links, 1):
        for linked_page in linked_pages:
            graph[page].append(linked_page)

    visited = set()
    queue = deque([(start, 0)])

    while queue:
        current_page, clicks = queue.popleft()

        if current_page == end:
            return clicks

        if current_page not in visited:
            visited.add(current_page)
            for linked_page in graph[current_page]:
                queue.append((linked_page, clicks + 1))

    return -1

try:
    # Input based on your provided format
    n = int(input())
    links = []
    for _ in range(n):
        linked_pages = list(map(int, input().split()))
        links.append(linked_pages)

    start_page, end_page = map(int, input().split())

    result = minimumClicksToReachEnd(start_page, end_page, links)

    if result != -1:
        print("\n")
        print(result)
    else:
        print("-1")
except Exception as e:
    print(f"An error occurred: {e}")