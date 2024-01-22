# Relatório de Progresso Diário

Este projeto tem como objetivo gerar um relatório de progresso diário para avaliar a produtividade dos funcionários com base em diferentes métricas, como horas trabalhadas, bugs corrigidos e tarefas concluídas.

## Como Utilizar

1. **Pré-requisitos:**
   - Certifique-se de ter o Python e as bibliotecas necessárias instaladas. Você pode instalar as dependências executando o comando:
     ```bash
     pip install -r requirements.txt
     ```

2. **Execução do Código:**
   - Execute o script `analise_progresso.py` para realizar a análise exploratória e gerar visualizações.
     ```bash
     python analise_progresso.py
     ```

3. **Resultados:**
   - Os resultados serão exibidos no console e visualizações gráficas serão salvas no diretório `imagens/`.

4. **Métricas Adicionais:**
   - Para obter métricas específicas do progresso diário, você pode executar os seguintes comandos no script `analise_progresso.py`:
     ```python
     # Total de Horas Trabalhadas
     total_horas_trabalhadas = df['Horas_Trabalhadas'].sum()
     print(f'Total de Horas Trabalhadas: {total_horas_trabalhadas} horas')

     # Média Diária de Horas Trabalhadas
     media_diaria_horas_trabalhadas = df['Horas_Trabalhadas'].mean()
     print(f'Média Diária de Horas Trabalhadas: {media_diaria_horas_trabalhadas} horas')

     # Total de Bugs Corrigidos
     total_bugs_corrigidos = df['Bugs_Corrigidos'].sum()
     print(f'Total de Bugs Corrigidos: {total_bugs_corrigidos} bugs')

     # Média Diária de Bugs Corrigidos
     media_diaria_bugs_corrigidos = df['Bugs_Corrigidos'].mean()
     print(f'Média Diária de Bugs Corrigidos: {media_diaria_bugs_corrigidos} bugs')

     # Total de Tarefas Concluídas
     total_tarefas_concluidas = df['Tarefas_Concluidas'].sum()
     print(f'Total de Tarefas Concluídas: {total_tarefas_concluidas} tarefas')

     # Média Diária de Tarefas Concluídas
     media_diaria_tarefas_concluidas = df['Tarefas_Concluidas'].mean()
     print(f'Média Diária de Tarefas Concluídas: {media_diaria_tarefas_concluidas} tarefas')

     # Produtividade Diária (Tarefas Concluídas por Hora)
     df['Produtividade'] = df['Tarefas_Concluidas'] / df['Horas_Trabalhadas']
     produtividade_diaria = df[['Dia', 'Produtividade']]
     print('\nProdutividade Diária (Tarefas Concluídas por Hora):\n', produtividade_diaria)
     ```

## Estrutura do Projeto

- **`dados_diarios.csv`**: Arquivo CSV contendo dados fictícios para o exemplo.
- **`analise_progresso.py`**: Script principal para análise exploratória e geração de visualizações.
- **`imagens/`**: Diretório para armazenar as visualizações geradas.

## Requisitos

- Python 3.x
- Bibliotecas Python: pandas, matplotlib, seaborn

## Contribuição

Sinta-se à vontade para contribuir, abrir issues ou fornecer feedback. Suas contribuições são bem-vindas!


