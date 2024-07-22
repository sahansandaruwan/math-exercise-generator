import numpy as np
import random
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Global variables to store user engagement data and performance metrics
engagement_data = []
performance_summary = {
    'addition': {'accuracy': 0, 'average_time': 0},
    'subtraction': {'accuracy': 0, 'average_time': 0},
    'multiplication': {'accuracy': 0, 'average_time': 0},
    'division': {'accuracy': 0, 'average_time': 0}
}
exercise_data = []

def generate_expression(operation):
    """
    Generates a random math expression based on the operation provided.
    """
    a = random.randint(0, 100)
    b = random.randint(1, 100) if operation == '/' else random.randint(0, 100)
    
    if operation == '+':
        return f"{a} + {b}", a, b, a + b
    elif operation == '-':
        return f"{a} - {b}", a, b, a - b
    elif operation == '*':
        return f"{a} * {b}", a, b, a * b
    elif operation == '/':
        if b == 0:
            return None  # Skip division by zero
        return f"{a} / {b}", a, b, a / b

def evaluate_user_performance():
    """
    Evaluates the user's performance by asking a set of questions for each operation.
    """
    num_questions = 10
    global engagement_data, performance_summary
    
    for operation in ['+', '-', '*', '/']:
        correct_answers = 0
        total_time = 0
        
        for _ in range(num_questions):
            result = generate_expression(operation)
            if result is None:  # Skip invalid expressions
                continue
            expression, a, b, correct_answer = result
            print(f"Solve: {expression}")
            start_time = time.time()
            
            while True:
                try:
                    user_answer = float(input("Your answer: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numerical value.")
            
            end_time = time.time()
            
            elapsed_time = end_time - start_time
            total_time += elapsed_time
            
            if abs(user_answer - correct_answer) < 1e-2:  # Check if the answer is close to correct
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Incorrect. The correct answer is {correct_answer:.2f}")
            
            engagement_data.append([a, b, operation, user_answer, correct_answer, elapsed_time, user_answer == correct_answer])
        
        accuracy = (correct_answers / num_questions) * 100
        average_time = total_time / num_questions
        performance_summary[operation] = {'accuracy': accuracy, 'average_time': average_time}
    
    # Save the engagement data to a CSV file
    df = pd.DataFrame(engagement_data, columns=['Operand1', 'Operand2', 'Operation', 'UserAnswer', 'CorrectAnswer', 'TimeTaken', 'IsCorrect'])
    df.to_csv('user_engagement_data.csv', index=False)
    
    return performance_summary

def generate_exercises():
    """
    Generates new exercises based on the user's performance.
    """
    global exercise_data
    for operation, metrics in performance_summary.items():
        if metrics['accuracy'] < 50:  # Generate exercises if accuracy is below 50%
            print(f"Generating exercises for {operation}...")
            for _ in range(5):  # Create 5 new exercises for each operation
                result = generate_expression(operation)
                if result is None:  # Skip invalid expressions
                    continue
                expression, a, b, answer = result
                exercise_data.append([a, b, operation, answer])
    
    # Save the generated exercises to a CSV file
    df = pd.DataFrame(exercise_data, columns=['Operand1', 'Operand2', 'Operation', 'Answer'])
    df.to_csv('generated_exercises.csv', index=False)

def update_plot(frame):
    """
    Updates the plot with real-time data for user engagement and performance summary.
    """
    plt.clf()
    
    if engagement_data:
        df = pd.DataFrame(engagement_data, columns=['Operand1', 'Operand2', 'Operation', 'UserAnswer', 'CorrectAnswer', 'TimeTaken', 'IsCorrect'])
        plt.subplot(1, 2, 1)
        plt.scatter(df['TimeTaken'], df['UserAnswer'], c=df['IsCorrect'], cmap='coolwarm', alpha=0.6)
        plt.title('User Engagement')
        plt.xlabel('Time Taken (s)')
        plt.ylabel('User Answer')
        plt.colorbar(label='Correct/Incorrect')
    
    if performance_summary:
        operations = list(performance_summary.keys())
        accuracies = [performance_summary[op]['accuracy'] for op in operations]
        avg_times = [performance_summary[op]['average_time'] for op in operations]
        
        plt.subplot(1, 2, 2)
        plt.bar(operations, accuracies, color='skyblue', label='Accuracy (%)', alpha=0.7)
        plt.plot(operations, avg_times, color='red', marker='o', label='Average Time (s)')
        plt.title('Performance Summary')
        plt.xlabel('Operation')
        plt.ylabel('Value')
        plt.legend()
    
    plt.tight_layout()

def continuous_exercise_session():
    """
    Continuously generates and presents exercises based on user performance.
    """
    while True:
        generate_exercises()
        
        if not exercise_data:
            print("No exercises generated based on current performance.")
            break
        
        for exercise in exercise_data:
            expression = f"{exercise[0]} {exercise[2]} {exercise[1]}"
            correct_answer = exercise[3]
            print(f"Solve: {expression}")
            
            while True:
                try:
                    user_answer = float(input("Your answer: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numerical value.")
            
            if abs(user_answer - correct_answer) < 1e-2:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is {correct_answer:.2f}")
        
        print("Evaluating user performance...")
        performance_summary = evaluate_user_performance()
        
        cont = input("Would you like to continue solving exercises? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

def main():
    """
    Main function to execute the workflow: evaluate performance, generate exercises, and plot results.
    """
    fig = plt.figure(figsize=(12, 6))
    ani = FuncAnimation(fig, update_plot, interval=5000)

    print("Evaluating user performance...")
    performance_summary = evaluate_user_performance()
    
    print("Generating and solving exercises based on performance...")
    continuous_exercise_session()
    
    plt.show()  # Display the real-time plot

if __name__ == "__main__":
    main()
