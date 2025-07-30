
---

## 🔹 Problem:

```cpp
int arr[] = {10, 5, 30, 22, 17};
int n = sizeof(arr) / sizeof(arr[0]);
```

আমাদের কাজ: `arr[]` থেকে সবচেয়ে বড় মান (maximum value) বের করা।

---

## ✅ বিভিন্ন পদ্ধতিতে Maximum বের করা:

---

### 1. 🔁 Loop দিয়ে (Manually)

```cpp
int findMaxLoop(int arr[], int n) {
    int maxVal = arr[0];
    for (int i = 1; i < n; ++i)
        if (arr[i] > maxVal)
            maxVal = arr[i];
    return maxVal;
}
```

**⏱ Time Complexity:** `O(n)`
🔹 যখন STL না ব্যবহার করতে চাও।

---

### 2. 🧮 `std::max_element()` ব্যবহার করে

```cpp
#include <algorithm>

int findMaxSTL(int arr[], int n) {
    return *std::max_element(arr, arr + n);
}
```

**⏱ Time Complexity:** `O(n)`
🔹 Clean এবং সহজভাবে STL ব্যবহার করার উপায়।

---

### 3. 🔼 Array sort করে → শেষ মান

```cpp
#include <algorithm>

int findMaxSort(int arr[], int n) {
    std::sort(arr, arr + n);
    return arr[n - 1];
}
```

**⏱ Time Complexity:** `O(n log n)`
❌ শুধুমাত্র sorting দরকার হলে।

---

### 4. 🔽 Descending sort করে → প্রথম মান

```cpp
#include <algorithm>

int findMaxDescSort(int arr[], int n) {
    std::sort(arr, arr + n, std::greater<int>());
    return arr[0];
}
```

**⏱ Time Complexity:** `O(n log n)`
❌ efficiency কম, কিন্তু descending দরকার হলে ভালো।

---

### 5. 📦 `std::vector` + `max_element()`

```cpp
#include <vector>
#include <algorithm>

int findMaxVector(const std::vector<int>& v) {
    return *std::max_element(v.begin(), v.end());
}
```

**⏱ Time Complexity:** `O(n)`
🔹 যদি input vector আকারে থাকে।

---

### 6. 🌳 `std::set` ব্যবহার করে

```cpp
#include <set>

int findMaxSet(int arr[], int n) {
    std::set<int> s(arr, arr + n);
    return *s.rbegin(); // সর্বশেষ মান
}
```

**⏱ Time Complexity:** `O(n log n)`
🔹 Sorted এবং unique elements দরকার হলে।

---

### 7. 🔁 `std::multiset` ব্যবহার করে (duplicates সহ)

```cpp
#include <set>

int findMaxMultiset(int arr[], int n) {
    std::multiset<int> ms(arr, arr + n);
    return *ms.rbegin();
}
```

**⏱ Time Complexity:** `O(n log n)`
🔹 Sorted + duplicates দরকার হলে।

---

### 8. 🏔 `std::priority_queue` (Max-Heap)

```cpp
#include <queue>

int findMaxHeap(int arr[], int n) {
    std::priority_queue<int> pq(arr, arr + n);
    return pq.top();
}
```

**⏱ Time Complexity:** `O(n)` (heap তৈরি করতে)
🔹 Priority based access দরকার হলে।

---

## 📊 Summary Table:

| পদ্ধতি                   | STL | Time       | Use Case                          |
| ------------------------ | --- | ---------- | --------------------------------- |
| Loop                     | ❌   | O(n)       | STL ছাড়া সাধারণ উপায়              |
| `max_element()`          | ✅   | O(n)       | সহজ, fastest STL way              |
| Sort → last/first        | ✅   | O(n log n) | যদি sort করতেই হয়                 |
| Set / Multiset           | ✅   | O(n log n) | Sorted data + duplicates কন্ট্রোল |
| Priority Queue           | ✅   | O(n)       | Highest value priority দরকার হলে  |
| Vector + `max_element()` | ✅   | O(n)       | যখন ভেক্টর ব্যবহার করো            |

---

## ✅ Conclusion:

🔹 Best choice: `std::max_element()`
🔹 STL ছাড়া: সাধারণ `for` loop
🔹 Priority দরকার: `priority_queue`
🔹 Sorted access দরকার: `set`, `multiset`

---


