import os
from google import genai
# CONNECTING LINK: Importing your Day 1 logic directly into Day 2
from triage import process_patient

def generate_ai_medical_summary(patient_report):
    """
    Takes the structured report dictionary from Day 1 and 
    uses Gemini to generate a professional clinical brief.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "ERROR: System API Key is missing. Check your environment configuration."
        
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
    You are an expert hospital triage assistant. 
    Analyze this incoming automated patient report and write a 2-sentence clinical brief for the on-duty doctor.
    
    Patient Name: {patient_report['patient_name']}
    Current Status: {patient_report['triage_status']}
    Urgency Flag: {patient_report['urgency_level']}
    
    Format the output exactly like this:
    Clinical Brief: [Your brief here]
    Immediate Next Step: [Your recommended action here]
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    return response.text

# ==========================================
# RUNNING THE CONNECTED SYSTEM
# ==========================================

# New live patient test case (Suffocation Risk)
live_patient_data = {
    "name": "Kamran",
    "age": 29,
    "vitals": {
        "heart_rate": 85,
        "spo2": 84,  # Low oxygen!
        "systolic_bp": 115,
        "diastolic_bp": 75
    }
}

print("--- INITIALIZING MULTI-MODULE INTERACTIVE PIPELINE ---")

# Step 1: Run your Day 1 local calculations
calculated_report = process_patient(live_patient_data)

# Step 2: Pass that real-time report to your Day 2 AI Brain
print("[SYSTEM LOG] Passing calculated report to Gemini Cloud API...")
ai_brief = generate_ai_medical_summary(calculated_report)

print("\n--- CONNECTED PRODUCTION PIPELINE OUTPUT ---")
print(ai_brief)
