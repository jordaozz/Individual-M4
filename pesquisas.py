#Total de Horas Trabalhadas:
total_horas_trabalhadas = df['Horas_Trabalhadas'].sum()
print(f'Total de Horas Trabalhadas: {total_horas_trabalhadas} horas')

#Média Diária de Horas Trabalhadas:
media_diaria_horas_trabalhadas = df['Horas_Trabalhadas'].mean()
print(f'Média Diária de Horas Trabalhadas: {media_diaria_horas_trabalhadas} horas')

#Total de Bugs Corrigidos:
total_bugs_corrigidos = df['Bugs_Corrigidos'].sum()
print(f'Total de Bugs Corrigidos: {total_bugs_corrigidos} bugs')

#Média Diária de Bugs Corrigidos:
media_diaria_bugs_corrigidos = df['Bugs_Corrigidos'].mean()
print(f'Média Diária de Bugs Corrigidos: {media_diaria_bugs_corrigidos} bugs')

#Total de Tarefas Concluídas:
total_tarefas_concluidas = df['Tarefas_Concluidas'].sum()
print(f'Total de Tarefas Concluídas: {total_tarefas_concluidas} tarefas')

#Média Diária de Tarefas Concluídas:
media_diaria_tarefas_concluidas = df['Tarefas_Concluidas'].mean()
print(f'Média Diária de Tarefas Concluídas: {media_diaria_tarefas_concluidas} tarefas')

#Produtividade Diária (Tarefas Concluídas por Hora):
df['Produtividade'] = df['Tarefas_Concluidas'] / df['Horas_Trabalhadas']
produtividade_diaria = df[['Dia', 'Produtividade']]
print('\nProdutividade Diária (Tarefas Concluídas por Hora):\n', produtividade_diaria)




