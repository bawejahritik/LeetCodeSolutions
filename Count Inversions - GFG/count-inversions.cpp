//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution{
  public:
    // arr[]: Input Array
    // N : Size of the Array arr[]
    // Function to count inversions in the array.
    long long int ans = 0;
    
    void merge(long long arr[], long long int l, long long int m, long long int r){
        int lsize = m - l + 1;
        int rsize = r - m;
        long long int left[lsize], right[rsize];
        
        for(long long int i=0; i<lsize; i++){
            left[i] = arr[l + i];
        }
        
        for(long long int i=0; i<rsize; i++){
            right[i] = arr[m + 1 + i];
        }
        
        long long int i=0, j=0, k=l;
        
        while(i < lsize and j < rsize){
            if(left[i] > right[j]){
                ans += (lsize-i);
                arr[k++] = right[j++];
            }else{
                arr[k++] = left[i++];
            }
        }
        
        while(i < lsize){
            arr[k++] = left[i++];
        }
        
        while(j < rsize){
            arr[k++] = right[j++];
        }
            
    }
    
    void mergeSort(long long arr[], long long int l, long long int r){
        if(l < r){
            int m = (l+r)/2;
            mergeSort(arr, l, m);
            mergeSort(arr, m+1, r);
            merge(arr, l, m, r);
        }
    }
    long long int inversionCount(long long arr[], long long N)
    {
        // Your Code Here
        mergeSort(arr, 0, N-1);
        
        return ans;
    }

};

//{ Driver Code Starts.

int main() {
    
    long long T;
    cin >> T;
    
    while(T--){
        long long N;
        cin >> N;
        
        long long A[N];
        for(long long i = 0;i<N;i++){
            cin >> A[i];
        }
        Solution obj;
        cout << obj.inversionCount(A,N) << endl;
    }
    
    return 0;
}

// } Driver Code Ends