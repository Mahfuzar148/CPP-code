
---

## 🔷 ১. কী হলো Rotated Sorted Array?

একটা sorted array ধরো:
`[1, 2, 3, 4, 5, 6, 7]`

এখন এটাকে একটা pivot দিয়ে ঘোরালে (rotate করলে) হয়:
`[4, 5, 6, 7, 1, 2, 3]`

এখানে array এখন পুরোপুরি sorted না, কিন্তু দুইটা sorted অংশ আছে — `[4,5,6,7]` এবং `[1,2,3]`।

---

## 🔷 ২. সাধারণ Binary Search (Sorted Array)

সাধারণ binary search কাজ করে কারণ array সম্পূর্ণ sorted। আমরা middle element নিয়ে দেখি, যদি target ছোট হয় তাহলে left সাইডে খুঁজি, বড় হলে right সাইডে খুঁজি।

---

## 🔷 ৩. Rotated Sorted Array-এ Binary Search কিভাবে?

array পুরোটা sorted না হলেও, প্রতিটা step-এ **middle element** নিয়ে দুই পাশের কোন অংশ sorted আছে তা খুঁজে বের করতে পারি।

ধাপগুলো:

1. Calculate `mid = (left + right) / 2`

2. যদি `arr[mid] == target` — তখন index পেয়ে গেছি, রিটার্ন করব।

3. else, check করে দেখতে হবে কোন দিক sorted:

   * যদি `arr[left] <= arr[mid]` হয়, তাহলে left থেকে mid পর্যন্ত অংশ **sorted**।

     * এখন যদি target থাকে এই sorted অংশে, অর্থাৎ `arr[left] <= target < arr[mid]` হয়, তাহলে আমরা খুঁজব **left থেকে mid-1** পর্যন্ত।
     * না হলে, target থাকতে পারে mid+1 থেকে right এ, তাই left = mid+1 করব।

   * না হলে, অর্থাৎ `arr[mid] < arr[left]`, তাহলে right থেকে mid পর্যন্ত অংশ **sorted**।

     * যদি target থাকে এই sorted অংশে, অর্থাৎ `arr[mid] < target <= arr[right]`, তাহলে left = mid + 1 করব।
     * না হলে, right = mid -1 করব।

---

## 🔷 ৪. একটা Example দিয়ে বুঝি

`arr = [4,5,6,7,1,2,3]`, target = 2

* left=0, right=6
* mid=3 → arr\[mid]=7
* arr\[left]=4 <= arr\[mid]=7 → left half sorted
* target=2 কোথায়? 4 থেকে 7 এর মধ্যে নয় → তাহলে left = mid+1 = 4
* এখন left=4, right=6
* mid=5 → arr\[mid]=2
* arr\[mid] == target → found at index 5

---

## সংক্ষেপে:

| Step                        | Action                                                               |
| --------------------------- | -------------------------------------------------------------------- |
| Check if mid == target      | Return mid                                                           |
| Check which half sorted     | `if arr[left] <= arr[mid]` → left half sorted else right half sorted |
| Decide which half to search | If target in sorted half → narrow to that half, else other half      |

---

## 🔷 ৫. Summary

* রোটেটেড sorted array-এ binary search চলতে পারে কারণ প্রতিটা ধাপে array এর একটি অংশ sorted থাকে।
* আমরা সেই অংশ চিহ্নিত করে খুঁজে সেই অংশেই সার্চকে সীমাবদ্ধ করি।
* তাই টাইম কমপ্লেক্সিটি সাধারণ binary search এর মতো `O(log n)` থাকে।

---



---

---

### ✅ Full C++ Code: Find Floor of Square Root using Binary Search

```cpp
#include <iostream>
using namespace std;

// Function to find largest x such that x^2 <= n
int squareRoot(int n) {
    int left = 0, right = n, ans = 0;
    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (1LL * mid * mid <= n) {
            ans = mid;         // mid is a possible answer
            left = mid + 1;    // try to find a bigger one
        } else {
            right = mid - 1;   // mid is too big
        }
    }
    return ans;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;

    int result = squareRoot(n);
    cout << "Largest x such that x^2 <= " << n << " is: " << result << endl;

    return 0;
}
```

---

### 🧪 Sample I/O:

```
Enter a number: 10
Largest x such that x^2 <= 10 is: 3
```

---

### 🧠 Time Complexity:

* **O(log n)** — Binary search reduces the range exponentially.

### ✅ Notes:

* This gives the **floor** value of square root.
* Uses `1LL * mid * mid` to avoid integer overflow during multiplication.

---


---

## 🔷 2. **Search in a Rotated Sorted Array**

### ❓ Problem:

Find the index of a target element in a rotated sorted array.

### ✅ C++ Solution:

```cpp
int searchRotated(int arr[], int n, int target) {
    int left = 0, right = n-1;
    while (left <= right) {
        int mid = (left + right)/2;
        if (arr[mid] == target) return mid;
        if (arr[left] <= arr[mid]) {
            if (arr[left] <= target && target < arr[mid])
                right = mid - 1;
            else left = mid + 1;
        } else {
            if (arr[mid] < target && target <= arr[right])
                left = mid + 1;
            else right = mid - 1;
        }
    }
    return -1;
}
```

📥 **Input:** `arr = [3,4,5,1,2], x = 2`
📤 **Output:** `4`

---

## 🔷 3. **Finding Minimum in a Rotated Sorted Array**


---

## ✅ Full Code with Multiple Test Cases

```cpp
#include <iostream>
using namespace std;

int findMin(int arr[], int n) {
    int left = 0, right = n - 1;

    while (left < right) {
        int mid = (left + right) / 2;

        // Right side is unsorted → minimum must be there
        if (arr[mid] > arr[right])
            left = mid + 1;
        else
            right = mid; // mid might be minimum
    }

    return arr[left];
}

int main() {
    // Test Case 1
    int arr1[] = {3, 4, 5, 1, 2};
    cout << "Minimum in arr1: " << findMin(arr1, 5) << endl; // Output: 1

    // Test Case 2
    int arr2[] = {10, 12, 15, 2, 5, 6, 8};
    cout << "Minimum in arr2: " << findMin(arr2, 7) << endl; // Output: 2

    // Test Case 3
    int arr3[] = {1, 2, 3, 4, 5}; // not rotated
    cout << "Minimum in arr3: " << findMin(arr3, 5) << endl; // Output: 1

    // Test Case 4
    int arr4[] = {5, 1, 2, 3, 4};
    cout << "Minimum in arr4: " << findMin(arr4, 5) << endl; // Output: 1

    // Test Case 5
    int arr5[] = {2};
    cout << "Minimum in arr5: " << findMin(arr5, 1) << endl; // Output: 2

    return 0;
}
```

---

## 🧪 Output:

```
Minimum in arr1: 1
Minimum in arr2: 2
Minimum in arr3: 1
Minimum in arr4: 1
Minimum in arr5: 2
```

---

## ✅ Complexity:

* **Time Complexity:** `O(log n)` → কারণ আমরা প্রতিবার array-র অর্ধেক বাদ দিচ্ছি।
* **Space Complexity:** `O(1)` → কোনো অতিরিক্ত মেমোরি ব্যবহার হচ্ছে না।

---


---

## 🔷 4. **Find the First Occurrence of a Target**

### ❓ Problem:

Return the first index of a target value in an array.

### ✅ C++ Solution:

```cpp
int firstOccurrence(int arr[], int n, int target) {
    int left = 0, right = n-1, res = -1;
    while (left <= right) {
        int mid = (left + right)/2;
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

📥 **Input:** `arr = [5,3,7,9,3], x = 3`
📤 **Output:** `1`

---

## 🔷 5. **Find the Maximum Element in an Array**

### ✅ C++ Solution:

```cpp
int findMax(int arr[], int n) {
    int maxVal = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > maxVal)
            maxVal = arr[i];
    return maxVal;
}
```

📥 **Input:** `arr = [1,7,3,9,5]`
📤 **Output:** `9`

---

## 🔷 6. **Count Occurrences of a Target**

### ✅ C++ Solution:

```cpp
int countOccurrences(int arr[], int n, int target) {
    int count = 0;
    for (int i = 0; i < n; i++)
        if (arr[i] == target)
            count++;
    return count;
}
```

📥 **Input:** `arr = [2,4,2,8,2], x = 2`
📤 **Output:** `3`

---


