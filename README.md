AI Competency-Based Classroom Evaluator (CBSE Science)
AI-assisted tool for competency-based evaluation of student answers aligned with Bloom’s Taxonomy.

What this project does
- Evaluates student answers  
- Identifies expected vs achieved understanding level  
- Extracts evidence from the answer  
- Highlights learning gaps  
- Suggests improvement
  
Features
•	Demo Mode (no API required)
•	AI Mode (dynamic evaluation using OpenAI)
•	History tracking
•	Download evaluation results
________________________________________
Tech Stack
•	Python
•	Streamlit
•	OpenAI API
________________________________________
How it works
User enters a question and student answer →
App sends prompt to AI →
AI returns structured evaluation →
App displays result
________________________________________
Run locally
pip install -r requirements.txt
streamlit run app.py
________________________________________
Note
This project focuses on prompt design and evaluation logic rather than complex model training.

