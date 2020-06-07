//unordered_map 이용해서 string을 int대신 사용!




#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

string Find(unordered_map<string, string>* arr, string str){
	if ((*arr)[str] == str)
		return str;
	(*arr)[str] = Find(arr, (*arr)[str]);
	return (*arr)[str];
}
string Union(unordered_map<string, string>* arr, unordered_map<string, int>* counts, string str1, string str2){
	string head1 = Find(arr, str1);
	string head2 = Find(arr, str2);
	if (head1 != head2){
		(*arr)[head2] = head1;
		(*counts)[head1] += (*counts)[head2];
	}
	return head1;
}

int main(){
	//ios_base :: sync_with_stdio(false);
    //cin.tie(NULL);
    //cout.tie(NULL);

	int N, F;
	cin>>N;

	string start, end;

	for(int i=0;i<N;i++){
		unordered_map <string, string>* friends = new unordered_map<string, string>;
		unordered_map <string, int> *counts = new unordered_map<string, int>;
		cin >> F;
		for(int j=0;j<F;j++){
			cin >> start >> end;
			// add friend 1
			if (!(*friends).count(start)){
				(*friends)[start] = start;
				(*counts)[start] = 1;
			}
			else
				start = Find(friends, start);
			// add friend 2
			if (!(*friends).count(end)){
				(*friends)[end] = end;
				(*counts)[end] = 1;
			}
			else
				end = Find(friends, end);

			start = Union(friends, counts, start, end);
			cout << (*counts)[start]<<'\n';
		}
	}

	return 0;
}
