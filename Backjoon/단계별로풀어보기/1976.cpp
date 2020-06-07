#include <iostream>

using namespace std;

int Find(int* arr, int n){
    int head1 = arr[n];
    if (head1 == n)
        return head1;
    head1 = Find(arr, head1);
    arr[n] = head1;
    return head1;
}
int Union(int* arr, int n1, int n2){
    int head1 = Find(arr, n1);
    int head2 = Find(arr, n2);
    arr[head2] = head1;
    
    return 0;
}

int main(){
    int N, M, connect;
    cin >> N >> M;
    int* arr = new int[N+1];
    for (int i=0;i<=N;i++){
        arr[i] = i;
    }
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            cin >> connect;
            if ((j >= i+1) && connect == 1){
                Union(arr, i+1, j+1);
            }
        }
    }
    int start, end;
    cin >> start;
    start = Find(arr, start);
    for (int i=1;i<M;i++){
        cin >> end;
        end = Find(arr, end);
        if (start != end){
            cout << "NO";
            return 0;
        }
    }
    cout << "YES";
    return 0;
}
