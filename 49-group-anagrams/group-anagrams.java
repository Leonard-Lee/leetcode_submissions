class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0) {
            return new ArrayList<>();
        }

        Map<Integer, List<String>> map = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            String str = strs[i];
            int hash = stringToHash(str);
            map.putIfAbsent(hash, new ArrayList<>());
            map.get(hash).add(str);
        }
        return new ArrayList<>(map.values());
        
    }

    private int stringToHash(String str) {
        int[] freqArr = new int[26];
        for (char c : str.toCharArray()) {
            freqArr[c - 'a'] += 1;
        }
        return Arrays.hashCode(freqArr);
    }
}