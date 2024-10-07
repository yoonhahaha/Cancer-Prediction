import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def func():
    symptom_to_cancer = {
        1: "Weight loss",
        2: "Fatigue",
        3: "Fever",
        4: "Skin changes",
        5: "Bleeding",
        6: "Nausea",
        7: "Vomiting",
        8: "Pain",
        9: "Shortness of breath",
        10: "Dizziness",
        11: "Cough",
        12: "Urination problems",
        13: "Difficulty swallowing",
        14: "Swelling",
        15: "Decreased appetite",
        16: "Constipation",
        17: "Diarrhea",
        18: "Sweating",
        19: "Skin rash",
        20: "Headache"
    }
    cancer_symptoms = {
        "Liver Cancer": [1, 4, 7],
        "Kidney Cancer": [1, 2, 5, 8],
        "Oral and Oropharyngeal Cancer": [5, 6, 7],
        "Bronchial and Lung Cancer": [1, 2, 9, 11],
        "Laryngeal Cancer": [2, 10, 11],
        "Gallbladder and Bile Duct Cancer": [1, 2, 3, 8],
        "Malignant Melanoma": [4, 19],
        "Leukemia": [1, 2, 3, 5, 6],
        "Hodgkin's Lymphoma": [2, 3, 1],
        "Multiple Myeloma": [1, 2, 8],
        "Breast Cancer": [5, 15],
        "Prostate Cancer": [2, 12],
        "Thyroid Cancer": [1, 13],
        "Stomach Cancer": [1, 3, 6, 7],
        "Bladder Cancer": [5, 12],
        "Cervical Cancer": [5, 12],
        "Ovarian Cancer": [1, 2, 14],
        "Uterine Cancer": [5, 12],
        "Brain and Central Nervous System Cancer": [2, 10, 20],
        "Non-Hodgkin's Lymphoma": [2, 3, 1],
        "Pancreatic Cancer": [1, 7, 15],
        "Esophageal Cancer": [1, 3, 6, 7, 13],
        "Testicular Cancer": [1, 8],
        "Nasopharyngeal Cancer": [2, 9],
        "Other Pharyngeal Cancer": [2, 13],
        "Colorectal Cancer": [5, 16, 17],
        "Non-Melanoma Skin Cancer": [4, 19],
        "Mesothelioma": [2, 9]
    }
    cancer_prevention = {
        "Liver Cancer": "Avoid excessive alcohol consumption",
        "Kidney Cancer": "Avoid smoking",
        "Oral and Oropharyngeal Cancer": "Maintain good oral hygiene",
        "Bronchial and Lung Cancer": "Avoid smoking or exposure to secondhand smoke",
        "Laryngeal Cancer": "Avoid smoking and excessive alcohol use",
        "Gallbladder and Bile Duct Cancer": "Maintain a healthy weight",
        "Malignant Melanoma": "Use sunscreen with high SPF",
        "Leukemia": "Avoid exposure to high doses of radiation",
        "Hodgkin's Lymphoma": "Maintain a healthy immune system",
        "Multiple Myeloma": "Maintain a healthy weight",
        "Breast Cancer": "Perform regular self-examinations",
        "Prostate Cancer": "Eat a healthy diet rich in fruits and vegetables",
        "Thyroid Cancer": "Avoid unnecessary exposure to radiation",
        "Stomach Cancer": "Avoid smoking",
        "Bladder Cancer": "Avoid smoking",
        "Cervical Cancer": "Get vaccinated against HPV",
        "Ovarian Cancer": "Consider genetic testing if there is a family history",
        "Uterine Cancer": "Maintain a healthy weight",
        "Brain and Central Nervous System Cancer": "Avoid exposure to ionizing radiation",
        "Non-Hodgkin's Lymphoma": "Avoid exposure to chemicals and radiation",
        "Pancreatic Cancer": "Avoid smoking",
        "Esophageal Cancer": "Avoid smoking",
        "Testicular Cancer": "Perform regular self-examinations",
        "Nasopharyngeal Cancer": "Avoid smoking",
        "Colorectal Cancer": "Eat a diet high in fiber, fruits, and vegetables",
        "Non-Melanoma Skin Cancer": "Avoid excessive sun exposure",
        "Mesothelioma": "Avoid exposure to asbestos"
    }
    cancer_death_rate = {
        "Liver Cancer": 20,
        "Kidney Cancer": 10,
        "Oral and Oropharyngeal Cancer": 15,
        "Bronchial and Lung Cancer": 35,
        "Laryngeal Cancer": 12,
        "Gallbladder and Bile Duct Cancer": 25,
        "Malignant Melanoma": 5,
        "Leukemia": 18,
        "Hodgkin's Lymphoma": 8,
        "Multiple Myeloma": 30,
        "Breast Cancer": 10,
        "Prostate Cancer": 8,
        "Thyroid Cancer": 4,
        "Stomach Cancer": 20,
        "Bladder Cancer": 12,
        "Cervical Cancer": 6,
        "Ovarian Cancer": 15,
        "Uterine Cancer": 7,
        "Brain and Central Nervous System Cancer": 25,
        "Non-Hodgkin's Lymphoma": 20,
        "Pancreatic Cancer": 40,
        "Esophageal Cancer": 30,
        "Testicular Cancer": 3,
        "Nasopharyngeal Cancer": 18,
        "Colorectal Cancer": 12,
        "Non-Melanoma Skin Cancer": 2,
        "Mesothelioma": 45,
        "Other Pharyngeal Cancer": 15
    }

    user_age = int(input("Enter your age: "))
    user_symptoms = list(map(int, input(
    '''Enter the symptom codes (comma-separated):
1: Weight loss
2: Fatigue
3: Fever
4: Skin changes
5: Bleeding
6: Nausea
7: Vomiting
8: Pain
9: Shortness of breath
10: Dizziness
11: Cough
12: Urination problems
13: Difficulty swallowing
14: Swelling
15: Decreased appetite
16: Constipation
17: Diarrhea
18: Sweating
19: Skin rash
20: Headache
'''
).split(',')))

    match_percentages = []
    death_rates = []
    output_text = ""
    matching_cancers = []

    for cancer, symptoms in cancer_symptoms.items():
        match_count = sum(1 for symptom in user_symptoms if symptom in symptoms)
        if match_count > 0:
            match_percentage = (match_count / len(symptoms)) * 100
            death_rate = cancer_death_rate[cancer]
            prevention = cancer_prevention[cancer]
            match_percentages.append(match_percentage)
            death_rates.append(death_rate)
            matching_cancers.append(cancer)

    x_labels = matching_cancers
    x = np.arange(len(x_labels))

    fig, ax = plt.subplots(figsize=(14, 8))

    ax.bar(x, match_percentages, label='Cancer Risk (%)', color='b')
    ax.plot(x, death_rates, color='r', marker='o', linestyle='-', linewidth=2, label='Death Rate (%)')

    max_match_index = np.argmax(match_percentages)
    ax.bar(x[max_match_index], match_percentages[max_match_index], color='yellow', alpha=0.5)

    max_death_index = np.argmax(death_rates)
    ax.plot(x[max_death_index], death_rates[max_death_index], color='yellow', marker='o', markersize=10)

    ax.set_xlabel('Cancer Types')
    ax.set_ylabel('Percentage')
    ax.set_title('Cancer Risk and Death Rates')
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels, rotation=90)
    ax.legend()

    plt.tight_layout()
    plt.show()

    highest_risk_index = np.argmax(match_percentages)
    highest_death_index = np.argmax(death_rates)
    highest_synthesis_index = np.argmax(np.array(match_percentages) + np.array(death_rates))

    highest_risk_cancer = matching_cancers[highest_risk_index]
    highest_risk_value = match_percentages[highest_risk_index]
    highest_death_cancer = matching_cancers[highest_death_index]
    highest_death_value = death_rates[highest_death_index]
    highest_synthesis_cancer = matching_cancers[highest_synthesis_index]
    highest_synthesis_value = match_percentages[highest_synthesis_index] + death_rates[highest_synthesis_index]

    root = tk.Tk()
    root.title("Cancer Risk Analysis")

    output_text = (
        f"당신이 걸릴수 있는 가장 높은 확률을 가지고 있는 암은 {highest_risk_cancer} ({highest_risk_value:.2f}%) 입니다. 이 암을 막으려면 {cancer_prevention[highest_risk_cancer]} 을/를 하셔야 합니다."
        f"하지만, 가장 높은 사망 위험을 가지고 있는 암은  {highest_death_cancer} ({highest_death_value:.2f}%)입니다. 이 암을 막으려면 {cancer_prevention[highest_risk_cancer]} 을/를 하셔야 합니다.\n"
        f"가장 높은 평균 위험은 {highest_synthesis_cancer}입니다."
        f"이 암을 막으려면 {cancer_prevention[highest_synthesis_cancer]} 을/를 하셔야 합니다"
    )

    label = tk.Label(root, text=output_text, padx=20, pady=20)
    label.pack()

    root.mainloop()

func()
