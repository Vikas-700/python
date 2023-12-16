/**** Program to Traverse a 2-D Array ****/
#include <stdio.h>
void traverse();
int a[50][50], m, n;
main()
{
int i, j;
printf("\nEnter number of rows & cols: ");
scanf("%d%d", &m, &n);
printf("\nEnter elements of 2-D array:\n");
for(i=0; i<m; i++)
for(j=0; j<n; j++)
scanf("%d", &a[i][j]);
printf("\n\n2-D array before traversing:\n\n");
for(i=0; i<m; i++)
{
for(j=0; j<n; j++)
printf("\t%d", a[i][j]);
printf("\n\n");
}
traverse();
printf("\n\n2-D array after traversing:\n\n");
for(i=0; i<m; i++)
{
for(j=0; j<n; j++)
printf("\t%d", a[i][j]);
printf("\n\n");
}
getch();
}

void traverse()
{
int i, j;
for(i=0; i<m; i++)
for(j=0; j<n; j++)
a[i][j] = a[i][j]*2;
}