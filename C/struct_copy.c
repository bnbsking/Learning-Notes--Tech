#include <stdio.h>
#include <stdlib.h>

typedef struct{
    int height;
    char* color;
    char* name;
}Dog;

Dog modifyDog(Dog d){
    d.height = 100;
    d.color = "black";
    d.name[0] = 'm';
    d.name[1] = 'o';
    d.name[2] = 'n';
    d.name[3] = 's';
    d.name[4] = 't';
    return d;
}

int main()
{
    Dog a;
    a.height = 20;
    a.color = "yellow";
    a.name = calloc(5,sizeof(char));
    a.name[0] = 's';
    a.name[1] = 'h';
    a.name[2] = 'i';
    a.name[3] = 'b';
    a.name[4] = 'a';
    printf("%x %x %x %x\n", &a, &a.height, a.color, a.name);
    
    Dog b = a;
    printf("%x %x %x %x\n\n", &b, &b.height, b.color, b.name);
    b.height = 30;
    b.color = "white";
    b.name[0] = 'c';
    b.name[1] = 'o';
    b.name[2] = 'r';
    b.name[3] = 'g';
    b.name[4] = 'i';
    
    Dog c = modifyDog(a);
    printf("%d %s %s\n", a.height, a.color, a.name);
    printf("%d %s %s\n", b.height, b.color, b.name);
    printf("%d %s %s\n", c.height, c.color, c.name);
    
    return 0;
}
