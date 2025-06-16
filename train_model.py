import pandas as pd
import sqlite3
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_and_save_model():
    print("--- Iniciando o processo de treinamento ---")
    try:
        conn = sqlite3.connect('db.sqlite3')
        # MUDE AQUI o nome da tabela se for diferente
        query = "SELECT Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome FROM resultado_dadosformulario"
        df = pd.read_sql_query(query, conn)
        conn.close()
        print(f"Dados carregados do banco: {df.shape[0]} registros.")
    except Exception as e:
        print(f"Erro ao ler o banco de dados: {e}")
        return

    df.dropna(inplace=True)
    if df.empty:
        print("Não há dados suficientes para treinar.")
        return

    if df['Outcome'].dtype == 'object':
        df['Outcome'] = df['Outcome'].map({'no_diabetes': 0, 'diabetes': 1}).fillna(0)
    df['Outcome'] = df['Outcome'].astype(int)

    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    
    model_columns = X.columns
    joblib.dump(model_columns, 'artefatos/model_columns.joblib')
    print("Colunas do modelo salvas.")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"Acurácia do novo modelo: {accuracy:.4f}")

    joblib.dump(model, 'artefatos/diabetes_model.joblib')
    print("Modelo salvo com sucesso em 'artefatos/diabetes_model.joblib'")

if __name__ == '__main__':
    train_and_save_model()