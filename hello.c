#include <stdio.h> 
#include <string.h>
#include <stdlib.h>

static int j;
int q[5];
char lo[1000]="";
char v[50];

void push(int item){
	system("clear");
	if(j>=5)
		printf("Stack overflow\n");
	else {
		q[j]=item;
		printf("\nadded %d at index %d",item,j);
		sprintf(v,"\nadded %d at index %d",item,j);
		strcat(lo,v);
		j++;
	}
}

void showlog(){
	system("clear");
	printf("\n--------------LOG---------------");
	printf("%s\n",lo);
	printf("--------------------------------\n");
}

int pop(){
	system("clear");
	int item;
	if(j<=0){ 
		printf("Stack underflow\n");
		return 0;
	}
	else {
		j--;
		item=q[j];
		q[j]=0;
		printf("removed %d at index %d",item,j);
		sprintf(v,"\nremoved %d at index %d",item,j);
		strcat(lo,v);
		return item;
	}
}

void display(){
	system("clear");
	int i;
	printf("{");
	for (i = 0; i < 5; i++){
		printf("%d, ",q[i]);
	}
	printf("}");
}

int menu(){
	int a;
	printf("\n\n  Choose operation: 1)Push 2)Pop 3)Display 4)Log 5)Exit: ");
	scanf("%d",&a);
	return a;
}

main() { 
	system("clear");
	int choice,qw;
	printf("Welcome to the demonstration of queue");
	while(1){
		choice=menu();
		switch(choice){
			case 1:
				printf("\nEnter item to push : ");
				scanf("%d",&qw);
				push(qw);
				break;
			case 2:
				pop();
				break;
			case 3:
				display();
				break;
			case 4:
				showlog();
				break;
			case 5:
				exit(0);
			default:
				system("clear");
				printf("\nWrong choice!");
		}
	}
}


