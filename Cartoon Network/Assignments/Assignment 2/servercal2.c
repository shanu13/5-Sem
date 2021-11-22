#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>

void error(const char *msg)
{
	perror(msg);
	exit(1);
}

int setup_server(short port ,int backlog)
{
	int server_socket,client_socket,addr_size;
	struct sockaddr_in serv_addr;	
	server_socket=socket(AF_INET,SOCK_STREAM,0);
	if(server_socket<0)
	{
		error("error opening socket");
	}
	serv_addr.sin_family=AF_INET;
	serv_addr.sin_addr.s_addr=INADDR_ANY;
	serv_addr.sin_port=htons(port);
	if(bind(server_socket,(struct sockaddr *) &serv_addr, sizeof(serv_addr))<0)
		error("binding failed");
	listen(server_socket,5);
	return server_socket;
}

int accept_new_connection(int server_socket)
{
//	int addr_size=sizeof(SA_IN);
	int client_socket;
	struct sockaddr_in cli_addr;
	socklen_t clilen;
	clilen=sizeof(cli_addr);
	client_socket=accept(server_socket,(struct sockaddr *) &cli_addr,&clilen);
	if(client_socket<0)
		error("error on accepting");
	return client_socket;
}

void *handle_connection(int client_socket)
{
	char buffer[255];
	int num1 ,num2,ans ,choice,n;

 S:	n=write(client_socket,"enter number 1 :",strlen("enter number 1 :"));
	if(n<0)
	{
		error("error writing to socket");
	}
	read(client_socket,&num1,sizeof(int));
	printf("client: First Number is :%d\n",num1);

	n=write(client_socket,"enter number 2 :",strlen("enter number 2 :"));
        if(n<0)
        {
                error("error writing to socket");
        }
        read(client_socket,&num2,sizeof(int));
        printf("client:Second number is :%d\n",num2);
	
	n=write(client_socket,"enter your choice\n 1)addition\n 2)substraction\n 3)multiplication\n 4)divison\n 5)exit\n",strlen("enter your choice\n 1)addition\n 2)substraction\n 3)multiplication\n 4)divison\n 5)exit\n"));
        if(n<0)
        {
                error("error writing to socket");
        }
        read(client_socket,&choice,sizeof(int));
        printf("client choice is :%d\n",choice);
	switch(choice)
	{
		case 1:
			ans=num1+num2;
			break;
		case 2:
			ans=num1-num2;
			break;
		case 3:
			ans=num1*num2;
			break;
		case 4:
			ans=num1/(num2);
			break;
		case 5:
			goto Q;
	}
	write(client_socket,&ans,sizeof(int));
	if(choice!=5)
		goto S;
	Q:	close(client_socket);
}

int main(int argc,char *argv[])
{
	if(argc<2)
	{
		fprintf(stderr,"Port no not provided ,program terminated\n");
		exit(1);
	}
	int z=0;	
	int portno=atoi(argv[1]);
	int server_socket=setup_server(portno,5);
	while(1)
	{
			int status=0;
			pid_t childID=fork();
			if(childID<0)
			{
				perror("fork()");
			}
			else if(childID==0)
			{
				int client_socket=accept_new_connection(server_socket);
                        	handle_connection(client_socket);
			}
			else
			{
				int client_socket=accept_new_connection(server_socket);
                        	handle_connection(client_socket);
			}
	}
	close(server_socket);
	return 0;
}
	

