

```cpp
#include <iostream>
using namespace std;

int main() {
    float weight, height, bmi;

    // Input weight in kilograms
    cout << "Enter your weight in kilograms: ";
    cin >> weight;

    // Input height in meters
    cout << "Enter your height in meters: ";
    cin >> height;

    // Calculate BMI
    bmi = weight / (height * height);

    // Display BMI
    cout << "Your BMI is: " << bmi << endl;

    // Determine category
    if (bmi < 18.5)
        cout << "Category: Underweight" << endl;
    else if (bmi >= 18.5 && bmi < 24.9)
        cout << "Category: Normal weight" << endl;
    else if (bmi >= 25 && bmi < 29.9)
        cout << "Category: Overweight" << endl;
    else
        cout << "Category: Obese" << endl;

    return 0;
}
```

### 💡 How it works:

* The program asks the user to input **weight in kilograms** and **height in meters**.
* It calculates BMI using the formula:

  $$
  \text{BMI} = \frac{\text{weight}}{\text{height}^2}
  $$
* Then, it classifies the result based on standard BMI categories.

### ✅ Example:

If you input:

* Weight: 70 kg
* Height: 1.75 m

Output:

```
Your BMI is: 22.8571
Category: Normal weight
```


