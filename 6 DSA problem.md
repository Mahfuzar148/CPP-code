
---

## 🔷 1. **Find the Square Root of a Number**

### ❓ Problem:

Given `n`, find the largest integer `x` such that `x^2 ≤ n` using binary search.

### ✅ C++ Solution:

```cpp
int squareRoot(int n) {
    int left = 0, right = n, ans = 0;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (1LL * mid * mid <= n) {
            ans = mid;
            left = mid + 1;
        } else right = mid - 1;
    }
    return ans;
}
```

📥 **Input:** `n = 10`
📤 **Output:** `3`

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

### ❓ Problem:

Find the minimum element in a rotated sorted array (all elements distinct).

### ✅ C++ Solution:

```cpp
int findMin(int arr[], int n) {
    int left = 0, right = n-1;
    while (left < right) {
        int mid = (left + right)/2;
        if (arr[mid] > arr[right])
            left = mid + 1;
        else
            right = mid;
    }
    return arr[left];
}
```

📥 **Input:** `arr = [3,4,5,1,2]`
📤 **Output:** `1`

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


