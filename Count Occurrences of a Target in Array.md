
---

# ✅ Problem: Count Occurrences of a Target in Array

**প্রশ্ন:**
তোমাকে একটি `array/vector` এবং একটি `target` দেওয়া হবে। তুমি বের করবে সেই `target` কতবার আছে।

---

## 📌 Input:

```cpp
arr = [2, 4, 2, 8, 2], target = 2
```

📤 Output:

```
3
```

---

# 🧠 সব পদ্ধতির সমাধান

---

## 🟩 1. **Linear Search (Brute Force)**

```cpp
int countByLinearSearch(int arr[], int n, int target) {
    int cnt = 0;
    for(int i = 0; i < n; i++) {
        if(arr[i] == target) cnt++;
    }
    return cnt;
}
```

✅ যেকোনো array-তে কাজ করে
🕒 Time: `O(n)`, Space: `O(1)`

---

## 🟩 2. **Built-in `count()` for Array (C-style)**

👉 C++-এ `count()` STL শুধুমাত্র iterator ব্যবহার করে, তাই raw array → iterator বানিয়ে দিতে হবে।

```cpp
#include <algorithm>

int countInArrayBuiltIn(int arr[], int n, int target) {
    return std::count(arr, arr + n, target);
}
```

🧼 Short & clean
🕒 Time: `O(n)`, Space: `O(1)`

---

## 🟩 3. **Built-in `count()` for Vector**

```cpp
#include <vector>
#include <algorithm>

int countInVectorBuiltIn(const std::vector<int>& vec, int target) {
    return std::count(vec.begin(), vec.end(), target);
}
```

---

## 🟩 4. **Binary Search (for sorted array - raw array)**

```cpp
#include <algorithm>

int countByBinarySearchArray(int arr[], int n, int target) {
    int* low = std::lower_bound(arr, arr + n, target);
    int* up = std::upper_bound(arr, arr + n, target);
    return up - low;
}
```

🔔 Only works if array is **sorted**
🕒 Time: `O(log n)`

---

## 🟩 5. **Binary Search with Vector (sorted vector)**

```cpp
int countByBinarySearchVector(const std::vector<int>& vec, int target) {
    auto low = std::lower_bound(vec.begin(), vec.end(), target);
    auto up = std::upper_bound(vec.begin(), vec.end(), target);
    return up - low;
}
```

---

## 🟩 6. **Frequency Array (for small integers)**

```cpp
int countUsingFrequencyArray(int arr[], int n, int target) {
    const int MAX = 1000;
    int freq[MAX] = {0};
    for(int i = 0; i < n; i++) {
        freq[arr[i]]++;
    }
    return freq[target];
}
```

⚠️ Only when values are small (e.g., 0–999)
🕒 Time: `O(n)`, Space: `O(MAX)`

---

## 🟩 7. **Using Map (unordered\_map)**

```cpp
#include <unordered_map>

int countUsingMap(int arr[], int n, int target) {
    std::unordered_map<int, int> freq;
    for(int i = 0; i < n; i++) {
        freq[arr[i]]++;
    }
    return freq[target];
}
```

📈 Effective when many frequency queries are needed
🕒 Time: `O(n)`, Space: `O(n)`

---



---

## 🟩 8. **Using Multiset (for fun/learning)**

```cpp
#include <set>

int countUsingMultiset(int arr[], int n, int target) {
    std::multiset<int> ms(arr, arr + n);
    return ms.count(target);
}
```

🧪 Not recommended in production, but works.

---

# 🧪 Sample Main Function

```cpp
int main() {
    int arr[] = {2, 4, 2, 8, 2};
    int n = sizeof(arr) / sizeof(arr[0]);
    vector<int> vec(arr, arr + n);
    int target = 2;

    cout << "Linear Search: " << countByLinearSearch(arr, n, target) << endl;
    cout << "Built-in count (Array): " << countInArrayBuiltIn(arr, n, target) << endl;
    cout << "Built-in count (Vector): " << countInVectorBuiltIn(vec, target) << endl;
    cout << "Map Count: " << countUsingMap(arr, n, target) << endl;
    cout << "Freq Array Count: " << countUsingFrequencyArray(arr, n, target) << endl;
    

    sort(arr, arr + n);
    sort(vec.begin(), vec.end());

    cout << "Binary Search (Array): " << countByBinarySearchArray(arr, n, target) << endl;
    cout << "Binary Search (Vector): " << countByBinarySearchVector(vec, target) << endl;

    return 0;
}
```

---

## 📘 Summary Table

| Method              | Time     | Space        | Use-case                                 |
| ------------------- | -------- | ------------ | ---------------------------------------- |
| Linear Search       | O(n)     | O(1)         | Universal                                |
| `std::count()`      | O(n)     | O(1)         | Clean STL                                |
| Binary Search       | O(log n) | O(1)         | Sorted arrays only                       |
| `unordered_map`     | O(n)     | O(n)         | For multiple queries                     |
| Frequency Array     | O(n)     | O(max value) | Fast & memory efficient for small values |
| Recursive           | O(n)     | O(n)         | For learning only                        |
| `multiset::count()` | O(log n) | O(n)         | Just for interest                        |

---

## 📁 GitHub File Name Suggestion:

```
count_occurrences_all_methods.cpp
```

---

🔧 *
