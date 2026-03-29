# Job Application Assistant

A small AI-assisted web application for analyzing job listings and helping tailor application materials.
<img width="1285" height="850" alt="image" src="https://github.com/user-attachments/assets/a66e3a4e-91b1-4c1a-b992-32f86777c0b0" />

## What it does

This project provides a simple interface where a user can:

- paste a job listing
- add profile notes or CV highlights
- choose between different assistance modes
- get structured help for job applications

Current modes include:

- **Job Ad Analyzer**: extracts key skills, responsibilities, and what to emphasize
- **CV / Cover Letter Helper**: suggests relevant strengths, CV bullet ideas, and application angles

## Why I built it

I built this project to learn the practical side of AI application development:

- frontend / backend separation
- safe API key handling
- structured prompt building
- conversation history management
- integrating LLM-powered features into a usable tool

## Tech stack

- Python
- Flask
- HTML / CSS / JavaScript
- OpenAI API
- dotenv

## Features

- Flask backend with separate frontend
- mode selector for different job-search tasks
- conversation history
- loading state and disabled inputs while waiting
- clear chat button
- structured input fields for:
  - job listing
  - profile / CV notes
  - extra instructions

## Project structure

```text
job-application-assistant/
  app.py
  requirements.txt
  README.md
  .gitignore
  templates/
    index.html
  static/
    style.css
