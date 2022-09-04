class Solution:
    def buildMatrix(self, k: int, row_con: List[List[int]], col_con: List[List[int]]) -> List[List[int]]:
        def topological_sort(digraph):
            indegrees = {node : 0 for node in range(1, k+1)}
            for node in digraph:
                for neighbor in digraph[node]:
                    indegrees[neighbor] += 1
                    
            nodes_with_no_incoming_edges = []
            for node in range(1, k+1):
                if indegrees[node] == 0:
                    nodes_with_no_incoming_edges.append(node)
                    
            topological_ordering = [] 
            while len(nodes_with_no_incoming_edges) > 0:
                node = nodes_with_no_incoming_edges.pop(0)
                topological_ordering.append(node)
                
                for neighbor in digraph[node]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        nodes_with_no_incoming_edges.append(neighbor)
                        
            if len(topological_ordering) == k:
                return topological_ordering  
            return []
        
        row_graph = defaultdict(list)
        col_graph = defaultdict(list)
        
        for [u, v] in row_con:
            row_graph[u].append(v)
        for [u, v] in col_con:
            col_graph[u].append(v)
            
        row_top_ord = topological_sort(row_graph)
        col_top_ord = topological_sort(col_graph)
        
        
        if (not row_top_ord) or (not col_top_ord):
            return []
        
        r_pos = [None for i in range(k+1)]
        c_pos = [None for i in range(k+1)]
        
        for i in range(k):
            r_pos[row_top_ord[i]] = i
            c_pos[col_top_ord[i]] = i
            
        mat = [[0 for j in range(k)]for i in range(k)]
        
        for i in range(1, k + 1):
            mat[r_pos[i]][c_pos[i]] = i
        
        return mat