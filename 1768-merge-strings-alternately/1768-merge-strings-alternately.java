class Solution {
    public String mergeAlternately(String word1, String word2) {
        int l1 = word1.length();
        char[] w1 = word1.toCharArray();
        int l2 = word2.length();
        char[] w2 = word2.toCharArray();
        int mini = Math.min(l1,l2);
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i<mini; i++){
            sb.append(w1[i]);
            sb.append(w2[i]);
        }
        String longW = "";
        if(mini == l1){
            longW = word2;
        }
        else if(mini == l2){
            longW = word1;
        }
        sb.append(longW.substring(mini));
        return sb.toString();
    }
}