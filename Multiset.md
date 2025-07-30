
---

# 🧠 C++ `std::multiset` — একদম পরিষ্কার ধারণা

---

## 🔷 `multiset` কী?

`std::multiset` হল C++ STL-এর একটি **associative container** যা:

* উপাদানগুলো **sorted রাখে** (default: ascending)
* একই উপাদান **multiple বার রাখতে পারে**
* ভিতরে **Red-Black Tree (Self-Balancing BST)** ব্যবহার করে
* Operations: `O(log n)` টাইমে insert, delete, search ইত্যাদি করে

---

## ✅ মূল কাজ ও ব্যবহার

| কাজ / ব্যবহার                        | উদাহরণ / ব্যাখ্যা                             |
| ------------------------------------ | --------------------------------------------- |
| 🔁 Sorted data রাখা                  | `{3,1,2,1}` → `1 1 2 3`                       |
| 🔂 একই উপাদান বারবার রাখা            | `{"Ali", "Bob", "Ali"}` → `Ali Ali Bob`       |
| 🔍 Value-based search, count         | `s.count(10)` → 10 এর কয়টা instance           |
| 📊 Frequency tracking in sorted way  | মার্কেটে দাম tracking, ফলাফল হিসাব            |
| 🏆 Leaderboard / Bidding system      | একই score সহ অনেক entry, অথচ sorted রাখতে হবে |
| 🎯 Efficient sliding window problems | Competitive programming-এর টিপিক্যাল use-case |

---

## 🛠️ গুরুত্বপূর্ণ Operations ও Time Complexity

| Operation          | Time Complexity | ব্যাখ্যা                          |
| ------------------ | --------------- | --------------------------------- |
| `insert(val)`      | `O(log n)`      | Tree-তে ডেটা ঢোকায়                |
| `erase(val)`       | `O(log n)`      | ডুপ্লিকেটসহ সব instance মুছে ফেলে |
| `find(val)`        | `O(log n)`      | উপাদান খুঁজে iterator দেয়         |
| `count(val)`       | `O(log n)`      | কয়বার আছে তা গুনে দেয়             |
| `lower_bound(val)` | `O(log n)`      | প্রথম `>= val` element            |
| `upper_bound(val)` | `O(log n)`      | প্রথম `> val` element             |
| `equal_range(val)` | `O(log n)`      | lower এবং upper bound এর pair     |
| `begin()/end()`    | `O(1)`          | প্রথম ও শেষ iterator              |
| `size()/empty()`   | `O(1)`          | মোট উপাদান সংখ্যা / খালি কিনা     |

---

## 🔀 কখন `multiset` Efficient?

| Use-case                        | কেন `multiset` উপযুক্ত               |
| ------------------------------- | ------------------------------------ |
| Sorted duplicate tracking       | Automatically sorted with duplicates |
| Fast insertion + search + erase | সব `O(log n)` টাইমে হয়               |
| Frequency query with order      | `count(val)` & sorted access         |
| Range queries                   | `lower_bound`, `upper_bound`         |
| Competitive programming         | Sliding window, Top K elements etc.  |

---

## 🚫 কখন `multiset` Use করা উচিত নয়?

| প্রয়োজন / সমস্যা                        | ভালো বিকল্প             | কারণ                          |
| ---------------------------------------- | ----------------------- | ----------------------------- |
| Unique element দরকার                     | `std::set`              | ডুপ্লিকেট support করে না      |
| Fast hash-based access দরকার             | `unordered_multiset`    | average O(1), কিন্তু unsorted |
| Indexed access দরকার                     | `vector` / `deque`      | Random access `O(1)`          |
| Key-value frequency tracking (unordered) | `unordered_map<T, int>` | More explicit frequency store |

---

## 📦 বাস্তব উদাহরণ

### 🧾 উদাহরণ ১: মার্কেটের দাম tracking

```cpp
std::multiset<int> prices = {100, 150, 100, 200};

prices.insert(100);
prices.erase(150);
```

➡ Output: `100 100 100 200`

---

### 🧾 উদাহরণ ২: ফলাফলের গ্রেডিং

```cpp
std::multiset<int> scores = {85, 90, 90, 78};

for (auto it = scores.rbegin(); it != scores.rend(); ++it)
    std::cout << *it << " ";
```

➡ Output: `90 90 85 78` (Descending Order)

---

## 🧠 সংক্ষেপে মনে রাখার ফর্মুলা

| Container            | ডুপ্লিকেট | Sorted | টাইম কমপ্লেক্সিটি | ব্যবহার                        |
| -------------------- | --------- | ------ | ----------------- | ------------------------------ |
| `set`                | ❌         | ✅      | `O(log n)`        | Unique, ordered data           |
| `multiset`           | ✅         | ✅      | `O(log n)`        | Duplicate + ordered            |
| `unordered_set`      | ❌         | ❌      | `avg O(1)`        | Unique, fast access, unordered |
| `unordered_multiset` | ✅         | ❌      | `avg O(1)`        | Duplicate + fast, unordered    |
| `map`, `multimap`    | Key-value | ✅      | `O(log n)`        | Key-value store with ordering  |
| `unordered_map`      | Key-value | ❌      | `avg O(1)`        | Key-value, fast, unordered     |

---

## ✅ উপসংহার

🔹 যদি **sorted** এবং **duplicate-friendly** container দরকার হয় — তাহলে `multiset` সেরা সমাধান।

🔹 যেখানে `insert`, `search`, `delete` — সব efficiently করতে হবে এবং ডেটা অর্ডার মেইনটেইন করতে হবে, সেখানেই `multiset` shine করে।

🔹 Competitive programming, frequency tracking, logics with sorted duplicates — এসব ক্ষেত্রে highly efficient।

---




---

### 📚 `std::multiset` এর সকল গুরুত্বপূর্ণ ফাংশনের লিস্ট

`std::multiset` হল একটি STL container যেটি **sorted** order এ এলিমেন্ট রাখে এবং **duplicate** এলিমেন্ট রাখতে পারে।

#### ✅ Constructor Functions

* `multiset<T> s;` — খালি multiset তৈরি।
* `multiset<T> s(begin, end);` — কোনো রেঞ্জ থেকে ডেটা দিয়ে তৈরি।
* `multiset<T> s(const multiset<T>&);` — কপি কনস্ট্রাক্টর।
* `multiset<T> s(std::initializer_list<T>);` — `{1,2,3}` এর মতো ইন্সার্ট।

---

#### ✅ Insertion

* `s.insert(value);` — এক বা একাধিক কপি ইনসার্ট।
* `s.insert(hint, value);` — iterator hint সহ ইনসার্ট।
* `s.emplace(value);` — ইন-প্লেস কনস্ট্রাকশন করে ইনসার্ট।

---

#### ✅ Deletion

* `s.erase(value);` — নির্দিষ্ট value এর সব instance মুছে ফেলে।
* `s.erase(pos);` — নির্দিষ্ট iterator position থেকে মুছে ফেলে।
* `s.erase(start, end);` — iterator রেঞ্জ থেকে মুছে ফেলে।
* `s.clear();` — সব মুছে ফেলে।

---

#### ✅ Search & Count

* `s.find(value);` — iterator রিটার্ন করে value পেলে, না পেলে `s.end()`।
* `s.count(value);` — কয়টা instance আছে সেটা রিটার্ন করে।
* `s.equal_range(value);` — pair\<iterator, iterator> দেয়, যেখানে value শুরু এবং শেষ হয়।
* `s.lower_bound(value);` — প্রথম iterator যা `>= value`।
* `s.upper_bound(value);` — প্রথম iterator যা `> value`।

---

#### ✅ Capacity

* `s.empty();` — খালি কিনা দেখে।
* `s.size();` — মোট কতটি এলিমেন্ট আছে।
* `s.max_size();` — সর্বোচ্চ কয়টি রাখতে পারে।

---

#### ✅ Iterator Functions

* `s.begin(), s.end()` — ফ্রন্ট থেকে ইটারেশন।
* `s.rbegin(), s.rend()` — রিভার্স ইটারেশন।
* `cbegin(), cend(), crbegin(), crend()` — const ইটারেশন।

---

#### ✅ Others

* `s.swap(other);` — দুইটা multiset এর মধ্যে data অদলবদল করে।
* `s.get_allocator();` — মেমোরি allocator রিটার্ন করে।

---



---

## ✅ Constructor Functions

---

### 1️⃣ `multiset<T> s;` — খালি multiset তৈরি

### 🧩 Problem:

একটি খালি multiset তৈরি করো এবং তাতে কিছু সংখ্যা insert করে প্রিন্ট করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s; // empty multiset

    s.insert(3);
    s.insert(1);
    s.insert(2);

    for (int x : s)
        std::cout << x << " ";
}
```

📤 **Output:**

```
1 2 3
```

---

### 2️⃣ `multiset<T> s(begin, end);` — রেঞ্জ থেকে তৈরি

### 🧩 Problem:

একটি অ্যারে থেকে multiset তৈরি করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    int arr[] = {5, 2, 3, 2, 5};

    std::multiset<int> s(arr, arr + 5); // range constructor

    for (int x : s)
        std::cout << x << " ";
}
```

📤 **Output:**

```
2 2 3 5 5
```

---

### 3️⃣ `multiset<T> s(const multiset<T>&);` — কপি কনস্ট্রাক্টর

### 🧩 Problem:

একটি multiset কপি করে আরেকটি তৈরি করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> original = {1, 2, 2, 3};

    std::multiset<int> copy(original); // copy constructor

    for (int x : copy)
        std::cout << x << " ";
}
```

📤 **Output:**

```
1 2 2 3
```

---

### 4️⃣ `multiset<T> s(std::initializer_list<T>);`

### 🧩 Problem:

একটি initializer list দিয়ে multiset তৈরি করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s{4, 1, 4, 3};

    for (int x : s)
        std::cout << x << " ";
}
```

📤 **Output:**

```
1 3 4 4
```

---

## ✅ Insertion Functions

---

### 5️⃣ `s.insert(value);` — সাধারণ ইনসার্ট

(ইতিমধ্যেই উপরের উদাহরণে দেওয়া আছে, চলছি পরেরটায়)

---

### 6️⃣ `s.insert(hint, value);` — hint সহ ইনসার্ট

### 🧩 Problem:

একটি multiset-এ insert করার সময় হিন্ট (iterator) ব্যবহার করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s = {10, 20, 30};

    auto it = s.begin(); // hint: beginning
    s.insert(it, 5);     // insert with hint (faster if correct)

    for (int x : s)
        std::cout << x << " ";
}
```

📤 **Output:**

```
5 10 20 30
```

---

### 7️⃣ `s.emplace(value);` — ইন-প্লেস ইনসার্ট

### 🧩 Problem:

multiset-এ `emplace` দিয়ে ইন-প্লেস ইনসার্ট করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s;

    s.emplace(8);
    s.emplace(3);
    s.emplace(8);

    for (int x : s)
        std::cout << x << " ";
}
```

📤 **Output:**

```
3 8 8
```

---



---

## ✅ Deletion Functions

---

### 1️⃣ `s.erase(value);` — নির্দিষ্ট value এর সব instance মুছে ফেলে

### 🧩 Problem:

একটি multiset থেকে একটি নির্দিষ্ট সংখ্যা সম্পূর্ণভাবে মুছে ফেলো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s = {1, 2, 2, 3, 4, 2};

    s.erase(2);  // remove all instances of 2

    for (int x : s)
        std::cout << x << " ";
}
```

📤 **Output:**

```
1 3 4
```

---

### 2️⃣ `s.erase(pos);` — নির্দিষ্ট iterator থেকে মুছে ফেলে

### 🧩 Problem:

multiset থেকে প্রথম উপাদানটি মুছে ফেলো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s = {10, 20, 30};

    auto it = s.begin(); // iterator to first element
    s.erase(it);         // remove first element

    for (int x : s)
        std::cout << x << " ";
}
```

📤 **Output:**

```
20 30
```

---

### 3️⃣ `s.erase(start, end);` — একটি রেঞ্জ মুছে ফেলো

### 🧩 Problem:

multiset থেকে প্রথম দুইটি উপাদান মুছে ফেলো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s = {5, 10, 15, 20};

    auto start = s.begin();
    auto end = std::next(start, 2); // second position

    s.erase(start, end); // remove first two elements

    for (int x : s)
        std::cout << x << " ";
}
```

📤 **Output:**

```
15 20
```

---

### 4️⃣ `s.clear();` — সব উপাদান মুছে ফেলো

### 🧩 Problem:

multiset পুরোপুরি খালি করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s = {1, 2, 3};

    s.clear();  // remove everything

    std::cout << "Size: " << s.size(); // should be 0
}
```

📤 **Output:**

```
Size: 0
```

---

## ✅ Search & Count Functions

---

### 5️⃣ `s.find(value);` — উপাদান খুঁজে বের করো

### 🧩 Problem:

multiset-এ 30 আছে কিনা খুঁজে বের করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s = {10, 20, 30, 40};

    auto it = s.find(30);
    if (it != s.end())
        std::cout << "Found: " << *it;
    else
        std::cout << "Not found";
}
```

📤 **Output:**

```
Found: 30
```

---

### 6️⃣ `s.count(value);` — কয়বার আছে সেটা বের করো

### 🧩 Problem:

multiset-এ 10 কয়বার আছে সেটা দেখাও।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s = {10, 10, 20, 10};

    std::cout << "10 occurs " << s.count(10) << " times.";
}
```

📤 **Output:**

```
10 occurs 3 times.
```

---

### 7️⃣ `s.equal_range(value);` — একটা value-এর শুরু ও শেষ iterator pair

### 🧩 Problem:

multiset-এ `10` এর range iterator বের করে, ঐ range প্রিন্ট করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s = {5, 10, 10, 10, 20};

    auto range = s.equal_range(10); // pair of iterators

    std::cout << "10s are: ";
    for (auto it = range.first; it != range.second; ++it)
        std::cout << *it << " ";
}
```

📤 **Output:**

```
10s are: 10 10 10
```

---

### 8️⃣ `s.lower_bound(value);` — প্রথম `>= value` এর position

### 🧩 Problem:

multiset-এ 15 বা তার চেয়ে বড় প্রথম সংখ্যা দেখাও।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s = {5, 10, 15, 20};

    auto it = s.lower_bound(15);
    if (it != s.end())
        std::cout << "Lower bound: " << *it;
}
```

📤 **Output:**

```
Lower bound: 15
```

---

### 9️⃣ `s.upper_bound(value);` — প্রথম `> value` এর position

### 🧩 Problem:

multiset-এ 15 এর চেয়ে বড় প্রথম সংখ্যা দেখাও।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s = {5, 10, 15, 20};

    auto it = s.upper_bound(15);
    if (it != s.end())
        std::cout << "Upper bound: " << *it;
}
```

📤 **Output:**

```
Upper bound: 20
```

---
চল এবার `std::multiset`-এর ✅ **Capacity**, ✅ **Iterator Functions**, এবং ✅ **Others** সেকশনের প্রতিটি ফাংশনের জন্য ছোট ছোট সমস্যা ও তার সমাধান দেখি।

---

## ✅ Capacity Functions

---

### 1️⃣ `s.empty();` — খালি কিনা যাচাই করা

### 🧩 Problem:

multiset খালি কিনা তা যাচাই করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s;

    if (s.empty())
        std::cout << "Set is empty\n";
    else
        std::cout << "Set has elements\n";

    s.insert(1);

    if (!s.empty())
        std::cout << "Now set has elements\n";
}
```

📤 **Output:**

```
Set is empty  
Now set has elements
```

---

### 2️⃣ `s.size();` — মোট কয়টি উপাদান আছে

### 🧩 Problem:

multiset-এ মোট কতটি এলিমেন্ট আছে তা দেখাও।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s = {1, 2, 2, 3};

    std::cout << "Size: " << s.size();
}
```

📤 **Output:**

```
Size: 4
```

---

### 3️⃣ `s.max_size();` — সর্বোচ্চ কতটি রাখতে পারবে (সিস্টেম নির্ভর)

### 🧩 Problem:

multiset ক'ভাবে সর্বোচ্চ কতটি উপাদান রাখতে পারবে, তা বের করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s;

    std::cout << "Max size: " << s.max_size();
}
```

📤 **Sample Output (ভিন্ন সিস্টেমে ভিন্ন):**

```
Max size: 461168601842738790
```

---

## ✅ Iterator Functions

---

### 4️⃣ `s.begin(), s.end()` — সামনের দিক থেকে ইটারেট করো

### 🧩 Problem:

multiset এর সব উপাদান সামনে থেকে প্রিন্ট করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s = {3, 1, 4};

    for (auto it = s.begin(); it != s.end(); ++it)
        std::cout << *it << " ";
}
```

📤 **Output:**

```
1 3 4
```

---

### 5️⃣ `s.rbegin(), s.rend()` — পেছন থেকে ইটারেট করো

### 🧩 Problem:

multiset এর উপাদান রিভার্স অর্ডারে প্রিন্ট করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s = {3, 1, 4};

    for (auto it = s.rbegin(); it != s.rend(); ++it)
        std::cout << *it << " ";
}
```

📤 **Output:**

```
4 3 1
```

---

### 6️⃣ `cbegin(), cend(), crbegin(), crend()` — const ইটারেটর ব্যবহার করে প্রিন্ট করো

### 🧩 Problem:

multiset এর উপাদান const\_iterator দিয়ে প্রিন্ট করো (modification allowed নয়)।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    const std::multiset<int> s = {2, 5, 1};

    for (auto it = s.cbegin(); it != s.cend(); ++it)
        std::cout << *it << " ";

    std::cout << "\nReverse:\n";
    for (auto it = s.crbegin(); it != s.crend(); ++it)
        std::cout << *it << " ";
}
```

📤 **Output:**

```
1 2 5  
Reverse:  
5 2 1
```

---

## ✅ Others

---

### 7️⃣ `s.swap(other);` — দুই multiset এর মধ্যে data অদলবদল করো

### 🧩 Problem:

দুই multiset এর মধ্যে মান অদলবদল করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> a = {1, 2};
    std::multiset<int> b = {10, 20, 30};

    a.swap(b);

    std::cout << "a: ";
    for (int x : a) std::cout << x << " ";

    std::cout << "\nb: ";
    for (int x : b) std::cout << x << " ";
}
```

📤 **Output:**

```
a: 10 20 30  
b: 1 2
```

---

### 8️⃣ `s.get_allocator();` — allocator object রিটার্ন করে

### 🧩 Problem:

একটি multiset এর allocator ব্যবহার করে ডায়নামিক মেমোরি allocate করো।

### 🧪 Solution:

```cpp
#include <iostream>
#include <set>

int main() {
    std::multiset<int> s;

    auto alloc = s.get_allocator();

    int* p = alloc.allocate(3); // allocate space for 3 integers

    p[0] = 100;
    p[1] = 200;
    p[2] = 300;

    std::cout << p[0] << " " << p[1] << " " << p[2] << "\n";

    alloc.deallocate(p, 3); // free the memory
}
```

📤 **Output:**

```
100 200 300
```

---



## 🌟 `std::multiset` Full Reference Sheet — C++ STL


# 🌟 C++ STL - std::multiset Reference Sheet

## ✅ Constructor Functions

| Function                                 | Description                                | Example                                    |
|------------------------------------------|--------------------------------------------|--------------------------------------------|
| `std::multiset<int> s;`                  | Create empty multiset                      | `std::multiset<int> s;`                    |
| `std::multiset<int> s(arr, arr+n);`      | Create from range                          | `std::multiset<int> s(arr, arr+5);`        |
| `std::multiset<int> s(other);`           | Copy constructor                           | `std::multiset<int> copy(s);`              |
| `std::multiset<int> s{1, 2, 3};`         | Initializer list                           | `std::multiset<int> s{1, 2, 3};`           |

---

## ✅ Insertion Functions

| Function                                  | Description                                  | Example                              |
|-------------------------------------------|----------------------------------------------|--------------------------------------|
| `insert(value)`                           | Insert an element                            | `s.insert(10);`                      |
| `insert(hint, value)`                     | Insert with iterator hint                    | `s.insert(s.begin(), 10);`           |
| `emplace(value)`                          | In-place insert                              | `s.emplace(10);`                     |

---

## ✅ Deletion Functions

| Function                                  | Description                                  | Example                              |
|-------------------------------------------|----------------------------------------------|--------------------------------------|
| `erase(value)`                            | Erase all instances of a value               | `s.erase(2);`                        |
| `erase(pos)`                              | Erase by iterator                            | `s.erase(s.begin());`               |
| `erase(start, end)`                       | Erase range                                  | `s.erase(s.begin(), s.end());`      |
| `clear()`                                 | Erase all elements                           | `s.clear();`                         |

---

## ✅ Search & Count

| Function                                  | Description                                  | Example                              |
|-------------------------------------------|----------------------------------------------|--------------------------------------|
| `find(value)`                             | Find first occurrence                        | `auto it = s.find(3);`               |
| `count(value)`                            | Count occurrences of value                   | `s.count(3);`                        |
| `equal_range(value)`                      | Returns pair of iterators                    | `auto p = s.equal_range(3);`         |
| `lower_bound(value)`                      | First element >= value                       | `s.lower_bound(3);`                  |
| `upper_bound(value)`                      | First element > value                        | `s.upper_bound(3);`                  |

---

## ✅ Capacity Functions

| Function                                  | Description                                  | Example                              |
|-------------------------------------------|----------------------------------------------|--------------------------------------|
| `empty()`                                 | Check if multiset is empty                   | `s.empty();`                         |
| `size()`                                  | Number of elements                           | `s.size();`                          |
| `max_size()`                              | Maximum number of elements storable          | `s.max_size();`                      |

---

## ✅ Iterator Functions

| Function                                  | Description                                  | Example                              |
|-------------------------------------------|----------------------------------------------|--------------------------------------|
| `begin(), end()`                          | Forward iteration                            | `for (auto it = s.begin(); ...)`     |
| `rbegin(), rend()`                        | Reverse iteration                            | `for (auto it = s.rbegin(); ...)`    |
| `cbegin(), cend()`                        | Constant forward iteration                   | `for (auto it = s.cbegin(); ...)`    |
| `crbegin(), crend()`                      | Constant reverse iteration                   | `for (auto it = s.crbegin(); ...)`   |

---

## ✅ Other Utilities

| Function                                  | Description                                  | Example                              |
|-------------------------------------------|----------------------------------------------|--------------------------------------|
| `swap(other)`                             | Swap two multisets                           | `a.swap(b);`                         |
| `get_allocator()`                         | Get memory allocator                         | `auto alloc = s.get_allocator();`    |
```

---


