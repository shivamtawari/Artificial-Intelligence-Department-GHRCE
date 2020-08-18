#include <iostream>

using namespace std;

void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

void insertion(int arr[], int siz)
{
    int temp, i, j;
    for(i=1; i<siz; i++)    {
        temp = arr[i];
        j = i;
        while(j>0 && temp<arr[j-1]) {
            arr[j] = arr[j-1];
            j -= 1;
        }
        arr[j] = temp;
    }
}

void merge(int A[] , int start, int mid, int end)
{
    int p=start, q=mid+1;
    int Arr[end-start+1], k=0;

    for(int i=start; i<=end; i++)   {
        if(p > mid)
            Arr[k++] = A[q++];
        else if(q > end)
            Arr[k++] = A[p++];
        else if(A[p] < A[q])
            Arr[k++] = A[p++];
        else
            Arr[k++] = A[q++];
    }
    for(int p=0; p<k; p++) {
        A[start++] = Arr[p];
  }
}
void mergeSort(int A[], int start, int end)
{
    if(start < end) {
    int mid = (start+end)/2 ;
    mergeSort(A, start, mid);
    mergeSort(A, mid+1, end);
    merge(A, start, mid, end);
   }
}

int partition (int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++)   {
        if (arr[j] < pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}
void quickSort(int arr[], int low, int high)
{
    if (low < high)  {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void heapify(int arr[], int n, int i)
{
    int largest = i;
    int l = 2*i + 1;
    int r = 2*i + 2;

    if (l < n && arr[l] > arr[largest])
        largest = l;

    if (r < n && arr[r] > arr[largest])
        largest = r;

    if (largest != i)   {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}
void heapSort(int arr[], int n)
{
    for (int i = n/2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i=n-1; i>0; i--)   {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

void display(int arr[], int n)
{
    for (int i=0; i<n; ++i)
        cout << arr[i] << " ";
    cout << "\n";
}

int main()
{
    int arr[100], n, ch;
    char ext;
    cout << "\n\tAuthor: Vishal Narnaware. (A - 63)";
    do {
        cout << "\n Enter the size of Array: ";
        cin >> n;
        cout << "\n Enter the Array: ";
        for(int i=0; i<n; i++)  {
            cin >> arr[i];
        }
        cout << "\n\n -----MAIN_MENU-----";
        cout << "\n 1. Insertion Sort";
        cout << "\n 2. Merge Sort";
        cout << "\n 3. Quick Sort";
        cout << "\n 4. Heap Sort";
        cout << "\n Enter your choice: ";
        cin >> ch;
        switch(ch)  {
            case 1: insertion(arr, n);
                    break;
            case 2: mergeSort(arr, 0, n-1);
                    break;
            case 3: quickSort(arr, 0, n-1);
                    break;
            case 4: heapSort(arr, n);
                    break;
            case 5:
            default: cout << "\n Err!!! Wrong Choice";
                    break;
        }
        cout << "\n Sorted array is: ";
        display(arr, n);
        cout << "\n Do you want to enter again?(y/n): ";
        cin >> ext;
    } while(ext != 'n');
}
