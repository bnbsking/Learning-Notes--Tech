#include <stdio.h>
#include <time.h>

int main() {
	
	FILE* f = fopen("example.txt", "a");	//a:append w:overwrite  
	if(f==NULL) return 1;
	fprintf(f, "hello world %d \n", time(0));
	fclose(f);
	
	char c;
	f = fopen("example.txt", "r");	//r:read
	if(f==NULL) return 1;
	while((c=getc(f))!=EOF) printf("%c",c);
	fclose(f);
	
	return 0;
}
