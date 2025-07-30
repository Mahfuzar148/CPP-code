
---

### 🔢 Input:

```cpp
int arr[] = {5, 3, 7, 9, 3};
int n = sizeof(arr) / sizeof(arr[0]);
int target = 3;
```

---

## ✅ 1. Linear Search (Brute Force)

```cpp
int firstOccurrenceLinear(int arr[], int n, int target) {
    for (int i = 0; i < n; ++i)
        if (arr[i] == target)
            return i;
    return -1;
}
```

---

## ✅ 2. STL `find()`

```cpp
#include <algorithm>

int firstOccurrenceSTL(int arr[], int n, int target) {
    auto it = std::find(arr, arr + n, target);
    return (it != arr + n) ? (it - arr) : -1;
}
```

---

## ✅ 3. Binary Search (If Sorted)

```cpp
int firstOccurrenceBinarySearch(int arr[], int n, int target) {
    int left = 0, right = n - 1, res = -1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] == target) {
            res = mid;
            right = mid - 1;
        } else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return res;
}
```

---

## ✅ 4. `std::lower_bound()` (Sorted Array)

```cpp
#include <algorithm>

int firstOccurrenceLowerBound(int arr[], int n, int target) {
    auto it = std::lower_bound(arr, arr + n, target);
    if (it != arr + n && *it == target)
        return it - arr;
    return -1;
}
```

---

## ✅ 5. Sort with Index Tracking (If You Must Sort)

```cpp
#include <algorithm>
#include <vector>

int firstOccurrenceSortedIndex(int arr[], int n, int target) {
    std::vector<std::pair<int, int>> v;
    for (int i = 0; i < n; ++i)
        v.push_back({arr[i], i});
    
    std::sort(v.begin(), v.end());

    for (auto& p : v)
        if (p.first == target)
            return p.second;
    return -1;
}
```

---

### ✅ Summary (Only Best Options)

| Method             | Time       | Sorted Required | Index Returned |
| ------------------ | ---------- | --------------- | -------------- |
| Linear Search      | O(n)       | ❌               | ✅              |
| `std::find()`      | O(n)       | ❌               | ✅              |
| Binary Search      | O(log n)   | ✅               | ✅              |
| `lower_bound()`    | O(log n)   | ✅               | ✅              |
| Sort + Index Track | O(n log n) | ❌               | ✅              |

---

