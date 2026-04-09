# 📄 AI Resume Critique: RAG-Powered ATS Optimizer

**AI Resume Critique** is a console based career-tech solution that leverages **Retrieval-Augmented Generation (RAG)** and the **Google Gemini API** to provide deep, semantic analysis of professional resumes. By cross-referencing a candidate's CV against specific Job Descriptions (JD), the system identifies skill gaps, optimizes for Applicant Tracking Systems (ATS), and provides actionable, impact-driven feedback.

## 🌟 Key Features
* **RAG-Driven Analysis:** Uses a Retrieval-Augmented Generation pipeline to ensure the AI's feedback is grounded specifically in the provided Job Description.
* **ATS Gap Identification:** Automatically detects missing keywords and industry-specific certifications required by modern hiring algorithms.
* **Impact-Oriented Rewriting:** Utilizes Gemini's creative reasoning to transform "task-based" bullet points into "results-oriented" achievements.
* **Semantic Alignment Score:** Provides a percentage match based on the semantic similarity between the candidate's experience and the job's core requirements.
* **Multi-Format Support:** Robust PDF and Docx parsing to ensure accurate data extraction regardless of resume layout.

## 🧠 Technical Architecture (RAG)
Unlike standard chatbots, this tool utilizes a specialized RAG workflow to minimize "hallucinations" and maximize accuracy:

1.  **Ingestion:** Extracts text from the User's CV and the Target Job Description.
2.  **Retrieval:** Fragments the JD into core "Competency Clusters" (Skills, Experience, Cultural Fit).
3.  **Augmentation:** Injects these clusters into the prompt context for the Gemini Model.
4.  **Generation:** The Gemini API processes the augmented context to produce a structured critique that is strictly aligned with the employer's needs.

## 🛠️ Tech Stack
* **LLM Engine:** Google Gemini API (Generative AI SDK)
* **Framework:** Python (LangChain / LlamaIndex for RAG orchestration)
* **Backend:** FastAPI / Streamlit
* **Document Processing:** PyPDF2 / PDFMiner
* **Prompt Engineering:** Custom templates for Chain-of-Thought (CoT) reasoning

## 📂 Project Structure
```text
AI-Resume-Critique/
├── main.py              # Main Application Entry Point, AG logic & Gemini API integration
├── tests/              # Sample Resumes & JDs for testing
└── requirements.txt    # Project Dependencies
