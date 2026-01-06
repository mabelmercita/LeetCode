class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int l = nums1.length+nums2.length;
        int arr[] = new int[l];
        for(int i = 0; i<nums1.length; i++){
            arr[i] = nums1[i];
        }
        for(int j = 0; j<nums2.length; j++){
            arr[j+nums1.length] = nums2[j];
        }
        Arrays.sort(arr);
        if(arr.length%2 != 0){
            double mid = (arr.length/2) + 0.5;
            return arr[(int)mid];
        }
        else{
            int mid = (arr.length/2);
            double median = (arr[mid] + arr[mid-1])/2.0;
            return median;
        }
    }
}