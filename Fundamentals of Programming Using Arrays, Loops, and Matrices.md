

---

## ✅ **1. Display *n* Natural Numbers and Their Sum**

---

### 📌 Problem:

Display the first `n` natural numbers and calculate their sum.

---

### 🧾 Code:

```cpp
#include <iostream>
using namespace std;

void displayNaturalNumbers(int n) {
    int sum = 0;
    cout << "Natural numbers are: ";
    for (int i = 1; i <= n; i++) {
        cout << i << " ";
        sum += i;
    }
    cout << "\nSum = " << sum << endl;
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;
    displayNaturalNumbers(n);
    return 0;
}
```

---

### 🖥️ Output:

```
Enter n: 5
Natural numbers are: 1 2 3 4 5 
Sum = 15
```

---

### 📘 Explanation:

Prints numbers from `1` to `n`, keeps a running total, and displays both.

---

## ✅ **2.i Print Number Pattern**

---

### 📌 Problem:

Print the following pattern:

```
1
22
333
4444
```

---

### 🧾 Code:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << i;
        }
        cout << endl;
    }
    return 0;
}
```

---

### 🖥️ Output (n=4):

```
1
22
333
4444
```

---

### 📘 Explanation:

Each row `i` prints `i` exactly `i` times.

---

## ✅ **2.ii Floyd’s Triangle (Binary Toggle)**

---

### 📌 Problem:

Print pattern toggling between 0 and 1:

```
1
01
101
0101
10101
```

---

### 🧾 Code:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter rows: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        int value = i % 2;
        for (int j = 1; j <= i; j++) {
            cout << value;
            value = 1 - value;
        }
        cout << endl;
    }
    return 0;
}
```

---

### 🖥️ Output (n=5):

```
1
01
101
0101
10101
```

---

### 📘 Explanation:

Starts with `1` on odd rows, `0` on even, and toggles the value each time.

---

## ✅ **2.iii Star Pattern**

---

### 📌 Problem:

Print the star pattern:

```
*
**
***
****
```

---

### 🧾 Code:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
```

---

### 🖥️ Output (n=4):

```
*
**
***
****
```

---

### 📘 Explanation:

Prints `i` stars on the `i-th` line.

---

## ✅ **3.i Read and Display Matrix**

---

### 📌 Problem:

Read a matrix of size m × n and display it.

---

### 🧾 Code:

```cpp
#include <iostream>
using namespace std;

void readAndDisplayMatrix(int m, int n) {
    int mat[10][10];
    cout << "Enter matrix elements:\n";
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            cin >> mat[i][j];

    cout << "Matrix is:\n";
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++)
            cout << mat[i][j] << " ";
        cout << endl;
    }
}

int main() {
    int m, n;
    cout << "Enter rows and cols: ";
    cin >> m >> n;
    readAndDisplayMatrix(m, n);
    return 0;
}
```

---

## ✅ **4. Matrix Multiplication**

---

### 📌 Problem:

Multiply two matrices A (m×n) and B (n×p), return result matrix C (m×p).

---

### 🧾 Code:

```cpp
#include <iostream>
using namespace std;

int main() {
    int m, n, p;
    cout << "Enter dimensions m n p: ";
    cin >> m >> n >> p;

    int A[10][10], B[10][10], C[10][10] = {0};

    cout << "Enter matrix A:\n";
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            cin >> A[i][j];

    cout << "Enter matrix B:\n";
    for (int i = 0; i < n; i++)
        for (int j = 0; j < p; j++)
            cin >> B[i][j];

    // Multiply
    for (int i = 0; i < m; i++)
        for (int j = 0; j < p; j++)
            for (int k = 0; k < n; k++)
                C[i][j] += A[i][k] * B[k][j];

    cout << "Result:\n";
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++)
            cout << C[i][j] << " ";
        cout << endl;
    }
    return 0;
}
```

---

## ✅ **5. Find Indices of Two Numbers Adding to Target**

---

### 📌 Problem:

Find 2 indices such that nums\[i] + nums\[j] = target.

---

### 🧾 Code:

```cpp
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    int nums[] = {2, 7, 11, 15};
    int target = 9;
    unordered_map<int, int> map;

    for (int i = 0; i < 4; i++) {
        int diff = target - nums[i];
        if (map.find(diff) != map.end()) {
            cout << "Indices: " << map[diff] << ", " << i << endl;
            return 0;
        }
        map[nums[i]] = i;
    }
    cout << "No solution";
    return 0;
}
```

---

### 🖥️ Output:

```
Indices: 0, 1
```

---

## ✅ **6.i Move All Zeros to End of Array**

---

### 📌 Problem:

Move all `0`s to the end while maintaining order of non-zero elements.

---

### 🧾 Code:

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {1, 0, 1, 0, 3, 12};
    int n = 6, count = 0;

    // Move non-zero elements
    for (int i = 0; i < n; i++)
        if (arr[i] != 0)
            arr[count++] = arr[i];

    // Fill remaining positions with 0
    while (count < n)
        arr[count++] = 0;

    cout << "Modified Array: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}
```

---

## ✅ **6.ii Find Duplicate Number in Array (n+1 Integers)**

---

### 📌 Problem:

Find duplicate in array where integers range from `1` to `n`.

---

### 🧾 Code:

```cpp
#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    int nums[] = {1, 3, 4, 2, 2};
    int n = 5;
    unordered_set<int> seen;

    for (int i = 0; i < n; i++) {
        if (seen.count(nums[i])) {
            cout << "Duplicate: " << nums[i] << endl;
            return 0;
        }
        seen.insert(nums[i]);
    }
    cout << "No duplicate found.";
    return 0;
}
```

---

