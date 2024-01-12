import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulando dados fictícios para o exemplo
dados = {
    'Dia': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
    'Horas_Trabalhadas': [8, 7, 8.5, 6.5],
    'Bugs_Corrigidos': [5, 8, 3, 6],
    'Tarefas_Concluidas': [10, 12, 8, 15]
}

df = pd.DataFrame(dados)

# Análise exploratória
print("Resumo Estatístico:")
print(df.describe())

# Visualização 1: Total de Horas Trabalhadas por Dia
plt.figure(figsize=(10, 6))
sns.barplot(x='Dia', y='Horas_Trabalhadas', data=df)
plt.title('Total de Horas Trabalhadas por Dia')
plt.xlabel('Dia')
plt.ylabel('Horas Trabalhadas')
plt.show()

# Visualização 2: Média Diária de Bugs Corrigidos
df['Media_Bugs_Corrigidos'] = df['Bugs_Corrigidos'].mean()

plt.figure(figsize=(10, 6))
sns.lineplot(x='Dia', y='Media_Bugs_Corrigidos', data=df, marker='o')
plt.title('Média Diária de Bugs Corrigidos')
plt.xlabel('Dia')
plt.ylabel('Média de Bugs Corrigidos')
plt.show()

# Visualização 3: Produtividade Diária (Tarefas Concluídas por Hora)
df['Produtividade'] = df['Tarefas_Concluidas'] / df['Horas_Trabalhadas']

plt.figure(figsize=(10, 6))
sns.barplot(x='Dia', y='Produtividade', data=df)
plt.title('Produtividade Diária (Tarefas Concluídas por Hora)')
plt.xlabel('Dia')
plt.ylabel('Produtividade')
plt.show()
