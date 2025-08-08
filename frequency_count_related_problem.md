
---

## **LeetCode (10 problems)**

| #  | Problem Title                                                  | Link                                                                                                      |
| -- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| 1  | Top K Frequent Elements                                        | [🔗 Click](https://leetcode.com/problems/top-k-frequent-elements/)                                        |
| 2  | Count Elements With Maximum Frequency                          | [🔗 Click](https://leetcode.com/problems/count-elements-with-maximum-frequency/)                          |
| 3  | Sort Array by Increasing Frequency                             | [🔗 Click](https://leetcode.com/problems/sort-array-by-increasing-frequency/)                             |
| 4  | Frequency of the Most Frequent Element                         | [🔗 Click](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)                         |
| 5  | Range Frequency Queries                                        | [🔗 Click](https://leetcode.com/problems/range-frequency-queries/)                                        |
| 6  | Most Frequent Number Following Key in an Array                 | [🔗 Click](https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/)                 |
| 7  | Count Substrings With K-Frequency Characters I                 | [🔗 Click](https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/)                 |
| 8  | Apply Operations to Maximize Frequency Score                   | [🔗 Click](https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/)                   |
| 9  | Maximum Frequency of an Element After Performing Operations II | [🔗 Click](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/) |
| 10 | Find Occurrences of an Element in an Array                     | [🔗 Click](https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/)                     |

---

## **Codeforces (10 problems)**

| #  | Problem Title                                          | Link                                                        |
| -- | ------------------------------------------------------ | ----------------------------------------------------------- |
| 1  | Petya and Strings (Frequency concept)                  | [🔗 Click](https://codeforces.com/problemset/problem/112/A) |
| 2  | Boy or Girl (Unique char frequency)                    | [🔗 Click](https://codeforces.com/problemset/problem/236/A) |
| 3  | Helpful Maths (Digit frequency sorting)                | [🔗 Click](https://codeforces.com/problemset/problem/339/A) |
| 4  | Pangram (Check letter frequency)                       | [🔗 Click](https://codeforces.com/problemset/problem/520/A) |
| 5  | Games (Matching color frequency)                       | [🔗 Click](https://codeforces.com/problemset/problem/268/A) |
| 6  | Word (Upper vs lower frequency)                        | [🔗 Click](https://codeforces.com/problemset/problem/59/A)  |
| 7  | Is your horseshoe on the other hoof? (Duplicate count) | [🔗 Click](https://codeforces.com/problemset/problem/228/A) |
| 8  | Anton and Letters (Unique frequency)                   | [🔗 Click](https://codeforces.com/problemset/problem/443/A) |
| 9  | Chat room (Subsequence frequency check)                | [🔗 Click](https://codeforces.com/problemset/problem/58/A)  |
| 10 | Dubstep (Rebuild frequency of words)                   | [🔗 Click](https://codeforces.com/problemset/problem/208/A) |

---

## **CodeChef (10 problems)**

| #  | Problem Title                                    | Link                                                                               |
| -- | ------------------------------------------------ | ---------------------------------------------------------------------------------- |
| 1  | Frequency of Each Element in the Array (Hashing) | [🔗 Click](https://www.codechef.com/learn/course/hashing/HASH01/problems/DSAAGP35) |
| 2  | Using Hashing to Optimize Counting Frequency     | [🔗 Click](https://www.codechef.com/learn/course/hashing/HASH01/problems/DSAAGP34) |
| 3  | Frequency of Elements Using Hashing              | [🔗 Click](https://www.codechef.com/learn/course/hashing/HASH01/problems/DSAAGP36) |
| 4  | Distinct Codes                                   | [🔗 Click](https://www.codechef.com/problems/DISTCODE)                             |
| 5  | Chef and Subarrays                               | [🔗 Click](https://www.codechef.com/problems/CHEFARRP)                             |
| 6  | Lapindromes                                      | [🔗 Click](https://www.codechef.com/problems/LAPIN)                                |
| 7  | Most Frequent                                    | [🔗 Click](https://www.codechef.com/problems/MOSTFREQ)                             |
| 8  | Clean the Sequence                               | [🔗 Click](https://www.codechef.com/problems/CLEANSEQ)                             |
| 9  | Count the Holidays                               | [🔗 Click](https://www.codechef.com/problems/HOLIDAYS)                             |
| 10 | Counting Words                                   | [🔗 Click](https://www.codechef.com/problems/WORDCNT)                              |

---


---

## **LeetCode (10)** — টেমপ্লেট ও হিন্ট

1. **Top K Frequent Elements**
   **Hint:** array-র প্রতিটি element এর frequency count করুন, তারপর সবচেয়ে বেশি frequency এর `k` টা element return করুন।

   ```cpp
   class Solution {
   public:
       vector<int> topKFrequent(vector<int>& nums, int k) {
           // TODO: frequency count + top k extraction
       }
   };
   ```

2. **Count Elements With Maximum Frequency**
   **Hint:** max frequency বের করুন, তারপর যত element এর frequency == max, তাদের frequency যোগ করুন।

   ```cpp
   class Solution {
   public:
       int maxFrequencyElements(vector<int>& nums) {
           // TODO
       }
   };
   ```

3. **Sort Array by Increasing Frequency**
   **Hint:** frequency অনুযায়ী sort করুন (asc), frequency same হলে value desc।

   ```cpp
   class Solution {
   public:
       vector<int> frequencySort(vector<int>& nums) {
           // TODO
       }
   };
   ```

4. **Frequency of the Most Frequent Element**
   **Hint:** sort + sliding window দিয়ে check করুন কতগুলো element equal করতে পারবেন `k` operations এ।

   ```cpp
   class Solution {
   public:
       int maxFrequency(vector<int>& nums, int k) {
           // TODO
       }
   };
   ```

5. **Range Frequency Queries**
   **Hint:** preprocess করে value→index list রাখুন, query তে binary search দিয়ে range এর count বের করুন।

   ```cpp
   class RangeFreqQuery {
   public:
       RangeFreqQuery(vector<int>& arr) {
           // TODO
       }
       int query(int left, int right, int value) {
           // TODO
       }
   };
   ```

6. **Most Frequent Number Following Key in an Array**
   **Hint:** array traverse করে key এর পরের value এর frequency count করুন, max return করুন।

   ```cpp
   class Solution {
   public:
       int mostFrequent(vector<int>& nums, int key) {
           // TODO
       }
   };
   ```

7. **Count Substrings With K-Frequency Characters I**
   **Hint:** sliding window + count array, যখন কোনো char-এর count ≥ k হয়, তখন substring count করুন।

   ```cpp
   class Solution {
   public:
       long long numberOfSubstrings(string s, int k) {
           // TODO
       }
   };
   ```

8. **Apply Operations to Maximize Frequency Score**
   **Hint:** sort + prefix sum + median ভিত্তিক cost calculation দিয়ে max window বের করুন।

   ```cpp
   class Solution {
   public:
       int maxFrequencyScore(vector<int>& nums, long long k) {
           // TODO
       }
   };
   ```

9. **Maximum Frequency of an Element After Performing Operations II**
   **Hint:** sweep line করে দেখুন কত element target-এ আনতে পারবেন k distance এর মধ্যে।

   ```cpp
   class Solution {
   public:
       int maxFrequency(vector<int>& nums, int k, int numOperations) {
           // TODO
       }
   };
   ```

10. **Find Occurrences of an Element in an Array**
    **Hint:** value এর সব index store করুন, query তে kth index return করুন বা -1 দিন।

    ```cpp
    class Solution {
    public:
        vector<int> occurrencesOfElement(vector<int>& nums, vector<int>& queries, int x) {
            // TODO
        }
    };
    ```

---

## **Codeforces (10)** — টেমপ্লেট ও হিন্ট

1. **Petya and Strings**
   **Hint:** case-insensitive comparison করুন।

   ```cpp
   int main(){
       // TODO
   }
   ```

2. **Boy or Girl**
   **Hint:** unique characters count করুন, odd হলে ignore him, even হলে chat with her।

   ```cpp
   int main(){
       // TODO
   }
   ```

3. **Helpful Maths**
   **Hint:** সংখ্যা আলাদা করে sort করুন, '+' দিয়ে join করুন।

   ```cpp
   int main(){
       // TODO
   }
   ```

4. **Pangram**
   **Hint:** সব alphabet এসেছে কিনা check করুন।

   ```cpp
   int main(){
       // TODO
   }
   ```

5. **Games**
   **Hint:** home jersey color == away jersey color হলে count++।

   ```cpp
   int main(){
       // TODO
   }
   ```

6. **Word**
   **Hint:** uppercase বেশি হলে সব upper করুন, নাহলে সব lower।

   ```cpp
   int main(){
       // TODO
   }
   ```

7. **Is your horseshoe on the other hoof?**
   **Hint:** set size ব্যবহার করে missing horseshoe count করুন।

   ```cpp
   int main(){
       // TODO
   }
   ```

8. **Anton and Letters**
   **Hint:** string এর unique lowercase letter count করুন।

   ```cpp
   int main(){
       // TODO
   }
   ```

9. **Chat room**
   **Hint:** "hello" subsequence আছে কিনা দেখুন।

   ```cpp
   int main(){
       // TODO
   }
   ```

10. **Dubstep**
    **Hint:** "WUB" মুছে দিয়ে বাকি শব্দ print করুন।

    ```cpp
    int main(){
        // TODO
    }
    ```

---

## **CodeChef (10)** — টেমপ্লেট ও হিন্ট

1. **Frequency of Each Element in the Array**
   **Hint:** map/unordered\_map ব্যবহার করে count করুন।

   ```cpp
   int main(){
       // TODO
   }
   ```

2. **Using Hashing to Optimize Counting Frequency**
   **Hint:** hash map store করে queries এর উত্তর দিন।

   ```cpp
   int main(){
       // TODO
   }
   ```

3. **Frequency of Elements Using Hashing**
   **Hint:** sorted order এ frequency print করুন।

   ```cpp
   int main(){
       // TODO
   }
   ```

4. **Distinct Codes**
   **Hint:** string এর সব 2-length substring unique করে count করুন।

   ```cpp
   int main(){
       // TODO
   }
   ```

5. **Chef and Subarrays**
   **Hint:** subarray এর sum==product হলে count++।

   ```cpp
   int main(){
       // TODO
   }
   ```

6. **Lapindromes**
   **Hint:** string এর দুই ভাগ sort করে compare করুন।

   ```cpp
   int main(){
       // TODO
   }
   ```

7. **Most Frequent**
   **Hint:** সর্বোচ্চ frequency এর element বের করুন, tie হলে ছোট number নিন।

   ```cpp
   int main(){
       // TODO
   }
   ```

8. **Clean the Sequence**
   **Hint:** consecutive duplicates remove করুন।

   ```cpp
   int main(){
       // TODO
   }
   ```

9. **Count the Holidays**
   **Hint:** set ব্যবহার করে weekend বাদ দিয়ে unique days count করুন।

   ```cpp
   int main(){
       // TODO
   }
   ```

10. **Counting Words**
    **Hint:** stringstream দিয়ে space-separated words count করুন।

    ```cpp
    int main(){
        // TODO
    }
    ```

---


