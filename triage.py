# Day 1 Logic File (triage.py)

def process_patient(patient_data):
    name = patient_data.get("name", "Unknown")
    age = patient_data.get("age")
    vitals = patient_data.get("vitals")
    
    if vitals is None:
        heart_rate = 75  
        spo2 = 98
        systolic_bp = 120
        diastolic_bp = 80
    else:
        heart_rate = vitals.get("heart_rate", 75)
        spo2 = vitals.get("spo2", 98)
        systolic_bp = vitals.get("systolic_bp", 120)
        diastolic_bp = vitals.get("diastolic_bp", 80)

    print(f"\n[SYSTEM LOG] Processing records locally for: {name}")
    
    if heart_rate > 120:
        status = "CRITICAL: Immediate ICU Intervention Required"
    elif heart_rate > 100:
        status = "WARNING: Monitor closely"
    else:
        status = "STABLE: Standard ward"

    if spo2 < 90:
        status = "CRITICAL: Patient suffocating! Immediate ICU Intervention Required"
    if systolic_bp > 140 or diastolic_bp > 90:
        status = "Critical: Hypertension detected! Immediate ICU Intervention Required"
        
    return {
        "patient_name": name,
        "triage_status": status,
        "urgency_level": "HIGH" if (heart_rate > 100 or spo2 < 90 or systolic_bp > 140 or diastolic_bp > 90) else "LOW"
    }
