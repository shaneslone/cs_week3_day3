def csFindAllPathsFromAToB(graph):
    result = []
    def inner(n, path):
        current_path = path.copy()
        current_path.append(n)
        if n == len(graph) - 1:
            result.append(current_path)
            return
        else:
            for num in graph[n]:
                inner(num, current_path)
    inner(0, [])
    return result
            