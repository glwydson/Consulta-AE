# processing_data.py
import sys
sys.path.append('C:/Users/Public/Downloads/Consulta-AE')
from variaveis.variaveis import var, pd, pl, Path, os  # Importando variáveis e bibliotecas
# Diretórios e caminhos
dir_1, data_save = var()

# === FUNÇÃO DE LEITURA E CONVERSÃO ===
def carregar_dados():
    # Leitura do Excel com Pandas
    df = pd.read_excel(dir_1, engine="openpyxl")
    
    # Salvando como CSV para facilitar leitura posterior
    df.to_csv(data_save, index=False, encoding='utf-8-sig') 
    
    return df

# === FUNÇÃO DE FILTRAGEM COM POLARS ===
def filtrar_tabelas():
    # Leitura do CSV com Pandas
    df = pd.read_csv(data_save, encoding='utf-8-sig', dtype= str)
    
    # Conversão para Polars
    df_pl = pl.from_pandas(df)
    
    # Seleção de colunas desejadas
    colunas_desejadas = [
        "CIDADE", "NUM LIGACAO", "CLIENTE", "SIT LIGACAO","MEDIDOR", "DOC", "CPF CNPJ", "ENDERECO", "BAIRRO"
        ]
    #criando uma variável para colunas filtradas
    df_filtrado = df_pl.select(colunas_desejadas)
    save_polar = df_filtrado.write_csv(fr"C:\Users\Public\Downloads\Consulta-AE\Data\dados.csv")
    
    return save_polar
save_polar = filtrar_tabelas

#Função de cosultas
#Função de consultas
def consultar_dados(campo: str, valor: str):
    """
    Exemplo: consultar_dados("CPF CNPJ", "12345678900")
    """
    if not os.path.exist(save_polar):
        print("Base não carregada")
    else:
        return None
    
    
    










