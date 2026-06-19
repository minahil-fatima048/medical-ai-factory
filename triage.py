# Day 1: Multi-Metric Crash-Proof Production Pipeline

def process_patient(patient_data):
    name = patient_data.get("name", "Unknown")
    age = patient_data.get("age")
    
    vitals = patient_data.get("vitals")
    
    if vitals is None:
        print("[ALERT] Vitals completely missing! Using fallback baseline.")
        heart_rate = 75  
        spo2 = 98
        systolic_bp = 120
        diastolic_bp = 80
    else:
        heart_rate = vitals.get("heart_rate", 75)
        spo2 = vitals.get("spo2", 98)
        systolic_bp = vitals.get("systolic_bp", 120)
        diastolic_bp = vitals.get("diastolic_bp", 80)

    print(f"\n[SYSTEM LOG] Processing records for: {name}")
    
    # Logic filtering based on calculated heart_rate
    if heart_rate > 120:
        status = "CRITICAL: Immediate ICU Intervention Required"
    elif heart_rate > 100:
        status = "WARNING: Monitor closely"
    else:
        status = "STABLE: Standard ward"

    # FIX 1: Pulled text string onto the same line to avoid syntax breaks
    if spo2 < 90:
        status = "CRITICAL: Patient suffocating! Immediate ICU Intervention Required"
    if systolic_bp > 140 or diastolic_bp > 90:
        status = "Critical: Hypertension detected! Immediate ICU Intervention Required"
    return {
        "patient_name": name,
        "triage_status": status,
        # FIX 2: Modified the priority engine to flag HIGH if heart rate is high OR oxygen is critically low
        "urgency_level": "HIGH" if (heart_rate > 100 or spo2 < 90 or systolic_bp > 140 or diastolic_bp > 90 ) else "LOW"
    }

# TEST CASE: Patient with dangerous oxygen levels
incoming_patient = {
    "name": "Zahid",
    "age": 45,
    "vitals": {"heart_rate": 72, "spo2": 97,"systolic_bp":155,"diastolic_bp":95}
}

# Running the production pipeline
medical_report = process_patient(incoming_patient)
print("\n--- FINAL GENERATED MEDICAL REPORT ---")
print(medical_report)
