

# 📘 C++ Topic 1: Basics of C++ – পূর্ণাঙ্গ ডকুমেন্টেশন

---

## 🧩 1.1 Structure of a C++ Program

### 📌 ব্যাখ্যা:

প্রতিটি C++ প্রোগ্রাম `main()` ফাংশন দিয়ে শুরু হয়। একটি সাধারণ C++ কোডে থাকে:

* Header file (`#include`)
* Namespace (`using namespace std;`)
* `main()` ফাংশন
* Output বা logic

### 🧪 উদাহরণ:

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!";
    return 0;
}
```

---

## 🧩 1.2 Input / Output (`cin`, `cout`)

### 📌 ব্যাখ্যা:

* `cin`: ইনপুট নেওয়ার জন্য
* `cout`: আউটপুট দেওয়ার জন্য
* এরা দুটোই `<iostream>` হেডার ফাইলের অংশ

### 🔑 কিওয়ার্ড:

* `>>` (Extraction Operator) — `cin` এর সাথে
* `<<` (Insertion Operator) — `cout` এর সাথে

### 🧪 উদাহরণ:

```cpp
int x;
cin >> x;  // input
cout << "Value is: " << x;  // output
```

---

## 🧩 1.3 Variables and Data Types

### 📌 ব্যাখ্যা:

Variables হলো এমন কন্টেইনার যেখানে ডেটা সংরক্ষণ করা হয়। Data type বলে দেয় কেমন ধরণের ডেটা সে রাখতে পারবে।

### 🔹 গুরুত্বপূর্ণ Data Types:

* `int` → পূর্ণ সংখ্যা
* `float`, `double` → দশমিক সংখ্যা
* `char` → অক্ষর
* `bool` → true/false

### 🧪 উদাহরণ:

```cpp
int age = 21;
double pi = 3.14;
char grade = 'A';
bool passed = true;
```

---

## 🧩 1.4 Constants and Macros

### 📌 ব্যাখ্যা:

* **Constants**: যেগুলোর মান বদলায় না
* **Macros**: compile হওয়ার আগেই রেপ্লেস হয় (Preprocessor directive)

### 🔹 Declaration:

* `const` দিয়ে: C++ way
* `#define` দিয়ে: Macro style

### 🧪 উদাহরণ:

```cpp
const float PI = 3.1416;
#define SIZE 100
```

---

## 🧩 1.5 Comments

### 📌 ব্যাখ্যা:

Comments হচ্ছে কোডে ব্যাখ্যা দেওয়ার জন্য ব্যবহৃত অংশ। এটি কম্পাইল হয় না।

### 🔹 দুই প্রকার:

* Single-line: `//`
* Multi-line: `/* */`

### 🧪 উদাহরণ:

```cpp
// This is a single-line comment

/*
  This is a multi-line
  comment example
*/
```

---

## 🧩 1.6 Typecasting

### 📌 ব্যাখ্যা:

Typecasting হলো এক ডেটা টাইপকে অন্য টাইপে রূপান্তর করা।

### 🔹 দুই ধরণের casting:

* Implicit: compiler নিজে করে
* Explicit: তুমি নিজে করো (manual)

### 🧪 উদাহরণ:

```cpp
int x = 5;
double y = (double)x;  // explicit
float z = x + 2.5;     // implicit
```

---

## ✅ সারসংক্ষেপ টেবিল:

| বিষয়             | কী শেখা হয়েছে                          |
| ---------------- | -------------------------------------- |
| Structure        | Header, namespace, main function       |
| Input/Output     | `cin` এবং `cout` দিয়ে ডেটা নেওয়া/দেওয়া |
| Variables        | বিভিন্ন ডেটা টাইপ ও ব্যবহার            |
| Constants/Macros | Fixed value & preprocessor directives  |
| Comments         | কোডে ব্যাখ্যার জন্য ব্যবহার            |
| Typecasting      | ডেটা টাইপ পরিবর্তন করা                 |


---

# 💡 Topic 1: Basics of C++ – বিস্তারিত কোড উদাহরণ

---

## 🔹 1.1 Structure of a C++ Program

### ✅ কোড উদাহরণ:

```cpp
#include <iostream> // Header file for input/output

using namespace std; // Use standard namespace

int main() {
    // Code execution starts here
    cout << "Hello, World!" << endl;
    return 0;
}
```

### 🔍 ব্যাখ্যা:

* `#include <iostream>`: I/O এর জন্য প্রয়োজনীয় লাইব্রেরি
* `using namespace std;`: `std::cout` না লিখে শুধু `cout` ব্যবহার করতে পারি
* `int main()`: C++ প্রোগ্রামের entry point
* `return 0;`: সফলভাবে প্রোগ্রাম শেষ

---

## 🔹 1.2 Input / Output (`cin`, `cout`)

### ✅ কোড উদাহরণ:

```cpp
#include <iostream>
using namespace std;

int main() {
    int age;
    cout << "Enter your age: ";
    cin >> age; // input from user
    cout << "You are " << age << " years old." << endl;
    return 0;
}
```

### 🔍 ব্যাখ্যা:

* `cin >> age;` → ইউজার থেকে ইনপুট নেয়
* `cout <<` → ইউজারকে আউটপুট দেখায়
* `endl` → লাইন ব্রেক দেয় (নতুন লাইন)

---

## 🔹 1.3 Variables and Data Types

### ✅ কোড উদাহরণ:

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 10;         // integer
    float pi = 3.14f;   // float
    char ch = 'A';      // character
    bool status = true; // boolean

    cout << "Integer: " << x << endl;
    cout << "Float: " << pi << endl;
    cout << "Character: " << ch << endl;
    cout << "Boolean: " << status << endl; // true = 1, false = 0
    return 0;
}
```

### 🔍 ব্যাখ্যা:

* `int`, `float`, `char`, `bool` → Built-in data types
* `true` = 1, `false` = 0 (boolean representation)

---

## 🔹 1.4 Constants and Macros

### ✅ কোড উদাহরণ:

```cpp
#include <iostream>
#define SIZE 100 // Macro
using namespace std;

int main() {
    const float PI = 3.1416; // Constant variable

    cout << "Value of PI: " << PI << endl;
    cout << "Defined Size: " << SIZE << endl;

    // PI = 3.15; // ❌ Error: can't change const value
    return 0;
}
```

### 🔍 ব্যাখ্যা:

* `const` → রানটাইমে রক্ষা করা যায় এমন fixed মান
* `#define` → compile-time এ replace হয়ে যায় (Preprocessor Macro)

---

## 🔹 1.5 Comments

### ✅ কোড উদাহরণ:

```cpp
#include <iostream>
using namespace std;

int main() {
    // This is a single-line comment

    /*
     * This is a multi-line comment.
     * Used to explain multiple lines of code.
     */

    cout << "Comments are ignored by compiler!" << endl;
    return 0;
}
```

### 🔍 ব্যাখ্যা:

* কোডে ব্যাখ্যা যোগ করার জন্য comments ব্যবহৃত হয়
* কম্পাইলার এগুলোকে skip করে দেয়

---

## 🔹 1.6 Typecasting

### ✅ কোড উদাহরণ:

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10;
    double b = 3.5;

    // Implicit conversion
    double sum = a + b; // int automatically converted to double

    // Explicit conversion (Typecasting)
    int c = (int)b; // double manually casted to int

    cout << "Sum (implicit): " << sum << endl;
    cout << "Value of b as int (explicit): " << c << endl;

    return 0;
}
```

### 🔍 ব্যাখ্যা:

* **Implicit casting**: Compiler নিজেই টাইপ কনভার্ট করে
* **Explicit casting**: `(type)` দিয়ে আমরা কনভার্ট করি

---

## ✅ BONUS: Combine Everything Example

```cpp
#include <iostream>
#define AUTHOR "David"
using namespace std;

int main() {
    // Declare variables
    const float PI = 3.14;
    int radius;

    // Take input
    cout << "Enter radius: ";
    cin >> radius;

    // Calculate area using typecasting
    float area = (float)PI * radius * radius;

    // Output result
    cout << "Area of circle = " << area << endl;

    // Author info
    cout << "Program by: " << AUTHOR << endl;

    return 0;
}
```

---

## 🎯 উপসংহার: এই চ্যাপ্টারে তুমি শিখেছো:

| বিষয়              | শেখা হয়েছে                                          |
| ----------------- | --------------------------------------------------- |
| Program structure | C++ কোড কিভাবে লেখা হয়                              |
| I/O               | ইউজার থেকে ইনপুট নেওয়া ও প্রিন্ট করা                |
| Variables         | বিভিন্ন ডেটা রাখার ধরন                              |
| Constants         | Fixed মান কীভাবে রাখা যায়                           |
| Comments          | কোডে ব্যাখ্যা কীভাবে যোগ করা হয়                     |
| Typecasting       | ডেটার ধরন কীভাবে একটার থেকে আরেকটায় রূপান্তর করা হয় |


অবশ্যই David! এখন আমি তোমাকে **C++ Topic 1: Basics** এর উপর ভিত্তি করে একটি **Problem List** দিচ্ছি, যেখানে প্রতিটি সাবটপিক অনুযায়ী **বিশ্বস্ত Competitive Programming Platforms (যেমন: Codeforces, HackerRank, LeetCode, AtCoder, etc.)** থেকে beginner-level সমস্যা দেওয়া হয়েছে।

---

# 📘 C++ Topic 1: Basics – Problem List with Online Links

| Subtopic                     | Problem Title                              | Platform      | Link                                                                                                                                        |
| ---------------------------- | ------------------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅ 1.1 Program Structure      | Hello World                                | HackerRank    | [🔗 Link](https://www.hackerrank.com/challenges/cpp-hello-world/problem)                                                                    |
| ✅ 1.2 Input / Output         | Basic Data Input                           | Codeforces    | [🔗 Link](https://codeforces.com/contest/4/problem/A) *(Watermelon)*                                                                        |
| ✅ 1.2 Input / Output         | A+B Problem                                | AtCoder       | [🔗 Link](https://atcoder.jp/contests/abs/tasks/practice_1)                                                                                 |
| ✅ 1.3 Variables & Data Types | Variable Types in Practice                 | HackerRank    | [🔗 Link](https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem)                                                        |
| ✅ 1.4 Constants and Macros   | Area of a Circle (using const)             | HackerEarth   | [🔗 Link](https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/circle-1/) |
| ✅ 1.5 Comments               | Debug Comments Practice                    | HackerRank    | [🔗 Link](https://www.hackerrank.com/challenges/cpp-input-and-output/problem) *(with extra comment parsing)*                                |
| ✅ 1.6 Typecasting            | Type Conversion Practice                   | Coding Ninjas | [🔗 Link](https://www.codingninjas.com/studio/problems/convert-character-case_1112623)                                                      |
| ✅ Mixed Practice             | Simple Calculator (I/O + Variables + Cast) | CodeChef      | [🔗 Link](https://www.codechef.com/problems/FLOW001) *(Add Two Numbers)*                                                                    |
| ✅ Mixed Practice             | Average of Three Numbers                   | HackerRank    | [🔗 Link](https://www.hackerrank.com/challenges/average/problem) *(custom test input)*                                                      |
| ✅ Mixed Practice             | Print the Result                           | LeetCode      | [🔗 Link](https://leetcode.com/problems/concatenation-of-array/) *(with cout use case)*                                                     |




# 🔥 More Problem List for C++ Topic 1 (Beginner Practice)

| 🔢 No. | Subtopic                | Problem Title                           | Platform    | Difficulty | Link                                                                                                                                        |
| ------ | ----------------------- | --------------------------------------- | ----------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 1      | Input/Output            | Sum of Two Numbers                      | CodeChef    | Easy       | [🔗 Link](https://www.codechef.com/problems/INTEST)                                                                                         |
| 2      | Input/Output            | Take input and print                    | AtCoder     | Easy       | [🔗 Link](https://atcoder.jp/contests/abc086/tasks/abc086_a)                                                                                |
| 3      | Variables & I/O         | Add Two Numbers                         | Codeforces  | Easy       | [🔗 Link](https://codeforces.com/contest/71/problem/A)                                                                                      |
| 4      | Data Types              | Basic Data Types                        | HackerRank  | Easy       | [🔗 Link](https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem)                                                        |
| 5      | Typecasting             | Float to Integer Conversion             | LeetCode    | Easy       | [🔗 Link](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)                                                                  |
| 6      | Constants/Macros        | Area of Circle (Fixed π value)          | HackerEarth | Easy       | [🔗 Link](https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/circle-1/) |
| 7      | Typecasting             | Average Grade Calculation               | Codeforces  | Easy       | [🔗 Link](https://codeforces.com/problemset/problem/617/A)                                                                                  |
| 8      | Typecasting + Variables | BMI Calculator                          | Practice    | Easy       | Use user input: weight & height, calculate BMI with float division                                                                          |
| 9      | Input/Output            | Print Integer, Float, Char, and Boolean | HackerRank  | Easy       | [🔗 Link](https://www.hackerrank.com/challenges/variable-sized-arrays/problem) *(modified)*                                                 |
| 10     | Program Structure       | First Program with Math Expression      | HackerRank  | Easy       | [🔗 Link](https://www.hackerrank.com/challenges/cpp-hello-world/problem)                                                                    |

---

## ✅ Practice Checklist:

| ✅ Subtopic         | Suggested Problems  |
| ------------------ | ------------------- |
| `cin`, `cout`      | Problem 1, 2, 3, 10 |
| `int`, `float`     | Problem 4, 5, 7, 9  |
| `const`, `#define` | Problem 6           |
| Typecasting        | Problem 5, 7, 8     |
| Structure          | Problem 10          |

---

## 📘 Bonus Practice Ideas (Write Yourself):

You can also try writing these mini programs:

1. **Add three numbers and find average**
2. **Take a character and print ASCII value**
3. **Convert Celsius to Fahrenheit**
4. **Swap two variables using a third variable**
5. **Check whether the number is even or odd (using modulus `%`)**

---

## 📎 Resource Suggestion

You can also practice problems by topic from:

* [HackerRank C++ Domain](https://www.hackerrank.com/domains/tutorials/10-days-of-cpp)
* [LeetCode Easy Problems](https://leetcode.com/problemset/all/?difficulty=Easy)
* [Codeforces Problemset: Difficulty Rating 800-1000](https://codeforces.com/problemset?tags=implementation)

---
---

## 🧠 বিশেষ টিপস:

* প্রতিটি সাবটপিক এর কমপক্ষে **১-২টি প্রব্লেম** করলে তোমার C++ এর foundation অনেক শক্ত হবে।
* তুমি চাইলে এসব প্রব্লেম C++ দিয়ে solve করার সময় `#include <bits/stdc++.h>` ব্যবহার করতে পারো।
* অনুশীলনের সময় input/output format ভালো করে দেখো।

---


