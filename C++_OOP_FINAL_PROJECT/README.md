# Student Grade Metrics System

## Project Description

This project implements a dynamic student grade management system that calculates multiple grade metrics (mean, maximum, minimum) using object-oriented programming principles including inheritance, polymorphism, and dynamic memory management. The system now features an **interactive CLI interface** for manual data entry and real-time function execution.

## Assignment Requirements

The project fulfills the following specific requirements:

1. **Student Structure**: Define `struct Student { char name[30]; float* grades; int nGrades; }` with dynamic grade allocation
2. **Abstract Base Class**: Create `GradeMetric` abstract class with `virtual float compute(const Student*) = 0`
3. **Inheritance**: Implement derived classes (`MeanMetric`, `MaxMetric`, `MinMetric`) extending `GradeMetric`
4. **Polymorphism**: Use dynamic array `GradeMetric** metrics` for polymorphic method dispatch
5. **Pointer Arithmetic**: Use pointer arithmetic on grades array for all computations
6. **Dynamic Memory**: Implement `addGrade(Student&, float)` and `removeGrade(Student&, int index)` with array resizing
7. **Interactive CLI**: Manual data entry and function calls through command-line interface

## New Features - Interactive CLI System

### Menu Options

The program now provides a comprehensive interactive menu system:

```
=== Student Grade Metrics System - Interactive Menu ===
1. Create new student
2. Display student information
3. Add grade to student
4. Remove grade from student
5. Calculate grade metrics
6. Run demonstration
7. Exit program
```

### Interactive Functions

#### 1. Create New Student (`createStudentInteractive`)
```cpp
void createStudentInteractive(Student& student) {
    char name[30];
    int numGrades;
    
    cout << "\nEnter student name (max 29 characters): ";
    cin.ignore();                                       // Clear input buffer
    cin.getline(name, 30);                             // Get full name with spaces
    
    cout << "Enter number of initial grades: ";
    cin >> numGrades;                                   // Get initial grade count
    
    if (numGrades <= 0) {
        strcpy(student.name, name);                     // Copy name to student
        student.grades = nullptr;                       // No grades allocated
        student.nGrades = 0;                           // Zero grade count
        return;
    }
    
    student.grades = new float[numGrades];              // Allocate grades array
    student.nGrades = numGrades;                        // Set grade count
    strcpy(student.name, name);                         // Copy name
    
    float* gradePtr = student.grades;                   // Get pointer for input
    for (int i = 0; i < numGrades; i++) {
        cout << "Grade " << (i + 1) << ": ";
        cin >> *(gradePtr + i);                         // POINTER ARITHMETIC: input grade
    }
}
```

**Purpose**: Allows users to manually create students with custom names and initial grades using pointer arithmetic for data entry.

#### 2. Interactive Grade Addition (`addGradeInteractive`)
```cpp
void addGradeInteractive(Student& student) {
    if (strlen(student.name) == 0) {                    // Check if student exists
        cout << "No student created yet. Please create a student first." << endl;
        return;
    }
    
    float grade;
    cout << "\nEnter grade to add: ";
    cin >> grade;                                       // Get grade from user
    
    addGrade(student, grade);                           // Call dynamic resize function
    cout << "Grade " << grade << " added successfully!" << endl;
}
```

**Purpose**: Provides user-friendly interface for adding grades with validation and confirmation.

#### 3. Interactive Grade Removal (`removeGradeInteractive`)
```cpp
void removeGradeInteractive(Student& student) {
    if (strlen(student.name) == 0) {                    // Validate student exists
        cout << "No student created yet. Please create a student first." << endl;
        return;
    }
    
    if (student.nGrades == 0) {                         // Check for grades to remove
        cout << "No grades to remove." << endl;
        return;
    }
    
    // Display current grades with indices for user selection
    cout << "\nCurrent grades:" << endl;
    float* gradePtr = student.grades;                   // Get pointer to grades
    for (int i = 0; i < student.nGrades; i++) {
        cout << "Index " << i << ": " << *(gradePtr + i) << endl;  // POINTER ARITHMETIC
    }
    
    int index;
    cout << "Enter index of grade to remove (0-" << (student.nGrades - 1) << "): ";
    cin >> index;                                       // Get index from user
    
    removeGrade(student, index);                        // Call dynamic resize function
}
```

**Purpose**: Shows all grades with indices and allows users to select which grade to remove with visual feedback.

#### 4. Interactive Metrics Calculation (`calculateMetricsInteractive`)
```cpp
void calculateMetricsInteractive(const Student& student) {
    if (strlen(student.name) == 0) {                    // Validate student exists
        cout << "No student created yet. Please create a student first." << endl;
        return;
    }
    
    if (student.nGrades == 0) {                         // Check for grades
        cout << "No grades available for metric calculation." << endl;
        return;
    }
    
    // Create metric objects for computation
    MeanMetric meanMetric;                              // Local object creation
    MaxMetric maxMetric;                                // No dynamic allocation needed
    MinMetric minMetric;
    
    cout << "\n=== Grade Metrics for " << student.name << " ===" << endl;
    cout << "Mean Grade: " << fixed << setprecision(2) << meanMetric.compute(&student) << endl;
    cout << "Maximum Grade: " << fixed << setprecision(2) << maxMetric.compute(&student) << endl;
    cout << "Minimum Grade: " << fixed << setprecision(2) << minMetric.compute(&student) << endl;
}
```

**Purpose**: Calculates and displays all grade metrics on demand with proper formatting and validation.

## Implementation Details

### Core Components

#### 1. Student Structure
```cpp
struct Student {
    char name[30];      // Fixed-size name storage (30 characters)
    float* grades;      // Dynamic array pointer for grades
    int nGrades;        // Current number of grades stored
};
```

**Purpose**: Stores student information with dynamically allocated grade array to allow flexible grade management.

#### 2. Abstract Base Class - GradeMetric
```cpp
class GradeMetric {
public:
    virtual float compute(const Student* student) = 0;  // Pure virtual - forces implementation
    virtual ~GradeMetric() {}                           // Virtual destructor for proper cleanup
    virtual const char* getName() = 0;                  // Pure virtual - get metric name
};
```

**Purpose**: Defines interface contract for all grade metric calculations, enabling polymorphism through pure virtual functions.

#### 3. Derived Metric Classes

##### MeanMetric Class
```cpp
class MeanMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        if (student->nGrades == 0) return 0.0f;        // Handle edge case: no grades
        
        float sum = 0.0f;                               // Initialize sum accumulator
        float* gradePtr = student->grades;              // Get base pointer to grades array
        for (int i = 0; i < student->nGrades; i++) {
            sum += *(gradePtr + i);                     // POINTER ARITHMETIC: access element at offset i
        }
        return sum / student->nGrades;                  // Calculate arithmetic mean
    }
    
    const char* getName() override {
        return "Mean";                                  // Return metric identifier
    }
};
```

**Key Features**:
- Uses pointer arithmetic `*(gradePtr + i)` instead of array notation `gradePtr[i]`
- Implements arithmetic mean calculation: sum of all grades divided by count
- Override keyword ensures proper virtual function implementation

##### MaxMetric Class
```cpp
class MaxMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        if (student->nGrades == 0) return 0.0f;        // Handle edge case: no grades
        
        float maxGrade = *student->grades;              // Initialize with first grade (dereference)
        float* gradePtr = student->grades;              // Get base pointer to grades array
        for (int i = 1; i < student->nGrades; i++) {    // Start from index 1 (second element)
            if (*(gradePtr + i) > maxGrade) {           // POINTER ARITHMETIC: compare element at offset i
                maxGrade = *(gradePtr + i);             // Update maximum value
            }
        }
        return maxGrade;                                // Return highest grade found
    }
    
    const char* getName() override {
        return "Maximum";                               // Return metric identifier
    }
};
```

**Key Features**:
- Initializes with first element using dereference operator `*student->grades`
- Uses pointer arithmetic for array traversal and comparison
- Linear search algorithm to find maximum value

##### MinMetric Class
```cpp
class MinMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        if (student->nGrades == 0) return 0.0f;        // Handle edge case: no grades
        
        float minGrade = *student->grades;              // Initialize with first grade (dereference)
        float* gradePtr = student->grades;              // Get base pointer to grades array
        for (int i = 1; i < student->nGrades; i++) {    // Start from index 1 (second element)
            if (*(gradePtr + i) < minGrade) {           // POINTER ARITHMETIC: compare element at offset i
                minGrade = *(gradePtr + i);             // Update minimum value
            }
        }
        return minGrade;                                // Return lowest grade found
    }
    
    const char* getName() override {
        return "Minimum";                               // Return metric identifier
    }
};
```

**Key Features**:
- Similar structure to MaxMetric but searches for minimum value
- Uses pointer arithmetic throughout for consistency
- Efficient single-pass algorithm

### Dynamic Memory Management Functions

#### addGrade Function
```cpp
void addGrade(Student& student, float grade) {
    // Step 1: Allocate new array with increased capacity
    float* newGrades = new float[student.nGrades + 1];  // Allocate space for one more grade
    
    // Step 2: Copy existing grades using pointer arithmetic
    float* oldPtr = student.grades;                     // Pointer to old array
    float* newPtr = newGrades;                          // Pointer to new array
    for (int i = 0; i < student.nGrades; i++) {
        *(newPtr + i) = *(oldPtr + i);                  // POINTER ARITHMETIC: copy each element
    }
    
    // Step 3: Add new grade at the end
    *(newPtr + student.nGrades) = grade;                // POINTER ARITHMETIC: add at end position
    
    // Step 4: Update student structure and cleanup
    delete[] student.grades;                            // Deallocate old array
    student.grades = newGrades;                         // Update pointer to new array
    student.nGrades++;                                  // Increment grade count
}
```

**Purpose**: Dynamically expands the grades array by one element and adds the new grade. Demonstrates dynamic memory reallocation with pointer arithmetic.

#### removeGrade Function
```cpp
void removeGrade(Student& student, int index) {
    // Step 1: Validate input parameters
    if (index < 0 || index >= student.nGrades) {        // Bounds checking
        cout << "Invalid index for grade removal!" << endl;
        return;
    }
    
    // Step 2: Handle special case - removing last grade
    if (student.nGrades == 1) {
        delete[] student.grades;                        // Deallocate array
        student.grades = nullptr;                       // Set pointer to null
        student.nGrades = 0;                           // Reset count
        return;
    }
    
    // Step 3: Allocate new smaller array
    float* newGrades = new float[student.nGrades - 1];  // Allocate space for one less grade
    
    // Step 4: Copy grades excluding the one at specified index
    float* oldPtr = student.grades;                     // Pointer to old array
    float* newPtr = newGrades;                          // Pointer to new array
    int newIndex = 0;                                   // Track position in new array
    
    for (int i = 0; i < student.nGrades; i++) {
        if (i != index) {                               // Skip the element to be removed
            *(newPtr + newIndex) = *(oldPtr + i);       // POINTER ARITHMETIC: copy element
            newIndex++;                                 // Advance new array position
        }
    }
    
    // Step 5: Update student structure and cleanup
    delete[] student.grades;                            // Deallocate old array
    student.grades = newGrades;                         // Update pointer to new array
    student.nGrades--;                                  // Decrement grade count
}
```

**Purpose**: Dynamically shrinks the grades array by removing the element at the specified index. Handles edge cases and maintains data integrity.

### Helper Functions

#### initializeStudent Function
```cpp
void initializeStudent(Student& student, const char* name, float initialGrades[], int numGrades) {
    strcpy(student.name, name);                         // Copy name string to student structure
    
    student.grades = new float[numGrades];              // Allocate dynamic array for grades
    student.nGrades = numGrades;                        // Set grade count
    
    // Copy initial grades using pointer arithmetic
    float* gradePtr = student.grades;                   // Get pointer to allocated array
    for (int i = 0; i < numGrades; i++) {
        *(gradePtr + i) = initialGrades[i];             // POINTER ARITHMETIC: copy each grade
    }
}
```

**Purpose**: Initializes a student structure with name and initial grades, demonstrating dynamic memory allocation.

#### displayStudent Function
```cpp
void displayStudent(const Student& student) {
    cout << "\nStudent: " << student.name << endl;     // Display student name
    cout << "Grades: ";
    
    if (student.nGrades == 0) {                         // Handle case with no grades
        cout << "No grades recorded" << endl;
        return;
    }
    
    // Display all grades using pointer arithmetic
    float* gradePtr = student.grades;                   // Get pointer to grades array
    for (int i = 0; i < student.nGrades; i++) {
        cout << fixed << setprecision(1) << *(gradePtr + i);  // POINTER ARITHMETIC: display grade
        if (i < student.nGrades - 1) cout << ", ";      // Add comma separator
    }
    cout << endl;
}
```

**Purpose**: Displays student information including all grades, using pointer arithmetic for array access.

### Polymorphism Implementation

The main function demonstrates polymorphism through a dynamic array of base class pointers:

```cpp
// Create dynamic array of metric pointers for polymorphism
const int numMetrics = 3;
GradeMetric** metrics = new GradeMetric*[numMetrics];   // Array of base class pointers

// Initialize metrics array with different derived class objects
metrics[0] = new MeanMetric();      // Polymorphic assignment - MeanMetric object
metrics[1] = new MaxMetric();       // Polymorphic assignment - MaxMetric object  
metrics[2] = new MinMetric();       // Polymorphic assignment - MinMetric object

// Polymorphic method calls - runtime dispatch to correct implementation
for (int i = 0; i < numMetrics; i++) {
    float result = metrics[i]->compute(&student);       // Virtual function call
    cout << metrics[i]->getName() << " Grade: " << result << endl;
}
```

**Key Concepts**:
- `GradeMetric**` is a pointer to an array of `GradeMetric*` pointers
- Each element points to a different derived class object
- Virtual function calls dispatch to the correct implementation at runtime
- Demonstrates the power of polymorphism in object-oriented design

## Key Programming Concepts Demonstrated

1. **Inheritance**: All metric classes inherit from `GradeMetric` base class
2. **Polymorphism**: Virtual function calls dispatch to correct derived class implementations
3. **Dynamic Memory Allocation**: Arrays allocated/deallocated using `new`/`delete` operators
4. **Pointer Arithmetic**: All array access uses `*(ptr + offset)` syntax instead of `ptr[offset]`
5. **Memory Management**: Proper cleanup prevents memory leaks
6. **Abstract Classes**: `GradeMetric` cannot be instantiated due to pure virtual functions
7. **Function Overriding**: Derived classes override base class virtual functions
8. **Dynamic Array Resizing**: Arrays grow and shrink as needed
9. **Interactive User Interface**: Command-line menu system with input validation
10. **Real-time Data Entry**: Manual input of student and grade information
11. **Error Handling**: Comprehensive validation and user feedback

## Program Execution Modes

### 1. Interactive Mode (Default)
- Manual student creation with custom names and grades
- Real-time grade addition and removal
- On-demand metric calculations
- User-driven program flow

### 2. Demonstration Mode (Option 6)
- Automated execution with predefined data
- Shows all functionality with "umunyeshuri mwiza" example
- Demonstrates polymorphism and memory management
- Original assignment requirements fulfilled

## Expected Output Examples

### Interactive Session
```
=== Student Grade Metrics System ===
Interactive CLI Version

=== Student Grade Metrics System - Interactive Menu ===
1. Create new student
2. Display student information
3. Add grade to student
4. Remove grade from student
5. Calculate grade metrics
6. Run demonstration
7. Exit program
Enter your choice (1-7): 1

Enter student name (max 29 characters): Bob Wilson
Enter number of initial grades: 4
Enter 4 grades:
Grade 1: 87.5
Grade 2: 91.0
Grade 3: 83.5
Grade 4: 95.0
Student created successfully!

=== Student Grade Metrics System - Interactive Menu ===
1. Create new student
2. Display student information
3. Add grade to student
4. Remove grade from student
5. Calculate grade metrics
6. Run demonstration
7. Exit program
Enter your choice (1-7): 5

=== Grade Metrics for Bob Wilson ===
Mean Grade: 89.25
Maximum Grade: 95.00
Minimum Grade: 83.50
```

### Demonstration Mode Output
```
=== Student Grade Metrics System ===
Demonstration Mode

Student: umunyeshuri mwiza
Grades: 85.5, 92.0, 78.5, 88.0, 95.5

=== Initial Grade Metrics ===
Mean Grade: 87.90
Maximum Grade: 95.50
Minimum Grade: 78.50

=== Adding Grade (90.0) ===

Student: umunyeshuri mwiza
Grades: 85.5, 92.0, 78.5, 88.0, 95.5, 90.0

=== Updated Grade Metrics ===
Mean Grade: 88.25
Maximum Grade: 95.50
Minimum Grade: 78.50

=== Removing Grade at Index 2 ===

Student: umunyeshuri mwiza
Grades: 85.5, 92.0, 88.0, 95.5, 90.0

=== Final Grade Metrics ===
Mean Grade: 90.20
Maximum Grade: 95.50
Minimum Grade: 85.50

=== Program Complete ===
```

## Memory Safety Features

The implementation includes comprehensive memory management:
- **Dynamic Allocation**: All arrays allocated with `new` operator
- **Proper Deallocation**: All arrays deallocated with `delete[]` operator
- **Virtual Destructors**: Base class has virtual destructor for proper cleanup
- **Bounds Checking**: Array access validated to prevent buffer overflows
- **Null Pointer Handling**: Checks for null/empty arrays before processing
- **Memory Leak Prevention**: All allocated memory is properly freed

## Technical Requirements Fulfilled

✅ **Student Structure**: `struct Student` with `char name[30]`, `float* grades`, `int nGrades`
✅ **Dynamic Allocation**: Grades array allocated dynamically with `new`
✅ **Abstract Base Class**: `GradeMetric` with pure virtual `compute()` method
✅ **Inheritance**: Three derived classes extend `GradeMetric`
✅ **Polymorphism**: `GradeMetric**` array enables runtime method dispatch
✅ **Pointer Arithmetic**: All array operations use `*(ptr + offset)` syntax
✅ **Dynamic Resizing**: `addGrade()` and `removeGrade()` functions resize arrays
✅ **Memory Management**: Proper allocation and deallocation throughout
✅ **Interactive CLI**: Manual data entry and function calls
✅ **Input Validation**: Comprehensive error checking and user feedback

## Compilation and Execution

To compile and run the program:
```bash
g++ -std=c++11 -o student_metrics main.cpp
./student_metrics
```

Or using Visual Studio:
```bash
cl /EHsc main.cpp /Fe:student_metrics.exe
student_metrics.exe
```

## Interactive CLI Benefits

1. **Educational Value**: Students can experiment with different data sets
2. **Real-time Testing**: Immediate feedback on function operations
3. **User Control**: Complete control over program execution flow
4. **Validation Learning**: Demonstrates proper input validation techniques
5. **Memory Management**: Shows dynamic allocation in real-time
6. **Polymorphism Practice**: Users can see virtual function dispatch in action

## Conclusion

The Student Grade Metrics System successfully implements all required specifications while providing an enhanced interactive experience. The CLI interface allows users to manually create students, manage grades dynamically, and calculate metrics on demand. The system demonstrates advanced C++ concepts including inheritance hierarchies, polymorphic method dispatch, dynamic memory management, and pointer arithmetic operations, all while maintaining memory safety and providing excellent user experience through comprehensive input validation and error handling.

The dual-mode approach (interactive and demonstration) makes this project suitable for both learning experimentation and requirements validation, showcasing the flexibility and power of object-oriented programming in C++.
