
---

# 🟡 Topic 2: Control Flow in C++

---

## 🔸 ২.১ `if`, `else`, `else if`

### 📌 ব্যাখ্যা:

`if`-`else` স্টেটমেন্টের মাধ্যমে নির্দিষ্ট শর্ত অনুযায়ী ভিন্ন ভিন্ন কোড চালানো যায়।

### ✅ সিনট্যাক্স:

```cpp
if (condition) {
    // Executes if condition is true
} else if (another_condition) {
    // Executes if second condition is true
} else {
    // Executes if no condition is true
}
```

### 🧪 কোড উদাহরণ:

```cpp
int number = 10;
if (number > 0)
    cout << "Positive";
else if (number < 0)
    cout << "Negative";
else
    cout << "Zero";
```

### ⚠️ লক্ষ্য:

* `=` আর `==` গুলিয়ে ফেললে বড় সমস্যা হয়! `==` হল তুলনা, আর `=` হল মান দেওয়া।

---

## 🔸 ২.২ `switch` Statement

### 📌 ব্যাখ্যা:

`switch` একটি variable-এর মানের ভিত্তিতে অনেকগুলো case চালাতে পারে। এটি `if-else` এর cleaner version যখন multiple constant value match করতে হয়।

### ✅ সিনট্যাক্স:

```cpp
switch (variable) {
    case value1:
        // code
        break;
    case value2:
        // code
        break;
    default:
        // code
}
```

### 🧪 কোড উদাহরণ:

```cpp
int day = 3;
switch (day) {
    case 1: cout << "Monday"; break;
    case 2: cout << "Tuesday"; break;
    case 3: cout << "Wednesday"; break;
    default: cout << "Invalid Day";
}
```

### ⚠️ লক্ষ্য:

* `break` না দিলে fall-through হয়ে পরবর্তী case গুলোও চলবে।

---

## 🔸 ২.৩ Loops in C++

Loops বারবার কোনো কাজ করতে ব্যবহৃত হয় যতক্ষণ না নির্দিষ্ট শর্ত মিথ্যা হয়।

---

### 🔹 `for` Loop

👉 **যখন iteration সংখ্যা জানা থাকে।**

```cpp
for (int i = 1; i <= 5; i++) {
    cout << i << " ";
}
```

⏱️ Output: `1 2 3 4 5`

---

### 🔹 `while` Loop

👉 **যখন কতবার চলবে আগে জানা নেই।**

```cpp
int i = 1;
while (i <= 5) {
    cout << i << " ";
    i++;
}
```

---

### 🔹 `do-while` Loop

👉 **কমপক্ষে একবার চলবেই।**

```cpp
int i = 1;
do {
    cout << i << " ";
    i++;
} while (i <= 5);
```

---

## 🔸 ২.৪ `break` ও `continue`

### ✅ `break`: লুপ থামিয়ে বাইরে চলে যায়

```cpp
for (int i = 1; i <= 10; i++) {
    if (i == 5)
        break;
    cout << i << " ";
}
// Output: 1 2 3 4
```

---

### ✅ `continue`: current iteration skip করে

```cpp
for (int i = 1; i <= 5; i++) {
    if (i == 3)
        continue;
    cout << i << " ";
}
// Output: 1 2 4 5
```

---

## 🔸 ২.৫ Nested Loops

👉 **লুপের ভিতরে আরেকটি লুপ**

### 🧪 কোড উদাহরণ:

```cpp
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 2; j++) {
        cout << "i=" << i << ", j=" << j << endl;
    }
}
```

⏱️ Output:

```
i=1, j=1
i=1, j=2
i=2, j=1
i=2, j=2
i=3, j=1
i=3, j=2
```

---

## 🧠 Critical Thinking প্রশ্ন ও উত্তর:

| প্রশ্ন                                | উত্তর                                                                               |
| ------------------------------------- | ----------------------------------------------------------------------------------- |
| `if(x=5)` কি কাজ করবে?                | হ্যাঁ, এটি `x` কে ৫ সেট করবে। কিন্তু এটি `comparison (==)` নয়, বরং `assignment (=)` |
| `do-while` vs `while` পার্থক্য?       | `do-while` অন্তত একবার চলবেই; `while` শুরুতেই চেক করে                               |
| `switch` কি `string` টাইপ নেয়?        | C++ standard switch `int`-based বা enum-based; `string` নেয় না                      |
| `break` আর `return` পার্থক্য?         | `break` লুপ থামায়, `return` পুরো ফাংশন থেকে বের করে দেয়                             |
| Nested loop-এ সময় জটিলতা বেশি হয় কেন? | কারণ প্রতিটি লুপ আরেকটিকে নির্ভর করে চালায় → Time Complexity বৃদ্ধি পায়             |

---

## 🔚 উপসংহার:

| টপিক                       | কী শিখলে                            |
| -------------------------- | ----------------------------------- |
| `if`, `else`, `else if`    | শর্ত অনুযায়ী একাধিক সিদ্ধান্ত নেওয়া |
| `switch`                   | ভ্যালু ভিত্তিক condition প্রয়োগ     |
| `for`, `while`, `do-while` | বিভিন্ন ধরণের iteration             |
| `break`, `continue`        | লুপ নিয়ন্ত্রণ                       |
| Nested loops               | দুই বা ততোধিক স্তরে লুপ চালানো      |

---


---

# 📘 C++ Control Flow – ২৫টি বাস্তব অনুশীলন সমস্যা (Practice Problem Documentation)

---

## 🎯 টপিক কাঠামো:

এই সমস্যাগুলো নিম্নোক্ত C++ কনসেপ্টের উপর ভিত্তি করে সাজানো হয়েছে:

* `if`, `else`, `else if`
* `switch-case`
* `for`, `while`, `do-while` loops
* `break`, `continue`
* Nested loops and menu-driven structures

---

## 📝 প্র্যাকটিস সমস্যার তালিকা:

| 🔢 No. | Problem Title                                    | Hint/Technique                            |
| ------ | ------------------------------------------------ | ----------------------------------------- |
| 1️⃣    | Check if a number is even or odd                 | Use `if-else` with `%` operator           |
| 2️⃣    | Check if a number is positive, negative, or zero | Use `if-else-if`                          |
| 3️⃣    | Find the maximum of three numbers                | Use nested `if` or `logical operators`    |
| 4️⃣    | Check if a year is a leap year                   | Check divisibility by 4, 100, 400         |
| 5️⃣    | Create a simple calculator (add, subtract, etc.) | Use `switch-case`                         |
| 6️⃣    | Print numbers from 1 to N                        | Use `for` loop                            |
| 7️⃣    | Print the sum of first N natural numbers         | Use `for` loop with accumulator           |
| 8️⃣    | Print multiplication table of a number           | Use `for` loop                            |
| 9️⃣    | Find factorial of a number                       | Use `loop` and multiplication             |
| 🔟     | Reverse a number                                 | Use `while` loop, `%` and `/`             |
| 1️⃣1️⃣ | Count digits in a number                         | Use `while` loop and counter              |
| 1️⃣2️⃣ | Check if a number is palindrome                  | Compare reversed number                   |
| 1️⃣3️⃣ | Print all even numbers up to N                   | Use `for` + condition (`% 2 == 0`)        |
| 1️⃣4️⃣ | Print Fibonacci series up to N terms             | Use loop and variable update logic        |
| 1️⃣5️⃣ | Check if a number is prime                       | Use loop and divisibility check           |
| 1️⃣6️⃣ | Find the sum of digits of a number               | Use `while` loop and `%`                  |
| 1️⃣7️⃣ | Display menu to user and perform action          | Use `switch` inside a loop                |
| 1️⃣8️⃣ | Print pattern of stars (triangle)                | Use nested `for` loops                    |
| 1️⃣9️⃣ | Check whether a character is vowel or consonant  | Use `if` or `switch`                      |
| 2️⃣0️⃣ | Convert lowercase to uppercase                   | Use ASCII difference or built-in function |
| 2️⃣1️⃣ | Find GCD of two numbers                          | Use Euclidean Algorithm via loop          |
| 2️⃣2️⃣ | Print reverse of a string                        | Use loop and indexing                     |
| 2️⃣3️⃣ | Implement a number guessing game                 | Use `while` loop and `break`              |
| 2️⃣4️⃣ | Check if a number is Armstrong number            | Use digit power sum logic                 |
| 2️⃣5️⃣ | Simulate login attempts with limited tries       | Use `do-while` and counter                |

---

## 🧠 Learning Outcome:

এই সমস্যা সমাধানের মাধ্যমে তোমার নিচের দক্ষতা তৈরি হবে:

| Skill Area              | অর্জিত দক্ষতা                                |
| ----------------------- | -------------------------------------------- |
| Decision Making         | Multiple `if-else` শর্ত ব্যবস্থাপনা          |
| Condition Checking      | Arithmetic এবং Boolean condition skill       |
| Looping Structure       | Entry & Exit Control, Infinite loop handling |
| Logical Thinking        | Palindrome, Armstrong, Prime Logic           |
| Input/Output Management | ইউজার ইন্টারঅ্যাকশন                          |
| Nested Logic            | Pattern printing, multi-layer execution      |




---

### ✅ 1️⃣ Problem: **Check if a number is even or odd**

**🔎 সমস্যা ব্যাখ্যা:**
ইউজার একটি সংখ্যা ইনপুট দিবে। আপনাকে বলতে হবে সংখ্যাটি **even** (জোড়) নাকি **odd** (বিজোড়)।

**💡 কৌশল:**
একটি সংখ্যা ২ দিয়ে ভাগ করে যদি ভাগশেষ (`%`) ০ হয়, তাহলে তা even।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;

    if (n % 2 == 0)
        cout << "Even" << endl;
    else
        cout << "Odd" << endl;

    return 0;
}
```

---

### ✅ 2️⃣ Problem: **Check if a number is positive, negative, or zero**

**🔎 সমস্যা ব্যাখ্যা:**
ইউজার একটি সংখ্যা ইনপুট দিবে। আপনাকে বলতে হবে সংখ্যাটি **positive**, **negative**, নাকি **zero**।

**💡 কৌশল:**

* `n > 0` হলে Positive
* `n < 0` হলে Negative
* `n == 0` হলে Zero

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;

    if (n > 0)
        cout << "Positive" << endl;
    else if (n < 0)
        cout << "Negative" << endl;
    else
        cout << "Zero" << endl;

    return 0;
}
```

---

### ✅ 3️⃣ Problem: **Find the maximum of three numbers**

**🔎 সমস্যা ব্যাখ্যা:**
তিনটি সংখ্যা ইনপুট নিয়ে, এর মধ্যে সবচেয়ে বড় সংখ্যাটি নির্ণয় করুন।

**💡 কৌশল:**
তুলনা করে `if-else` বা `nested if` দিয়ে বড় সংখ্যা বের করা।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cout << "Enter three numbers: ";
    cin >> a >> b >> c;

    if (a >= b && a >= c)
        cout << "Maximum is: " << a << endl;
    else if (b >= a && b >= c)
        cout << "Maximum is: " << b << endl;
    else
        cout << "Maximum is: " << c << endl;

    return 0;
}
```

---

### ✅ 4️⃣ Problem: **Check if a year is a leap year**

**🔎 সমস্যা ব্যাখ্যা:**
একটি বছর ইনপুট নিয়ে বলুন সেটি **Leap Year** কি না।

**💡 কৌশল:**
Leap year এর নিয়ম:

* ৪ দিয়ে বিভাজ্য
* তবে ১০০ দিয়ে বিভাজ্য হলে হতে হবে ৪০০ দিয়ে বিভাজ্য

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int year;
    cout << "Enter a year: ";
    cin >> year;

    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
        cout << "Leap Year" << endl;
    else
        cout << "Not a Leap Year" << endl;

    return 0;
}
```

---

### ✅ 5️⃣ Problem: **Create a simple calculator (add, subtract, etc.)**

**🔎 সমস্যা ব্যাখ্যা:**
দুইটি সংখ্যা ও একটি অপারেটর ইনপুট নিয়ে ফলাফল প্রিন্ট করতে হবে।

**💡 কৌশল:**

* `+`, `-`, `*`, `/` অপারেটর গুলোর জন্য `switch-case` ব্যবহার করা।
* `/` ক্ষেত্রে `0` দিয়ে ভাগ হওয়া যাচাই করা।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    char op;
    cout << "Enter expression (e.g. 5 + 3): ";
    cin >> a >> op >> b;

    switch(op) {
        case '+': cout << "Result: " << a + b; break;
        case '-': cout << "Result: " << a - b; break;
        case '*': cout << "Result: " << a * b; break;
        case '/': 
            if (b != 0)
                cout << "Result: " << a / b;
            else
                cout << "Division by zero error";
            break;
        default:
            cout << "Invalid operator";
    }

    return 0;
}
```

---

### ✅ 6️⃣ Problem: **Print numbers from 1 to N**

**🔎 সমস্যা ব্যাখ্যা:**
ইউজার একটি সংখ্যা `N` ইনপুট দিবে। আপনাকে `1` থেকে `N` পর্যন্ত সব সংখ্যা প্রিন্ট করতে হবে।

**💡 কৌশল:**

* `for` লুপ ব্যবহার করে `1` থেকে `N` পর্যন্ত ইটারেট করা।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter N: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        cout << i << " ";
    }

    return 0;
}
```

---

### ✅ 7️⃣ Problem: **Print the sum of first N natural numbers**

**🔎 সমস্যা ব্যাখ্যা:**
ইউজার একটি সংখ্যা `N` ইনপুট দিবে। আপনাকে `1` থেকে `N` পর্যন্ত সব সংখ্যার যোগফল বের করতে হবে।

**💡 কৌশল:**

* একটি `sum` ভ্যারিয়েবল নিয়ে প্রতিটি সংখ্যাকে যোগ করতে হবে `for` লুপের মাধ্যমে।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, sum = 0;
    cout << "Enter N: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        sum += i;
    }

    cout << "Sum: " << sum << endl;
    return 0;
}
```

---

### ✅ 8️⃣ Problem: **Print multiplication table of a number**

**🔎 সমস্যা ব্যাখ্যা:**
ইউজার একটি সংখ্যা ইনপুট দিবে। আপনাকে সেই সংখ্যার **গুণের তালিকা** (Multiplication Table) প্রিন্ট করতে হবে।

**💡 কৌশল:**

* `for` লুপ ব্যবহার করে ১ থেকে ১০ পর্যন্ত গুণ করে প্রিন্ট করা।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;

    for (int i = 1; i <= 10; i++) {
        cout << n << " x " << i << " = " << n * i << endl;
    }

    return 0;
}
```

---

### ✅ 9️⃣ Problem: **Find factorial of a number**

**🔎 সমস্যা ব্যাখ্যা:**
ইউজার একটি সংখ্যা দিবে। আপনাকে তার **factorial** (গুণফল) বের করতে হবে।

**💡 কৌশল:**

* `1 × 2 × 3 × ... × n` হিসেব করে ফলাফল বের করতে হবে।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    long long fact = 1;
    cout << "Enter a number: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        fact *= i;
    }

    cout << "Factorial: " << fact << endl;
    return 0;
}
```

---

### ✅ 🔟 Problem: **Reverse a number**

**🔎 সমস্যা ব্যাখ্যা:**
ইউজার একটি পূর্ণ সংখ্যা দিবে। আপনাকে সংখ্যাটি **উল্টো করে** প্রিন্ট করতে হবে।

**💡 কৌশল:**

* `%` দিয়ে শেষ ডিজিট বের করে এবং `/` দিয়ে আগের ডিজিটে যাওয়া যায়।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, reversed = 0;
    cout << "Enter a number: ";
    cin >> n;

    while (n != 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }

    cout << "Reversed number: " << reversed << endl;
    return 0;
}
```


### ✅ 1️⃣1️⃣ Problem: **Count digits in a number**

**🔎 সমস্যা ব্যাখ্যা:**
একটি পূর্ণসংখ্যা ইনপুট নিয়ে সেটির কতটি অঙ্ক আছে তা বের করতে হবে।

**💡 কৌশল:**

* `while` লুপ দিয়ে প্রতি ধাপে `/10` করে অঙ্ক কমিয়ে `count` বাড়ানো।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, count = 0;
    cout << "Enter a number: ";
    cin >> n;

    if (n == 0)
        count = 1;
    else {
        while (n != 0) {
            n /= 10;
            count++;
        }
    }

    cout << "Number of digits: " << count << endl;
    return 0;
}
```

---

### ✅ 1️⃣2️⃣ Problem: **Check if a number is palindrome**

**🔎 সমস্যা ব্যাখ্যা:**
Palindrome সংখ্যায় উল্টো করলেও সংখ্যাটি একই থাকে। যেমন: 121, 1331

**💡 কৌশল:**

* সংখ্যা রিভার্স করে আগেরটার সাথে তুলনা করতে হবে।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, original, reversed = 0;
    cout << "Enter a number: ";
    cin >> n;

    original = n;
    while (n != 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }

    if (original == reversed)
        cout << "Palindrome" << endl;
    else
        cout << "Not a Palindrome" << endl;

    return 0;
}
```

---

### ✅ 1️⃣3️⃣ Problem: **Print all even numbers up to N**

**🔎 সমস্যা ব্যাখ্যা:**
ইউজার `N` ইনপুট দিলে `1` থেকে `N` পর্যন্ত সব **even numbers** প্রিন্ট করতে হবে।

**💡 কৌশল:**

* `for` লুপ এবং `% 2 == 0` দিয়ে চেক করা।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter N: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0)
            cout << i << " ";
    }

    return 0;
}
```

---

### ✅ 1️⃣4️⃣ Problem: **Print Fibonacci series up to N terms**

**🔎 সমস্যা ব্যাখ্যা:**
Fibonacci সিরিজের শুরু: `0 1 1 2 3 5 8 13 ...` — প্রতিটি সংখ্যা আগের দুইটার যোগফল।

**💡 কৌশল:**

* প্রথম দুই মান fix করে বাকি গুলো লুপ দিয়ে বের করা।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, a = 0, b = 1, next;
    cout << "Enter number of terms: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        cout << a << " ";
        next = a + b;
        a = b;
        b = next;
    }

    return 0;
}
```

---

### ✅ 1️⃣5️⃣ Problem: **Check if a number is prime**

**🔎 সমস্যা ব্যাখ্যা:**
প্রাইম নাম্বার হলো যেটি ১ ও নিজের দ্বারা বিভাজ্য হয়, অন্য কিছুর দ্বারা নয়।

**💡 কৌশল:**

* `2` থেকে `sqrt(n)` পর্যন্ত চেক করে যদি কিছুর দ্বারা বিভাজ্য হয় → প্রাইম নয়।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, flag = 0;
    cout << "Enter a number: ";
    cin >> n;

    if (n <= 1)
        flag = 1;
    else {
        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0) {
                flag = 1;
                break;
            }
        }
    }

    if (flag == 0)
        cout << "Prime" << endl;
    else
        cout << "Not Prime" << endl;

    return 0;
}
```

---

# 📘 C++ Control Flow – সমস্যা 1️⃣6️⃣ থেকে 2️⃣0️⃣ পর্যন্ত বিস্তারিত সমাধান

---

### ✅ 1️⃣6️⃣ Problem: **Find the sum of digits of a number**

**🔎 সমস্যা ব্যাখ্যা:**
একটি পূর্ণসংখ্যা ইনপুট নিয়ে তার সব অঙ্ক (digit) গুলোর যোগফল নির্ণয় করতে হবে।

**💡 কৌশল:**

* `%` দিয়ে শেষ অঙ্ক বের করে `sum` এ যোগ করতে হবে
* `/` দিয়ে সংখ্যাটি ছোট করে নিতে হবে
* `while` লুপে এটি চালানো হয় যতক্ষণ না `n == 0`

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, sum = 0;
    cout << "Enter a number: ";
    cin >> n;

    while (n != 0) {
        sum += n % 10;
        n /= 10;
    }

    cout << "Sum of digits: " << sum << endl;
    return 0;
}
```

---

### ✅ 1️⃣7️⃣ Problem: **Display menu to user and perform action**

**🔎 সমস্যা ব্যাখ্যা:**
ইউজারকে একটি মেনু দেখাতে হবে এবং সেই অনুযায়ী কাজ করতে হবে। যেমন: যোগ, বিয়োগ, গুণ ইত্যাদি।

**💡 কৌশল:**

* `do-while` লুপ দিয়ে মেনু চালানো
* `switch-case` দিয়ে অপারেশন নির্বাচন
* exit অপশন থাকলে `break` করা

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int choice, a, b;
    do {
        cout << "\nMenu:\n1.Add\n2.Subtract\n3.Multiply\n4.Exit\nEnter choice: ";
        cin >> choice;

        if (choice >= 1 && choice <= 3) {
            cout << "Enter two numbers: ";
            cin >> a >> b;
        }

        switch(choice) {
            case 1: cout << "Sum: " << a + b << endl; break;
            case 2: cout << "Difference: " << a - b << endl; break;
            case 3: cout << "Product: " << a * b << endl; break;
            case 4: cout << "Exiting..."; break;
            default: cout << "Invalid choice!";
        }
    } while (choice != 4);

    return 0;
}
```

---

### ✅ 1️⃣8️⃣ Problem: **Print pattern of stars (triangle)**

**🔎 সমস্যা ব্যাখ্যা:**
ইউজার একটি সংখ্যা দিবে যেটি হচ্ছে **rows**, এবং আপনাকে একটি ত্রিভুজের মত **তারকা চিহ্নের pattern** প্রিন্ট করতে হবে।

**💡 কৌশল:**

* `for` লুপ দিয়ে প্রতিটি row প্রিন্ট
* ভিতরের `for` লুপ দিয়ে কতগুলো তারকা প্রিন্ট হবে তা নির্ধারণ

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int rows;
    cout << "Enter number of rows: ";
    cin >> rows;

    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}
```

---

### ✅ 1️⃣9️⃣ Problem: **Check whether a character is vowel or consonant**

**🔎 সমস্যা ব্যাখ্যা:**
ইউজার একটি অক্ষর ইনপুট দিবে। আপনাকে বলতে হবে এটি **vowel** (স্বরবর্ণ) নাকি **consonant** (ব্যঞ্জনবর্ণ)।

**💡 কৌশল:**

* `switch` বা `if` দিয়ে অক্ষরটি 'a', 'e', 'i', 'o', 'u' কিনা চেক করতে হবে
* কেস-ইনসেনসিটিভ করতে চাইলে ছোট/বড় দুটোই চেক করতে হবে

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    char ch;
    cout << "Enter a character: ";
    cin >> ch;

    switch(ch) {
        case 'a': case 'e': case 'i': case 'o': case 'u':
        case 'A': case 'E': case 'I': case 'O': case 'U':
            cout << "Vowel"; break;
        default:
            cout << "Consonant";
    }

    return 0;
}
```

---

### ✅ 2️⃣0️⃣ Problem: **Convert lowercase to uppercase**

**🔎 সমস্যা ব্যাখ্যা:**
ইউজার একটি ছোট হাতের অক্ষর দিবে। আপনাকে এটি **বড় হাতের অক্ষরে** রূপান্তর করতে হবে।

**💡 কৌশল:**

* ASCII অনুযায়ী 'a' এর মান 97, আর 'A' এর মান 65
* পার্থক্য = 32 → `ch - 32` করলে বড় হাতের অক্ষর পাওয়া যায়

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    char ch;
    cout << "Enter a lowercase letter: ";
    cin >> ch;

    if (ch >= 'a' && ch <= 'z') {
        ch = ch - 32;
        cout << "Uppercase: " << ch;
    } else {
        cout << "Not a lowercase letter.";
    }

    return 0;
}
```



# 📘 C++ Control Flow – সমস্যা 2️⃣1️⃣ থেকে 2️⃣5️⃣ পর্যন্ত বিস্তারিত সমাধান

---

### ✅ 2️⃣1️⃣ Problem: **Find GCD of two numbers**

**🔎 সমস্যা ব্যাখ্যা:**
GCD (Greatest Common Divisor) হলো দুটি সংখ্যার সবচেয়ে বড় গুণিতক যেটা উভয় সংখ্যাকে ভাগ করতে পারে।

**💡 কৌশল:**

* ইউক্লিডিয়ান অ্যালগরিদম অনুসারে:
  `GCD(a, b) = GCD(b, a % b)`
* যতক্ষণ পর্যন্ত `b ≠ 0`, ততক্ষণ `a % b` দিয়ে নতুন `b` বের করে লুপ চালাতে হবে।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;

    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }

    cout << "GCD is: " << a << endl;
    return 0;
}
```

---

### ✅ 2️⃣2️⃣ Problem: **Print reverse of a string**

**🔎 সমস্যা ব্যাখ্যা:**
একটি স্ট্রিং ইনপুট নিয়ে আপনাকে তা **উল্টো করে** প্রিন্ট করতে হবে।

**💡 কৌশল:**

* স্ট্রিংয়ের শেষে থেকে শুরু করে প্রথম পর্যন্ত `for` লুপ চালিয়ে প্রতিটি অক্ষর প্রিন্ট করতে হবে।

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cout << "Enter a string: ";
    cin >> s;

    for (int i = s.length() - 1; i >= 0; i--) {
        cout << s[i];
    }

    return 0;
}
```

---

### ✅ 2️⃣3️⃣ Problem: **Implement a number guessing game**

**🔎 সমস্যা ব্যাখ্যা:**
কম্পিউটার একটি গোপন সংখ্যা ধার্য করবে (১ থেকে ১০০ এর মধ্যে)। ইউজারকে এটি অনুমান করতে হবে যতক্ষণ না সে সঠিক সংখ্যা বলে।

**💡 কৌশল:**

* `rand()` ও `srand(time(0))` ব্যবহার করে র‍্যান্ডম সংখ্যা তৈরি
* `while(true)` লুপ ব্যবহার করে প্রতি গেসের পর চেক করা
* যদি সঠিক হয় তাহলে `break`

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int secret = rand() % 100 + 1, guess;

    while (true) {
        cout << "Guess the number (1-100): ";
        cin >> guess;

        if (guess == secret) {
            cout << "Correct! You guessed it.";
            break;
        } else if (guess < secret) {
            cout << "Too low!" << endl;
        } else {
            cout << "Too high!" << endl;
        }
    }

    return 0;
}
```

---

### ✅ 2️⃣4️⃣ Problem: **Check if a number is Armstrong number**

**🔎 সমস্যা ব্যাখ্যা:**
একটি সংখ্যা যদি তার প্রতিটি অঙ্কের শক্তি (power) যোগফলের সমান হয়, তাহলে সেটা Armstrong number।
উদাহরণ: 153 = 1³ + 5³ + 3³

**💡 কৌশল:**

* প্রথমে কতটি digit আছে তা বের করতে হবে
* তারপর প্রতিটি digit এর `pow(digit, total_digits)` হিসাব করে যোগ করতে হবে

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n, sum = 0, temp, digits = 0;
    cout << "Enter a number: ";
    cin >> n;
    temp = n;

    while (temp != 0) {
        digits++;
        temp /= 10;
    }

    temp = n;
    while (temp != 0) {
        int digit = temp % 10;
        sum += pow(digit, digits);
        temp /= 10;
    }

    if (sum == n)
        cout << "Armstrong Number";
    else
        cout << "Not Armstrong";

    return 0;
}
```

---

### ✅ 2️⃣5️⃣ Problem: **Simulate login attempts with limited tries**

**🔎 সমস্যা ব্যাখ্যা:**
ইউজার যদি ৩ বারের বেশি ভুল পাসওয়ার্ড দেয়, তাহলে "Account Locked" দেখাতে হবে। সঠিক পাসওয়ার্ড দিলে “Access Granted”।

**💡 কৌশল:**

* `do-while` লুপ
* `tries` কাউন্টার দিয়ে চেক
* পাসওয়ার্ড যাচাইয়ের জন্য `if` ব্যবহার

**✅ পূর্ণ C++ কোড:**

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string password = "cpp123", input;
    int tries = 3;

    do {
        cout << "Enter password: ";
        cin >> input;

        if (input == password) {
            cout << "Access Granted!";
            break;
        } else {
            tries--;
            cout << "Incorrect! Tries left: " << tries << endl;
        }
    } while (tries > 0);

    if (tries == 0)
        cout << "Account locked.";

    return 0;
}
```


## 🎯 C++ Control Flow Interview Questions (Link সহ)

| #  | প্রশ্ন                                                                                    | লিঙ্ক                                                                                                                           |
| -- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 1  | Default case কি switch‑এ বাধ্যতামূলক?                                                     | [Quiz: C++ Flow Control](https://www.geeksforgeeks.org/quizzes/cpp-flow-control/) ([InterviewPrep][1], [GeeksforGeeks][2])      |
| 2  | `if(0)` ব্লকে কী আউটপুট হয়?                                                               | [Quiz: C++ Flow Control](https://www.geeksforgeeks.org/quizzes/cpp-flow-control/)                                               |
| 3  | semicolon-মুক্ত for‑loop vs loop‑body জানাও।                                              | [Quiz: C++ Loops](https://www.geeksforgeeks.org/quizzes/c-loops/)                                                               |
| 4  | কোন লুপ গ্যারান্টিযুক্তভাবে একবারও চালানো হয়?                                             | [Quiz: C++ Loops](https://www.geeksforgeeks.org/quizzes/c-loops/)                                                               |
| 5  | break vs continue – কখন কোনটা ব্যবহার হয়?                                                 | [Quiz: Loops & Conditional](https://www.geeksforgeeks.org/quizzes/c-loops-and-conditional-statements/)                          |
| 6  | switch এ কোন `case` ছাড়া প্রবেশ করলে কী হয়?                                               | [Quiz: C++ Flow Control](https://www.geeksforgeeks.org/quizzes/cpp-flow-control/)                                               |
| 7  | if, if‑else vs switch‑case—কবে কী ব্যবহার?                                                | [Article: Decision Making](https://www.geeksforgeeks.org/cpp/decision-making-c-cpp/)                                            |
| 8  | C++‑এর loop গুলো (for, while, do‑while) এর পার্থক্য কী?                                   | [Article: Decision Making](https://www.geeksforgeeks.org/cpp/decision-making-c-cpp/)                                            |
| 9  | `else` যখন while‑এর সাথে এলে কী কাজ করে?                                                  | [Quiz: Conditionals & Flow](https://www.geeksforgeeks.org/quizzes/conditionals-and-flow-control/)                               |
| 10 | nested if‑else এর execution order কী?                                                     | [Quiz: C++ Flow Control](https://www.geeksforgeeks.org/quizzes/cpp-flow-control/)                                               |
| 11 | semicolon পরে `for(...);` করলে কী হয়?                                                     | [Quiz: C++ Loops](https://www.geeksforgeeks.org/quizzes/c-loops/)                                                               |
| 12 | switch চলাকালীন semicolon রাখা কি ঠিক?                                                    | [Control Flow Statements](https://www.geeksforgeeks.org/computer-science-fundamentals/control-flow-statements-in-programming/)  |
| 13 | `goto`, `break`, `continue` এর মধ্যে পার্থক্য কী?                                         | [Control Flow Statements](https://www.geeksforgeeks.org/computer-science-fundamentals/control-flow-statements-in-programming/)  |
| 14 | `default` না দিলে switch কীভাবে handle করে?                                               | [Quiz: C++ Flow Control](https://www.geeksforgeeks.org/quizzes/cpp-flow-control/)                                               |
| 15 | conditional operator? (`?:`)                                                              | [Flow Control Quiz](https://www.geeksforgeeks.org/quizzes/c-loops-and-conditional-statements/)                                  |
| 16 | কোনটি সঠিক – switch যদি string নেয়?                                                       | [Quiz: C++ Flow Control](https://www.geeksforgeeks.org/quizzes/cpp-flow-control/)                                               |
| 17 | loop control variable না বদলে গেলে কী সমস্যা হয়?                                          | [Quiz: C++ Loops](https://www.geeksforgeeks.org/quizzes/c-loops/)                                                               |
| 18 | semicolon ভুলে গেলে while/do-while কীভাবে কাজ করবে?                                       | [Decision Making](https://www.geeksforgeeks.org/cpp/decision-making-c-cpp/)                                                     |
| 19 | কাজের উদাহরণ – triangle pattern print?                                                    | [Pattern Printing](https://www.geeksforgeeks.org/quizzes/c-loops-and-conditional-statements/)                                   |
| 20 | Condition inside loop অস্বাভাবিক output হলে কী করেন?                                      | [Control Flow Statements](https://www.geeksforgeeks.org/computer-science-fundamentals/control-flow-statements-in-programming/)  |
| 21 | while(1) এবং do-while(true) মধ্যে পার্থক্য কী?                                            | [Decision Making](https://www.geeksforgeeks.org/cpp/decision-making-c-cpp/)                                                     |
| 22 | nested loop এর time complexity কিভাবে বুঝবেন?                                             | [Control Flow Statements](https://www.geeksforgeeks.org/computer-science-fundamentals/control-flow-statements-in-programming/)  |
| 23 | break কতখানি nested loop ভেঙে?                                                            | [Control Flow Statements](https://www.geeksforgeeks.org/computer-science-fundamentals/control-flow-statements-in-programming/)  |
| 24 | continue কোথায় use করলে code efficient হবে?                                               | [Quiz: Loops](https://www.geeksforgeeks.org/quizzes/c-loops/)                                                                   |
| 25 | উদাহরণ— number palindrome, Armstrong, GCD, factorial: explain loops+conditions প্র্যাকটিস | [C++ Coding Interview Qs 2025](https://www.geeksforgeeks.org/cpp/cpp-coding-interview-questions-and-answers/)                   |

---



[1]: https://interviewprep.org/conditional-statements-interview-questions/?utm_source=chatgpt.com "Top 25 Conditional Statements Interview Questions and Answers"
[2]: https://www.geeksforgeeks.org/quizzes/cpp-flow-control/?utm_source=chatgpt.com "Quiz about C++ Flow Control - GeeksforGeeks"



## 🧠 30 Codeforces  Control Flow সমস্যা

1. **Bit++** – [https://codeforces.com/problemset/problem/282/A](https://codeforces.com/problemset/problem/282/A)
2. **Next Round** – [https://codeforces.com/problemset/problem/158/A](https://codeforces.com/problemset/problem/158/A)
3. **Beautiful Matrix** – [https://codeforces.com/problemset/problem/263/A](https://codeforces.com/problemset/problem/263/A)
4. **Petya and Strings** – [https://codeforces.com/problemset/problem/112/A](https://codeforces.com/problemset/problem/112/A)
5. **Helpful Maths** – [https://codeforces.com/problemset/problem/339/A](https://codeforces.com/problemset/problem/339/A)
6. **Boy or Girl** – [https://codeforces.com/problemset/problem/236/A](https://codeforces.com/problemset/problem/236/A)
7. **Kevin and Combination Lock** – [https://codeforces.com/problemset/problem/2048/A](https://codeforces.com/problemset/problem/2048/A)
8. **Alyona and a Square** – [https://codeforces.com/problemset/problem/2047/A](https://codeforces.com/problemset/problem/2047/A)
9. **Draw a Square** – [https://codeforces.com/problemset/problem/2074/A](https://codeforces.com/problemset/problem/2074/A)
10. **Common Subsequence** – [https://codeforces.com/problemset/problem/1144/A](https://codeforces.com/problemset/problem/1144/A) *(arrays+loops)*
11. **A+B Again?** – [https://codeforces.com/problemset/problem/1999/A](https://codeforces.com/problemset/problem/1999/A)
12. **Lucky?** – [https://codeforces.com/problemset/problem/1676/A](https://codeforces.com/problemset/problem/1676/A)
13. **Division?** – [https://codeforces.com/problemset/problem/1669/A](https://codeforces.com/problemset/problem/1669/A)
14. **Remove Smallest** – [https://codeforces.com/problemset/problem/1399/A](https://codeforces.com/problemset/problem/1399/A)
15. **Holiday Of Equality** – [https://codeforces.com/problemset/problem/758/A](https://codeforces.com/problemset/problem/758/A)
16. **Interesting Drink** – [https://codeforces.com/problemset/problem/706/B](https://codeforces.com/problemset/problem/706/B)
17. **Codeforces Checking** – [https://codeforces.com/problemset/problem/1791/A](https://codeforces.com/problemset/problem/1791/A)
18. **Team** – [https://codeforces.com/problemset/problem/231/A](https://codeforces.com/problemset/problem/231/A)
19. **The Picky Cat** – [https://codeforces.com/problemset/problem/2102/B](https://codeforces.com/problemset/problem/2102/B)
20. **Mex in the Grid** – [https://codeforces.com/problemset/problem/2101/A](https://codeforces.com/problemset/problem/2101/A)
21. **Energy Crystals** – [https://codeforces.com/problemset/problem/2111/A](https://codeforces.com/problemset/problem/2111/A)
22. **SUMdamental Decomposition** – [https://codeforces.com/problemset/problem/2108/B](https://codeforces.com/problemset/problem/2108/B)
23. **pspspsps** – [https://codeforces.com/problemset/problem/2049/B](https://codeforces.com/problemset/problem/2049/B)
24. **Robot Program** – [https://codeforces.com/problemset/problem/2070/B](https://codeforces.com/problemset/problem/2070/B)
25. **Greedy with Strings** – [https://codeforces.com/problemset/problem/2063/F2](https://codeforces.com/problemset/problem/2063/F2) *(but use loops)*
26. **Draw a Square** (variations practice) – repeat? skip
27. **Kevin and Math Class** – [https://codeforces.com/problemset/problem/2048/F](https://codeforces.com/problemset/problem/2048/F)
28. **Kevin and Binary Strings** – [https://codeforces.com/problemset/problem/2048/C](https://codeforces.com/problemset/problem/2048/C)
29. **A+B** (very basic) – [https://codeforces.com/problemset/problem/610/A](https://codeforces.com/problemset/problem/610/A) *(Practice Code)*
30. **Checkposts** – [https://codeforces.com/problemset/problem/427/C](https://codeforces.com/problemset/problem/427/C) *(loop + if)*

---

### 📌 নির্দেশনা:

* সমস্যা নম্বর 1–9,11–18 হলো **A-পরিসরের** শিক্ষামূলক প্রবলেম — Control Flow-এর জন্য উপযোগী।
* 19–30 এ কিছু মিশ্র difficulty, তবে loop বা condition ভিত্তিক অংশ রয়েছে।


---

## 🔹 LeetCode – Control Flow ও Loop ভিত্তিক সমস্যা (১–৪০)

1. **Two Sum** – [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)
2. **Reverse Integer** – [https://leetcode.com/problems/reverse-integer/](https://leetcode.com/problems/reverse-integer/)
3. **Palindrome Number** – [https://leetcode.com/problems/palindrome-number/](https://leetcode.com/problems/palindrome-number/)
4. **Fizz Buzz** – [https://leetcode.com/problems/fizz-buzz/](https://leetcode.com/problems/fizz-buzz/)
5. **Count Primes** – [https://leetcode.com/problems/count-primes/](https://leetcode.com/problems/count-primes/)
6. **Power of Two** – [https://leetcode.com/problems/power-of-two/](https://leetcode.com/problems/power-of-two/)
7. **Missing Number** – [https://leetcode.com/problems/missing-number/](https://leetcode.com/problems/missing-number/)
8. **Find Pivot Index** – [https://leetcode.com/problems/find-pivot-index/](https://leetcode.com/problems/find-pivot-index/)
9. **Plus One** – [https://leetcode.com/problems/plus-one/](https://leetcode.com/problems/plus-one/)
10. **Valid Parentheses** – [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)
11. **Merge Two Sorted Lists** – [https://leetcode.com/problems/merge-two-sorted-lists/](https://leetcode.com/problems/merge-two-sorted-lists/)
12. **Climbing Stairs** – [https://leetcode.com/problems/climbing-stairs/](https://leetcode.com/problems/climbing-stairs/)
13. **Best Time to Buy and Sell Stock** – [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
14. **Move Zeroes** – [https://leetcode.com/problems/move-zeroes/](https://leetcode.com/problems/move-zeroes/)
15. **Single Number** – [https://leetcode.com/problems/single-number/](https://leetcode.com/problems/single-number/)
16. **Intersection of Two Arrays II** – [https://leetcode.com/problems/intersection-of-two-arrays-ii/](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
17. **Maximum Subarray** – [https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)
18. **Contains Duplicate** – [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)
19. **Roman to Integer** – [https://leetcode.com/problems/roman-to-integer/](https://leetcode.com/problems/roman-to-integer/)
20. **Add Digits** – [https://leetcode.com/problems/add-digits/](https://leetcode.com/problems/add-digits/)
21. **Factorial Trailing Zeroes** – [https://leetcode.com/problems/factorial-trailing-zeroes/](https://leetcode.com/problems/factorial-trailing-zeroes/)
22. **Happy Number** – [https://leetcode.com/problems/happy-number/](https://leetcode.com/problems/happy-number/)
23. **Sqrt(x)** – [https://leetcode.com/problems/sqrtx/](https://leetcode.com/problems/sqrtx/)
24. **Guess Number Higher or Lower** – [https://leetcode.com/problems/guess-number-higher-or-lower/](https://leetcode.com/problems/guess-number-higher-or-lower/)
25. **Number of 1 Bits** – [https://leetcode.com/problems/number-of-1-bits/](https://leetcode.com/problems/number-of-1-bits/)
26. **Add Binary** – [https://leetcode.com/problems/add-binary/](https://leetcode.com/problems/add-binary/)
27. **Sum of Square Numbers** – [https://leetcode.com/problems/sum-of-square-numbers/](https://leetcode.com/problems/sum-of-square-numbers/)
28. **Hamming Distance** – [https://leetcode.com/problems/hamming-distance/](https://leetcode.com/problems/hamming-distance/)
29. **Power of Three** – [https://leetcode.com/problems/power-of-three/](https://leetcode.com/problems/power-of-three/)
30. **Excel Sheet Column Number** – [https://leetcode.com/problems/excel-sheet-column-number/](https://leetcode.com/problems/excel-sheet-column-number/)
31. **Roman to Integer** – already listed; skip → replace with **Reverse String** – [https://leetcode.com/problems/reverse-string/](https://leetcode.com/problems/reverse-string/)
32. **Implement strStr()** – [https://leetcode.com/problems/implement-strstr/](https://leetcode.com/problems/implement-strstr/)
33. **Length of Last Word** – [https://leetcode.com/problems/length-of-last-word/](https://leetcode.com/problems/length-of-last-word/)
34. **Add Strings** – [https://leetcode.com/problems/add-strings/](https://leetcode.com/problems/add-strings/)
35. **String to Integer (atoi)** – [https://leetcode.com/problems/string-to-integer-atoi/](https://leetcode.com/problems/string-to-integer-atoi/)
36. **Validate Palindrome** – [https://leetcode.com/problems/valid-palindrome/](https://leetcode.com/problems/valid-palindrome/)
37. **Zigzag Conversion** – [https://leetcode.com/problems/zigzag-conversion/](https://leetcode.com/problems/zigzag-conversion/)
38. **Container With Most Water** – [https://leetcode.com/problems/container-with-most-water/](https://leetcode.com/problems/container-with-most-water/)
39. **Rotate Array** – [https://leetcode.com/problems/rotate-array/](https://leetcode.com/problems/rotate-array/)
40. **Move Zeroes** – duplicate; replace with **Find All Numbers Disappeared in an Array** – [https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

---



## 🎯 C++ Control Flow – Interview Questions (Link সহ)

| #  | প্রশ্ন                                                          | রেফারেন্স / লিঙ্ক                                                                                                                                                    |
| -- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | Check whether a number is even or odd                           | [GfG Quiz: Even/Odd](https://www.geeksforgeeks.org/cpp-program-to-check-whether-number-is-even-or-odd/) ([GeeksforGeeks][1], [GeeksforGeeks][2], [GeeksforGeeks][3]) |
| 2  | Determine if a year is a leap year                              | [GfG: Leap Year Check](https://www.geeksforgeeks.org/c-program-check-given-year-leap-year/)                                                                          |
| 3  | Compare three numbers and find the maximum                      | [GfG: Maximum of Three](https://www.geeksforgeeks.org/cpp-program-to-find-maximum-or-minimum-of-three-numbers/)                                                      |
| 4  | Check if a character is a vowel or consonant                    | [GfG: Vowel or Consonant](https://www.geeksforgeeks.org/program-check-vowel-consonant-character/)                                                                    |
| 5  | Implement a simple calculator using switch-case                 | [GfG: Simple Calculator](https://www.geeksforgeeks.org/cpp-simple-calculator-switch-case/)                                                                           |
| 6  | Print the sum of first N natural numbers                        | [GfG: Sum of N Numbers](https://www.geeksforgeeks.org/cpp-program-to-find-sum-of-first-n-natural-numbers/)                                                           |
| 7  | Reverse a number and check if it’s a palindrome                 | [GfG: Palindrome Number](https://www.geeksforgeeks.org/c-program-check-number-palindrome/)                                                                           |
| 8  | Print multiplication table of a number                          | [GfG: Multiplication Table](https://www.geeksforgeeks.org/cpp-program-print-multiplication-table-number/)                                                            |
| 9  | Count the number of digits in a number                          | [GfG: Count Digits](https://www.geeksforgeeks.org/c-program-find-number-digits/)                                                                                     |
| 10 | Calculate factorial of a number via loop                        | [GfG: Factorial using Loop](https://www.geeksforgeeks.org/cpp-program-find-factorial-number-using-loop/)                                                             |
| 11 | Check if a number is an Armstrong number                        | [GfG: Armstrong Number](https://www.geeksforgeeks.org/c-program-to-check-armstrong-number/)                                                                          |
| 12 | Generate Fibonacci series up to N terms                         | [GfG: Fibonacci Series](https://www.geeksforgeeks.org/cpp-program-to-print-fibonacci-series-up-to-n-th-term/)                                                        |
| 13 | Find GCD of two numbers using Euclidean algorithm               | [GfG: GCD of Two Numbers](https://www.geeksforgeeks.org/c-program-to-find-gcd-or-hcf-of-two-numbers/)                                                                |
| 14 | Implement a number guessing game with loop and break            | [PrepInsta Flow Control Quiz 1](https://prepinsta.com/zoho/computer-programming/control-flow/quiz-1/)                                                                |
| 15 | Print star patterns (e.g. triangle, pyramid) using nested loops | [GfG: Pattern Printing](https://www.geeksforgeeks.org/cpp-program-patterns/)                                                                                         |
| 16 | Understand missing break in switch-case                         | [GfG Quiz on Flow Control](https://www.geeksforgeeks.org/quizzes/cpp-flow-control/)                                                                                  |
| 17 | Differentiate between for, while, and do‑while                  | [GfG Quiz on Flow Control](https://www.geeksforgeeks.org/quizzes/cpp-flow-control/)                                                                                  |
| 18 | Explain use‐cases for break vs continue                         | [GfG Quiz on Flow Control](https://www.geeksforgeeks.org/quizzes/cpp-flow-control/)                                                                                  |
| 19 | Demonstrate nested if‑else complexity                           | [GfG: Nested if Levels](https://www.geeksforgeeks.org/questions/in-cc-how-many-levels-of-nested-if-statements/)                                                      |
| 20 | Use goto, break, continue in control flow                       | [GfG: Control Flow Statements](https://www.geeksforgeeks.org/computer-science-fundamentals/control-flow-statements-in-programming/)                                  |

---



[1]: https://www.geeksforgeeks.org/computer-science-fundamentals/control-flow-statements-in-programming/?utm_source=chatgpt.com "Control flow statements in Programming - GeeksforGeeks"
[2]: https://www.geeksforgeeks.org/cpp/cpp-programming-examples/?utm_source=chatgpt.com "C++ Programming Examples - GeeksforGeeks"
[3]: https://www.geeksforgeeks.org/cpp/cpp-coding-interview-questions-and-answers/?utm_source=chatgpt.com "Top 100 C++ Coding Interview Questions and Answers [2025 Updated]"

