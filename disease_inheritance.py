import pandas as pd
import random

# Initialize the dataset
data = []

# Synthetic dataset parameters
num_rows = 1000
diseases = ['Diabetes', 'Heart Disease', 'Cystic Fibrosis', 'Hypertension', 'Cancer', 'Asthma', 'Breast Cancer', 'Obesity']
inheritance_types = ['Maternal', 'Paternal', 'Both', 'None']
genders = ['Male', 'Female']
locations = ['New York', 'London', 'Canada', 'Germany', 'Japan', 'India', 'Italy', 'France', 'Korea', 'China', 'Africa']
age_groups = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61+']
comorbidities = ['Hypertension', 'Stroke', 'None', 'Arthritis', 'Alzheimer’s']

# Data generation
for i in range(num_rows):
    year_of_birth = random.randint(1950, 2024)
    age = 2024 - year_of_birth
    
    # Determine age group
    if age <= 10:
        age_group = '0-10'
    elif age <= 20:
        age_group = '11-20'
    elif age <= 30:
        age_group = '21-30'
    elif age <= 40:
        age_group = '31-40'
    elif age <= 50:
        age_group = '41-50'
    elif age <= 60:
        age_group = '51-60'
    else:
        age_group = '61+'

    # Randomly select the inheritance type
    inheritance_type = random.choice(inheritance_types)
    
    # Set inheritance percentages based on the inheritance type
    if inheritance_type == 'Maternal':
        inheritance_percentage_mother = random.uniform(50, 100)
        inheritance_percentage_father = 0
    elif inheritance_type == 'Paternal':
        inheritance_percentage_mother = 0
        inheritance_percentage_father = random.uniform(50, 100)
    elif inheritance_type == 'Both':
        inheritance_percentage_mother = random.uniform(25, 75)
        inheritance_percentage_father = 100 - inheritance_percentage_mother
    else:  # 'None'
        inheritance_percentage_mother = 0
        inheritance_percentage_father = 0

    # Create the survey dictionary using the previously selected inheritance type
    survey = {
        'Person_ID': i + 1,
        'Gender': random.choice(genders),
        'Year_of_Birth': year_of_birth,
        'Age_Group': age_group,
        'Location': random.choice(locations),
        'Disease_Name': random.choice(diseases),
        'Inheritance_Type': inheritance_type,  # Use the same inheritance_type from above
        'Generations_Back': random.randint(1, 4),
        'Comorbidity_Diseases': random.choice(comorbidities),
        'Inheritance_Percentage_Mother': round(inheritance_percentage_mother, 2),
        'Inheritance_Percentage_Father': round(inheritance_percentage_father, 2),
        'Statistical_Significance': random.choice(['Yes', 'No'])
    }
    
    # Append the survey to the dataset
    data.append(survey)

# Convert to DataFrame
df = pd.DataFrame(data)

# Display first few rows to verify
print(df.head())

# Save the DataFrame to CSV
df.to_csv('disease_inheritance_data.csv', index=False)
