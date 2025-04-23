import os
import django
import pandas as pd

# Configura o ambiente Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from formulario.models import DadosDiabetes

# Lê o CSV 
df = pd.read_csv(r"C:\Users\Henri\archive\diabetes.csv", sep=",") # Essa parte faz a leitura do arquivo CSV e o separa por vírgula


# Salva no banco de dados
for _, row in df.iterrows():
    DadosDiabetes.objects.using('formulario_db').create(
        gravidez=row['Pregnancies'],
        glicose=row['Glucose'],
        pressao=row['BloodPressure'],
        espessura_pele=row['SkinThickness'],
        insulina=row['Insulin'],
        imc=row['BMI'],
        pedigree=row['DiabetesPedigreeFunction'],
        idade=row['Age'],
        resultado=row['Outcome']
    )

print("Importação concluída!")
