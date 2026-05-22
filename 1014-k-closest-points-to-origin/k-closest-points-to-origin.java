class Solution {
    public int[][] kClosest(int[][] points, int k) {
        if (points == null || points.length == 0) {
            return null;
        }

        int[][] res = new int[k][2];
        // max heap
        PriorityQueue<int[]> pq = new PriorityQueue<>((p1, p2) -> dist(p2) - dist(p1)); 
        for (int[] point: points) {
            pq.offer(point);
            if(pq.size() > k) {
                pq.poll();
            }
        }

        for (int i = k - 1; i >= 0; i--) {
            res[i] = pq.poll();
        }
        return res;
    }

    private int dist(int[] point) {
        return (point[0] * point[0]) + (point[1] * point[1]);
    }
}