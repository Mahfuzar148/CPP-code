
---

# 🔹 **Bit Manipulation Study Guide**

---

## **Batch–1: Basics (অপারেশনস ও সহজ ট্রিকস)**

1. **Bitwise AND (`&`)** – common set bits খুঁজতে। (masking, parity check)
2. **Bitwise OR (`|`)** – at least one bit 1 হলে 1। (union-type operation)
3. **Bitwise XOR (`^`)** – ভিন্ন হলে 1, সমান হলে 0। (parity, swapping, single number problems)
4. **Bitwise NOT (`~`)** – সব বিট উল্টে দেয়। (two’s complement বোঝার জন্য জরুরি)
5. **Left Shift (`<<`)** – multiply by 2^k (overflow না হলে)।
6. **Right Shift (`>>`)** – divide by 2^k (floor)।
7. **Odd/Even Check** – `(n & 1)` দিয়ে।
8. **Multiply/Divide by 2** – `n << 1`, `n >> 1`।
9. **XOR Swap Trick** – temp variable ছাড়াই swap।
10. **Set a bit** – `n | (1<<k)`।
11. **Clear a bit** – `n & ~(1<<k)`।
12. **Toggle a bit** – `n ^ (1<<k)`।
13. **Check if a bit is set** – `(n & (1<<k)) != 0`।

---

## **Batch–2: Counting & Fundamental Tricks**

14. **Count set bits** – Brian Kernighan’s Algorithm (`n &= (n-1)`)।
15. **Check if power of 2** – `n > 0 && (n & (n-1)) == 0`।
16. **Most Significant Bit (MSB)** – সর্বোচ্চ সেট বিট বের করা।
17. **Least Significant Bit (LSB)** – সবচেয়ে নিচের সেট বিট বের করা।
18. **Extract lowest set bit** – `n & -n`।
19. **Remove lowest set bit** – `n & (n-1)`।
20. **Bit length / log2 tricks** – MSB বের করতে।

---

## **Batch–3: Subsets & Advanced Use**

21. **Subset generation with bitmasks** – `for(mask=0; mask < (1<<n); mask++)`।
22. **Check if subset** – `(mask & sub) == sub`।
23. **Gray Code generation** – `i ^ (i>>1)`।
24. **Sum Over Subsets (SOS) DP** – DP over subsets using masks।
25. **Bit compression** – ছোট state-space রাখার জন্য।

---

## **Batch–4: Problem Patterns**

26. **Single number problem** – XOR দিয়ে একটাই element খুঁজে বের করা।
27. **Find two odd occurring numbers** – XOR trick দিয়ে।
28. **Maximum XOR pair** – Trie of bits দিয়ে।
29. **Minimum XOR pair** – sorting + XOR।
30. **Maximum XOR subarray** – prefix XOR + Trie।
31. **Hamming Distance** – দুই সংখ্যা/স্ট্রিং-এর আলাদা বিট গোনা।
32. **Reverse Bits** – 32-bit integer উল্টানো।
33. **Rotate bits (circular shifts)** – cyclic left/right shift।
34. **Parity Check** – মোট set bit odd/even বের করা।
35. **Bitwise sieve tricks** – prime checks এর জন্য।

---

## **Batch–5: Advanced Competitive Programming Tools**

36. **SOS DP (Sum over subsets DP)** – fast DP solution (O(n\*2^n)) → O(2^n \* n)।
37. **FWHT (Fast Walsh-Hadamard Transform)** – XOR/AND/OR convolution।
38. **Bitset optimization** – fast subset sums / knapsack।
39. **Using bitmasks in combinatorics** – n ≤ 20 হলে subset DP।
40. **Applications in Graph** – Traveling Salesman DP, Hamiltonian path।

---



---

## 1) Bitwise AND (`&`)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int a = 13; // 1101
    int b = 10; // 1010
    cout << (a & b) << "\n"; // 1101 & 1010 = 1000 (8)
}
```

**ক্যালকুলেশন:**

```
  1101
& 1010
= 1000  => 8
```

**ব্যবহার:** কোনো বিট দুটোতেই 1 হলে তবেই 1।

---

## 2) Bitwise OR (`|`)

```cpp
int a = 13; // 1101
int b = 10; // 1010
cout << (a | b) << "\n"; // 1111 (15)
```

```
  1101
| 1010
= 1111  => 15
```

---

## 3) Bitwise XOR (`^`)

```cpp
int a = 13; // 1101
int b = 10; // 1010
cout << (a ^ b) << "\n"; // 0111 (7)
```

```
  1101
^ 1010
= 0111  => 7
```

**ব্যবহার:** ভিন্ন হলে 1; সমান হলে 0। (Parity, swap trick ইত্যাদি)

---

## 4) Bitwise NOT (`~`)

```cpp
int x = 5; // ...00000101
cout << (~x) << "\n"; // two's complement: ...11111010 = -6 (on 32-bit)
```

**ব্যাখ্যা:** সব বিট উল্টে দেয়। signed int-এ two’s complement ফলে `~5 = -6`।

---

## 5) Left Shift (`<<`)

```cpp
int x = 7;      // 0000...0111
cout << (x << 1) << "\n"; // 14
cout << (x << 2) << "\n"; // 28
```

**ক্যালকুলেশন:** `x << k` ≈ `x * 2^k` (overflow না হলে)
`7 << 1 = 14`, `7 << 2 = 28`।

---

## 6) Right Shift (`>>`)

```cpp
int x = 19;           // 10011
cout << (x >> 1) << "\n"; // 9
cout << (x >> 2) << "\n"; // 4
```

**ক্যালকুলেশন:** `x >> k` ≈ `floor(x / 2^k)` (signed-এ implementation-defined for negatives)
`19 >> 1 = 9`, `19 >> 2 = 4`।

---

## 7) Odd/Even check: `(n & 1)`

```cpp
int n = 29; // 11101
if(n & 1) cout << "odd\n"; else cout << "even\n"; // odd
```

**কেন কাজ করে:** LSB = 1 ⇒ odd, LSB = 0 ⇒ even।

---

## 8) ×2 / ÷2 via shift

```cpp
int n = 11;
int mul2 = n << 1; // 22
int div2 = n >> 1; // 5
cout << mul2 << " " << div2 << "\n";
```

**ক্যালকুলেশন:** `11<<1 = 22`, `11>>1 = 5` (floor)।

---

## 9) XOR swap (temp ছাড়াই swap)

```cpp
int a = 5, b = 9;
a ^= b; // a = 5^9
b ^= a; // b = 9^(5^9) = 5
a ^= b; // a = (5^9)^5 = 9
cout << a << " " << b << "\n"; // 9 5
```

**নোট:** আধুনিক কম্পাইলারে `std::swap`-ই prefer; তবে ট্রিকটা বুঝতে সুবিধা।

---

## 10) Set a bit: `n | (1<<k)`

```cpp
int n = 10;  // 1010
int k = 1;   // 0-based, LSB=0
int ans = n | (1 << k); // set bit#1 -> stays 1010 (10), already set
k = 0;
ans = n | (1 << k);     // set bit#0 -> 1011 (11)
cout << ans << "\n";
```

**ব্যাখ্যা:** নির্দিষ্ট অবস্থানে 1 বসিয়ে দাও।

---

## 11) Clear a bit: `n & ~(1<<k)`

```cpp
int n = 10;  // 1010
int k = 3;
int ans = n & ~(1 << k); // clear bit#3 -> 0010 (2)
cout << ans << "\n";
```

**ব্যাখ্যা:** `(1<<k)`-এ NOT নিলে ওই বিটে 0, বাকিগুলো 1; AND করলে ওই বিট মুছে যায়।

---

## 12) Toggle (flip) a bit: `n ^ (1<<k)`

```cpp
int n = 10;  // 1010
int k = 1;
int ans = n ^ (1 << k); // flip bit#1 -> 1000 (8)
cout << ans << "\n";
```

**ব্যাখ্যা:** XOR 1 দিলে উল্টে যায়, XOR 0 দিলে একই থাকে:

* 1^1=0 (off), 0^1=1 (on)।

---

### Bonus: 13) Check a bit is set?

```cpp
int n = 10; // 1010
int k = 3;
bool set = (n & (1 << k)) != 0; // true
cout << boolalpha << set << "\n";
```

---

---

## 14) Count set bits — Brian Kernighan’s Algorithm

আইডিয়া: `n &= (n-1)` করলে সবচেয়ে নিচের সেট বিটটা এক ধাপে মুছে যায়। যতবার করতে পারি = কতগুলো 1 ছিল।

```cpp
#include <bits/stdc++.h>
using namespace std;

int countSetBits(unsigned int n) {
    int cnt = 0;
    while (n) {         // যতক্ষণ না 0
        n &= (n - 1);   // lowest set bit remove
        ++cnt;
    }
    return cnt;
}

int main() {
    unsigned int x = 29; // 29 = 11101b → set bits = 4
    cout << countSetBits(x) << "\n"; // 4
}
```

**ক্যালকুলেশন (29 = 11101):**

* `n=11101 → n-1=11100 → n&=n-1 → 11100`
* `11100 → 11011 → 11000`
* `11000 → 10111 → 10000`
* `10000 → 01111 → 00000` → মোট 4 ধাপ ⇒ 4টি সেট বিট।

---

## 15) Check if number is power of 2

আইডিয়া: power of 2 হলে বাইনারিতে একটাই 1 থাকে। তাই `n > 0 && (n & (n-1)) == 0`.

```cpp
#include <bits/stdc++.h>
using namespace std;

bool isPowerOfTwo(unsigned int n) {
    return n > 0 && ( (n & (n - 1)) == 0 );
}

int main() {
    cout << boolalpha;
    cout << isPowerOfTwo(1) << "\n";   // true  (1)
    cout << isPowerOfTwo(16) << "\n";  // true  (10000b)
    cout << isPowerOfTwo(18) << "\n";  // false (10010b)
}
```

---

## 16) Most Significant Bit (MSB) — index/মান বের করা

কয়েকভাবে করা যায়: (i) built-in `__builtin_clz`, (ii) লগ/শিফট করে।

```cpp
#include <bits/stdc++.h>
using namespace std;

// MSB index: highest set bit position (0-based)
int msbIndex(unsigned int n) {
    if (n == 0) return -1;                 // undefined for 0
    return 31 - __builtin_clz(n);          // GCC/Clang: count leading zeros
}

// MSB value: 1 << msbIndex
unsigned int msbValue(unsigned int n) {
    int idx = msbIndex(n);
    return (idx == -1) ? 0u : (1u << idx);
}

int main() {
    unsigned int x = 18; // 10010b, MSB index = 4, value = 1<<4 = 16
    cout << msbIndex(x) << " " << msbValue(x) << "\n"; // 4 16
}
```

**ক্যালকুলেশন (18=10010b):** সবচেয়ে বাম 1 হচ্ছে 2⁴ ⇒ `idx=4`, `value=16`.

> যদি `__builtin_clz` না ব্যবহার করতে চাও, লুপ/শিফট/লগ২ দিয়েও করা যায়।

---

## 17) Least Significant Bit (LSB) — index/মান

LSB মান (mask) বের করা সহজ: `n & -n` (সাইনড টু'স কমপ্লিমেন্টে কাজ করে)। index চাইলে `__builtin_ctz`.

```cpp
#include <bits/stdc++.h>
using namespace std;

int lsbIndex(unsigned int n) {
    if (n == 0) return -1;
    return __builtin_ctz(n);     // count trailing zeros
}

unsigned int lsbValue(unsigned int n) {
    return n & (~n + 1);         // i.e., n & -n
}

int main() {
    unsigned int x = 18; // 10010b, LSB index = 1, value = 2
    cout << lsbIndex(x) << " " << lsbValue(x) << "\n"; // 1 2
}
```

**ক্যালকুলেশন:** `18 & -18 = 10010 & 01110(2’s comp) = 00010 (=2)`।

---

## 18) Extract lowest set bit — `n & -n`

এটা উপরেরটাই—সবচেয়ে নিচের 1-বিটকে আলাদা করে দেয় (mask হিসেবে)।

```cpp
#include <bits/stdc++.h>
using namespace std;

unsigned int lowestSetBitMask(unsigned int n) {
    return n & -n; // same as n & (~n + 1)
}

int main() {
    cout << lowestSetBitMask(12) << "\n"; // 12=1100b → LSB=4 (0100b)
}
```

**ক্যালকুলেশন (12=1100b):** `12 & -12 = 1100 & 0100 = 0100 (=4)`।

---

## 19) Remove lowest set bit — `n & (n-1)`

সবচেয়ে নিচের 1-বিট ক্লিয়ার করা।

```cpp
#include <bits/stdc++.h>
using namespace std;

unsigned int clearLowestSetBit(unsigned int n) {
    return n & (n - 1);
}

int main() {
    cout << clearLowestSetBit(12) << "\n"; // 12=1100b → 1000b (=8)
}
```

**ক্যালকুলেশন:** `1100 & 1011 = 1000 (=8)`।

---

## 20) Bit length / floor(log2(n)) / next power of two

MSB index = `floor(log2(n))`. Built-ins দিয়ে দ্রুত করা যায়।

```cpp
#include <bits/stdc++.h>
using namespace std;

int bitLength(unsigned int n) {          // #bits to represent (without leading zeros)
    if (n == 0) return 0;
    return 32 - __builtin_clz(n);        // e.g., n in [2^(k-1), 2^k - 1] → length k
}

int floorLog2(unsigned int n) {          // = MSB index
    if (n == 0) return -1;
    return 31 - __builtin_clz(n);
}

unsigned int nextPowerOfTwo(unsigned int n) {
    if (n == 0) return 1;
    // if already power of two, return n
    if ((n & (n - 1)) == 0) return n;
    int idx = 31 - __builtin_clz(n);     // MSB index
    return 1u << (idx + 1);
}

int main() {
    cout << bitLength(18) << "\n";       // 18=10010b → length 5
    cout << floorLog2(18) << "\n";       // 4
    cout << nextPowerOfTwo(18) << "\n";  // 32
}
```

**ক্যালকুলেশন:**

* `18` কে দেখাতে 5 বিট লাগে (`10010`) ⇒ `bitLength=5`
* `floorLog2(18) = 4` (কারণ 2⁴ ≤ 18 < 2⁵)
* `nextPowerOfTwo(18) = 32`

---

### ছোট নোটস

* `__builtin_clz`, `__builtin_ctz` GCC/Clang এভেইলেবল; MSVC-এ `_BitScanReverse/Forward`.
* signed/unsigned সাবধানে—bit-tricks সাধারণত **unsigned**-এ করাই নিরাপদ।
* 64-bit চাইলে `__builtin_clzll / ctzll` এবং `unsigned long long` ব্যবহার করো।

---

---

## 21) Subset generation with bitmasks

**আইডিয়া:** `n` আইটেম থাকলে সব সাবসেটের জন্য `mask` 0..(1<\<n)-1 লুপ করলেই হয়। কোনো আইটেম `i` সাবসেটে আছে কি না → `mask & (1<<i)`।

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<string> items = {"A","B","C"};
    int n = items.size();

    for (int mask = 0; mask < (1<<n); ++mask) {
        cout << "{ ";
        for (int i = 0; i < n; ++i) {
            if (mask & (1<<i)) cout << items[i] << " ";
        }
        cout << "}\n";
    }
    return 0;
}
```

**আউটপুট (n=3):**

```
{} {A} {B} {A B} {C} {A C} {B C} {A B C}
```

(ক্রম mask-এর উপর নির্ভর।)

---

## 22) Submask enumeration (একটা mask-এর সব submask)

**আইডিয়া:** কোনো `mask` দেওয়া থাকলে তার সব submask enumerate:

```cpp
for (int sub = mask; ; sub = (sub-1) & mask) {
    // use sub
    if (sub == 0) break;
}
```

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int mask = 0b10110; // উদাহরণ: {1,2,4} সেট (0-based বিট 1,2,4 অন)
    cout << "mask = " << bitset<8>(mask) << "\n";

    cout << "Submasks:\n";
    for (int sub = mask;; sub = (sub - 1) & mask) {
        cout << bitset<8>(sub) << "\n";
        if (sub == 0) break;
    }
    return 0;
}
```

**ব্যাখ্যা:** প্রতিবার `sub = (sub-1)&mask` করলে `sub` `mask`-এর পরবর্তী (ছোট) submask হয়ে যায়; শেষ পর্যন্ত 0-তেও আসে।

---

## 23) Gray Code generation (`i ^ (i>>1)`) + inverse

**আইডিয়া:** Gray code-এ successive সংখ্যাগুলোর বাইনারি রূপে **exactly 1 bit** বদলায়। জেনারেশন: `g = i ^ (i>>1)`।

```cpp
#include <bits/stdc++.h>
using namespace std;

// binary Gray -> binary normal
unsigned grayToBinary(unsigned g) {
    unsigned b = 0;
    for (; g; g >>= 1) b ^= g;
    return b;
}

int main() {
    int n = 3; // 3-bit gray codes: 0..7
    cout << "i  bin(i)  gray  bin(gray)\n";
    for (int i = 0; i < (1<<n); ++i) {
        unsigned g = i ^ (i >> 1);
        cout << setw(2) << i << "  "
             << bitset<3>(i)   << "   "
             << bitset<3>(g)   << "   "
             << bitset<3>(grayToBinary(g)) << "\n";
    }
    return 0;
}
```

**নোট:** `grayToBinary`-তে বারবার XOR করলে MSB→LSB cumulative XOR হয়; এটাতেই inverse কাজ করে।

---

## 24) SOS DP (Sum Over Subsets DP) — বেসিক টেমপ্লেট

**সমস্যা:** `F[mask] = sum of A[sub]` for all `sub ⊆ mask`.
**Naive:** O(3^n).
**SOS DP:** O(n·2^n)। (প্রতিটি বিটের উপর ডিপি চালাই)

```cpp
#include <bits/stdc++.h>
using namespace std;

// SOS DP: F[mask] = sum_{sub ⊆ mask} A[sub]
int main() {
    int n = 3;                      // ছোট ডেমোর জন্য
    int N = 1<<n;
    vector<long long> A(N), F(N);

    // উদাহরণ ভ্যালু
    // mask: 0..7 (000..111)
    for (int m = 0; m < N; ++m) A[m] = m; // A[sub] = sub

    F = A; // শুরুতে F = A
    for (int bit = 0; bit < n; ++bit) {
        for (int mask = 0; mask < N; ++mask) {
            if (mask & (1<<bit)) {
                F[mask] += F[mask ^ (1<<bit)];
            }
        }
    }

    // চেক: F[mask] এখন সব sub ⊆ mask এর A[sub] এর যোগফল
    for (int mask = 0; mask < N; ++mask) {
        cout << "mask " << bitset<3>(mask) << " -> sum = " << F[mask] << "\n";
    }
    return 0;
}
```

**কীভাবে কাজ করে:** প্রতিটি `bit` নিয়ে ভাবুন—যে mask-এ `bit` সেট, সেখানে `bit`-টা আনসেট করা submask-এর F যোগ করে দিই। শেষে F\[mask] তে সাবসেটগুলোর সাম অ্যাকিউমুলেটেড থাকে।

---

## 25) Bit compression (state as a bitmask) — add/remove/check/count

**আইডিয়া:** কোনো subset/state-কে ইনটিজারে কম্প্রেস করা—ফাস্ট চেক/আপডেট।

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int state = 0; // empty set

    auto add = [&](int i){ state |=  (1<<i); }; // আইটেম i যোগ
    auto remove_ = [&](int i){ state &= ~(1<<i); }; // মুছে ফেলা
    auto has = [&](int i){ return (state & (1<<i)) != 0; }; // আছে?
    auto toggle = [&](int i){ state ^= (1<<i); };
    auto countBits = [&](int s){ return __builtin_popcount(s); };

    // ডেমো:
    add(1); add(3); // {1,3}
    cout << "state = " << bitset<8>(state) << "\n"; // 00001010

    cout << "has(3)? " << boolalpha << has(3) << "\n"; // true
    toggle(1); // {3}
    cout << "state = " << bitset<8>(state) << "\n"; // 00001000

    add(0); add(2); // {0,2,3}
    cout << "count = " << countBits(state) << "\n"; // 3

    remove_(3); // {0,2}
    cout << "state = " << bitset<8>(state) << "\n"; // 00000101

    return 0;
}
```

**ব্যবহারক্ষেত্র:**

* Subset DP (যেমন TSP, set cover)
* Constraints/Features অন-অফ রাখা
* দ্রুত membership/check/count (O(1))

---

### ছোট সারাংশ

* **Subset gen:** সব সাবসেট → `mask` লুপ।
* **Submask enum:** `for(sub=mask; ; sub=(sub-1)&mask)`।
* **Gray code:** `g = i ^ (i>>1)` (adjacent 1-bit change), inverseও দেখানো হলো।
* **SOS DP:** `F[mask] += F[mask^(1<<bit)]`—O(n·2^n) এ সব সাবসেট সাম পেয়ে যাই।
* **Bit compression:** add/remove/check/toggle/count—সব O(1)।


---

## 26) Single Number (সবাই জোড়ায়, শুধু একজন বাদে)

👉 সমস্যা: Array-তে সব সংখ্যা ২ বার এসেছে, শুধু ১টা এসেছে একবার। সেটি খুঁজো।
**আইডিয়া:** XOR cancel হয় (x^x=0, 0^y=y)।

```cpp
#include <bits/stdc++.h>
using namespace std;

int singleNumber(vector<int>& nums) {
    int x = 0;
    for (int v : nums) x ^= v;
    return x;
}

int main() {
    vector<int> arr = {2, 3, 5, 4, 5, 3, 4};
    cout << singleNumber(arr) << "\n"; // Output: 2
}
```

**ক্যালকুলেশন:** 2^3^5^4^5^3^4
\= (3^3)^(5^5)^(4^4)^2
\= 0^0^0^2 = 2 ✅

---

## 27) Single Number II (সবাই 3 বার, শুধু একজন বাদে)

👉 সমস্যা: Array-তে সব সংখ্যা ৩ বার এসেছে, শুধু ১টা এসেছে একবার।
**আইডিয়া:** প্রতিটি বিটে কতবার 1 এসেছে count করো; যদি 3 দিয়ে ভাগ করলে রিমেইন্ডার থাকে → সেই বিট সিঙ্গেল নাম্বারে সেট।

```cpp
#include <bits/stdc++.h>
using namespace std;

int singleNumber3(vector<int>& nums) {
    int res = 0;
    for (int bit = 0; bit < 32; bit++) {
        int cnt = 0;
        for (int v : nums) {
            if (v >> bit & 1) cnt++;
        }
        if (cnt % 3) res |= (1 << bit);
    }
    return res;
}

int main() {
    vector<int> arr = {2, 2, 3, 2};
    cout << singleNumber3(arr) << "\n"; // Output: 3
}
```

**ব্যাখ্যা:** bitwise mod 3 কাজ করছে।

---

## 28) Find Two Single Numbers (সবাই 2 বার, শুধু 2 জন একবার)

👉 সমস্যা: Array-তে সব সংখ্যা ২ বার এসেছে, শুধু ২টা সংখ্যা একবার এসেছে।

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> twoSingles(vector<int>& nums) {
    int xorsum = 0;
    for (int v : nums) xorsum ^= v;

    int diff = xorsum & -xorsum; // lowest set bit
    int a = 0, b = 0;
    for (int v : nums) {
        if (v & diff) a ^= v; else b ^= v;
    }
    return {a, b};
}

int main() {
    vector<int> arr = {1,2,1,3,2,5};
    auto ans = twoSingles(arr);
    cout << ans[0] << " " << ans[1] << "\n"; // 3 5
}
```

**ব্যাখ্যা:** `xorsum=a^b`. তার কোনো এক বিট `diff`. সেই বিট দিয়ে আলাদা করলে দুই গ্রুপে ভাগ হয়।

---

## 29) Maximum XOR Pair

👉 সমস্যা: Array-র দুই এলিমেন্ট নিয়ে ম্যাক্স XOR বের করো।
**আইডিয়া:** Trie (bitwise trie)।

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Trie {
    Trie* child[2]{};
};

void insert(Trie* root, int num) {
    for (int i = 31; i >= 0; i--) {
        int bit = (num >> i) & 1;
        if (!root->child[bit]) root->child[bit] = new Trie();
        root = root->child[bit];
    }
}

int query(Trie* root, int num) {
    int ans = 0;
    for (int i = 31; i >= 0; i--) {
        int bit = (num >> i) & 1;
        int want = 1 - bit;
        if (root->child[want]) {
            ans |= (1 << i);
            root = root->child[want];
        } else {
            root = root->child[bit];
        }
    }
    return ans;
}

int maxXor(vector<int>& nums) {
    Trie* root = new Trie();
    for (int v : nums) insert(root, v);
    int ans = 0;
    for (int v : nums) ans = max(ans, query(root, v));
    return ans;
}

int main() {
    vector<int> arr = {3,10,5,25,2,8};
    cout << maxXor(arr) << "\n"; // 28 (5^25)
}
```

---

## 30) Hamming Distance

👉 সমস্যা: দুটি সংখ্যার মধ্যে কতগুলো বিট আলাদা সেটি।
**আইডিয়া:** `x ^ y` করলে আলাদা বিটগুলো 1 হয়, তারপর popcount।

```cpp
#include <bits/stdc++.h>
using namespace std;

int hammingDistance(int x, int y) {
    return __builtin_popcount(x ^ y);
}

int main() {
    cout << hammingDistance(1, 4) << "\n"; // 1=001, 4=100 → diff=2 bits
}
```

---

## 31) Reverse Bits

👉 সমস্যা: 32-bit unsigned int-এর বিট উল্টে দাও।

```cpp
#include <bits/stdc++.h>
using namespace std;

uint32_t reverseBits(uint32_t n) {
    uint32_t res = 0;
    for (int i = 0; i < 32; i++) {
        res = (res << 1) | (n & 1);
        n >>= 1;
    }
    return res;
}

int main() {
    uint32_t x = 13; // 0000...1101
    cout << reverseBits(x) << "\n"; // reversed int
}
```

---

## 32) Rotate Bits (Left/Right)

👉 সমস্যা: n-bit সংখ্যা k ধাপে rotate করা।

```cpp
#include <bits/stdc++.h>
using namespace std;

unsigned int rol(unsigned int n, int k, int bits=32) {
    return (n << k) | (n >> (bits - k));
}

unsigned int ror(unsigned int n, int k, int bits=32) {
    return (n >> k) | (n << (bits - k));
}

int main() {
    unsigned int x = 0b1001; // 9
    cout << bitset<8>(rol(x, 1, 4)) << "\n"; // left rotate by 1: 0011
    cout << bitset<8>(ror(x, 1, 4)) << "\n"; // right rotate by 1: 1100
}
```

---


---

## **36. SOS DP (Sum over Subsets DP)**

👉 আইডিয়া:
ধরি `F[mask] = sum of A[sub] for all sub ⊆ mask`
Naive: O(3^n), কিন্তু **SOS DP** দিয়ে → O(n·2^n)।

```cpp
#include <bits/stdc++.h>
using namespace std;

// SOS DP Example
int main() {
    int n = 3; // ছোট উদাহরণ
    int N = 1 << n;
    vector<int> A(N), F(N);

    // A[sub] ইনিশিয়ালাইজ (যেমন sub নিজেকেই ধরলাম)
    for (int mask = 0; mask < N; mask++) A[mask] = mask;

    F = A; 
    for (int bit = 0; bit < n; bit++) {
        for (int mask = 0; mask < N; mask++) {
            if (mask & (1 << bit)) {
                F[mask] += F[mask ^ (1 << bit)];
            }
        }
    }

    for (int mask = 0; mask < N; mask++) {
        cout << "mask " << bitset<3>(mask) << " → sum = " << F[mask] << "\n";
    }
}
```

✅ ব্যাখ্যা:

* প্রতিটি `mask` তার সাবসেটের সাম রিকারসিভলি জমা করে।
* এই টেকনিক ইউজ হয় `subset DP`, inclusion-exclusion ইত্যাদিতে।

---

## **37. FWHT (Fast Walsh-Hadamard Transform)**

👉 আইডিয়া:
FFT-এর মত, কিন্তু **XOR/AND/OR convolution** করতে লাগে।
**XOR convolution:** `(f*g)[i] = sum f[a]*g[b] যেখানে (a^b)=i`।

```cpp
#include <bits/stdc++.h>
using namespace std;

void fwht(vector<int>& a, bool invert) {
    int n = a.size();
    for (int len = 1; 2*len <= n; len <<= 1) {
        for (int i = 0; i < n; i += 2*len) {
            for (int j = 0; j < len; j++) {
                int u = a[i+j], v = a[i+len+j];
                a[i+j] = u+v;
                a[i+len+j] = u-v;
            }
        }
    }
    if (invert) {
        for (int &x : a) x /= n;
    }
}

int main() {
    int n = 2; // 2^n size
    vector<int> A = {1,2,3,4}; // length 4
    vector<int> B = {4,3,2,1};

    fwht(A, false);
    fwht(B, false);
    for (int i = 0; i < A.size(); i++) A[i] *= B[i];
    fwht(A, true);

    cout << "XOR convolution: ";
    for (int x : A) cout << x << " ";
}
```

✅ ব্যাখ্যা:

* FWHT FFT-এর মত ট্রান্সফর্ম, কিন্তু basis = Hadamard।
* Applications: XOR subset convolution, polynomial ops।

---

## **38. Bitset optimization**

👉 আইডিয়া:
`std::bitset` বা `__builtin_popcount` দিয়ে **knapsack / subset sum** অনেক ফাস্ট হয়।

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int W = 10;
    vector<int> items = {3, 4, 7};
    bitset<100> dp;
    dp[0] = 1;

    for (int w : items) {
        dp |= (dp << w);
    }
    cout << "Subset sums possible up to 10: ";
    for (int i = 0; i <= W; i++) if (dp[i]) cout << i << " ";
}
```

✅ ব্যাখ্যা:

* Shift মানে **একটি আইটেম যোগ করা**।
* `dp |= (dp << w)` → সব পুরানো sum-এ `w` যোগ হয়।

---

## **39. Using Bitmasks in Combinatorics (n ≤ 20)**

👉 ছোট n হলে (n ≤ 20) সব সাবসেট (2^n) লুপ করে DP করা যায়।

উদাহরণ: **Count subsets whose sum ≤ K**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> arr = {2, 4, 5};
    int n = arr.size(), K = 6;
    int cnt = 0;

    for (int mask = 0; mask < (1<<n); mask++) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (mask & (1<<i)) sum += arr[i];
        }
        if (sum <= K) cnt++;
    }
    cout << "Valid subsets = " << cnt << "\n";
}
```

✅ ব্যাখ্যা:

* প্রত্যেক সাবসেটকে mask দিয়ে encode করে iterate।
* ছোট n হলে brute force OK, বড় n হলে SOS/FWHT দরকার।

---

## **40. Applications in Graph – Traveling Salesman DP**

👉 বিখ্যাত `TSP DP with bitmask`:
`dp[mask][i] = min cost to visit all nodes in mask, ending at i`।

```cpp
#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;

int main() {
    int n = 4; // nodes
    vector<vector<int>> cost = {
        {0, 20, 42, 35},
        {20, 0, 30, 34},
        {42, 30, 0, 12},
        {35, 34, 12, 0}
    };

    int N = 1<<n;
    vector<vector<int>> dp(N, vector<int>(n, INF));
    dp[1][0] = 0; // start at 0

    for (int mask = 1; mask < N; mask++) {
        for (int u = 0; u < n; u++) if (mask & (1<<u)) {
            for (int v = 0; v < n; v++) if (!(mask & (1<<v))) {
                dp[mask|1<<v][v] = min(dp[mask|1<<v][v], dp[mask][u] + cost[u][v]);
            }
        }
    }

    int ans = INF;
    for (int u = 1; u < n; u++) {
        ans = min(ans, dp[N-1][u] + cost[u][0]);
    }
    cout << "TSP cost = " << ans << "\n";
}
```

✅ ব্যাখ্যা:

* State = `(mask, u)`
* Transition: অন্য node যোগ করা
* Complexity: O(n·2^n)

---

### 🔑 Batch–5 সারাংশ

* **36 SOS DP** → সাবসেট সাম দ্রুত করা
* **37 FWHT** → XOR/AND/OR convolution
* **38 Bitset** → knapsack/subset sum ফাস্ট
* **39 Combinatorics with mask** → brute force when n ≤ 20
* **40 Graph DP** → TSP/Hamiltonian path in O(n·2^n)

---

---

# 🔑 Bitmask Operations

## 1. **Check if the i-th bit is set**

👉 `(mask >> i) & 1`

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int mask = 42; // 42 = 101010 (binary)
    int i = 3;
    cout << ((mask >> i) & 1) << "\n"; 
}
```

**ক্যালকুলেশন:**
42 = `101010`₂
bit(3) = 1 (কারণ ডান থেকে 0-index)

---

## 2. **Set the i-th bit**

👉 `mask | (1 << i)`

```cpp
int mask = 5;   // 0101
int i = 2;
mask = mask | (1 << i);  
cout << mask;  // 0101 | 0100 = 0111 = 7
```

---

## 3. **Clear the i-th bit**

👉 `mask & ~(1 << i)`

```cpp
int mask = 13;  // 1101
int i = 2;
mask = mask & ~(1 << i); 
cout << mask;  // 1101 & 1011 = 1001 = 9
```

---

## 4. **Toggle the i-th bit**

👉 `mask ^ (1 << i)`

```cpp
int mask = 9;   // 1001
int i = 0;
mask = mask ^ (1 << i); 
cout << mask;  // 1001 ^ 0001 = 1000 = 8
```

---

## 5. **Check if a number is power of two**

👉 `(n > 0 && (n & (n-1)) == 0)`

```cpp
int n = 16;
cout << ((n > 0 && (n & (n-1)) == 0) ? "YES":"NO"); 
// 16=10000, 15=01111 → 10000 & 01111 = 0 ✅
```

---

## 6. **Get lowest set bit (LSB)**

👉 `n & -n`

```cpp
int n = 12;  // 1100
cout << (n & -n);  
```

**ক্যালকুলেশন:**
12 = `1100`
-12 = 2’s complement = `0100`
`1100 & 0100 = 0100 = 4` ✅

---

## 7. **Remove lowest set bit**

👉 `n & (n-1)`

```cpp
int n = 12;  // 1100
cout << (n & (n-1));  
```

**ক্যালকুলেশন:**
12 = `1100`
11 = `1011`
`1100 & 1011 = 1000 = 8` ✅

---

## 8. **Count set bits (population count)**

👉 `__builtin_popcount(n)`

```cpp
int n = 29;  // 11101
cout << __builtin_popcount(n); // 4
```

---

✅ এগুলোই বেসিক **Bitmask Operations**

* Check, Set, Clear, Toggle
* Power of 2
* LSB extract/remove
* Count bits

---



---

## **1. Initialization**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    bitset<8> b1(string("10110010"));  // binary string দিয়ে init
    bitset<8> b2(42);                  // integer দিয়ে init (42 = 00101010)

    cout << "b1 = " << b1 << "\n";
    cout << "b2 = " << b2 << "\n";
}
```

📌 **Explanation:**

* `bitset<8>` → 8 বিটের fixed size array
* `b1` = `"10110010"`
* `b2(42)` → 42 এর binary `00101010`

---

## **2. Access & Modify Bits**

```cpp
bitset<8> b("10110010");

cout << b[0] << "\n";  // LSB check (0th bit = 0)

b.set(0);   // 0th bit set → 10110011
b.reset(1); // 1st bit clear → 10110001
b.flip(2);  // 2nd bit toggle → 10110101

cout << b << "\n";
```

📌 **Explanation:**

* `.set(i)` → i-th bit = 1
* `.reset(i)` → i-th bit = 0
* `.flip(i)` → i-th bit toggle (0→1, 1→0)

---

## **3. Bitwise Operations**

```cpp
bitset<8> b1(string("10110101"));
bitset<8> b2(string("00101010"));

cout << (b1 & b2) << "\n"; // AND → 00100000
cout << (b1 | b2) << "\n"; // OR  → 10111111
cout << (b1 ^ b2) << "\n"; // XOR → 10011111
cout << (~b1) << "\n";     // NOT → 01001010
```

📌 **Explanation:**

* AND → common 1-bit রাখে
* OR  → যেকোনো 1 হলে 1
* XOR → আলাদা হলে 1
* `~`  → সব বিট উল্টে দেয়

---

## **4. Shifts**

```cpp
bitset<8> b(string("10110101"));

cout << (b << 2) << "\n"; // Left shift 2 → 11010100
cout << (b >> 1) << "\n"; // Right shift 1 → 01011010
```

📌 **Explanation:**

* Left shift → 2 জায়গা বামে যাবে, ডানে 0 আসবে
* Right shift → 1 জায়গা ডানে যাবে, বামে 0 আসবে

---

## **5. Utility Functions**

```cpp
bitset<8> b(string("10110101"));

cout << b.count() << "\n";  // 1 এর সংখ্যা = 5
cout << b.any() << "\n";    // কোনো bit set আছে? (1) → true
cout << b.all() << "\n";    // সব bit set আছে? (0) → false
cout << b.none() << "\n";   // কোনো bit set নাই? (0) → false
```

📌 **Explanation:**

* `.count()` → কয়টা 1 আছে
* `.any()` → অন্তত 1টা 1 আছে কিনা
* `.all()` → সবগুলো 1 কিনা
* `.none()` → কোনো 1 নাই কিনা

---

## **6. Conversion**

```cpp
bitset<8> b(42); // 00101010

cout << b.to_ulong() << "\n"; // integer → 42
cout << b.to_string() << "\n"; // string → "00101010"
```

📌 **Explanation:**

* `.to_ulong()` → decimal number
* `.to_string()` → binary string

---








