import sys
sys.path.append('C:/Users/Public/Downloads/Consulta-AE') #gambiarra para que o código funcione sem problemas
from variaveis.variaveis import var, os, time#variaveis principais
from watchdog.observers import Observer #importando o observador
from watchdog.events import FileSystemEventHandler #importa classe para lidar com eventos do sistemas
from processing_data import carregar_dados, filtrar_tabelas #funçoes de processamentos de dados

dir_1, data_save= var() #Importando os dois caminhos principais

class WorkflowHandler(FileSystemEventHandler):                       #classe princiapl
    def on_modified(self, event):                                    #Nomeando função pra definir o arquivo que vai ser monitorado
        if str(event.src_path).endswith('.xlsx'):                    #definido o tipo de arquivo que vai ser monitorado   
            print(f"Detectado arquivo modificado: {event.src_path}") 
            executar_workflow()

def executar_workflow():                                             #função do fluxo de trabalho organizado a partir do
    if os.path.exists(data_save):
        print("CSV encontrado. Filtrando dados...")
        filtrar_tabelas()
    else:
        print("Base Inexistente. Convertendo Base...")
        carregar_dados()
        
print("Base carregada, convertendo e filtrando base")
filtrar_tabelas()
    

if __name__ == "__main__":
    pasta_monitorada = os.path.dirname(dir_1)
    observer = Observer()
    observer.schedule(WorkflowHandler(), path=pasta_monitorada, recursive=False)
    observer.start()

    print(f"Workflow iniciado. Monitorando: {pasta_monitorada}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
