import pandas as pd
import glob
import os

# 1. SETUP: Load all your uploaded files
# (Assuming all unzipped CSVs are in a folder named 'aadhaar_data')

def load_and_merge_data():
    print("Loading Data... this might take a minute.")
    
    # Load Enrolment Data (The 'Fresh' entries)
    enrol_files = glob.glob("api_data_aadhar_enrolment*.csv")
    df_enrol = pd.concat((pd.read_csv(f) for f in enrol_files), ignore_index=True)
    # Rename columns for clarity
    df_enrol = df_enrol.rename(columns={'age_0_5': 'enrol_0_5', 'age_5_17': 'enrol_5_17', 'age_18_greater': 'enrol_18_plus'})

    # Load Biometric Data (The 'Update' entries - Critical for fraud detection)
    bio_files = glob.glob("api_data_aadhar_biometric*.csv")
    df_bio = pd.concat((pd.read_csv(f) for f in bio_files), ignore_index=True)
    df_bio = df_bio.rename(columns={'bio_age_5_17': 'bio_update_child', 'bio_age_17_': 'bio_update_adult'})

    # Load Demographic Data (Address/Name changes)
    demo_files = glob.glob("api_data_aadhar_demographic*.csv")
    df_demo = pd.concat((pd.read_csv(f) for f in demo_files), ignore_index=True)
    df_demo = df_demo.rename(columns={'demo_age_5_17': 'demo_update_child', 'demo_age_17_': 'demo_update_adult'})

    # 2. MERGE: Combine them into one Master DataFrame
    # We merge on Date, State, District, and Pincode
    merge_cols = ['date', 'state', 'district', 'pincode']
    
    # First merge Enrolment + Biometric
    df_master = pd.merge(df_enrol, df_bio, on=merge_cols, how='outer').fillna(0)
    
    # Then merge with Demographic
    df_master = pd.merge(df_master, df_demo, on=merge_cols, how='outer').fillna(0)

    # Convert date to datetime object for sorting
    df_master['date'] = pd.to_datetime(df_master['date'], format='%d-%m-%Y', errors='coerce')
    
    print(f"Data Loaded Successfully! Total Rows: {len(df_master)}")
    return df_master

# Run the function
df = load_and_merge_data()

# 3. QUICK INSIGHT: Check for "Ghost" Centers
# (Pincodes with huge updates but zero new enrolments - suspicious!)
df['suspicion_score'] = df['bio_update_adult'] / (df['enrol_18_plus'] + 1)
suspicious_pincodes = df.sort_values(by='suspicion_score', ascending=False).head(10)

print("\nTOP 10 SUSPICIOUS PINCODES (High Biometric Updates vs Low Enrolment):")
print(suspicious_pincodes[['state', 'pincode', 'date', 'suspicion_score']])
# ... your existing print statements ...
print(suspicious_pincodes[['state', 'pincode', 'date', 'suspicion_score']])

# ADD THIS LINE TO SAVE THE FILE:
df.to_csv("master_data.csv", index=False)
print("✅ master_data.csv saved successfully!")