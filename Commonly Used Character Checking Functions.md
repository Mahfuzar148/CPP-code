C++ এ **character check করার জন্য** `<cctype>` হেডার ফাইলে অনেকগুলো built-in ফাংশন আছে। এগুলো দিয়ে আমরা character এর ধরন (digit, letter, space, punctuation ইত্যাদি) চেক করতে পারি।

---

## ✅ Commonly Used Character Checking Functions ( `<cctype>` থেকে )

| Function       | কাজ                                                         |
| -------------- | ----------------------------------------------------------- |
| `isalnum(ch)`  | Alphabet অথবা digit কিনা চেক করে (`A-Z`, `a-z`, `0-9`)      |
| `isalpha(ch)`  | Alphabet কিনা (শুধু `A-Z`, `a-z`)                           |
| `isdigit(ch)`  | Digit কিনা (`0-9`)                                          |
| `islower(ch)`  | Small letter কিনা (`a-z`)                                   |
| `isupper(ch)`  | Capital letter কিনা (`A-Z`)                                 |
| `isspace(ch)`  | Space, tab, newline ইত্যাদি whitespace কিনা                 |
| `ispunct(ch)`  | Punctuation কিনা (`. , ! ? ; : - _ @ # ...`)                |
| `isxdigit(ch)` | Hexadecimal digit কিনা (`0-9`, `A-F`, `a-f`)                |
| `isprint(ch)`  | Printable character কিনা                                    |
| `isgraph(ch)`  | Printable কিন্তু space না হলে (যেমন `!`, `A`, `%`, ইত্যাদি) |
| `isblank(ch)`  | শুধুমাত্র `' '` (space) অথবা `\t` (tab) চেক করে             |
| `iscntrl(ch)`  | Control character কিনা (যেমন newline `\n`, tab `\t`)        |

---

## 🎯 Common Syntax (সবগুলোর জন্য একই)

```cpp
functionName(character)
```

👉 Return করে **non-zero (true)** যদি condition match করে, নাহলে **0 (false)**

---

## 🧪 Full Example to Test All:

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    char ch;
    cout << "Enter any character: ";
    cin >> ch;

    if (isalnum(ch))  cout << "isalnum: Alphanumeric" << endl;
    if (isalpha(ch))  cout << "isalpha: Alphabet" << endl;
    if (isdigit(ch))  cout << "isdigit: Digit" << endl;
    if (islower(ch))  cout << "islower: Lowercase letter" << endl;
    if (isupper(ch))  cout << "isupper: Uppercase letter" << endl;
    if (isspace(ch))  cout << "isspace: Whitespace character" << endl;
    if (ispunct(ch))  cout << "ispunct: Punctuation" << endl;
    if (isxdigit(ch)) cout << "isxdigit: Hexadecimal digit" << endl;
    if (isprint(ch))  cout << "isprint: Printable character" << endl;
    if (isgraph(ch))  cout << "isgraph: Printable & not space" << endl;
    if (isblank(ch))  cout << "isblank: Space or Tab" << endl;
    if (iscntrl(ch))  cout << "iscntrl: Control character" << endl;

    return 0;
}
```

---

### 📌 Bonus Tip:

* সব ফাংশনের return type **int** হয়, কিন্তু আমরা সেটা **true/false** হিসেবে ব্যবহার করি।
* Example: `if (isdigit(ch)) { ... }` ✅ সোজা ব্যবহার করতে পারো।

---

