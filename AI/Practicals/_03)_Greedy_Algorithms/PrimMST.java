import java.util.*;

public class PrimMST {
    private static int prim(int[][] graph) {
        int n = graph.length;
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        boolean[] visited = new boolean[n];
        dist[0] = 0;

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(0);

        int sum = 0;
        while (!pq.isEmpty()) {
            int u = pq.poll();
            if (visited[u]) {
                continue;
            }
            visited[u] = true;
            sum += dist[u];
            for (int v = 0; v < n; v++) {
                if (graph[u][v] != 0 && !visited[v] && graph[u][v] < dist[v]) {
                    dist[v] = graph[u][v];
                    pq.add(v);
                }
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        int[][] graph = {
            {0, 5, 10, 0},
            {5, 0, 7, 8},
            {10, 7, 0, 9},
            {0, 8, 9, 0}
        };
        int sum = prim(graph);
        System.out.println("Minimal spanning tree weight: " + sum); // Output: 16
    }
}
