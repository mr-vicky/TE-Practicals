// Java program for the above approach
import java.util.HashMap;

public class SingleS {

	// DFS memoization
	static int adjMatrix[][];
	static HashMap<int[], Integer> mp
		= new HashMap<int[], Integer>();

	// Function to implement DFS Traversal
	static int DFSUtility(int node, int stops, int dst,
						int cities)
	{
		// Base Case
		if (node == dst)
			return 0;

		if (stops < 0)
			return Integer.MAX_VALUE;

		int[] key = new int[] { node, stops };

		// Find value with key in a map
		if (mp.containsKey(key))
			return mp.get(mp);

		int ans = Integer.MAX_VALUE;

		// Traverse adjacency matrix of
		// source node
		for (int neighbour = 0; neighbour < cities;
			++neighbour) {
			int weight = adjMatrix[node][neighbour];

			if (weight > 0) {
				// Recursive DFS call for
				// child node
				int minVal = DFSUtility(
					neighbour, stops - 1, dst, cities);

				if (minVal + weight > 0)
					ans = Math.min(ans, minVal + weight);
			}
			mp.put(key, ans);
		}
		// Return ans
		return ans;
	}

	// Function to find the cheapest price
	// from given source to destination
	static int findCheapestPrice(int cities,
								int[][] flights, int src,
								int dst, int stops)
	{
		// Resize Adjacency Matrix
		adjMatrix = new int[cities + 1][cities + 1];

		// Traverse flight[][]
		for (int[] item : flights) {
			// Create Adjacency Matrix
			adjMatrix[item[0]][item[1]] = item[2];
		}

		// DFS Call to find shortest path
		int ans = DFSUtility(src, stops, dst, cities);

		// Return the cost
		return ans >= Integer.MAX_VALUE ? -1 : ans;
	}

	// Driver Code
	public static void main(String[] args)
	{
		// Input flight : :Source,
		// Destination, Cost
		int[][] flights
			= { { 4, 1, 1 }, { 1, 2, 3 }, { 0, 3, 2 },
				{ 0, 4, 10 }, { 3, 1, 1 }, { 1, 4, 3 } };

		// vec, n, stops, src, dst
		int stops = 2;
		int totalCities = 5;
		int sourceCity = 0;
		int destCity = 4;

		// Function Call
		int ans = findCheapestPrice(totalCities, flights,
									sourceCity, destCity,
									stops);

		System.out.println(ans);
	}
}

// This code is contributed by Lovely Jain
