# 풀이 1. dfs
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        route = []
        def dfs(a):
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
            
        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]
# 풀이 2. 스택 연산으로 큐 연산 최적화 시도
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프를 뒤집어서 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
            
        route = []
        def dfs(a):
            # 마지막 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)
            
        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]
