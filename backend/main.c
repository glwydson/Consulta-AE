#include <stdio.h>
#include <stdlib.h>

int main() {
    char campo[50];
    char valor[100];

    printf("Digite o campo para consulta (ex: CPF CNPJ, CLIENTE, NUM LIGACAO): ");
    fgets(campo, sizeof(campo), stdin);

    printf("Digite o valor para consulta: ");
    fgets(valor, sizeof(valor), stdin);

    // Remove quebras de linha
    campo[strcspn(campo, "\n")] = 0;
    valor[strcspn(valor, "\n")] = 0;

    // Monta o comando Python
    char comando[300];
    snprintf(comando, sizeof(comando),
             "python -c \"from processing_data import consultar_dados; consultar_dados('%s', '%s')\"",
             campo, valor);

    // Executa o comando
    system(comando);

    return 0;
}
