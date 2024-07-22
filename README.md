# Math Practice and Performance Evaluation Tool

## Overview

This repository contains a Python application designed to help users practice basic arithmetic operations (addition, subtraction, multiplication, division) and evaluate their performance. The application provides real-time feedback on user answers, tracks engagement metrics, and generates new exercises based on performance data.

## Features

- **Exercise Generation**: Generates random arithmetic problems for addition, subtraction, multiplication, and division.
- **Performance Evaluation**: Assesses user performance by recording accuracy and time taken to solve problems.
- **Dynamic Exercise Generation**: Adapts the difficulty of exercises based on user performance.
- **Real-Time Visualization**: Provides real-time updates on user engagement and performance through interactive plots.
- **Data Storage**: Saves user engagement data and generated exercises to CSV files for further analysis.

## How It Works

1. **Generate Math Expressions**: 
   - The application creates random math problems based on the selected operation (addition, subtraction, multiplication, division).

2. **Evaluate User Performance**:
   - The user is prompted to solve a series of problems.
   - User answers are compared to the correct answers.
   - Performance metrics such as accuracy and time taken are recorded.

3. **Generate Exercises Based on Performance**:
   - Exercises are generated based on the user's accuracy in previous sessions.
   - If the accuracy for any operation falls below 50%, additional exercises for that operation are created.

4. **Real-Time Feedback and Visualization**:
   - The application provides immediate feedback on user answers (correct or incorrect).
   - Performance metrics and user engagement data are visualized using matplotlib.
   - Real-time updates are shown through plots that include user answer accuracy and time taken.

5. **Continuous Practice**:
   - Users are given the option to continue solving new exercises based on their performance.
   - The application continuously evaluates and adjusts the difficulty of exercises.

## Requirements

- Python 3.x
- numpy
- pandas
- matplotlib

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/math-exercise-generator.git
