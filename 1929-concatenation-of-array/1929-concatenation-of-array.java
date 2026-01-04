class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] l = new int[(nums.length)*2];
        for(int i = 0; i<nums.length; i++){
            l[i] = nums[i];
        }
        for(int i = 0; i<nums.length; i++){
            l[nums.length+i] = nums[i];
        }
        return l;
    }
}