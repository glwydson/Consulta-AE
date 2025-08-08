import sys
sys.path.append('C:/Users/Public/Downloads/Consulta-AE')
from variaveis.variaveis import var, os
from processing.processing_data import carregar_dados, filtrar_tabelas

def testar_carregamento():
    print(" Testando carregar_dados()...")
    df = carregar_dados()
    print(f" Dados carregados: {len(df)} registros.")
    assert not df.empty, "❌ O DataFrame está vazio após carregar_dados()."

def testar_filtragem():
    print(" Testando filtrar_dados()...")
    caminho_saida = r"C:\Users\Public\Downloads\Consulta-AE\Data\dados.csv"
    filtrar_tabelas()
    assert os.path.exists(caminho_saida), f"❌ O arquivo CSV filtrado não foi criado em {caminho_saida}."
    print(f" Arquivo CSV filtrado gerado: {caminho_saida}")

if __name__ == "__main__":
    dir_1, data_save = var()

    print(" Iniciando testes de processamento de dados...\n")

    if not os.path.exists(data_save):
        print("📂 CSV base não encontrado. Executando carregar_dados()...")
        testar_carregamento()
    else:
        print("📂 CSV base já existe. Pulando carregar_dados().")

    testar_filtragem()

    print("\n✅ Todos os testes foram concluídos com sucesso.")
