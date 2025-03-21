import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from langgraph.graph import StateGraph, END
from dotenv import load_dotenv
import streamlit as st
from typing import Dict, Any
from pydantic import BaseModel, ValidationError
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()

llm = ChatGroq(model_name="llama3-70b-8192", groq_api_key=os.getenv("GROQ_API_KEY"))

class JobRequirements(BaseModel):
    skills: list
    qualifications: str
    experience: str
def extract_resume_skills(state):
    resume_text = state["resume"]
    prompt = PromptTemplate.from_template(
    """Extract the most relevant technical and professional skills from the following resume:
    {resume}
    Return the skills as a comma-separated list."""
    )
    chain = prompt | llm
    return chain.invoke({"resume": resume_text}).content
    # Define agent functions
def research_job_posting(state):
    url = state["url"]
    prompt = PromptTemplate.from_template(
        """Analyze the job posting at {url} and extract:
        - Required skills
        - Qualifications
        - Experience
        Return as JSON."""
    )
    chain = prompt | llm | JsonOutputParser()
    return {**state,"requirements":chain.invoke({"url": url})}

def profile_candidate(state):
    resume_text = state["resume"]
    prompt = PromptTemplate.from_template(
        """Summarize the resume below:
        {resume}
        Return skills, experiences, education, and strengths as JSON."""
    )
    chain = prompt | llm | JsonOutputParser()
    return {**state,"profile":chain.invoke({"resume": resume_text})}

def tailor_resume(state):
    profile, requirements = state["profile"],state["requirements"]
    prompt = PromptTemplate.from_template(
        """Using candidate profile:
        {profile}
        and job requirements:
        {requirements}
        tailor the resume highlighting relevant skills and experiences."""
    )
    chain = prompt | llm
    return {**state,"tailored_resume":chain.invoke({"profile": profile, "requirements": requirements}).content}

def prepare_interview(state):
    profile, requirements = state["profile"],state["requirements"]
    prompt = PromptTemplate.from_template(
        """Based on candidate profile:
        {profile}
        and job requirements:
        {requirements}
        Prepare 5 interview questions and key talking points."""
    )
    chain = prompt | llm
    return {**state,"interview_materials":chain.invoke({"profile": profile, "requirements": requirements}).content}

# LangGraph Workflow Definition
workflow = StateGraph(Dict[str, Any])
workflow.add_node("researcher", research_job_posting)
workflow.add_node("profiler", profile_candidate)
workflow.add_node("resume_strategist", tailor_resume)
workflow.add_node("interview_preparer", prepare_interview)
workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "profiler")
workflow.add_edge("profiler", "resume_strategist")
workflow.add_edge("resume_strategist", "interview_preparer")
workflow.add_edge("interview_preparer", END)
app = workflow.compile()


