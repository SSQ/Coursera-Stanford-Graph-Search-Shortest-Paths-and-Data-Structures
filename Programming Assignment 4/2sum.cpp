#include <bits/stdc++.h>
using namespace std;

std::ifstream infile("numbers.txt");
long long a[1000005]={0};

int main(){
	// Answer : 427
	// Expected Running time : <2secs
	// O(n log n) solution
	long long in;
	int i = 0;
	while (infile >> in)
		a[i++] = in;
	int size = i;
	sort(a,a+size);
	map<long long,bool> mp;
	int ans = 0;
	for(int i=0;i<size;++i){
		long long l = (-10000) - a[i];
		long long r = (10000) - a[i];
		for(int j = lower_bound (a, a+size, l) - a; j>=0 && j<size && a[j] <= r; ++j){
			
			long long sum = a[i]+a[j];
			if(sum<-10000 or sum>10000){
				cout<<"input set not suitable for this algorithm!"<<endl;
				cout<<i<<','<<a[i]<<endl;
				cout<<j<<','<<a[j]<<endl;
				cout<<sum<<endl;
				return 0;
			}

			if(mp[sum] == 0){
				mp[sum] = 1;
				++ans;
			}
		}
	}
	cout<<ans<<endl;
}