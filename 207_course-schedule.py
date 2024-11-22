class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adj list
        prereqs = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            prereqs[a].append(b)

        visited = set()
        def dfs(course):
            if not prereqs[course]:
                return True
            if course in visited:
                return False
            
            visited.add(course)

            for prereq in prereqs[course]:
                if dfs(prereq) == False:
                    return False
            
            visited.remove(course)
            prereqs[course] = []
            
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True
