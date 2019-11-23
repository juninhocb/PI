#include <sys/socket.h>
#include <arpa/inet.h> //inet_addr
#include <unistd.h>    //write
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#pragma pack(1)
/*
typedef struct payload_t {
    uint32_t id;
    uint32_t counter;
    float temp;
} payload;
*/
//#pragma pack()

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


int createSocket(int port)
{
    int sock;
    struct sockaddr_in server;

    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        printf("ERROR: Socket não criado\n");
        exit(1);
    }
    printf("Socket criado\n");

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

int main()
{
    int PORT = 2300;
    int BUFFSIZE = 512;
    char buff[BUFFSIZE];
    int ssock, csock;
    int nread;
    struct sockaddr_in client;
    unsigned int clilen = sizeof(client);
    struct sockaddr_in serv_addr; 

    ssock = createSocket(PORT);
    printf("Servidor está funcionando na porta: %d\n", PORT);

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    serv_addr.sin_port = htons(2300);

    bind(ssock, (struct sockaddr*)&serv_addr, sizeof(clilen)); 

    listen(ssock, 10); 

    while (1)
    {
        csock = accept(ssock, (struct sockaddr *)&client, &clilen);
        if (csock < 0)
        {
            printf("Error: Conexão Fail\n");
            continue;
        }

        printf("Conexão bem sucedida com %s\n", inet_ntoa(client.sin_addr));
        bzero(buff, BUFFSIZE);
        while ((nread=read(csock, buff, BUFFSIZE)) > 0)
        {
            printf("\nRecebido %d bytes\n", nread);
            payload *p = (payload*) buff;
            /*printf("Conteúdo recebido: rpm=%d, velocidade=%d, temp=%f\n",
                    p->rpm, p->vel, p->temp, p->acel, p->dist, p->comb, p->);*/


            printf("Contéudo recebido: rpm=%d, vel=%d, temp=%f, acel=%d, dist=%d, comb=%d, volt=%d, ambtemp=%d\n",
            p->rpm, p->vel, p->temp, p->acel, p->dist, p->comb, p->volt, p->ambtemp);



            printf("Evnia os dados de volta.. ");
            sendMsg(csock, p, sizeof(payload));
        }

    }

    closeSocket(ssock);
    printf("sair");
    return 0;
}
