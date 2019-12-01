#include "thinger/thinger.h"
#include <sys/socket.h>
#include <arpa/inet.h> //inet_addr
#include <unistd.h>    //write
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Alias do programa
#define USER_ID             "juninhocb"
#define DEVICE_ID           "Raspberry"
#define DEVICE_CREDENTIAL   "Teste12345"

// Declaração de estrutura de dados
#pragma pack(1)
typedef struct payload_t {
    int rpm;
    int vel;
    float temp;
    int acel;
    int dist;
    int comb;
    int volt;
    int ambtemp;
} payload;
#pragma pack()

// Declaração de Funções
int createSocket(int port);
void closeSocket(int sock);
void sendMsg(int sock, void* msg, int msgsize);

// Função Main do Programa
int main(int argc, char *argv[])
{
    // Conectando-se ao thinger
    thinger_device thing(USER_ID, DEVICE_ID, DEVICE_CREDENTIAL);

    // Instanciando as variáveis locais do Main
	int PORT = 2300;
    int BUFFSIZE = 512;
    char buff[BUFFSIZE];
    int ssock, csock;
    int nread;
    struct sockaddr_in client;
    int clilen = sizeof(client);

    // Chamar a função que criará o socket para utilização do mesmo para comunicação na porta 2300
    ssock = createSocket(PORT);
    printf("Servidor está funcionando na porta: %d\n", PORT);


    while (1){

         thing["sum"] = [](pson& in, pson& out){
        out["result"] = (int) in["value1"] + (int) in["value2"];
    };

    	thing.handle();  //Inicia a comunicação com a nuvem

        printf("Volto aqui");
        thing["LED"] << [](pson& in){

                };


        // Recebendo a conexão do clinete
		csock = accept(ssock, (struct sockaddr *)&client, (socklen_t*)&clilen);
        if (csock < 0)
        	{
            printf("Error: Conexão Fail\n");
            continue;
        	}

		printf("Conexão bem sucedida com %s\n", inet_ntoa(client.sin_addr));
        bzero(buff, BUFFSIZE); // Instancia o Buffer

		// Enquanto houver mensagens do Cliente ao servidor.... ler as mensagens
        while ((nread=read(csock, buff, BUFFSIZE)) > 0)
        	{
            printf("\nRecebido %d bytes\n", nread);
  			payload *p = (payload*) buff;

		// Mostra os pacotes recebidos se houver (Efeito de teste)
			printf("Contéudo recebido: rpm=%d, vel=%d, temp=%f, acel=%d, dist=%d, comb=%d, volt=%d, ambtemp=%d\n",
        	p->rpm, p->vel, p->temp, p->acel, p->dist, p->comb, p->volt, p->ambtemp);

			printf("Evnia os dados de volta.. ");  //...
        	sendMsg(csock, p, sizeof(payload));
    		}
		}

	// Fechará o Socket se necessário
	closeSocket(ssock);
    printf("sair");
	return 0;

}

// Funções do Programa
int createSocket(int port)
{
    int sock, err;
    struct sockaddr_in server;
    // Criação do socket "sock"
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        printf("ERROR: Socket não criado\n");
        exit(1);
    }
    printf("Socket criado\n");

    // Conectando e fazendo bind do server na estrutura de dados
    bzero((char *) &server, sizeof(server));
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(port);
    if (bind(sock, (struct sockaddr *)&server , sizeof(server)) < 0)
    {
        printf("ERROR: Bind não funcionou\n");
        exit(1);
    }
    printf("Bind feit com sucesso!\n");

    listen(sock , 3);

    return sock;
}

void closeSocket(int sock)
{
    // Fechar a conexão socket
    close(sock);
    return;
}

void sendMsg(int sock, void* msg, int msgsize)
{
    if (write(sock, msg, msgsize) < 0)
    {
        printf("Não enviou a mensagem.\n");
        exit(1);
    }
    printf("Mensagem enviada (%d bytes).\n", msgsize);
    return;
}
