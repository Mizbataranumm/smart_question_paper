# 📄 Smart Question Paper Generator

A Python-based tool to automatically generate question papers from a predefined question bank stored in CSV format.

## 🚀 Features
- Loads questions from a CSV file
- Randomly selects questions for the paper
- Displays marks for each question

## 📂 Project Structure
smart_question_paper/
│
├── main.py # Main script to generate papers
├── requirements.txt # Python dependencies
├── data/
│ └── sample_questions.csv # Question bank
└── database.sql # Optional DB structure for future
## 🛠️ How to Run
1. **Clone the repository**
   git clone https://github.com/Mizbataranumm/smart_question_paper.git
   cd smart_question_paper
2. **Install dependencies**
    pip install -r requirements.txt
3. **Run the script**
    python main.py

**Example Output**

🚀 Starting Smart Question Paper Generator...
🔄 Loading CSV...
✅ Loaded 8 questions
📄 Generating question paper...

📘 Your Generated Question Paper:

1. Define DBMS. [Marks: 6]
2. List the departments with more than 5 employees using relational algebra. [Marks: 7]
3. Write an SQL query to delete a record from EMPLOYEE table. [Marks: 5]
4. Write a short note on data models. [Marks: 7]
5. Retrieve names of employees who work in 'Sales' department. [Marks: 7]

---

For `requirements.txt`, just add:

Once you update both files, run:
```powershell
git add README.md requirements.txt
git commit -m "Updated README and requirements"
git push
