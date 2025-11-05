import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from models import Topic, Question
from datetime import datetime

def populate_questions():
    with app.app_context():
        print("Starting to populate questions...")
        
        # Questions data organized by topic
        questions_data: dict = {
            "Basic Declarations": [
                {
                    "question": "Write a C program to print 'Hello, World!'",
                    "answer": "#include <stdio.h>\n\nint main() {\n    printf(\"Hello, World!\\n\");\n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to declare and initialize variables of different data types",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int age = 25;\n    float salary = 50000.50;\n    char grade = 'A';\n    double pi = 3.14159;\n    \n    printf(\"Age: %d\\n\", age);\n    printf(\"Salary: %.2f\\n\", salary);\n    printf(\"Grade: %c\\n\", grade);\n    printf(\"PI: %.5f\\n\", pi);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate arithmetic operations",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int a = 10, b = 3;\n    \n    printf(\"a + b = %d\\n\", a + b);\n    printf(\"a - b = %d\\n\", a - b);\n    printf(\"a * b = %d\\n\", a * b);\n    printf(\"a / b = %d\\n\", a / b);\n    printf(\"a %% b = %d\\n\", a % b);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to find the size of different data types",
                    "answer": "#include <stdio.h>\n\nint main() {\n    printf(\"Size of int: %zu bytes\\n\", sizeof(int));\n    printf(\"Size of float: %zu bytes\\n\", sizeof(float));\n    printf(\"Size of char: %zu bytes\\n\", sizeof(char));\n    printf(\"Size of double: %zu bytes\\n\", sizeof(double));\n    printf(\"Size of long: %zu bytes\\n\", sizeof(long));\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate type casting",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int a = 10, b = 3;\n    float result;\n    \n    result = (float)a / b;  // Explicit type casting\n    printf(\"Result with casting: %.2f\\n\", result);\n    \n    result = a / b;  // Without casting\n    printf(\"Result without casting: %.2f\\n\", result);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to use const keyword",
                    "answer": "#include <stdio.h>\n\nint main() {\n    const float PI = 3.14159;\n    const int MAX_SIZE = 100;\n    \n    float radius = 5.0;\n    float area = PI * radius * radius;\n    \n    printf(\"Area of circle: %.2f\\n\", area);\n    printf(\"Max size: %d\\n\", MAX_SIZE);\n    \n    // PI = 3.14;  // This would cause error - const cannot be modified\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate enum data type",
                    "answer": "#include <stdio.h>\n\nenum Days {MON, TUE, WED, THU, FRI, SAT, SUN};\n\nint main() {\n    enum Days today = WED;\n    \n    printf(\"Today is day number: %d\\n\", today);\n    \n    if(today == SAT || today == SUN) {\n        printf(\"It's weekend!\\n\");\n    } else {\n        printf(\"It's a weekday\\n\");\n    }\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to use typedef keyword",
                    "answer": "#include <stdio.h>\n\ntypedef int Integer;\ntypedef float Decimal;\n\ntypedef struct {\n    int x;\n    int y;\n} Point;\n\nint main() {\n    Integer a = 10;\n    Decimal b = 3.14;\n    Point p1 = {5, 10};\n    \n    printf(\"Integer value: %d\\n\", a);\n    printf(\"Decimal value: %.2f\\n\", b);\n    printf(\"Point coordinates: (%d, %d)\\n\", p1.x, p1.y);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate variable scope",
                    "answer": "#include <stdio.h>\n\nint global_var = 100;  // Global variable\n\nvoid test_function() {\n    int local_var = 50;  // Local variable\n    printf(\"Inside function - local_var: %d\\n\", local_var);\n    printf(\"Inside function - global_var: %d\\n\", global_var);\n}\n\nint main() {\n    int local_var = 20;  // Local to main\n    \n    printf(\"In main - local_var: %d\\n\", local_var);\n    printf(\"In main - global_var: %d\\n\", global_var);\n    \n    test_function();\n    \n    // printf(\"%d\", local_var from test_function); // Error - not accessible\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate static variables",
                    "answer": "#include <stdio.h>\n\nvoid counter() {\n    static int count = 0;  // Static variable retains value\n    count++;\n    printf(\"Function called %d times\\n\", count);\n}\n\nint main() {\n    counter();\n    counter();\n    counter();\n    counter();\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                }
            ],
            
            "Variables": [
                {
                    "question": "Write a program to swap two numbers using a temporary variable",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int a = 5, b = 10, temp;\n    \n    printf(\"Before swap: a = %d, b = %d\\n\", a, b);\n    \n    temp = a;\n    a = b;\n    b = temp;\n    \n    printf(\"After swap: a = %d, b = %d\\n\", a, b);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to swap two numbers without using a temporary variable",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int a = 5, b = 10;\n    \n    printf(\"Before swap: a = %d, b = %d\\n\", a, b);\n    \n    a = a + b;\n    b = a - b;\n    a = a - b;\n    \n    printf(\"After swap: a = %d, b = %d\\n\", a, b);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate local and global variables",
                    "answer": "#include <stdio.h>\n\nint global = 100;  // Global variable\n\nvoid test() {\n    int local = 50;  // Local variable\n    printf(\"Inside test - local: %d, global: %d\\n\", local, global);\n    global++;  // Modifying global variable\n}\n\nint main() {\n    int local = 10;  // Local to main\n    \n    printf(\"In main - local: %d, global: %d\\n\", local, global);\n    test();\n    printf(\"After test - local: %d, global: %d\\n\", local, global);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate automatic and static variables",
                    "answer": "#include <stdio.h>\n\nvoid test() {\n    auto int auto_var = 0;  // Automatic (default)\n    static int static_var = 0;  // Static\n    \n    auto_var++;\n    static_var++;\n    \n    printf(\"Auto: %d, Static: %d\\n\", auto_var, static_var);\n}\n\nint main() {\n    test();\n    test();\n    test();\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate register variables",
                    "answer": "#include <stdio.h>\n\nint main() {\n    register int i;  // Register variable for fast access\n    int sum = 0;\n    \n    for(i = 1; i <= 100; i++) {\n        sum += i;\n    }\n    \n    printf(\"Sum of first 100 numbers: %d\\n\", sum);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate volatile variables",
                    "answer": "#include <stdio.h>\n\nint main() {\n    volatile int sensor_value = 0;  // Volatile - can change unexpectedly\n    \n    // Simulating sensor reading that might change due to external factors\n    for(int i = 0; i < 5; i++) {\n        printf(\"Sensor reading: %d\\n\", sensor_value);\n        // In real scenario, sensor_value might be modified by hardware\n    }\n    \n    return 0;\n}",
                    "difficulty": "Medium"
                },
                {
                    "question": "Write a program to demonstrate external variables",
                    "answer": "#include <stdio.h>\n\nextern int external_var;  // Declare external variable\n\nvoid display() {\n    printf(\"External variable value: %d\\n\", external_var);\n}\n\nint main() {\n    display();\n    return 0;\n}\n\n// This would typically be in another file\nint external_var = 100;",
                    "difficulty": "Medium"
                },
                {
                    "question": "Write a program to demonstrate variable initialization",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int a;  // Uninitialized - contains garbage value\n    int b = 10;  // Initialized\n    int c = b * 2;  // Initialized with expression\n    \n    printf(\"a (uninitialized): %d\\n\", a);\n    printf(\"b: %d\\n\", b);\n    printf(\"c: %d\\n\", c);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate constant variables",
                    "answer": "#include <stdio.h>\n\nint main() {\n    const int MAX_SIZE = 100;\n    const float PI = 3.14159;\n    const char NEWLINE = '\\n';\n    \n    printf(\"Max size: %d%c\", MAX_SIZE, NEWLINE);\n    printf(\"PI value: %.5f%c\", PI, NEWLINE);\n    \n    // MAX_SIZE = 200;  // This would cause compilation error\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate variable naming conventions",
                    "answer": "#include <stdio.h>\n\nint main() {\n    // Valid variable names\n    int age;\n    float salary_amount;\n    char first_name;\n    double _temp;\n    int num1;\n    \n    // Invalid variable names (commented out)\n    // int 1number;  // Cannot start with digit\n    // float salary-amount;  // Cannot contain hyphen\n    // char first name;  // Cannot contain space\n    // int return;  // Cannot use keyword\n    \n    age = 25;\n    salary_amount = 50000.50;\n    first_name = 'A';\n    _temp = 98.6;\n    num1 = 100;\n    \n    printf(\"Age: %d\\n\", age);\n    printf(\"Salary: %.2f\\n\", salary_amount);\n    printf(\"First name initial: %c\\n\", first_name);\n    printf(\"Temperature: %.1f\\n\", _temp);\n    printf(\"Number: %d\\n\", num1);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                }
            ],
            
            "Loops": [
                {
                    "question": "Write a program to print numbers from 1 to 10 using for loop",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int i;\n    \n    printf(\"Numbers from 1 to 10:\\n\");\n    for(i = 1; i <= 10; i++) {\n        printf(\"%d \", i);\n    }\n    printf(\"\\n\");\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to print numbers from 1 to 10 using while loop",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int i = 1;\n    \n    printf(\"Numbers from 1 to 10:\\n\");\n    while(i <= 10) {\n        printf(\"%d \", i);\n        i++;\n    }\n    printf(\"\\n\");\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to print numbers from 1 to 10 using do-while loop",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int i = 1;\n    \n    printf(\"Numbers from 1 to 10:\\n\");\n    do {\n        printf(\"%d \", i);\n        i++;\n    } while(i <= 10);\n    printf(\"\\n\");\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to calculate factorial of a number",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int n, i;\n    long long factorial = 1;\n    \n    printf(\"Enter a positive integer: \");\n    scanf(\"%d\", &n);\n    \n    if(n < 0) {\n        printf(\"Error! Factorial of negative number doesn't exist.\\n\");\n    } else {\n        for(i = 1; i <= n; i++) {\n            factorial *= i;\n        }\n        printf(\"Factorial of %d = %lld\\n\", n, factorial);\n    }\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to print Fibonacci series",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int n, first = 0, second = 1, next, i;\n    \n    printf(\"Enter number of terms: \");\n    scanf(\"%d\", &n);\n    \n    printf(\"Fibonacci series: \");\n    \n    for(i = 0; i < n; i++) {\n        if(i <= 1) {\n            next = i;\n        } else {\n            next = first + second;\n            first = second;\n            second = next;\n        }\n        printf(\"%d \", next);\n    }\n    printf(\"\\n\");\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to check if a number is prime",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int n, i, isPrime = 1;\n    \n    printf(\"Enter a positive integer: \");\n    scanf(\"%d\", &n);\n    \n    if(n <= 1) {\n        isPrime = 0;\n    } else {\n        for(i = 2; i <= n/2; i++) {\n            if(n % i == 0) {\n                isPrime = 0;\n                break;\n            }\n        }\n    }\n    \n    if(isPrime) {\n        printf(\"%d is a prime number.\\n\", n);\n    } else {\n        printf(\"%d is not a prime number.\\n\", n);\n    }\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to print multiplication table",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int n, i;\n    \n    printf(\"Enter an integer: \");\n    scanf(\"%d\", &n);\n    \n    printf(\"Multiplication table of %d:\\n\", n);\n    for(i = 1; i <= 10; i++) {\n        printf(\"%d x %d = %d\\n\", n, i, n * i);\n    }\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to find sum of digits of a number",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int num, sum = 0, digit;\n    \n    printf(\"Enter a number: \");\n    scanf(\"%d\", &num);\n    \n    while(num != 0) {\n        digit = num % 10;\n        sum += digit;\n        num /= 10;\n    }\n    \n    printf(\"Sum of digits: %d\\n\", sum);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to reverse a number",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int num, reversed = 0, remainder;\n    \n    printf(\"Enter a number: \");\n    scanf(\"%d\", &num);\n    \n    while(num != 0) {\n        remainder = num % 10;\n        reversed = reversed * 10 + remainder;\n        num /= 10;\n    }\n    \n    printf(\"Reversed number: %d\\n\", reversed);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate nested loops (pattern printing)",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int i, j, rows;\n    \n    printf(\"Enter number of rows: \");\n    scanf(\"%d\", &rows);\n    \n    printf(\"Pattern:\\n\");\n    for(i = 1; i <= rows; i++) {\n        for(j = 1; j <= i; j++) {\n            printf(\"* \");\n        }\n        printf(\"\\n\");\n    }\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate break statement",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int i;\n    \n    printf(\"Numbers from 1 to 10 (stopping at 5):\\n\");\n    for(i = 1; i <= 10; i++) {\n        if(i == 6) {\n            break;\n        }\n        printf(\"%d \", i);\n    }\n    printf(\"\\nLoop terminated at i = %d\\n\", i);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate continue statement",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int i;\n    \n    printf(\"Odd numbers from 1 to 10:\\n\");\n    for(i = 1; i <= 10; i++) {\n        if(i % 2 == 0) {\n            continue;\n        }\n        printf(\"%d \", i);\n    }\n    printf(\"\\n\");\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to find GCD of two numbers",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int a, b, gcd, i;\n    \n    printf(\"Enter two integers: \");\n    scanf(\"%d %d\", &a, &b);\n    \n    for(i = 1; i <= a && i <= b; i++) {\n        if(a % i == 0 && b % i == 0) {\n            gcd = i;\n        }\n    }\n    \n    printf(\"GCD of %d and %d is %d\\n\", a, b, gcd);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to find LCM of two numbers",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int a, b, max, lcm;\n    \n    printf(\"Enter two integers: \");\n    scanf(\"%d %d\", &a, &b);\n    \n    max = (a > b) ? a : b;\n    \n    while(1) {\n        if(max % a == 0 && max % b == 0) {\n            lcm = max;\n            break;\n        }\n        max++;\n    }\n    \n    printf(\"LCM of %d and %d is %d\\n\", a, b, lcm);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate infinite loop with break condition",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int num;\n    \n    printf(\"Enter numbers (0 to exit):\\n\");\n    \n    while(1) {  // Infinite loop\n        printf(\"Enter a number: \");\n        scanf(\"%d\", &num);\n        \n        if(num == 0) {\n            printf(\"Exiting program.\\n\");\n            break;\n        }\n        \n        printf(\"You entered: %d\\n\", num);\n    }\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                }
            ],
            
            "Arrays": [
                {
                    "question": "Write a program to read and display array elements",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int arr[5], i;\n    \n    printf(\"Enter 5 integers:\\n\");\n    for(i = 0; i < 5; i++) {\n        printf(\"Element %d: \", i + 1);\n        scanf(\"%d\", &arr[i]);\n    }\n    \n    printf(\"\\nArray elements are: \");\n    for(i = 0; i < 5; i++) {\n        printf(\"%d \", arr[i]);\n    }\n    printf(\"\\n\");\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to find the largest element in an array",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int arr[5] = {34, 12, 56, 78, 23};\n    int i, max;\n    \n    max = arr[0];\n    \n    for(i = 1; i < 5; i++) {\n        if(arr[i] > max) {\n            max = arr[i];\n        }\n    }\n    \n    printf(\"Largest element: %d\\n\", max);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to find the smallest element in an array",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int arr[5] = {34, 12, 56, 78, 23};\n    int i, min;\n    \n    min = arr[0];\n    \n    for(i = 1; i < 5; i++) {\n        if(arr[i] < min) {\n            min = arr[i];\n        }\n    }\n    \n    printf(\"Smallest element: %d\\n\", min);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to calculate sum of array elements",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int arr[5] = {10, 20, 30, 40, 50};\n    int i, sum = 0;\n    \n    for(i = 0; i < 5; i++) {\n        sum += arr[i];\n    }\n    \n    printf(\"Sum of array elements: %d\\n\", sum);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to reverse an array",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int arr[5] = {1, 2, 3, 4, 5};\n    int i, temp;\n    \n    printf(\"Original array: \");\n    for(i = 0; i < 5; i++) {\n        printf(\"%d \", arr[i]);\n    }\n    printf(\"\\n\");\n    \n    // Reverse the array\n    for(i = 0; i < 5/2; i++) {\n        temp = arr[i];\n        arr[i] = arr[4 - i];\n        arr[4 - i] = temp;\n    }\n    \n    printf(\"Reversed array: \");\n    for(i = 0; i < 5; i++) {\n        printf(\"%d \", arr[i]);\n    }\n    printf(\"\\n\");\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to sort an array in ascending order (Bubble Sort)",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int arr[5] = {64, 34, 25, 12, 22};\n    int i, j, temp, n = 5;\n    \n    printf(\"Original array: \");\n    for(i = 0; i < n; i++) {\n        printf(\"%d \", arr[i]);\n    }\n    printf(\"\\n\");\n    \n    // Bubble sort\n    for(i = 0; i < n-1; i++) {\n        for(j = 0; j < n-i-1; j++) {\n            if(arr[j] > arr[j+1]) {\n                // Swap elements\n                temp = arr[j];\n                arr[j] = arr[j+1];\n                arr[j+1] = temp;\n            }\n        }\n    }\n    \n    printf(\"Sorted array (ascending): \");\n    for(i = 0; i < n; i++) {\n        printf(\"%d \", arr[i]);\n    }\n    printf(\"\\n\");\n    \n    return 0;\n}",
                    "difficulty": "Medium"
                },
                {
                    "question": "Write a program to search an element in array (Linear Search)",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int arr[5] = {10, 20, 30, 40, 50};\n    int i, search, found = 0;\n    \n    printf(\"Enter element to search: \");\n    scanf(\"%d\", &search);\n    \n    for(i = 0; i < 5; i++) {\n        if(arr[i] == search) {\n            printf(\"Element %d found at position %d\\n\", search, i + 1);\n            found = 1;\n            break;\n        }\n    }\n    \n    if(!found) {\n        printf(\"Element %d not found in array\\n\", search);\n    }\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate 2D array",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int matrix[3][3] = {\n        {1, 2, 3},\n        {4, 5, 6},\n        {7, 8, 9}\n    };\n    int i, j;\n    \n    printf(\"2D Array (Matrix):\\n\");\n    for(i = 0; i < 3; i++) {\n        for(j = 0; j < 3; j++) {\n            printf(\"%d \", matrix[i][j]);\n        }\n        printf(\"\\n\");\n    }\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to add two matrices",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int mat1[2][2] = {{1, 2}, {3, 4}};\n    int mat2[2][2] = {{5, 6}, {7, 8}};\n    int sum[2][2];\n    int i, j;\n    \n    printf(\"Matrix 1:\\n\");\n    for(i = 0; i < 2; i++) {\n        for(j = 0; j < 2; j++) {\n            printf(\"%d \", mat1[i][j]);\n        }\n        printf(\"\\n\");\n    }\n    \n    printf(\"\\nMatrix 2:\\n\");\n    for(i = 0; i < 2; i++) {\n        for(j = 0; j < 2; j++) {\n            printf(\"%d \", mat2[i][j]);\n        }\n        printf(\"\\n\");\n    }\n    \n    // Adding matrices\n    for(i = 0; i < 2; i++) {\n        for(j = 0; j < 2; j++) {\n            sum[i][j] = mat1[i][j] + mat2[i][j];\n        }\n    }\n    \n    printf(\"\\nSum of matrices:\\n\");\n    for(i = 0; i < 2; i++) {\n        for(j = 0; j < 2; j++) {\n            printf(\"%d \", sum[i][j]);\n        }\n        printf(\"\\n\");\n    }\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to multiply two matrices",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int mat1[2][3] = {{1, 2, 3}, {4, 5, 6}};\n    int mat2[3][2] = {{7, 8}, {9, 10}, {11, 12}};\n    int result[2][2] = {0};\n    int i, j, k;\n    \n    // Matrix multiplication\n    for(i = 0; i < 2; i++) {\n        for(j = 0; j < 2; j++) {\n            for(k = 0; k < 3; k++) {\n                result[i][j] += mat1[i][k] * mat2[k][j];\n            }\n        }\n    }\n    \n    printf(\"Result of matrix multiplication:\\n\");\n    for(i = 0; i < 2; i++) {\n        for(j = 0; j < 2; j++) {\n            printf(\"%d \", result[i][j]);\n        }\n        printf(\"\\n\");\n    }\n    \n    return 0;\n}",
                    "difficulty": "Medium"
                },
                {
                    "question": "Write a program to find transpose of a matrix",
                    "answer": "#include <stdio.h>\n\nint main() {\n    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};\n    int transpose[3][3];\n    int i, j;\n    \n    printf(\"Original matrix:\\n\");\n    for(i = 0; i < 3; i++) {\n        for(j = 0; j < 3; j++) {\n            printf(\"%d \", matrix[i][j]);\n        }\n        printf(\"\\n\");\n    }\n    \n    // Finding transpose\n    for(i = 0; i < 3; i++) {\n        for(j = 0; j < 3; j++) {\n            transpose[j][i] = matrix[i][j];\n        }\n    }\n    \n    printf(\"\\nTranspose of matrix:\\n\");\n    for(i = 0; i < 3; i++) {\n        for(j = 0; j < 3; j++) {\n            printf(\"%d \", transpose[i][j]);\n        }\n        printf(\"\\n\");\n    }\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to demonstrate character array (string)",
                    "answer": "#include <stdio.h>\n\nint main() {\n    char str[100];\n    \n    printf(\"Enter a string: \");\n    fgets(str, sizeof(str), stdin);\n    \n    printf(\"You entered: %s\", str);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to find length of a string",
                    "answer": "#include <stdio.h>\n\nint main() {\n    char str[100];\n    int length = 0;\n    \n    printf(\"Enter a string: \");\n    fgets(str, sizeof(str), stdin);\n    \n    // Calculate length\n    while(str[length] != '\\0' && str[length] != '\\n') {\n        length++;\n    }\n    \n    printf(\"Length of string: %d\\n\", length);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to copy one string to another",
                    "answer": "#include <stdio.h>\n\nint main() {\n    char source[100], destination[100];\n    int i = 0;\n    \n    printf(\"Enter a string: \");\n    fgets(source, sizeof(source), stdin);\n    \n    // Copy string\n    while(source[i] != '\\0') {\n        destination[i] = source[i];\n        i++;\n    }\n    destination[i] = '\\0';\n    \n    printf(\"Original string: %s\", source);\n    printf(\"Copied string: %s\", destination);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                },
                {
                    "question": "Write a program to concatenate two strings",
                    "answer": "#include <stdio.h>\n\nint main() {\n    char str1[100], str2[100], result[200];\n    int i = 0, j = 0;\n    \n    printf(\"Enter first string: \");\n    fgets(str1, sizeof(str1), stdin);\n    printf(\"Enter second string: \");\n    fgets(str2, sizeof(str2), stdin);\n    \n    // Remove newline characters\n    while(str1[i] != '\\n' && str1[i] != '\\0') {\n        result[i] = str1[i];\n        i++;\n    }\n    \n    // Concatenate second string\n    while(str2[j] != '\\n' && str2[j] != '\\0') {\n        result[i] = str2[j];\n        i++;\n        j++;\n    }\n    result[i] = '\\0';\n    \n    printf(\"Concatenated string: %s\\n\", result);\n    \n    return 0;\n}",
                    "difficulty": "Basic"
                }
        ],
        "Structures": [
            {
                "question": "Write a program to demonstrate basic structure",
                "answer": "#include <stdio.h>\n\n// Define a structure\nstruct Student {\n    int roll_no;\n    char name[50];\n    float marks;\n};\n\nint main() {\n    // Declare structure variable\n    struct Student s1;\n    \n    // Input data\n    printf(\"Enter roll number: \");\n    scanf(\"%d\", &s1.roll_no);\n    \n    printf(\"Enter name: \");\n    scanf(\"%s\", s1.name);\n    \n    printf(\"Enter marks: \");\n    scanf(\"%f\", &s1.marks);\n    \n    // Display data\n    printf(\"\\nStudent Details:\\n\");\n    printf(\"Roll No: %d\\n\", s1.roll_no);\n    printf(\"Name: %s\\n\", s1.name);\n    printf(\"Marks: %.2f\\n\", s1.marks);\n    \n    return 0;\n}",
                "difficulty": "Basic"
            },
                    {
                        "question": "Write a program to demonstrate array of structures",
                        "answer": "#include <stdio.h>\n\nstruct Student {\n    int roll_no;\n    char name[50];\n    float marks;\n};\n\nint main() {\n    struct Student students[3];\n    int i;\n    \n    // Input data for 3 students\n    for(i = 0; i < 3; i++) {\n        printf(\"\\nEnter details for student %d:\\n\", i + 1);\n        printf(\"Roll No: \");\n        scanf(\"%d\", &students[i].roll_no);\n        printf(\"Name: \");\n        scanf(\"%s\", students[i].name);\n        printf(\"Marks: \");\n        scanf(\"%f\", &students[i].marks);\n    }\n    \n    // Display all students\n    printf(\"\\nStudent Details:\\n\");\n    for(i = 0; i < 3; i++) {\n        printf(\"\\nStudent %d:\\n\", i + 1);\n        printf(\"Roll No: %d\\n\", students[i].roll_no);\n        printf(\"Name: %s\\n\", students[i].name);\n        printf(\"Marks: %.2f\\n\", students[i].marks);\n    }\n    \n    return 0;\n}",
                        "difficulty": "Basic"
                    }
                ]
                }
    
            # I'll provide the remaining topics in separate responses
            # due to the character limit

        print("Populating questions for all topics...")

        for topic_name, questions_list in questions_data.items():
            topic = Topic.query.filter_by(name=topic_name).first()
            if topic:
                print(f"Adding questions to '{topic_name}'...")

                for q_data in questions_list:
                    # Check if question already exists
                    existing_question = Question.query.filter_by(
                        question=q_data["question"],
                        topic_id=topic.id
                    ).first()

                    if not existing_question:
                        question = Question(
                            question=q_data["question"],
                            answer=q_data["answer"],
                            difficulty=q_data["difficulty"],
                            topic_id=topic.id
                        )
                        db.session.add(question)

                db.session.commit()
                print(f"Added {len(questions_list)} questions to '{topic_name}'")
            else:
                print(f"Topic '{topic_name}' not found!")

        print("\nQuestion population completed successfully!")

        # Display summary
        topics = Topic.query.all()
        print("\n=== SUMMARY ===")
        for topic in topics:
            count = Question.query.filter_by(topic_id=topic.id).count()
            print(f"{topic.name}: {count} questions")

if __name__ == "__main__":
    populate_questions()