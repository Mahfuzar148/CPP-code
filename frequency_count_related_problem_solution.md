
---

# **LeetCode Frequency Count — C++ Solutions (10 Problems)**

নীচে ১০টি LeetCode frequency count সম্পর্কিত সমস্যা দেওয়া আছে, প্রত্যেকটার জন্য ক্লিকযোগ্য লিংক এবং সংক্ষিপ্ত C++ সমাধান।

---

| #  | Problem                                                        | Link                                                                                                      |
| -- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| 1  | Top K Frequent Elements                                        | [🔗 Click](https://leetcode.com/problems/top-k-frequent-elements/)                                        |
| 2  | Count Elements With Maximum Frequency                          | [🔗 Click](https://leetcode.com/problems/count-elements-with-maximum-frequency/)                          |
| 3  | Sort Array by Increasing Frequency                             | [🔗 Click](https://leetcode.com/problems/sort-array-by-increasing-frequency/)                             |
| 4  | Frequency of the Most Frequent Element                         | [🔗 Click](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)                         |
| 5  | Range Frequency Queries (Design)                               | [🔗 Click](https://leetcode.com/problems/range-frequency-queries/)                                        |
| 6  | Most Frequent Number Following Key in an Array                 | [🔗 Click](https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/)                 |
| 7  | Count Substrings With K-Frequency Characters I                 | [🔗 Click](https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/)                 |
| 8  | Apply Operations to Maximize Frequency Score                   | [🔗 Click](https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/)                   |
| 9  | Maximum Frequency of an Element After Performing Operations II | [🔗 Click](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/) |
| 10 | Find Occurrences of an Element in an Array                     | [🔗 Click](https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/)                     |

---

## **1. Top K Frequent Elements**

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> cnt;
        for (int x: nums) cnt[x]++;
        vector<pair<int,int>> v(cnt.begin(), cnt.end());
        nth_element(v.begin(), v.begin()+k-1, v.end(),
                    [](auto &a, auto &b){ return a.second > b.second; });
        sort(v.begin(), v.begin()+k,
             [](auto &a, auto &b){ return a.second > b.second; });
        vector<int> ans;
        for (int i=0;i<k;i++) ans.push_back(v[i].first);
        return ans;
    }
};
```

## **2. Count Elements With Maximum Frequency**

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int,int> c;
        int mx = 0;
        for (int x: nums) mx = max(mx, ++c[x]);
        int sum = 0;
        for (auto &p: c) if (p.second == mx) sum += p.second;
        return sum;
    }
};
```

## **3. Sort Array by Increasing Frequency**

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int,int> c;
        for (int x: nums) c[x]++;
        sort(nums.begin(), nums.end(), [&](int a, int b){
            if (c[a] != c[b]) return c[a] < c[b];
            return a > b;
        });
        return nums;
    }
};
```

## **4. Frequency of the Most Frequent Element**

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        long long sum = 0;
        int l = 0, ans = 1;
        for (int r = 0; r < (int)nums.size(); ++r) {
            sum += nums[r];
            while (1LL*nums[r]*(r-l+1) - sum > k) {
                sum -= nums[l];
                ++l;
            }
            ans = max(ans, r-l+1);
        }
        return ans;
    }
};
```

## **5. Range Frequency Queries (Design)**

```cpp
#include <bits/stdc++.h>
using namespace std;
class RangeFreqQuery {
    unordered_map<int, vector<int>> pos;
public:
    RangeFreqQuery(vector<int>& arr) {
        for (int i=0;i<(int)arr.size();++i) pos[arr[i]].push_back(i);
    }
    int query(int left, int right, int value) {
        auto it = pos.find(value);
        if (it == pos.end()) return 0;
        auto &v = it->second;
        auto L = lower_bound(v.begin(), v.end(), left);
        auto R = upper_bound(v.begin(), v.end(), right);
        return (int)(R - L);
    }
};
```

## **6. Most Frequent Number Following Key in an Array**

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int mostFrequent(vector<int>& nums, int key) {
        unordered_map<int,int> c;
        for (int i=0;i+1<(int)nums.size();++i)
            if (nums[i]==key) c[nums[i+1]]++;
        int best=-1, bf=-1;
        for (auto &p: c) if (p.second > bf) { bf=p.second; best=p.first; }
        return best;
    }
};
```

## **7. Count Substrings With K-Frequency Characters I**

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    long long numberOfSubstrings(string s, int k) {
        vector<int> cnt(26,0);
        int n = s.size(), l = 0;
        long long ans = 0;
        int ge = 0;
        auto idx = [&](char ch){ return ch - 'a'; };
        for (int r=0;r<n;++r){
            int j = idx(s[r]);
            if (++cnt[j] == k) ge++;
            while (ge > 0){
                ans += (n - r);
                int cj = idx(s[l]);
                if (--cnt[cj] == k-1) ge--;
                ++l;
            }
        }
        return ans;
    }
};
```

## **8. Apply Operations to Maximize Frequency Score**

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxFrequencyScore(vector<int>& nums, long long k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<long long> pref(n+1,0);
        for (int i=0;i<n;++i) pref[i+1] = pref[i] + nums[i];
        int ans = 1, l = 0;
        for (int r=0;r<n;++r){
            while (l<=r){
                int m = (l+r)/2;
                long long leftCost = 1LL*nums[m]*(m-l) - (pref[m]-pref[l]);
                long long rightCost = (pref[r+1]-pref[m+1]) - 1LL*nums[m]*(r-m);
                long long cost = leftCost + rightCost;
                if (cost <= k) break;
                ++l;
            }
            ans = max(ans, r-l+1);
        }
        return ans;
    }
};
```

## **9. Maximum Frequency of an Element After Performing Operations II**

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        unordered_map<int,int> cnt;
        for (int x: nums) cnt[x]++;
        map<long long,int> diff;
        set<long long> cand;
        for (long long x: nums){
            diff[x - k]++; 
            diff[x + k + 1]--;
            cand.insert(x);
            cand.insert(x - k);
            cand.insert(x + k + 1);
        }
        int adjustable = 0, ans = 1;
        for (long long t: cand){
            if (diff.count(t)) adjustable += diff[t];
            int base = cnt.count((int)t) ? cnt[(int)t] : 0;
            int can_change = max(0, adjustable - base);
            ans = max(ans, base + min(numOperations, can_change));
        }
        return ans;
    }
};
```

## **10. Find Occurrences of an Element in an Array**

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> occurrencesOfElement(vector<int>& nums, vector<int>& queries, int x) {
        vector<int> pos;
        for (int i=0;i<(int)nums.size();++i) if (nums[i]==x) pos.push_back(i);
        vector<int> ans;
        for (int q: queries){
            if (1 <= q && q <= (int)pos.size()) ans.push_back(pos[q-1]);
            else ans.push_back(-1);
        }
        return ans;
    }
};
```

---


---

# **Codeforces Frequency Count — C++ Solutions (10 Problems)**

| #  | Problem                              | Link                                                        |
| -- | ------------------------------------ | ----------------------------------------------------------- |
| 1  | Petya and Strings                    | [🔗 Click](https://codeforces.com/problemset/problem/112/A) |
| 2  | Boy or Girl                          | [🔗 Click](https://codeforces.com/problemset/problem/236/A) |
| 3  | Helpful Maths                        | [🔗 Click](https://codeforces.com/problemset/problem/339/A) |
| 4  | Pangram                              | [🔗 Click](https://codeforces.com/problemset/problem/520/A) |
| 5  | Games                                | [🔗 Click](https://codeforces.com/problemset/problem/268/A) |
| 6  | Word                                 | [🔗 Click](https://codeforces.com/problemset/problem/59/A)  |
| 7  | Is your horseshoe on the other hoof? | [🔗 Click](https://codeforces.com/problemset/problem/228/A) |
| 8  | Anton and Letters                    | [🔗 Click](https://codeforces.com/problemset/problem/443/A) |
| 9  | Chat room                            | [🔗 Click](https://codeforces.com/problemset/problem/58/A)  |
| 10 | Dubstep                              | [🔗 Click](https://codeforces.com/problemset/problem/208/A) |

---

## **1. Petya and Strings**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    string a,b;
    cin>>a>>b;
    for(auto &c:a) c=tolower(c);
    for(auto &c:b) c=tolower(c);
    if(a<b) cout<<-1;
    else if(a>b) cout<<1;
    else cout<<0;
}
```

## **2. Boy or Girl**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    string s; cin>>s;
    set<char> st(s.begin(), s.end());
    cout << ((st.size()%2) ? "IGNORE HIM!" : "CHAT WITH HER!");
}
```

## **3. Helpful Maths**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    string s; cin>>s;
    vector<char> nums;
    for(int i=0;i<s.size();i+=2) nums.push_back(s[i]);
    sort(nums.begin(), nums.end());
    for(int i=0;i<nums.size();i++){
        cout<<nums[i];
        if(i+1<nums.size()) cout<<"+";
    }
}
```

## **4. Pangram**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; cin>>n;
    string s; cin>>s;
    set<char> st;
    for(auto &c:s) st.insert(tolower(c));
    cout << (st.size()==26 ? "YES" : "NO");
}
```

## **5. Games**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; cin>>n;
    vector<pair<int,int>> v(n);
    for(int i=0;i<n;i++) cin>>v[i].first>>v[i].second;
    int ans=0;
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            if(i!=j && v[i].first==v[j].second) ans++;
    cout<<ans;
}
```

## **6. Word**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    string s; cin>>s;
    int up=0, low=0;
    for(char c:s) isupper(c)?up++:low++;
    if(up>low) for(char &c:s) c=toupper(c);
    else for(char &c:s) c=tolower(c);
    cout<<s;
}
```

## **7. Is your horseshoe on the other hoof?**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    set<int> s;
    for(int i=0;i<4;i++){ int x; cin>>x; s.insert(x); }
    cout << 4 - s.size();
}
```

## **8. Anton and Letters**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    string s; getline(cin,s);
    set<char> st;
    for(char c:s) if(islower(c)) st.insert(c);
    cout<<st.size();
}
```

## **9. Chat room**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    string s; cin>>s;
    string t="hello"; int j=0;
    for(char c:s) if(c==t[j]) j++;
    cout << (j==5?"YES":"NO");
}
```

## **10. Dubstep**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    string s; cin>>s;
    string res;
    for(int i=0;i<s.size();){
        if(i+2<s.size() && s.substr(i,3)=="WUB"){
            if(!res.empty() && res.back()!=' ') res+=' ';
            i+=3;
        }else res+=s[i++];
    }
    if(!res.empty() && res.back()==' ') res.pop_back();
    cout<<res;
}
```

---


---

# **CodeChef Frequency Count — C++ Solutions (10 Problems)**

| #  | Problem                                          | Link                                                                               |
| -- | ------------------------------------------------ | ---------------------------------------------------------------------------------- |
| 1  | Frequency of Each Element in the Array (Hashing) | [🔗 Click](https://www.codechef.com/learn/course/hashing/HASH01/problems/DSAAGP35) |
| 2  | Using Hashing to Optimize Counting Frequency     | [🔗 Click](https://www.codechef.com/learn/course/hashing/HASH01/problems/DSAAGP34) |
| 3  | Frequency of Elements Using Hashing              | [🔗 Click](https://www.codechef.com/learn/course/hashing/HASH01/problems/DSAAGP36) |
| 4  | Distinct Codes                                   | [🔗 Click](https://www.codechef.com/problems/DISTCODE)                             |
| 5  | Chef and Subarrays                               | [🔗 Click](https://www.codechef.com/problems/CHEFARRP)                             |
| 6  | Lapindromes                                      | [🔗 Click](https://www.codechef.com/problems/LAPIN)                                |
| 7  | Most Frequent                                    | [🔗 Click](https://www.codechef.com/problems/MOSTFREQ)                             |
| 8  | Clean the Sequence                               | [🔗 Click](https://www.codechef.com/problems/CLEANSEQ)                             |
| 9  | Count the Holidays                               | [🔗 Click](https://www.codechef.com/problems/HOLIDAYS)                             |
| 10 | Counting Words                                   | [🔗 Click](https://www.codechef.com/problems/WORDCNT)                              |

---

## **1. Frequency of Each Element in the Array (Hashing)**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; cin>>n;
    vector<int> a(n);
    for(int i=0;i<n;i++) cin>>a[i];
    unordered_map<int,int> freq;
    for(int x:a) freq[x]++;
    for(auto &p:freq) cout<<p.first<<" "<<p.second<<"\n";
}
```

## **2. Using Hashing to Optimize Counting Frequency**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; cin>>n;
    vector<int> a(n);
    for(int i=0;i<n;i++) cin>>a[i];
    unordered_map<int,int> mp;
    for(int x:a) mp[x]++;
    int q; cin>>q;
    while(q--){
        int x; cin>>x;
        cout<<mp[x]<<"\n";
    }
}
```

## **3. Frequency of Elements Using Hashing**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; cin>>n;
    map<int,int> freq;
    for(int i=0;i<n;i++){
        int x; cin>>x;
        freq[x]++;
    }
    for(auto &p:freq) cout<<p.first<<" "<<p.second<<"\n";
}
```

## **4. Distinct Codes**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    string s; cin>>s;
    set<string> st;
    for(int i=0;i+1<s.size();i++)
        st.insert(s.substr(i,2));
    cout<<st.size();
}
```

## **5. Chef and Subarrays**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; cin>>n;
    vector<int> a(n);
    for(int &x:a) cin>>x;
    int ans=0;
    for(int i=0;i<n;i++){
        int sum=0,prod=1;
        for(int j=i;j<n;j++){
            sum+=a[j];
            prod*=a[j];
            if(sum==prod) ans++;
        }
    }
    cout<<ans;
}
```

## **6. Lapindromes**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        string s; cin>>s;
        int n=s.size();
        string a=s.substr(0,n/2);
        string b=s.substr((n+1)/2);
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        cout<<(a==b?"YES\n":"NO\n");
    }
}
```

## **7. Most Frequent**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; cin>>n;
    unordered_map<int,int> freq;
    for(int i=0;i<n;i++){
        int x; cin>>x; freq[x]++;
    }
    int ans=-1, mx=-1;
    for(auto &p:freq) if(p.second>mx || (p.second==mx && p.first<ans)){
        mx=p.second; ans=p.first;
    }
    cout<<ans;
}
```

## **8. Clean the Sequence**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; cin>>n;
    vector<int> a(n);
    for(int &x:a) cin>>x;
    a.erase(unique(a.begin(),a.end()),a.end());
    for(int x:a) cout<<x<<" ";
}
```

## **9. Count the Holidays**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; cin>>n;
    set<int> days;
    for(int i=0;i<n;i++){
        int x; cin>>x;
        if(x%7!=6 && x%7!=0) days.insert(x);
    }
    cout<<days.size();
}
```

## **10. Counting Words**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    string s; 
    getline(cin, s);
    stringstream ss(s);
    string word; int cnt=0;
    while(ss>>word) cnt++;
    cout<<cnt;
}
```

---




