# Agentic-Job-Application-Helper
 
<img width="540" alt="image" src="https://github.com/user-attachments/assets/493a5b39-d49e-4690-8d52-12b6d90f1011" />


## Overview
This repository hosts a Streamlit-based AI-powered application designed to streamline and enhance job application processes. By leveraging advanced language models (LangGraph and Groq API LLMs), it automatically tailors resumes and prepares interview questions based on specific job postings.

## Features
- **Job Posting Analysis**: Automatically extracts required skills, qualifications, and experiences from job postings.
- **Resume Parsing**: Reads and analyzes uploaded PDF resumes.
- **Resume Tailoring**: Creates customized resumes matching the extracted job requirements.
- **Interview Preparation**: Generates relevant interview questions and talking points tailored to both the candidate profile and job requirements.

## Tech Stack
- **LangGraph**: For building a state-driven multi-agent workflow.
- **Groq API (LLAMA 3)**: High-performance language model for parsing and generating text.
- **Streamlit**: Interactive web UI for user-friendly interactions.
- **PyPDF2**: Extracts and processes text from PDF resumes.
- **Pydantic**: Ensures structured data handling and validation.



### Prerequisites
- Python 3.8+
- Groq API Key

### Setup

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/job-application-helper.git
cd job-application-helper
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Configure Environment Variables**:
Create a `.env` file in your project directory and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key
```

## Running the Application
```bash
streamlit run main.py
```

The application will be available at:
```
http://localhost:8501
```

## Usage

### Step-by-Step
1. **Open the web application in your browser**.
2. **Input the URL** of the job posting you're interested in.
3. **Upload your resume** as a PDF file.
4. Click **Submit**.

The application will:
- Analyze the job posting.
- Parse your resume.
- Generate a tailored resume highlighting relevant experiences and skills.
- Provide customized interview questions and talking points.

## Project Structure
```
.
├── main.py                       # Streamlit application entry point
├── chains.py                     # Core LangGraph workflow definitions
├── requirements.txt              # Python dependencies
├── .env                          # Environment configuration (API keys)
└── README.md                     # Project documentation
```

## Contributing
Contributions are welcome! Feel free to fork this repo, open an issue, or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
- **Author**: [Pratik Shankar Jadhav](https://github.com/pratikjadhav2726)
- **LinkedIn**: [Pratik Shankar Jadhav](https://www.linkedin.com/in/pratikjadhav2726)

---

Happy job hunting! 🚀📑

