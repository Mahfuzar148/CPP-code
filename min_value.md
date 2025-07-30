
---

## 🔹 Problem:

```cpp
int arr[] = {10, 5, 30, 22, 17};
int n = sizeof(arr) / sizeof(arr[0]);
```

আমাদের কাজ: `arr[]` থেকে সবচেয়ে ছোট মান (minimum value) বের করা।

---

## ✅ বিভিন্ন পদ্ধতিতে Minimum বের করা:

---

### 1. 🔁 Loop দিয়ে (Manually)

```cpp
int findMinLoop(int arr[], int n) {
    int minVal = arr[0];
    for (int i = 1; i < n; ++i)
        if (arr[i] < minVal)
            minVal = arr[i];
    return minVal;
}
```

**⏱ Time Complexity:** `O(n)`
🔹 যখন STL ব্যবহার করতে না চাও।

---

### 2. 🧮 `std::min_element()` ব্যবহার করে

```cpp
#include <algorithm>

int findMinSTL(int arr[], int n) {
    return *std::min_element(arr, arr + n);
}
```

**⏱ Time Complexity:** `O(n)`
🔹 Simple এবং fastest STL solution।

---

### 3. 🔼 Array sort করে → প্রথম মান

```cpp
#include <algorithm>

int findMinSort(int arr[], int n) {
    std::sort(arr, arr + n);
    return arr[0];
}
```

**⏱ Time Complexity:** `O(n log n)`
🔹 যদি array আগেই sort করা দরকার হয়।

---

### 4. 🔽 Descending sort করে → শেষ মান

```cpp
#include <algorithm>

int findMinDescSort(int arr[], int n) {
    std::sort(arr, arr + n, std::greater<int>());
    return arr[n - 1];
}
```

**⏱ Time Complexity:** `O(n log n)`
❌ efficiency কম, কিন্তু descending দরকার হলে উপযুক্ত।

---

### 5. 📦 `std::vector` + `min_element()`

```cpp
#include <vector>
#include <algorithm>

int findMinVector(const std::vector<int>& v) {
    return *std::min_element(v.begin(), v.end());
}
```

**⏱ Time Complexity:** `O(n)`
🔹 যখন input vector আকারে থাকে।

---

### 6. 🌳 `std::set` ব্যবহার করে

```cpp
#include <set>

int findMinSet(int arr[], int n) {
    std::set<int> s(arr, arr + n);
    return *s.begin(); // প্রথম মান
}
```

**⏱ Time Complexity:** `O(n log n)`
🔹 Sorted এবং unique elements দরকার হলে।

---

### 7. 🔁 `std::multiset` ব্যবহার করে (duplicates সহ)

```cpp
#include <set>

int findMinMultiset(int arr[], int n) {
    std::multiset<int> ms(arr, arr + n);
    return *ms.begin();
}
```

**⏱ Time Complexity:** `O(n log n)`
🔹 Sorted + duplicates দরকার হলে।

---

### 8. 🏔 `std::priority_queue` → Min Heap

```cpp
#include <queue>
#include <vector>
#include <functional>

int findMinHeap(int arr[], int n) {
    std::priority_queue<int, std::vector<int>, std::greater<int>> pq(arr, arr + n);
    return pq.top();
}
```

**⏱ Time Complexity:** `O(n)`
🔹 যদি প্রাধান্য ভিত্তিক (priority-based) access দরকার হয়।

---

## 📊 Summary Table:

| পদ্ধতি                    | STL | Time       | Use Case                          |
| ------------------------- | --- | ---------- | --------------------------------- |
| Loop                      | ❌   | O(n)       | STL ছাড়া সাধারণ উপায়              |
| `min_element()`           | ✅   | O(n)       | সহজ ও efficient STL ব্যবহার       |
| Sort → প্রথম মান          | ✅   | O(n log n) | যদি sort লাগেই                    |
| Set / Multiset            | ✅   | O(n log n) | Sorted data + duplicates কন্ট্রোল |
| Priority Queue (Min-Heap) | ✅   | O(n)       | Lowest value priority দরকার হলে   |
| Vector + `min_element()`  | ✅   | O(n)       | যখন ভেক্টর ব্যবহার করো            |

---

## ✅ Conclusion:

🔹 Best overall: `std::min_element()`
🔹 STL ছাড়া: সাধারণ `for` loop
🔹 Priority দরকার: `priority_queue (min-heap)`
🔹 Sorted access দরকার: `set`, `multiset`

---
