#include <stdio.h>
#include <stdlib.h>

struct Car1{
    int wheel;
    char* color;
};

typedef struct{
    int wheel;
    char* color;
}Car2;

int main()
{
    struct Car1 a;
    a.wheel = 4;
    a.color = "red";
    printf("%d %s \n", a.wheel, a.color); //printf("?", a); a is struct object cannot print
    
    struct Car1* b = malloc(1*sizeof(struct Car1)); //b is pointer so b[0] is invalid so does *b
    b->wheel = 5;
    b->color = "blue";
    printf("%d %s \n", b->wheel, b->color);

    Car2 c;
    c.wheel = 6;
    c.color = "green";
    printf("%d %s \n", c.wheel, c.color);
    
    Car2* d = malloc(1*sizeof(Car2));
    d->wheel = 7;
    d->color = "black";
    printf("%d %s \n", d->wheel, d->color);
    
    return 0;
}
