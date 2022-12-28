class Solution {
public:
    int count = 0;
    void merge(vector<int>& nums, int si, int mid, int ei){
        if(si > ei) return;
        
        int lsize = mid - si + 1;
        int rsize = ei-mid;
        
        vector<int> left(lsize);
        vector<int> right(rsize);
        
        for(int i=0; i<lsize; i++){
            left[i] = nums[si + i];
        }
        
        for(int i=0; i<rsize; i++){
            right[i] = nums[mid + 1 + i];
        }
        
        int i=0, j=0, k=si, c = 0;
        
        for(i=0; i<lsize; i++){
            while(j < rsize and left[i] > (double) 2 * right[j]){
                j++;
            }
            
            c += j;
        }
        
        count += c;
        
        i=0;
        j=0;
        
        while(i < lsize and j < rsize){
            if(left[i] < right[j]){
                nums[k++] = left[i++];
            }else{
                nums[k++] = right[j++];
            }
        }
        
        while(i < lsize){
            nums[k++] = left[i++];
        }
        
        while(j < rsize){
            nums[k++] = right[j++];
        }
    }
    void mergeSort(vector<int> &nums, int si, int ei){
        if(si < ei) {
        
        int mid = (si+ei)/2;
        
        mergeSort(nums, si, mid);
        mergeSort(nums, mid+1, ei);
        merge(nums, si, mid, ei);
        }
    }
    int reversePairs(vector<int>& nums) {
        
        mergeSort(nums, 0, nums.size()-1);
        
        return count;
    }
};