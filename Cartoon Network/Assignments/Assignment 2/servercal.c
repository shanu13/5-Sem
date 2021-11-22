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

int main(int argc,char *argv[])
{
	if(argc<2)
	{
		fprintf(stderr,"Port no not provided ,program terminated\n");
		exit(1);
	}
	int sockfd,newsockfd,portno,n;
	char buffer[255];
	struct sockaddr_in serv_addr, cli_addr;
	socklen_t clilen;

	sockfd=socket(AF_INET,SOCK_STREAM,0);
	if(sockfd<0)
	{
		error("error opening socket");
	}
	bzero((char*) &serv_addr,sizeof(serv_addr));
	portno=atoi(argv[1]);

	serv_addr.sin_family=AF_INET;
	serv_addr.sin_addr.s_addr=INADDR_ANY;
	serv_addr.sin_port=htons(portno);

	if(bind(sockfd,(struct sockaddr *) &serv_addr, sizeof(serv_addr))<0)
		error("binding failed");
	listen(sockfd,5);
	clilen=sizeof(cli_addr);

	newsockfd=accept(sockfd,(struct sockaddr *) &cli_addr,&clilen);
	if(newsockfd<0)
		error("error on accepting");
	int num1 ,num2,ans ,choice;

 S:	n=write(newsockfd,"enter number 1 :",strlen("enter number 1 :"));
	if(n<0)
	{
		error("error writing to socket");
	}
	read(newsockfd,&num1,sizeof(int));
	printf("client: First Number is :%d\n",num1);

	n=write(newsockfd,"enter number 2 :",strlen("enter number 2 :"));
        if(n<0)
        {
                error("error writing to socket");
        }
        read(newsockfd,&num2,sizeof(int));
        printf("client:Second number is :%d\n",num2);
	
	n=write(newsockfd,"enter your choice\n 1)addition\n 2)substraction\n 3)multiplication\n 4)divison\n 5)exit\n",strlen("enter your choice\n 1)addition\n 2)substraction\n 3)multiplication\n 4)divison\n 5)exit\n"));
        if(n<0)
        {
                error("error writing to socket");
        }
        read(newsockfd,&choice,sizeof(int));
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
	write(newsockfd,&ans,sizeof(int));
	if(choice!=5)
		goto S;

Q:	close(newsockfd);
	close(sockfd);
	return 0;
}
	

