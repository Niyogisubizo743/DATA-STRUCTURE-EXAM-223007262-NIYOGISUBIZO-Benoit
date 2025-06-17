#include <iostream>
#include <cstring>
#include <iomanip>
#include <vector>
using namespace std;

// Student structure with dynamic grade allocation
struct Student {
    char name[30];      // Student name storage
    float* grades;      // Dynamic array for grades
    int nGrades;        // Number of grades stored
};

// Abstract base class for grade metrics
class GradeMetric {
public:
    // Pure virtual function for computing metrics
    virtual float compute(const Student* student) = 0;
    // Virtual destructor for proper cleanup
    virtual ~GradeMetric() {}
    // Pure virtual function to get metric name
    virtual const char* getName() = 0;
};

// Derived class for calculating mean grade
class MeanMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        if (student->nGrades == 0) return 0.0f;
        
        float sum = 0.0f;
        // Use pointer arithmetic to traverse grades array
        float* gradePtr = student->grades;
        for (int i = 0; i < student->nGrades; i++) {
            sum += *(gradePtr + i);  // Pointer arithmetic access
        }
        return sum / student->nGrades;
    }
    
    const char* getName() override {
        return "Mean";
    }
};

// Derived class for finding maximum grade
class MaxMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        if (student->nGrades == 0) return 0.0f;
        
        float maxGrade = *student->grades;  // Initialize with first grade
        // Use pointer arithmetic to find maximum
        float* gradePtr = student->grades;
        for (int i = 1; i < student->nGrades; i++) {
            if (*(gradePtr + i) > maxGrade) {
                maxGrade = *(gradePtr + i);
            }
        }
        return maxGrade;
    }
    
    const char* getName() override {
        return "Maximum";
    }
};

// Derived class for finding minimum grade
class MinMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        if (student->nGrades == 0) return 0.0f;
        
        float minGrade = *student->grades;  // Initialize with first grade
        // Use pointer arithmetic to find minimum
        float* gradePtr = student->grades;
        for (int i = 1; i < student->nGrades; i++) {
            if (*(gradePtr + i) < minGrade) {
                minGrade = *(gradePtr + i);
            }
        }
        return minGrade;
    }
    
    const char* getName() override {
        return "Minimum";
    }
};

// Function to add a grade to student's grade array
void addGrade(Student& student, float grade) {
    // Allocate new array with one more element
    float* newGrades = new float[student.nGrades + 1];
    
    // Copy existing grades using pointer arithmetic
    float* oldPtr = student.grades;
    float* newPtr = newGrades;
    for (int i = 0; i < student.nGrades; i++) {
        *(newPtr + i) = *(oldPtr + i);
    }
    
    // Add new grade at the end
    *(newPtr + student.nGrades) = grade;
    
    // Clean up old array and update student
    delete[] student.grades;
    student.grades = newGrades;
    student.nGrades++;
}

// Function to remove a grade at specified index
void removeGrade(Student& student, int index) {
    if (index < 0 || index >= student.nGrades) {
        cout << "Invalid index for grade removal!" << endl;
        return;
    }
    
    if (student.nGrades == 1) {
        // If only one grade, delete array and reset
        delete[] student.grades;
        student.grades = nullptr;
        student.nGrades = 0;
        return;
    }
    
    // Allocate new array with one less element
    float* newGrades = new float[student.nGrades - 1];
    
    // Copy grades excluding the one at specified index
    float* oldPtr = student.grades;
    float* newPtr = newGrades;
    int newIndex = 0;
    
    for (int i = 0; i < student.nGrades; i++) {
        if (i != index) {
            *(newPtr + newIndex) = *(oldPtr + i);
            newIndex++;
        }
    }
    
    // Clean up old array and update student
    delete[] student.grades;
    student.grades = newGrades;
    student.nGrades--;
}

// Function to initialize a student with initial grades
void initializeStudent(Student& student, const char* name, float initialGrades[], int numGrades) {
    // Copy name to student structure
    strcpy(student.name, name);
    
    // Allocate memory for grades array
    student.grades = new float[numGrades];
    student.nGrades = numGrades;
    
    // Copy initial grades using pointer arithmetic
    float* gradePtr = student.grades;
    for (int i = 0; i < numGrades; i++) {
        *(gradePtr + i) = initialGrades[i];
    }
}

// Function to display student information
void displayStudent(const Student& student) {
    cout << "\nStudent: " << student.name << endl;
    cout << "Grades: ";
    
    if (student.nGrades == 0) {
        cout << "No grades recorded" << endl;
        return;
    }
    
    // Display all grades using pointer arithmetic
    float* gradePtr = student.grades;
    for (int i = 0; i < student.nGrades; i++) {
        cout << fixed << setprecision(1) << *(gradePtr + i);
        if (i < student.nGrades - 1) cout << ", ";
    }
    cout << endl;
}

// Function to cleanup student memory
void cleanupStudent(Student& student) {
    delete[] student.grades;
    student.grades = nullptr;
    student.nGrades = 0;
}

// Function to display menu options
void displayMenu() {
    cout << "\n=== Student Grade Metrics System - Interactive Menu ===" << endl;
    cout << "1. Create new student" << endl;
    cout << "2. Display student information" << endl;
    cout << "3. Add grade to student" << endl;
    cout << "4. Remove grade from student" << endl;
    cout << "5. Calculate grade metrics" << endl;
    cout << "6. Run demonstration" << endl;
    cout << "7. Exit program" << endl;
    cout << "Enter your choice (1-7): ";
}

// Function to get user input for creating a student
void createStudentInteractive(Student& student) {
    char name[30];
    int numGrades;
    
    cout << "\nEnter student name (max 29 characters): ";
    cin.ignore(); // Clear input buffer
    cin.getline(name, 30);
    
    cout << "Enter number of initial grades: ";
    cin >> numGrades;
    
    if (numGrades <= 0) {
        // Initialize with empty grades array
        strcpy(student.name, name);
        student.grades = nullptr;
        student.nGrades = 0;
        cout << "Student created with no initial grades." << endl;
        return;
    }
    
    // Allocate memory for grades
    student.grades = new float[numGrades];
    student.nGrades = numGrades;
    strcpy(student.name, name);
    
    // Get grades from user using pointer arithmetic
    float* gradePtr = student.grades;
    cout << "Enter " << numGrades << " grades:" << endl;
    for (int i = 0; i < numGrades; i++) {
        cout << "Grade " << (i + 1) << ": ";
        cin >> *(gradePtr + i);
    }
    
    cout << "Student created successfully!" << endl;
}

// Function to add grade interactively
void addGradeInteractive(Student& student) {
    if (strlen(student.name) == 0) {
        cout << "No student created yet. Please create a student first." << endl;
        return;
    }
    
    float grade;
    cout << "\nEnter grade to add: ";
    cin >> grade;
    
    addGrade(student, grade);
    cout << "Grade " << grade << " added successfully!" << endl;
}

// Function to remove grade interactively
void removeGradeInteractive(Student& student) {
    if (strlen(student.name) == 0) {
        cout << "No student created yet. Please create a student first." << endl;
        return;
    }
    
    if (student.nGrades == 0) {
        cout << "No grades to remove." << endl;
        return;
    }
    
    // Display current grades with indices
    cout << "\nCurrent grades:" << endl;
    float* gradePtr = student.grades;
    for (int i = 0; i < student.nGrades; i++) {
        cout << "Index " << i << ": " << *(gradePtr + i) << endl;
    }
    
    int index;
    cout << "Enter index of grade to remove (0-" << (student.nGrades - 1) << "): ";
    cin >> index;
    
    removeGrade(student, index);
    if (index >= 0 && index < student.nGrades + 1) {
        cout << "Grade at index " << index << " removed successfully!" << endl;
    }
}

// Function to calculate and display metrics interactively
void calculateMetricsInteractive(const Student& student) {
    if (strlen(student.name) == 0) {
        cout << "No student created yet. Please create a student first." << endl;
        return;
    }
    
    if (student.nGrades == 0) {
        cout << "No grades available for metric calculation." << endl;
        return;
    }
    
    // Create metric objects
    MeanMetric meanMetric;
    MaxMetric maxMetric;
    MinMetric minMetric;
    
    cout << "\n=== Grade Metrics for " << student.name << " ===" << endl;
    cout << "Mean Grade: " << fixed << setprecision(2) << meanMetric.compute(&student) << endl;
    cout << "Maximum Grade: " << fixed << setprecision(2) << maxMetric.compute(&student) << endl;
    cout << "Minimum Grade: " << fixed << setprecision(2) << minMetric.compute(&student) << endl;
}

// Function to run the original demonstration
void runDemonstration() {
    cout << "\n=== Running Demonstration ===" << endl;
    
    // Create a student with initial grades
    Student demoStudent;
    float initialGrades[] = {85.5f, 92.0f, 78.5f, 88.0f, 95.5f};
    initializeStudent(demoStudent, "umunyeshuri mwiza", initialGrades, 5);
    
    // Display initial student information
    displayStudent(demoStudent);
    
    // Create dynamic array of metric pointers for polymorphism
    const int numMetrics = 3;
    GradeMetric** metrics = new GradeMetric*[numMetrics];
    
    // Initialize metrics array with different metric types
    metrics[0] = new MeanMetric();      // Mean calculation
    metrics[1] = new MaxMetric();       // Maximum calculation  
    metrics[2] = new MinMetric();       // Minimum calculation
    
    // Demonstrate polymorphism by calling compute() on each metric
    cout << "\n=== Initial Grade Metrics ===" << endl;
    for (int i = 0; i < numMetrics; i++) {
        // Polymorphic call - dispatches to correct derived class
        float result = metrics[i]->compute(&demoStudent);
        cout << metrics[i]->getName() << " Grade: " 
             << fixed << setprecision(2) << result << endl;
    }
    
    // Demonstrate adding a grade
    cout << "\n=== Adding Grade (90.0) ===" << endl;
    addGrade(demoStudent, 90.0f);
    displayStudent(demoStudent);
    
    // Recalculate metrics after adding grade
    cout << "\n=== Updated Grade Metrics ===" << endl;
    for (int i = 0; i < numMetrics; i++) {
        float result = metrics[i]->compute(&demoStudent);
        cout << metrics[i]->getName() << " Grade: " 
             << fixed << setprecision(2) << result << endl;
    }
    
    // Demonstrate removing a grade
    cout << "\n=== Removing Grade at Index 2 ===" << endl;
    removeGrade(demoStudent, 2);
    displayStudent(demoStudent);
    
    // Final metrics calculation
    cout << "\n=== Final Grade Metrics ===" << endl;
    for (int i = 0; i < numMetrics; i++) {
        float result = metrics[i]->compute(&demoStudent);
        cout << metrics[i]->getName() << " Grade: " 
             << fixed << setprecision(2) << result << endl;
    }
    
    // Memory cleanup
    for (int i = 0; i < numMetrics; i++) {
        delete metrics[i];  // Clean up metric objects
    }
    delete[] metrics;       // Clean up metrics array
    cleanupStudent(demoStudent); // Clean up student grades
    
    cout << "\n=== Demonstration Complete ===" << endl;
}

int main() {
    cout << "=== Student Grade Metrics System ===" << endl;
    cout << "Interactive CLI Version" << endl;
    
    // Initialize empty student for interactive use
    Student student;
    student.name[0] = '\0';  // Empty name indicates no student created yet
    student.grades = nullptr;
    student.nGrades = 0;
    
    int choice;
    bool running = true;
    
    while (running) {
        displayMenu();
        cin >> choice;
        
        switch (choice) {
            case 1:
                // Clean up existing student data if any
                if (student.grades != nullptr) {
                    cleanupStudent(student);
                }
                createStudentInteractive(student);
                break;
                
            case 2:
                if (strlen(student.name) == 0) {
                    cout << "No student created yet. Please create a student first." << endl;
                } else {
                    displayStudent(student);
                }
                break;
                
            case 3:
                addGradeInteractive(student);
                break;
                
            case 4:
                removeGradeInteractive(student);
                break;
                
            case 5:
                calculateMetricsInteractive(student);
                break;
                
            case 6:
                runDemonstration();
                break;
                
            case 7:
                cout << "Exiting program..." << endl;
                running = false;
                break;
                
            default:
                cout << "Invalid choice. Please enter a number between 1 and 7." << endl;
                break;
        }
        
        // Clear input buffer for next iteration
        if (cin.fail()) {
            cin.clear();
            cin.ignore(10000, '\n');
        }
    }
    
    // Final cleanup
    cleanupStudent(student);
    
    cout << "\n=== Program Complete ===" << endl;
    return 0;
}
