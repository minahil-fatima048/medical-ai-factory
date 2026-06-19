# Automated Medical Triage and Operational Risk Pipeline

Hi! I am a Software Engineering student at the University of Sargodha. Instead of waiting for internship calls during my summer break, I am treating these 2 months like an intense corporate boot camp. This repository tracks my daily shift from vibe coding to building production-grade logic by hand.

This project is a Python operational engine designed to parse, validate, and flag patient medical data streams dynamically. It acts as a digital first-responder triage layer for hospital intake systems, ensuring zero crashes even when diagnostic fields are completely missing.

## Core Engineering Highlights
* Zero-Crash Resilience: Uses dynamic dictionary .get() lookups to intercept missing objects and prevent runtime crashes.
* Fallback Baselines: Automates baseline medical default assumptions (Heart Rate: 75, SpO2: 98, BP: 120/80) when intake data is corrupted or incomplete.
* Multi-Metric Risk Aggregation: Runs an integrated conditional priority engine leveraging logical chaining (or operators) to evaluate patient urgency dynamically.

## My Learning Progression and Bug Fixes
* Day 1 (Data Plumbing): Mastered dictionary extraction paths. Encountered syntax spacing errors and unaligned line breaks, which I manually refactored.
* Day 2 (Environment Setup): Handled local virtual environments, debugged PowerShell terminal redirection loops, and successfully deployed my local files to the cloud.

## Tech Stack and Environment
* Language: Python 3.x
* Version Control: Git and GitHub Architecture
* Environment Sandboxing: Python Virtual Environments (venv)
