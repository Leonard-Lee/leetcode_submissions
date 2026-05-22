class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0) {
            return new ArrayList<>();
        }
        
        Map<Integer, List<String>> map = new HashMap<>();
        for (String str : strs) {
            int hashCode = strToHash(str);
            map.putIfAbsent(hashCode, new ArrayList<>());
            map.get(hashCode).add(str);
        }
        return new ArrayList<>(map.values());
    }

    private int strToHash(String str) {
        int[] arr = new int[26];
        for (char c : str.toCharArray()) {
            arr[c - 'a'] += 1;
        }
        return Arrays.hashCode(arr);
    }
}