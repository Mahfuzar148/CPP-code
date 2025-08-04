
---

### ✅ 1. [Binary Search (704)](https://leetcode.com/problems/binary-search/)

**Approach:** Classic binary search.

```cpp
int search(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

---

### ✅ 2. [Search in Rotated Sorted Array (33)](https://leetcode.com/problems/search-in-rotated-sorted-array/)

**Approach:** Modified binary search with rotation handling.

```cpp
int search(vector<int>& nums, int target) {
    int l = 0, r = nums.size() - 1;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (nums[mid] == target) return mid;

        if (nums[l] <= nums[mid]) {
            if (nums[l] <= target && target < nums[mid]) r = mid - 1;
            else l = mid + 1;
        } else {
            if (nums[mid] < target && target <= nums[r]) l = mid + 1;
            else r = mid - 1;
        }
    }
    return -1;
}
```

---

### ✅ 3. [Find Minimum in Rotated Sorted Array (153)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

**Approach:** Binary search on rotation point.

```cpp
int findMin(vector<int>& nums) {
    int left = 0, right = nums.size() - 1;
    while (left < right) {
        int mid = (left + right) / 2;
        if (nums[mid] > nums[right]) left = mid + 1;
        else right = mid;
    }
    return nums[left];
}
```

---

### ✅ 4. [Search a 2D Matrix (74)](https://leetcode.com/problems/search-a-2d-matrix/)

**Approach:** Flattened 2D binary search.

```cpp
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int m = matrix.size(), n = matrix[0].size();
    int left = 0, right = m * n - 1;

    while (left <= right) {
        int mid = (left + right) / 2;
        int val = matrix[mid / n][mid % n];
        if (val == target) return true;
        else if (val < target) left = mid + 1;
        else right = mid - 1;
    }
    return false;
}
```

---

### ✅ 5. [Search Insert Position (35)](https://leetcode.com/problems/search-insert-position/)

**Approach:** Binary search to find insert point.

```cpp
int searchInsert(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return left;
}
```

---

### ✅ 6. [Find First and Last Position of Element (34)](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

**Approach:** Two binary searches for left and right bounds.

```cpp
vector<int> searchRange(vector<int>& nums, int target) {
    auto lower = lower_bound(nums.begin(), nums.end(), target);
    auto upper = upper_bound(nums.begin(), nums.end(), target);
    
    if (lower == nums.end() || *lower != target) return {-1, -1};
    return {int(lower - nums.begin()), int(upper - nums.begin() - 1)};
}
```

---

### ✅ 7. [Median of Two Sorted Arrays (4)](https://leetcode.com/problems/median-of-two-sorted-arrays/)

**Approach:** Binary search on partition.

```cpp
double findMedianSortedArrays(vector<int>& A, vector<int>& B) {
    if (A.size() > B.size()) return findMedianSortedArrays(B, A);
    int m = A.size(), n = B.size();
    int imin = 0, imax = m, half = (m + n + 1) / 2;

    while (imin <= imax) {
        int i = (imin + imax) / 2;
        int j = half - i;
        if (i < m && B[j - 1] > A[i]) imin = i + 1;
        else if (i > 0 && A[i - 1] > B[j]) imax = i - 1;
        else {
            int maxLeft = 0;
            if (i == 0) maxLeft = B[j - 1];
            else if (j == 0) maxLeft = A[i - 1];
            else maxLeft = max(A[i - 1], B[j - 1]);

            if ((m + n) % 2 == 1) return maxLeft;

            int minRight = 0;
            if (i == m) minRight = B[j];
            else if (j == n) minRight = A[i];
            else minRight = min(A[i], B[j]);

            return (maxLeft + minRight) / 2.0;
        }
    }
    return 0.0;
}
```

---

### ✅ 8. [Peak Index in a Mountain Array (852)](https://leetcode.com/problems/peak-index-in-a-mountain-array/)

**Approach:** Binary search for peak.

```cpp
int peakIndexInMountainArray(vector<int>& arr) {
    int left = 0, right = arr.size() - 1;
    while (left < right) {
        int mid = (left + right) / 2;
        if (arr[mid] < arr[mid + 1]) left = mid + 1;
        else right = mid;
    }
    return left;
}
```

---

### ✅ 9. [Guess Number Higher or Lower (374)](https://leetcode.com/problems/guess-number-higher-or-lower/)

**Assume** you’re given a guess API.

```cpp
int guess(int num); // Provided API

int guessNumber(int n) {
    int low = 1, high = n;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        int res = guess(mid);
        if (res == 0) return mid;
        else if (res < 0) high = mid - 1;
        else low = mid + 1;
    }
    return -1;
}
```

---

### ✅ 10. [Find Peak Element (162)](https://leetcode.com/problems/find-peak-element/)

**Approach:** Binary search for any peak.

```cpp
int findPeakElement(vector<int>& nums) {
    int l = 0, r = nums.size() - 1;
    while (l < r) {
        int mid = (l + r) / 2;
        if (nums[mid] > nums[mid + 1]) r = mid;
        else l = mid + 1;
    }
    return l;
}
```

---

---

## ✅ CodeChef Problem Solutions

---

### 1. [The Wave](https://www.codechef.com/problems/WAV2)

**Approach:** Use `binary_search` or `lower_bound` for checking presence.

```cpp
void solve() {
    int n, q; cin >> n >> q;
    vector<int> a(n);
    for (int &x : a) cin >> x;
    sort(a.begin(), a.end());

    while (q--) {
        int x; cin >> x;
        if (binary_search(a.begin(), a.end(), x)) cout << "0\n";
        else {
            int pos = lower_bound(a.begin(), a.end(), x) - a.begin();
            cout << (n - pos) << "\n";
        }
    }
}
```

---

### 2. [Coins and Triangle](https://www.codechef.com/problems/TRICOIN)

**Approach:** Find maximum `k` such that `k*(k+1)/2 ≤ N` using binary search.

```cpp
void solve() {
    int t; cin >> t;
    while (t--) {
        long long n; cin >> n;
        long long l = 1, r = 1e5, ans = 0;
        while (l <= r) {
            long long mid = (l + r) / 2;
            if (mid * (mid + 1) / 2 <= n) {
                ans = mid;
                l = mid + 1;
            } else r = mid - 1;
        }
        cout << ans << "\n";
    }
}
```

---

### 3. [Minion Chef and Bananas](https://www.codechef.com/problems/MINPERM)

**Approach:** Permutation with constraint that all increasing prefixes are at least size 1.

```cpp
void solve() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        cout << n << " ";
        for (int i = 1; i < n; i++) cout << i << " ";
        cout << "\n";
    }
}
```

---

### 4. [Wildfire](https://www.codechef.com/problems/WILDFIRE)

**Approach:** Find the maximum distance from tree to firefighter. Use `max()` on abs diff.

```cpp
void solve() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        string a, b;
        cin >> a >> b;
        int ans = 0;
        for (int i = 0; i < n; ++i)
            if (a[i] == '1') {
                int j = i;
                while (j >= 0 && b[j] != '1') --j;
                if (j >= 0) ans = max(ans, i - j);
                else ans = INT_MAX;
            }
        cout << ans << "\n";
    }
}
```

---

### 5. [Cutting Recipes](https://www.codechef.com/problems/RECIPE)

**Approach:** Find GCD of all ingredients.

```cpp
void solve() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<int> a(n);
        for (int &x : a) cin >> x;
        int g = a[0];
        for (int i = 1; i < n; i++) g = __gcd(g, a[i]);
        for (int x : a) cout << x / g << " ";
        cout << "\n";
    }
}
```

---

## ✅ Codeforces Problem Solutions

---

### 6. [Chef and Horses](https://www.codechef.com/problems/HORSES)

**Approach:** Sort the array and get minimum absolute diff.

```cpp
void solve() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<int> a(n);
        for (int &x : a) cin >> x;
        sort(a.begin(), a.end());
        int ans = INT_MAX;
        for (int i = 1; i < n; i++) ans = min(ans, a[i] - a[i - 1]);
        cout << ans << "\n";
    }
}
```

---

### 7. [Binary Search Trees (BSTOPS)](https://www.codechef.com/problems/BSTOPS)

**Approach:** Simulate insert and erase with set.

```cpp
void solve() {
    int t; cin >> t;
    while (t--) {
        int q; cin >> q;
        set<int> bst;
        while (q--) {
            string op; int x;
            cin >> op >> x;
            if (op == "i") bst.insert(x);
            else bst.erase(x);
        }
        cout << bst.size() << "\n";
    }
}
```

---

### 8. [Finding Shoes](https://www.codechef.com/problems/FINDSHOES)

**Approach:** Always need at least `n`, plus one more if `m < n`.

```cpp
void solve() {
    int t; cin >> t;
    while (t--) {
        int n, m; cin >> n >> m;
        cout << (n + max(0, n - m)) << "\n";
    }
}
```

---

### 9. [Saving the City](https://www.codechef.com/problems/SAVINGIT)

**Approach:** Greedy: Cost of cluster (first `a`, rest choose `b` or `a` depending).

```cpp
void solve() {
    int t; cin >> t;
    while (t--) {
        int a, b;
        string s;
        cin >> a >> b >> s;
        int cost = 0, first = 0, flag = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '1') {
                if (!flag) {
                    cost += a;
                    flag = 1;
                } else {
                    cost += min(a, b * (i - first - 1));
                }
                first = i;
            }
        }
        cout << cost << "\n";
    }
}
```

---

### 10. [Binary String MEX](https://www.codechef.com/problems/MEXSTRING)

**Approach:** Count 0’s and 1’s. Smallest number not present is the answer.

```cpp
void solve() {
    int t; cin >> t;
    while (t--) {
        string s; cin >> s;
        if (s.find('0') == string::npos) cout << "0\n";
        else if (s.find("01") == string::npos) cout << "1\n";
        else cout << "01\n";
    }
}
```

---

---

## ✅ Codeforces Problem Solutions (Full C++)

---

### 1. [230B. T-primes](https://codeforces.com/problemset/problem/230/B)

**Approach:** T-primes are squares of primes (e.g. 4, 9, 25, …). Precompute primes and check if the number is a square and its square root is prime.

```cpp
const int N = 1e6 + 1;
vector<bool> is_prime(N, true);

void sieve() {
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i < N; ++i)
        if (is_prime[i])
            for (int j = i * i; j < N; j += i)
                is_prime[j] = false;
}

void solve() {
    sieve();
    int n; cin >> n;
    while (n--) {
        long long x; cin >> x;
        long long root = sqrt(x);
        if (root * root == x && is_prime[root]) cout << "YES\n";
        else cout << "NO\n";
    }
}
```

---

### 2. [287B. Pipeline](https://codeforces.com/problemset/problem/287/B)

**Approach:** Use binary search to find minimum number of operations.

```cpp
void solve() {
    long long n, k; cin >> n >> k;
    if (k >= n) { cout << "1\n"; return; }

    long long left = 1, right = k - 1, ans = -1;
    while (left <= right) {
        long long mid = (left + right) / 2;
        long long pipes = (k - mid + k - 1) * mid / 2;
        if (pipes + 1 >= n) {
            ans = mid;
            right = mid - 1;
        } else left = mid + 1;
    }
    cout << ans << "\n";
}
```

---

### 3. [1237C2. Balanced Removals](https://codeforces.com/problemset/problem/1237/C2)

**Approach:** Group points based on x, y, z, and pair greedily.

```cpp
struct Point { int x, y, z, i; };
vector<Point> pts;

void solve() {
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        int x, y, z; cin >> x >> y >> z;
        pts.push_back({x, y, z, i + 1});
    }
    sort(pts.begin(), pts.end(), [](auto &a, auto &b) {
        if (a.x != b.x) return a.x < b.x;
        if (a.y != b.y) return a.y < b.y;
        return a.z < b.z;
    });

    map<pair<int,int>, vector<Point>> mp;
    for (auto &p : pts)
        mp[{p.x, p.y}].push_back(p);

    vector<Point> rest;
    for (auto &[_, group] : mp) {
        while (group.size() >= 2) {
            auto a = group.back(); group.pop_back();
            auto b = group.back(); group.pop_back();
            cout << a.i << " " << b.i << "\n";
        }
        if (!group.empty()) rest.push_back(group[0]);
    }

    // Pair remaining by x
    sort(rest.begin(), rest.end(), [](auto &a, auto &b) {
        if (a.x != b.x) return a.x < b.x;
        return a.y < b.y;
    });
    for (int i = 0; i + 1 < rest.size(); i += 2)
        cout << rest[i].i << " " << rest[i + 1].i << "\n";
}
```

---

### 4. [1201B. Zero Array](https://codeforces.com/problemset/problem/1201/B)

**Approach:** If the total sum is even and no single element is more than half, then possible.

```cpp
void solve() {
    int n; cin >> n;
    vector<int> a(n);
    long long sum = 0;
    int mx = 0;
    for (int &x : a) {
        cin >> x;
        sum += x;
        mx = max(mx, x);
    }
    cout << ((sum % 2 == 0 && mx <= sum / 2) ? "YES\n" : "NO\n");
}
```

---

### 5. [987C. Three displays](https://codeforces.com/problemset/problem/987/C)

**Approach:** Try every middle display, and find min cost left and right.

```cpp
void solve() {
    int n; cin >> n;
    vector<int> s(n), c(n);
    for (int &x : s) cin >> x;
    for (int &x : c) cin >> x;

    int ans = INT_MAX;
    for (int j = 1; j < n - 1; j++) {
        int left = INT_MAX, right = INT_MAX;
        for (int i = 0; i < j; i++)
            if (s[i] < s[j]) left = min(left, c[i]);
        for (int k = j + 1; k < n; k++)
            if (s[j] < s[k]) right = min(right, c[k]);
        if (left != INT_MAX && right != INT_MAX)
            ans = min(ans, left + c[j] + right);
    }
    cout << (ans == INT_MAX ? -1 : ans) << "\n";
}
```

---

### 6. [115A. Party](https://codeforces.com/problemset/problem/115/A)

**Approach:** Build tree, find height (max depth).

```cpp
vector<int> adj[2001];

int dfs(int u) {
    int depth = 1;
    for (int v : adj[u]) depth = max(depth, 1 + dfs(v));
    return depth;
}

void solve() {
    int n; cin >> n;
    for (int i = 1; i <= n; i++) {
        int p; cin >> p;
        if (p != -1) adj[p].push_back(i);
    }

    int ans = 0;
    for (int i = 1; i <= n; i++)
        if (adj[i].size()) ans = max(ans, dfs(i));
    cout << max(ans, 1) << "\n";
}
```

---

### 7. [160D. Edges in MST](https://codeforces.com/problemset/problem/160/D)

**Approach:** Kruskal’s MST, then find edges that can be replaced with same weight edges.

```cpp
struct Edge {
    int u, v, w, idx;
    bool operator<(const Edge &o) const {
        return w < o.w;
    }
};

vector<Edge> edges;
int par[100001], rnk[100001];

int find(int x) {
    return x == par[x] ? x : par[x] = find(par[x]);
}

bool unite(int u, int v) {
    u = find(u), v = find(v);
    if (u == v) return false;
    if (rnk[u] < rnk[v]) swap(u, v);
    par[v] = u;
    if (rnk[u] == rnk[v]) rnk[u]++;
    return true;
}

void solve() {
    int n, m; cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int u, v, w; cin >> u >> v >> w;
        edges.push_back({u, v, w, i});
    }

    iota(par, par + n + 1, 0);
    sort(edges.begin(), edges.end());

    vector<string> status(m, "none");

    for (int i = 0; i < m;) {
        int j = i;
        vector<Edge> same;
        while (j < m && edges[j].w == edges[i].w) same.push_back(edges[j++]);

        vector<pair<int, int>> added;
        for (auto &e : same) {
            if (find(e.u) != find(e.v)) added.push_back({e.u, e.v});
        }

        for (auto &[u, v] : added) unite(u, v);
        for (auto &e : same)
            if (find(e.u) != find(e.v)) status[e.idx] = "any";
            else status[e.idx] = "at least one";

        i = j;
    }

    for (auto &s : status) cout << s << "\n";
}
```

---

### 8. [1374C. Move Brackets](https://codeforces.com/problemset/problem/1374/C)

**Approach:** Count unmatched closing brackets.

```cpp
void solve() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        string s; cin >> s;
        int bal = 0, ans = 0;
        for (char c : s) {
            if (c == '(') bal++;
            else {
                if (bal) bal--;
                else ans++;
            }
        }
        cout << ans << "\n";
    }
}
```

---

### 9. [1312C. Adding Powers](https://codeforces.com/problemset/problem/1312/C)

**Approach:** Convert each number to base `k`, and check for overlapping powers.

```cpp
void solve() {
    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        map<int, int> used;
        bool ok = true;
        for (int i = 0; i < n; i++) {
            long long a; cin >> a;
            int pow = 0;
            while (a > 0) {
                int rem = a % k;
                if (rem > 1) ok = false;
                if (rem == 1) {
                    if (used[pow]) ok = false;
                    used[pow] = 1;
                }
                a /= k;
                pow++;
            }
        }
        cout << (ok ? "YES\n" : "NO\n");
    }
}
```

---

### 10. [371C. Hamburgers](https://codeforces.com/problemset/problem/371/C)

**Approach:** Binary search max burgers.

```cpp
void solve() {
    string s; cin >> s;
    long long nb, ns, nc, pb, ps, pc, r;
    cin >> nb >> ns >> nc >> pb >> ps >> pc >> r;

    int b = count(s.begin(), s.end(), 'B');
    int s_ = count(s.begin(), s.end(), 'S');
    int c = count(s.begin(), s.end(), 'C');

    long long low = 0, high = 1e13, ans = 0;
    while (low <= high) {
        long long mid = (low + high) / 2;
        long long need = max(0LL, mid * b - nb) * pb
                       + max(0LL, mid * s_ - ns) * ps
                       + max(0LL, mid * c - nc) * pc;
        if (need <= r) {
            ans = mid;
            low = mid + 1;
        } else high = mid - 1;
    }
    cout << ans << "\n";
}
```

---



## ✅ AtCoder Problem Solutions (Full C++)

---

### 1. [ABC118 B – Foods Loved by Everyone](https://atcoder.jp/contests/abc118/tasks/abc118_b)

**Approach:** Count how many people like each food, then find how many foods everyone likes.

```cpp
void solve() {
    int n, m;
    cin >> n >> m;
    vector<int> count(m + 1);
    for (int i = 0; i < n; ++i) {
        int k; cin >> k;
        for (int j = 0; j < k; ++j) {
            int x; cin >> x;
            count[x]++;
        }
    }
    int ans = 0;
    for (int i = 1; i <= m; ++i)
        if (count[i] == n) ans++;
    cout << ans << "\n";
}
```

---

### 2. [ABC203 D – Pond](https://atcoder.jp/contests/abc203/tasks/abc203_d)

**Approach:** Binary search the answer, use prefix sums to count if a median exists ≤ mid.

```cpp
int n, k;
int a[405][405], s[405][405];

bool check(int mid) {
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            s[i][j] = (a[i][j] > mid ? 1 : 0) + s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1];

    for (int i = k; i <= n; ++i)
        for (int j = k; j <= n; ++j) {
            int cnt = s[i][j] - s[i - k][j] - s[i][j - k] + s[i - k][j - k];
            if (cnt <= (k * k) / 2) return true;
        }
    return false;
}

void solve() {
    cin >> n >> k;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            cin >> a[i][j];

    int l = 0, r = 1e9, ans = -1;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (check(mid)) ans = mid, r = mid - 1;
        else l = mid + 1;
    }
    cout << ans << "\n";
}
```

---

### 3. [ABC223 D – Restricted Permutation](https://atcoder.jp/contests/abc223/tasks/abc223_d)

**Approach:** Topological sort with lexicographical order using min-heap.

```cpp
void solve() {
    int n, m; cin >> n >> m;
    vector<vector<int>> g(n + 1);
    vector<int> in(n + 1);
    for (int i = 0; i < m; ++i) {
        int a, b; cin >> a >> b;
        g[a].push_back(b);
        in[b]++;
    }

    priority_queue<int, vector<int>, greater<>> pq;
    for (int i = 1; i <= n; i++)
        if (in[i] == 0) pq.push(i);

    vector<int> res;
    while (!pq.empty()) {
        int u = pq.top(); pq.pop();
        res.push_back(u);
        for (int v : g[u])
            if (--in[v] == 0) pq.push(v);
    }

    if (res.size() != n) cout << "-1\n";
    else for (int x : res) cout << x << " ";
}
```

---

### 4. [ABC143 C – Slimes](https://atcoder.jp/contests/abc143/tasks/abc143_c)

**Approach:** Count how many character pairs are different from the previous.

```cpp
void solve() {
    int n; cin >> n;
    string s; cin >> s;
    int ans = 1;
    for (int i = 1; i < n; i++)
        if (s[i] != s[i - 1]) ans++;
    cout << ans << "\n";
}
```

---

### 5. [ABC115 C – Christmas Eve](https://atcoder.jp/contests/abc115/tasks/abc115_c)

**Approach:** Sort and find minimum height range among k items.

```cpp
void solve() {
    int n, k; cin >> n >> k;
    vector<int> h(n);
    for (int &x : h) cin >> x;
    sort(h.begin(), h.end());

    int ans = INT_MAX;
    for (int i = 0; i <= n - k; i++)
        ans = min(ans, h[i + k - 1] - h[i]);

    cout << ans << "\n";
}
```

---

### 6. [ARC104 B – DNA Sequence](https://atcoder.jp/contests/arc104/tasks/arc104_b)

**Approach:** Count how many substrings satisfy equal A-T and C-G balance.

```cpp
void solve() {
    string s; cin >> s;
    int n = s.size(), ans = 0;
    for (int i = 0; i < n; i++) {
        int a = 0, t = 0, c = 0, g = 0;
        for (int j = i; j < n; j++) {
            if (s[j] == 'A') a++;
            if (s[j] == 'T') t++;
            if (s[j] == 'C') c++;
            if (s[j] == 'G') g++;
            if (a == t && c == g) ans++;
        }
    }
    cout << ans << "\n";
}
```

---

### 7. [ARC118 B – Digital Graffiti](https://atcoder.jp/contests/arc118/tasks/arc118_b)

**Approach:** Construct a grid with guaranteed unique surrounding patterns for each 2x2 square.

```cpp
void solve() {
    int k; cin >> k;
    const int n = 100;
    vector<string> grid(n, string(n, '.'));

    int i = 0, j = 0;
    while (k--) {
        grid[i][j] = '#';
        grid[i][j + 1] = '#';
        grid[i + 1][j] = '#';
        grid[i + 1][j + 1] = '#';
        j += 3;
        if (j + 2 >= n) {
            j = 0;
            i += 3;
        }
    }
    cout << n << "\n";
    for (auto &row : grid) cout << row << "\n";
}
```

---

### 8. [ARC065 C – bugs](https://atcoder.jp/contests/arc065/tasks/arc065_c)

**Approach:** DSU on (man, woman) split by offset, check contradiction.

```cpp
const int N = 2e5 + 5;
int par[N * 2];

int find(int x) {
    return x == par[x] ? x : par[x] = find(par[x]);
}

void unite(int u, int v) {
    par[find(u)] = find(v);
}

void solve() {
    int n, m; cin >> n >> m;
    for (int i = 1; i <= 2 * n; i++) par[i] = i;

    bool ok = true;
    while (m--) {
        int x, y; cin >> x >> y;
        unite(x, y + n);
        unite(x + n, y);
        if (find(x) == find(x + n)) ok = false;
    }
    cout << (ok ? "YES" : "NO") << "\n";
}
```

---

### 9. [ABC067 C – Splitting Piles](https://atcoder.jp/contests/abc067/tasks/arc078_b)

**Approach:** Prefix sum; try every split and minimize absolute difference.

```cpp
void solve() {
    int n; cin >> n;
    vector<long long> a(n), pref(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    pref[0] = a[0];
    for (int i = 1; i < n; i++) pref[i] = pref[i - 1] + a[i];

    long long ans = LLONG_MAX;
    for (int i = 0; i < n - 1; ++i)
        ans = min(ans, abs(pref[i] - (pref[n - 1] - pref[i])));
    cout << ans << "\n";
}
```

---

### 10. [ABC217 D – Cutting Woods](https://atcoder.jp/contests/abc217/tasks/abc217_d)

**Approach:** Maintain cut positions using `set`, and use `upper_bound` to find segment.

```cpp
void solve() {
    int L, Q; cin >> L >> Q;
    set<int> cuts = {0, L};
    while (Q--) {
        int c, x; cin >> c >> x;
        if (c == 1) cuts.insert(x);
        else {
            auto r = *cuts.upper_bound(x);
            auto l = *prev(cuts.upper_bound(x));
            cout << r - l << "\n";
        }
    }
}
```

---




