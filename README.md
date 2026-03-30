link to run this streamlit app:
https://fundamentals-in-ai-and-ml-eh4mhnvb9xzcmenhd6ozme.streamlit.app/L

# Student Performance Predictor

##  Overview

The **Student Performance Predictor** is a web-based application developed using Python and Streamlit. It helps students estimate their academic performance based on key factors such as study hours, attendance, and sleep patterns.

The application not only predicts marks but also provides personalized suggestions to improve performance, making it a practical self-assessment tool.

---

## Problem Statement

Students often lack awareness of how their daily habits affect their academic results. There is no simple system that gives real-time feedback based on study behavior.

This project aims to:

* Predict student performance before exams
  
* Highlight weak areas
  
* Provide actionable advice

---

##  Features

*  Interactive multi-step user interface
  
*  Subject-wise performance prediction
  
*  Smart logic-based evaluation (not random)
   
*  Balanced scoring (study + attendance + sleep)
  
*  Personalized improvement suggestions
   
*  Restart functionality

---

## 🛠️ Technologies Used

* Python
  
* Streamlit
  
* VS Code
  
* GitHub


##  Usage

1. Open the app in your browser
2. Click on **Start**
3. Enter your name
4. Input:

   * Sleep hours
   * Study hours (per subject)
   * Attendance percentage
5. Click on **Predict Performance**
6. View:

   * Predicted marks
   * Overall average
   * Personalized advice

---

##  Prediction Logic

The system uses a rule-based approach:

* Study hours → Major contribution
  
* Attendance → Moderate contribution
  
* Sleep → Performance modifier

### Additional Conditions:

* Low study + high attendance → penalized
* High study + low attendance → penalized
* Very low or high sleep → reduces efficiency

This ensures realistic and fair predictions.

---

##  Output

The application displays:

* Subject-wise predicted marks
  
* Overall average score
  
* Performance category (Good / Average / Needs Improvement)
  
* Customized advice for improvement

---

##  Challenges Faced

* Setting up Streamlit environment
 
* Resolving pip and PATH issues
  
* Designing balanced scoring logic
  
* Creating smooth multi-step UI

---

##  Learning Outcomes

* Built a real-world application using Python
  
* Learned Streamlit framework
  
* Improved debugging and problem-solving skills
  
* Understood user experience design basics

---

##  Future Enhancements

* Machine Learning-based prediction
  
* Graphical performance charts
  
* User login system
  
* Data storage and history tracking

---

##  Author

**Shriya Parmar**

---

##  Conclusion

This project demonstrates how simple logic and programming can be used to solve real-life academic problems. It helps students become more aware of their habits and improve their performance effectively.

