import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

caminho_do_arquivo = '/content/da-ebac/gasolina.csv'
dados = pd.read_csv(caminho_do_arquivo)

sns.lineplot(x='dia', y='venda', data=dados, palette='viridis')

plt.title('Gráfico do preço da gasolina ao longo dos dias')
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.savefig('/content/da-ebac/gasolina.png')


with open('/content/da-ebac/gasolina.py', 'w') as f:
    f.write('codigo_python')