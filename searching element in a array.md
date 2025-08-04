# 📘 C++ STL দিয়ে একটি সংখ্যা খুঁজে বের করার সব পদ্ধতি — সম্পূর্ণ ডকুমেন্টেশন

এই ডকুমেন্টে C++ Standard Template Library (STL)-এর সাহায্যে কিভাবে একটি সংখ্যা অ্যারে বা ভেক্টর থেকে খুঁজে বের করা যায়, তার সবগুলো উপায় একে একে ব্যাখ্যা করা হয়েছে। প্রতিটি পদ্ধতির ক্ষেত্রে রয়েছে — ব্যবহারের শর্ত, সময় জটিলতা, উপযোগিতা এবং পূর্ণাঙ্গ C++ কোড।

---

## 🔹 Overview

C++-এ একটি সংখ্যা খুঁজে বের করার জন্য বিভিন্ন ধরনের প্রশ্ন সামনে আসে:

* সংখ্যা আছে কি না?
* কতবার আছে?
* কোথায় শুরু হয়েছে?
* কোথায় শেষ হয়েছে?
* পুরোটা একসাথে বের করতে পারি?

এই প্রশ্নগুলোর উত্তর পাওয়ার জন্য STL-এ রয়েছে একাধিক built-in এবং optimized ফাংশন। নিচে আমরা সেগুলো একে একে দেখবো।

---

## ✅ ১. Linear Search

### 📌 ব্যবহার:

যেকোনো unsorted অ্যারেতে সরাসরি খুঁজতে চাইলে।

### 🧠 ব্যাখ্যা:

এই পদ্ধতিতে অ্যারের প্রতিটি উপাদানকে এক এক করে চেক করা হয়। যদি কোনো উপাদান খোঁজার সংখ্যার (key) সমান হয়, তাহলে সেই উপাদানের index ফেরত দেয়। না পেলে `-1` রিটার্ন করে।

### 🕒 Time Complexity: `O(n)`

### ✅ কোড:

```cpp
#include <iostream>
using namespace std;

int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; ++i) {
        if (arr[i] == key)
            return i;
    }
    return -1;
}

int main() {
    int arr[] = {7, 4, 2, 8, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 8;

    int index = linearSearch(arr, n, key);

    if (index != -1)
        cout << "Number found at index: " << index << endl;
    else
        cout << "Number not found" << endl;
}
```

---

## ✅ ২. Binary Search

### 📌 ব্যবহার:

Sorted array-এর মধ্যে দ্রুত খোঁজার জন্য।

### 🧠 ব্যাখ্যা:

Binary Search শুধুমাত্র **sorted array**-এর জন্য প্রযোজ্য। প্রতিবার অ্যারেকে অর্ধেক করে ভাগ করে নেয় এবং মধ্যের উপাদানের সাথে তুলনা করে।

### 🕒 Time Complexity: `O(log n)`

### ✅ কোড:

```cpp
#include <iostream>
using namespace std;

int binarySearch(int arr[], int n, int key) {
    int left = 0, right = n - 1;

    while (left <= right) {
        int mid = (left + right) / 2;

        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            left = mid + 1;
        else
            right = mid - 1;
    }

    return -1;
}

int main() {
    int arr[] = {1, 3, 5, 7, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 7;

    int index = binarySearch(arr, n, key);

    if (index != -1)
        cout << "Number found at index: " << index << endl;
    else
        cout << "Number not found" << endl;
}
```

---

## ✅ ৩. Count Frequency (Manual)

### 📌 ব্যবহার:

একটি সংখ্যা অ্যারেতে কতবার আছে, সেটা জানতে।

### 🧠 ব্যাখ্যা:

এই পদ্ধতিতে প্রতিটি উপাদানকে চেক করে দেখা হয়, সেটি কী খোঁজার সংখ্যার (key) সমান কিনা। সমান হলে কাউন্টার বাড়িয়ে দেওয়া হয়।

### 🕒 Time Complexity: `O(n)`

### ✅ কোড:

```cpp
#include <iostream>
using namespace std;

int countFrequency(int arr[], int n, int key) {
    int count = 0;

    for (int i = 0; i < n; ++i) {
        if (arr[i] == key)
            count++;
    }

    return count;
}

int main() {
    int arr[] = {2, 5, 2, 8, 2, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 2;

    int count = countFrequency(arr, n, key);

    if (count > 0)
        cout << "Number found " << count << " times." << endl;
    else
        cout << "Number not found" << endl;
}
```

---

## ✅ ৪. Using `std::find()` (with vector)

### 🧠 ব্যাখ্যা:

`std::find()` হল STL-এর একটি built-in algorithm যা একটি iterator রেঞ্জে লুপ চালিয়ে **প্রথম মিল পাওয়া উপাদান** return করে।

🔍 এটি linear search ভিত্তিক এবং `==` অপারেটরের সাহায্যে element match করে।

✅ যদি উপাদান খুঁজে পায়, তাহলে তার iterator return করে। না পেলে `.end()` return করে।

### ⏱ Time Complexity:

* `O(n)` (worst-case)

### ✅ কখন ব্যবহার করা ভালো:

* container unsorted হলে
* প্রথম match-এর index দরকার হলে
* শুধুমাত্র STL container যেমন vector, list, deque-তে

### 📌 ব্যবহার:

STL container (vector, list) এর মধ্যে সংখ্যার অবস্থান বের করতে।

### 🧠 ব্যাখ্যা:

`std::find()` হল C++ STL-এর একটি ফাংশন যা ভেক্টরের মধ্যে থেকে খোঁজার সংখ্যা (key) খুঁজে বের করে। এটি প্রথম match-এর iterator রিটার্ন করে।

### 🕒 Time Complexity: `O(n)`

### ✅ কোড:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> vec = {10, 20, 30, 40, 50};
    int key = 30;

    auto it = find(vec.begin(), vec.end(), key);

    if (it != vec.end()) {
        int index = it - vec.begin();
        cout << "Number found at index: " << index << endl;
    } else {
        cout << "Number not found" << endl;
    }
}
```

---

## ✅ ৫. `std::count()` (Built-in)

### 🧠 ব্যাখ্যা:

`std::count()` হল একটি linear search ভিত্তিক built-in function যেটি container-এর শুরু থেকে শেষ পর্যন্ত গিয়ে key-এর সাথে মিলে এমন উপাদানগুলোর সংখ্যা গণনা করে।

🔍 এটি `for` লুপের মতো করেই কাজ করে, কিন্তু STL লাইব্রেরির ভেতরে `__count_if()` নামে একটি internal template ব্যবহার করে ইটারেটর রেঞ্জে traversal করে।

### ⏱ Time Complexity:

* `O(n)` (কারণ প্রতিটি উপাদান একবার করে চেক করে)

### ✅ কখন ব্যবহার করা ভালো:

* অ্যারে/ভেক্টর unsorted হলেও
* শুধু count দরকার হলে — index দরকার নেই
* কোড ছোট রাখতে চাইলে

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> vec = {2, 3, 4, 2, 5, 2};
    int key = 2;

    int count_val = count(vec.begin(), vec.end(), key);
    if (count_val > 0)
        cout << "Number found " << count_val << " times." << endl;
    else
        cout << "Number not found" << endl;
}
```

---

## ✅ ৬. `std::binary_search()`

### 🧠 ব্যাখ্যা:

`std::binary_search()` হল STL-এর একটি built-in function যা internally `lower_bound()` ব্যবহার করে, এবং শুধু `true`/`false` রিটার্ন করে — সংখ্যাটি আছে কি না।

🔍 এটি Binary Search algorithm ব্যবহার করে এবং `O(log n)` সময়ে কাজ করে। যদি `lower_bound()` যে position return করে তা valid হয় এবং ঐ position-এ থাকা উপাদান `key`-এর সমান হয়, তাহলে `true` return করে।

### ⏱ Time Complexity:

* `O(log n)`

### ✅ কখন ব্যবহার করা ভালো:

* sorted container-এ শুধুমাত্র presence চেক করতে (index দরকার না হলে)
* performance important হলে

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> vec = {1, 3, 5, 7, 9};
    int key = 5;

    bool found = binary_search(vec.begin(), vec.end(), key);
    if (found)
        cout << "Number found." << endl;
    else
        cout << "Number not found." << endl;
}
```

---

## ✅ ৭. `std::lower_bound()`

### 🧠 ব্যাখ্যা:

`std::lower_bound()` হল একটি Binary Search ভিত্তিক ফাংশন যা `__lower_bound()` internal helper function ব্যবহার করে। এটি binary partition technique এর উপর কাজ করে। প্রতি ধাপে search space অর্ধেক হয়।

🔍 এটি key-এর প্রথম >= position return করে, এবং iterator দিয়ে কাজ করে — যেটা iterator arithmetic দ্বারা position নির্ণয় করে।

### 📝 শর্ত:

* container অবশ্যই **sorted** হতে হবে।

### 🕒 Time Complexity: `O(log n)`

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> vec = {1, 3, 3, 5, 7};
    int key = 3;

    auto it = lower_bound(vec.begin(), vec.end(), key);
    int index = it - vec.begin();

    if (index != vec.size() && *it == key)
        cout << "Number found at index: " << index << endl;
    else
        cout << "Number not found" << endl;
}
```

---

## ✅ ৮. `std::upper_bound()`

### 🧠 ব্যাখ্যা:

`std::upper_bound()` ও Binary Search ভিত্তিক একটি ফাংশন যা `__upper_bound()` নামে STL-এর internal helper function ব্যবহার করে। এটি key-এর থেকে বড় প্রথম উপাদান খোঁজে।

🔍 এর মধ্যকার main difference হচ্ছে, `lower_bound()` key সহ সব বড় মানের দিকে যায়, আর `upper_bound()` শুধু strictly greater উপাদানে যায়।

### 📝 শর্ত:

* container অবশ্যই **sorted** হতে হবে।

### 🕒 Time Complexity: `O(log n)`

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> vec = {1, 3, 3, 5, 7};
    int key = 3;

    auto it = upper_bound(vec.begin(), vec.end(), key);
    int index = it - vec.begin();

    cout << "Upper bound index: " << index << endl;
}
```

---

## ✅ ৯. `std::equal_range()`

### 🧠 ব্যাখ্যা:

`std::equal_range()` হল C++ STL-এর একটি Binary Search ভিত্তিক ফাংশন, যা একই সঙ্গে দুটি iterator রিটার্ন করে:

* প্রথমটি হল `lower_bound` (প্রথম ≥ key)
* দ্বিতীয়টি হল `upper_bound` (প্রথম > key)

📌 এই দুটি position-এর মধ্যকার পার্থক্য হল key-টি অ্যারেতে **কতবার এসেছে**।

🔍 এটি একসাথে **start এবং end position** পেতে দারুণ কার্যকর, বিশেষ করে যখন তুমি frequency, range বা সীমানা জানতে চাও।

### ✅ কখন ব্যবহার করা ভালো:

* একই key অনেকবার আছে এবং তুমি চাও তার **range** বা **count**
* তুমি একসাথে শুরু ও শেষ index পেতে চাও → তখন `equal_range()` ব্যবহার করো।
* performance চাও `O(log n)`-এ

### 📝 শর্ত:

* container অবশ্যই **sorted** হতে হবে।

### 🕒 Time Complexity: `O(log n)`

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> vec = {1, 3, 3, 3, 5, 7};
    int key = 3;

    auto range = equal_range(vec.begin(), vec.end(), key);
    int lb = range.first - vec.begin();
    int ub = range.second - vec.begin();

    cout << "Number found " << (ub - lb) << " times." << endl;
}
```

---

## ✅ কখন কোন টেকনিক ব্যবহার করা ভালো?

| Technique         | কবে ব্যবহার করবে                                                     |
| ----------------- | -------------------------------------------------------------------- |
| `linearSearch()`  | অ্যারে unsorted হলে, ছোট input হলে, সহজ পদ্ধতিতে presence check করতে |
| `binarySearch()`  | অ্যারে sorted হলে এবং index জানার দরকার হলে                          |
| `count()`         | অ্যারে unsorted হলেও চলবে, শুধু সংখ্যা কতবার এসেছে জানতে             |
| `std::find()`     | vector বা STL container-এ প্রথম match কোথায় তা জানার জন্য           |
| `binary_search()` | অ্যারে sorted হলে এবং শুধু আছে কি না জানতে (true/false)              |
| `lower_bound()`   | key-এর প্রথম অবস্থান পেতে (>= key), অথবা insert position পেতে        |
| `upper_bound()`   | key-এর পরে প্রথম বড় সংখ্যার অবস্থান পেতে                            |
| `equal_range()`   | শুরু ও শেষ একসাথে পেতে, এবং একসাথে count বের করতে                    |

---

## 🧮 Summary Table

| Technique         | Sorted Required | Returns                  | Time Complexity | Use Case          |
| ----------------- | --------------- | ------------------------ | --------------- | ----------------- |
| `count()`         | ❌ No            | Count of key             | O(n)            | কতবার আছে         |
| `binary_search()` | ✅ Yes           | true / false             | O(log n)        | আছে কি না         |
| `lower_bound()`   | ✅ Yes           | Iterator to first >= key | O(log n)        | প্রথম অবস্থান     |
| `upper_bound()`   | ✅ Yes           | Iterator to first > key  | O(log n)        | শেষের পরে         |
| `equal_range()`   | ✅ Yes           | pair\<lower, upper>      | O(log n)        | শুরু ও শেষ একসাথে |

---

## ✅ উপসংহার

* যদি অ্যারে **unsorted** হয় → `count()`, `find()` বা `linearSearch()` ব্যবহার করো
* যদি অ্যারে **sorted** হয় → `binary_search()`, `lower_bound()`, `equal_range()` এগুলো সবচেয়ে কার্যকর
* সময় এবং performance sensitive প্রোগ্রামে `O(log n)` ভিত্তিক টেকনিক প্রাধান্য দাও

---


---

## ✅ LeetCode Problems (Binary Search, Bounds)

| Problem                                                 | Link                                                                                                                                                                             |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Binary Search                                           | [https://leetcode.com/problems/binary-search/](https://leetcode.com/problems/binary-search/)                                                                                     |
| Search in Rotated Sorted Array                          | [https://leetcode.com/problems/search-in-rotated-sorted-array/](https://leetcode.com/problems/search-in-rotated-sorted-array/)                                                   |
| Find Minimum in Rotated Sorted Array                    | [https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)                                       |
| Search a 2D Matrix                                      | [https://leetcode.com/problems/search-a-2d-matrix/](https://leetcode.com/problems/search-a-2d-matrix/)                                                                           |
| Search Insert Position                                  | [https://leetcode.com/problems/search-insert-position/](https://leetcode.com/problems/search-insert-position/)                                                                   |
| Find First and Last Position of Element in Sorted Array | [https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |
| Median of Two Sorted Arrays                             | [https://leetcode.com/problems/median-of-two-sorted-arrays/](https://leetcode.com/problems/median-of-two-sorted-arrays/)                                                         |
| Peak Index in a Mountain Array                          | [https://leetcode.com/problems/peak-index-in-a-mountain-array/](https://leetcode.com/problems/peak-index-in-a-mountain-array/)                                                   |
| Guess Number Higher or Lower                            | [https://leetcode.com/problems/guess-number-higher-or-lower/](https://leetcode.com/problems/guess-number-higher-or-lower/)                                                       |
| Find Peak Element                                       | [https://leetcode.com/problems/find-peak-element/](https://leetcode.com/problems/find-peak-element/)                                                                             |

---

## ✅ CodeChef Problems

| Problem                 | Link                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| The Wave                | [https://www.codechef.com/problems/WAV2](https://www.codechef.com/problems/WAV2)           |
| Coins and Triangle      | [https://www.codechef.com/problems/TRICOIN](https://www.codechef.com/problems/TRICOIN)     |
| Minion Chef and Bananas | [https://www.codechef.com/problems/MINPERM](https://www.codechef.com/problems/MINPERM)     |
| Wildfire                | [https://www.codechef.com/problems/WILDFIRE](https://www.codechef.com/problems/WILDFIRE)   |
| Cutting Recipes         | [https://www.codechef.com/problems/RECIPE](https://www.codechef.com/problems/RECIPE)       |
| Chef and Horses         | [https://www.codechef.com/problems/HORSES](https://www.codechef.com/problems/HORSES)       |
| Binary Search Trees     | [https://www.codechef.com/problems/BSTOPS](https://www.codechef.com/problems/BSTOPS)       |
| Finding Shoes           | [https://www.codechef.com/problems/FINDSHOES](https://www.codechef.com/problems/FINDSHOES) |
| Saving the City         | [https://www.codechef.com/problems/SAVINGIT](https://www.codechef.com/problems/SAVINGIT)   |
| Binary String MEX       | [https://www.codechef.com/problems/MEXSTRING](https://www.codechef.com/problems/MEXSTRING) |

---

## ✅ Codeforces Problems

| Problem                          | Link                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 230B. T-primes                   | [https://codeforces.com/problemset/problem/230/B](https://codeforces.com/problemset/problem/230/B)     |
| 287B. Pipeline                   | [https://codeforces.com/problemset/problem/287/B](https://codeforces.com/problemset/problem/287/B)     |
| 1237C2. Balanced Removals (hard) | [https://codeforces.com/problemset/problem/1237/C2](https://codeforces.com/problemset/problem/1237/C2) |
| 1201B. Zero Array                | [https://codeforces.com/problemset/problem/1201/B](https://codeforces.com/problemset/problem/1201/B)   |
| 987C. Three displays             | [https://codeforces.com/problemset/problem/987/C](https://codeforces.com/problemset/problem/987/C)     |
| 115A. Party                      | [https://codeforces.com/problemset/problem/115/A](https://codeforces.com/problemset/problem/115/A)     |
| 160D. Edges in MST               | [https://codeforces.com/problemset/problem/160/D](https://codeforces.com/problemset/problem/160/D)     |
| 1374C. Move Brackets             | [https://codeforces.com/problemset/problem/1374/C](https://codeforces.com/problemset/problem/1374/C)   |
| 1312C. Adding Powers             | [https://codeforces.com/problemset/problem/1312/C](https://codeforces.com/problemset/problem/1312/C)   |
| 371C. Hamburgers                 | [https://codeforces.com/problemset/problem/371/C](https://codeforces.com/problemset/problem/371/C)     |

---

## ✅ AtCoder Problems

| Problem                            | Link                                                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------- |
| ABC118 B – Foods Loved by Everyone | [https://atcoder.jp/contests/abc118/tasks/abc118\_b](https://atcoder.jp/contests/abc118/tasks/abc118_b) |
| ABC203 D – Pond                    | [https://atcoder.jp/contests/abc203/tasks/abc203\_d](https://atcoder.jp/contests/abc203/tasks/abc203_d) |
| ABC223 D – Restricted Permutation  | [https://atcoder.jp/contests/abc223/tasks/abc223\_d](https://atcoder.jp/contests/abc223/tasks/abc223_d) |
| ABC143 C – Slimes                  | [https://atcoder.jp/contests/abc143/tasks/abc143\_c](https://atcoder.jp/contests/abc143/tasks/abc143_c) |
| ABC115 C – Christmas Eve           | [https://atcoder.jp/contests/abc115/tasks/abc115\_c](https://atcoder.jp/contests/abc115/tasks/abc115_c) |
| ARC104 B – DNA Sequence            | [https://atcoder.jp/contests/arc104/tasks/arc104\_b](https://atcoder.jp/contests/arc104/tasks/arc104_b) |
| ARC118 B – Digital Graffiti        | [https://atcoder.jp/contests/arc118/tasks/arc118\_b](https://atcoder.jp/contests/arc118/tasks/arc118_b) |
| ARC065 C – bugs                    | [https://atcoder.jp/contests/arc065/tasks/arc065\_c](https://atcoder.jp/contests/arc065/tasks/arc065_c) |
| ABC067 C – Splitting Piles         | [https://atcoder.jp/contests/abc067/tasks/arc078\_b](https://atcoder.jp/contests/abc067/tasks/arc078_b) |
| ABC217 D – Cutting Woods           | [https://atcoder.jp/contests/abc217/tasks/abc217\_d](https://atcoder.jp/contests/abc217/tasks/abc217_d) |

---



এই ডকুমেন্টটি এখন একটি পূর্ণাঙ্গ রেফারেন্স — C++-এ সংখ্যার presence, frequency এবং অবস্থান বের করার জন্য।
