#include <cs50.h>
#include <stdio.h>

void print_step(int air, int block);

int main(void)
{
    // Prompt for get height
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 |  8 < height);

    // generate mario's pyramid
    for (int i = 1; i <= height; i++)
    {
        print_step(height - i, i);
    }
}

//print air
void print_air(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%c", ' ');
    }
}

//print blocks
void print_blocks(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%c", '#');
    }
}

//print ditch
void print_ditch(void)
{
    print_air(2);
}

//print step
void print_step(int air, int block)
{
    print_air(air);
    print_blocks(block);
    print_ditch();
    print_blocks(block);
    printf("%s", "\n");
}