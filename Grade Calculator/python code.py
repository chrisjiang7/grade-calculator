#!/usr/bin/env python
# coding: utf-8

# # Computing 3 Assignment
# 

# ---
# ## Background
# 
# Generating statistics from a set of data is a task that computers love. In this assignment, you and your team will be implementing a grade processing system that will generate the mean and standard deviation for a set of final exam grades.
# 
# We will assume that final grades are stored in a list, where each entry in the list is a string with the following format:
# 
# <div align="center">
# "studentNum-finalGrade%"
# </div>
# 
# The string represents the final exam mark (*finalGrade*) that the student (*studentNum*) achieved. For example, the cell below contains a list of final exam marks from two students. Student **1007089** achieved a mark of **91%**, and student **1009989** achieved a mark of **77.5%**.
# 
# ```
# grades = ['1007089-91%','1009989-77.5%']
# ```
# 
# We want to calculate the mean final exam mark from a list of grades. If we assume that we have **N** grades, the mean **$\bar{x}$** can be calculated from the following formula:
# 
# 
# <br/>
# \begin{align}
#   \bar{x} = \frac{1}{N}\sum_{i=0}^{N-1} x_i \tag{1}
# \end{align}
# <br/>
# 
# The variable **$x_i$** represents each grade in our list at index i. We assume that we start counting at 0.
# 
# We also want to be able to calculate the standard deviation from a list of grades. The standard deviation measures the amount of variability in our data set. For example, let’s say we want to compute the average and standard deviation for the grades [80, 90, 70, 60]. The average of these grades is 75, and the standard deviation is 11.2. Now imagine we want to compute the average and standard deviation for the grades [80, 76 ,74, 70]. The average of these grades is 75, but the standard deviation is 3.6. Although both sets of grades have the same average, the second set has a smaller standard deviation. The reason is because the grades are not as “spread out” as the grades in the first set. The grades in the second set deviate from their average by a small amount.
# 
# The standard deviation $\sigma$ is calculated using our mean $\bar{x}$ and the following formula:
# 
# <br/>
# \begin{align}
#   \sigma = \sqrt{\frac{1}{N}\sum_{i=0}^{N-1} (x_i-\bar{x})^2} \tag{2}
# \end{align}
# <br/>
# 
# The requirements of the program are given below.
# 
# 
# 

# ---
# ## Requirements
# 
# The requirements of the program are given below. Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks.
# 
# 1. Define a function **extractGrade**(*x*):
#   - ***x***: A *string* containing a student number and grade in the format "studentNum-Grade%"
#   - **Return**: The student's grade as a *float*.
#   
# 
# 2. Define a function **classAverage**(*final_marks*):
#   - ***final_marks***: A *list* of strings, where each string is formatted as "studentNum-Grade%".
#   - **Return**: The mean grade of the grades in *final_marks* calculated using equation (1).<br/>*(Hint: Use your **extractGrade** function and a for loop!)*
# 
# 
# 3. Define a function **classStdDev**(*final_marks*):
#   - ***final_marks***: A *list* of strings, where each string is formatted as "studentNum-Grade%".
#   - **Return**: The standard deviation of the grades in *final_marks* calculated using equation (2).

# ---
# ## Implementation
# Please define all functions in the cell below

# In[7]:


# YOUR CODE HERE
def extractGrade(x):
    splitstudentnumber=x.split('-') #splits student number and grade into 2 indexs
    gradewithnopercent=splitstudentnumber[1].strip('%') #goes into index 1 and gets rid of the % sign
    return float(gradewithnopercent) #returns grade as a float

def classAverage(final_marks):
    count1=0
    for grade in final_marks:
        count1 += 1
        totalsum += gradewithnopercent #sums grades
    average=totalsum/count1    
    return float(average)
    
def classStdDev(final_marks):
    count2=0
    for standard in final_marks():
        count2 += 1
        sumvalue += (gradewithnopercent(standard)-average(final_marks))**2
    dev=(sumvalue/count2)**0.5
    return float(dev)


# ---
# ## Testing
# 
# The following code creates a main function that you can use to test out your code once you have implemented your functions.
# 
# ```
# def main():
#   final_exam_grades = ["1003324-71.5%","1001425-99.5%","1009980-86.0%","1001480-84.0%","1005244-87.0%"]
#   avg = classAverage(final_exam_grades)
#   std_dev = classStdDev(final_exam_grades)
#   print("Final exam class average:",round(avg,3),"%")
#   print("Final exam standard deviation:",round(std_dev,3),"%")
# main()
# ```
# 
# Copy the code and paste it into the cell below. Run the cell to verify that your code works correctly with the provided input. The following message should be printed after the main() function above is run:
# 
# >*Final exam class average: 85.6 %<br/>
# >Final exam standard deviation: 8.907 %<br/>*
# 
# 
# 
# 
# 
# 
# 

# In[17]:


# PASTE CODE HERE
def extractGrade(x):
    splitstudentnumber=x.split('-') #splits student number and grade into 2 indexs
    gradewithnopercent=splitstudentnumber[1].strip('%') #goes into index 1 and gets rid of the % sign
    return float(gradewithnopercent) #returns grade as a float

def classAverage(final_marks):
    count1=0
    totalsum=0
    for grade in final_marks:
        count1 += 1
        totalsum += extractGrade(grade) #sums grades
    average=totalsum/count1    
    return float(average)
    
def classStdDev(final_marks):
    count2=0
    sumvalue=0
    for standard in final_marks:
        count2 += 1
        sumvalue += (extractGrade(standard)-classAverage(final_marks))**2
    dev=(sumvalue/count2)**0.5
    return float(dev)

def main():
    final_exam_grades = ["1003324-71.5%","1001425-99.5%","1009980-86.0%","1001480-84.0%","1005244-87.0%"]
    avg = classAverage(final_exam_grades)
    std_dev = classStdDev(final_exam_grades)
    print("Final exam class average:",round(avg,3),"%")
    print("Final exam standard deviation:",round(std_dev,3),"%")
main()


# Note that your code is not necessarily correct if your output matches the expected output. Your code will be checked against multiple inputs for correctness. The cell above it not graded, so feel free to modify the code as you wish!

# ---
# ## Reflective Questions
# 
# 1. Assume that you always supply the correctly formatted input into your **classAverage** and **classStdDev** functions. That is, a list where entries are strings that follow the “studentNum-finalGrade%” format. Is there any input that can cause your program to fail?
# 
# 2. How would your code change if the string format was changed from “studentNum-finalGrade%” to “studentNum:finalGrade”? You do not need to implement this change but explain what needs to be modified. 
# 
# 3. Can you compute the average and standard deviation grade using a single for loop? Why or why not.
# 
# Please answer all questions in the cell below!

# ```
# 1. Assuming that the format is the same, I dont think there is any input that would cause the program to fail.
# 2. Only the extract grade function needs to be modified because you dont need the strip method anymore because there is no percent being inputed. As well as the hyphen in the split function would need to be changed to a colon.
# 3. You can not compute the average and standard deviation grade using a single for loop because you need the average to calculate the standard deviation. And this simply can't be done at the same time. You would need to do this in separate for loops.
# ```

# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 3 dropbox on avenue with the naming convention: macID_CL3.py
# 
# This assignment is due the day after your Lab A section at 11:59 PM EST
# 
# Late labs will not be accepted
