# Inheritance of Diseases Analysis

## Overview
This project explores the patterns of disease inheritance to understand how genetic factors contribute to the prevalence of various diseases across populations. We used Python (Jupyter Notebook) for data exploration and Power BI for visualization. The analysis focuses on:
 - Identifying which diseases are more likely to be inherited.
 - Examining the role of gender in disease inheritance.
 - Understanding the prevalence of inherited diseases across different locations and age groups.
 - Analyzing inheritance types (Maternal, Paternal, Both, None) to identify which type is more common.
 - Studying family history and its relation to disease transmission over generations.
 - An interactive Power BI Dashboard provides a comprehensive visualization of these insights.

### Tools Used:
**Python (Pandas, Seaborn, Matplotlib)** : For data generation, cleaning, exploration, and analysis.
**Power BI**: For creating interactive visualizations and reports.

## Analysis in Jupyter Notebook
The data cleaning and exploratory analysis were performed in Jupyter Notebook using Python libraries like Pandas, Seaborn, and Matplotlib.

### Key Steps in Jupyter Notebook:
1. **Data Generation**: 
    - Created a synthetic dataset containing information on individuals, their diseases, and the inheritance patterns.
    - Variables included gender, disease name, inheritance type (Maternal, Paternal, Both, None), age group, location, and comorbidities.
2. **Data Cleaning**:
    - Addressed missing values and ensured the accuracy of inheritance percentages based on the inheritance type.
    - Grouped diseases by type and prevalence, and validated inheritance patterns.
3. **Disease Inheritance Analysis**:
    - Analyzed the likelihood of disease inheritance.
    - Explored which diseases are more likely to be inherited.
4. **Gender-Based Inheritance**:
    - Compared the inheritance rates for males and females across various diseases.
    - This analysis focused on determining whether males or females are more likely to inherit diseases.
5. **Family History**:
    - Explored inheritance patterns across generations (1-4 generations back) and their significance for disease transmission.
6. **Location-Based Inheritance**:
    - Analyzed the inheritance patterns based on geographic location to identify which regions have a higher occurrence of inherited diseases.

## Visualizations in the Power BI Report
The Power BI report includes various visualizations to make the insights accessible:
 - Disease Inheritance Analysis: A bar chart showing the likelihood of inheritance for each disease.
 - Gender-Based Inheritance: A stacked bar chart that highlights the inheritance distribution by gender.
 - Inheritance Type Distribution: A pie chart visualizing the proportion of inheritance types (Maternal, Paternal, Both, None).
 - Location vs. Inheritance: A visualization comparing how location influences disease inheritance patterns.
 - Age Group Distribution: A filter to analyze how the prevalence of diseases changes across different age groups.

![Inheritance of Diseases report img](https://github.com/user-attachments/assets/34365e12-fdcb-48e0-bcf8-6b10d365ae78)

## Key Insights
1. **Disease Inheritance**: Diseases like Asthama and Cystic Fibrosis show higher inheritance rates compared to others.
2. **Gender-Based Patterns**: Females are slightly more likely to inherit diseases, especially in the case of maternal inheritance.
3. **Location Trends**: Regions such as India and London show a higher prevalence of inherited diseases, particularly for conditions like hypertension and heart disease.
4. **Inheritance Types**: Maternal inheritance dominates for diseases such as asthma and cancer, while paternal inheritance is common for conditions like cystic fibrosis.
5. **Family History**: Diseases inherited across generations tend to have higher rates of comorbidities, such as stroke or Alzheimer’s.



## Conclusion
This project provides an in-depth look into the inheritance patterns of diseases, revealing significant trends based on gender, location, and family history. The combination of Python for data analysis and Power BI for interactive visualization makes it easy to explore these findings and gain valuable insights into genetic disease transmission.


