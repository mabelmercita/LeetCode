class Solution {
    public int maximumWealth(int[][] accounts) {
        int s  = 0;
        for(int i = 0; i<accounts.length; i++){
            int c_s = 0;
            for(int j = 0; j<accounts[i].length; j++){
                c_s+=accounts[i][j];
            }
            if(c_s > s){
                s = c_s;
            }
        }
        return s;
    }
}