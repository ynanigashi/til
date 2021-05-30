#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long get_credit_number(void);
string get_type(long credit_number);
bool is_valid_number(long credit_number);
long del_first_one_digits(long num, int num_of_digits);

int main(void)
{
    // get credit number
    long credit_number = get_credit_number();

    // get card type
    string type = get_type(credit_number);

    // check valid number
    if (strcmp(type, "INVALID") != 0)
    {
        if (is_valid_number(credit_number) == false)
        {
            type = "INVALID";
        }
    }

    // print result
    printf("%s\n", type);
}

// get credit number
long get_credit_number(void)
{
    long credit_number;
    do
    {
        credit_number = get_long("Number: ");
    }
    while (credit_number < 0);
    return credit_number;
}

// get num of digits
int get_num_of_digits(long n)
{
    int digit = 0;
    while (n != 0)
    {
        n = n / 10;
        digit++;
    }
    return digit;
}

int get_first_n_digits(int n, long num, int num_of_digits)
{
    long mask = 1;
    int first_n_digits = 0;
    for (int i = 0; i < num_of_digits - n; i++)
    {
        mask *= 10;
    }
    first_n_digits = num / mask;
    return first_n_digits;
}

string get_type(long credit_number)
{
    // AMEX conditions
    int AMEX_NUM_OF_DIGITS = 15;
    int AMEX_FIRST_TWO_DIGITS_1 = 34;
    int AMEX_FIRST_TWO_DIGITS_2 = 37;

    // master card conditions
    int MASTERCARD_NUM_OF_DIGITS = 16;
    int MASTERCARD_FIRST_TWO_DIGITS_MIN = 51;
    int MASTERCARD_FIRST_TWO_DIGITS_MAX = 55;

    // visa conditions
    int VISA_NUM_OF_DIGITS_1 = 13;
    int VISA_NUM_OF_DIGITS_2 = 16;
    int VISA_FIRST_ONE_DIGIT = 4;

    // get number of digits
    int num_of_digits = get_num_of_digits(credit_number);

    // get first deigits
    int first_one_digits = get_first_n_digits(1, credit_number, num_of_digits);
    int first_two_digits = get_first_n_digits(2, credit_number, num_of_digits);

    //check amex
    if (num_of_digits == AMEX_NUM_OF_DIGITS)
    {
        if (first_two_digits == AMEX_FIRST_TWO_DIGITS_1 || first_two_digits == AMEX_FIRST_TWO_DIGITS_2)
        {
            return "AMEX";
        }
    }
    //check master card
    if (num_of_digits == MASTERCARD_NUM_OF_DIGITS)
    {
        if (MASTERCARD_FIRST_TWO_DIGITS_MIN <= first_two_digits && first_two_digits <= MASTERCARD_FIRST_TWO_DIGITS_MAX)
        {
            return "MASTERCARD";
        }
    }
    //check visa
    if (num_of_digits == VISA_NUM_OF_DIGITS_1 || num_of_digits == VISA_NUM_OF_DIGITS_2)
    {
        if (first_one_digits == VISA_FIRST_ONE_DIGIT)
        {
            return "VISA";
        }
    }
    return "INVALID";
}

bool is_valid_number(long credit_number)
{
    int num_of_digits = get_num_of_digits(credit_number);
    int current_digits = 1;
    int even_sum = 0;
    int odd_sum = 0;

    // sum degits
    while (credit_number > 1)
    {
        int i =  credit_number % 10;
        if (current_digits % 2 == 0)
        {
            if (i < 5)
            {
                even_sum += i * 2;
            }
            if (i == 5)
            {
                even_sum += 1;
            }
            if (i == 6)
            {
                even_sum += 3;
            }
            if (i == 7)
            {
                even_sum += 5;
            }
            if (i == 8)
            {
                even_sum += 7;
            }
            if (i == 9)
            {
                even_sum += 9;
            }
        }
        else
        {
            odd_sum += i;
        }
        credit_number = credit_number / 10;
        current_digits++;
    }

    // culculate checksum
    if ((even_sum + odd_sum) % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}