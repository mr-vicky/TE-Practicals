import java.util.*;

public class JobScheduling {
    public static int jobSchedule(int[][] jobs) {
        // Sort jobs in decreasing order of their profits
        Arrays.sort(jobs, (a, b) -> Integer.compare(b[2], a[2]));
        
        // Create a list to keep track of the assigned time slots
        int[] schedule = new int[jobs.length];
        
        // Loop through each job and assign it to the earliest available time slot
        for (int i = 0; i < jobs.length; i++) {
            // Find the earliest available time slot
            for (int j = Math.min(jobs[i][1], schedule.length) - 1; j >= 0; j--) {
                if (schedule[j] == 0) {
                    schedule[j] = jobs[i][2];
                    break;
                }
            }
        }
        
        // Calculate the total profit
        int totalProfit = 0;
        for (int profit : schedule) {
            totalProfit += profit;
        }
        
        return totalProfit;
    }

    public static void main(String[] args) {
        int[][] jobs = {{1, 2, 50}, {3, 5, 20}, {6, 19, 100}, {2, 100, 200}};
        int totalProfit = jobSchedule(jobs);
        System.out.println(totalProfit); // Output: 300
    }
}
