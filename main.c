#include <stdio.h>
#include <stdlib.h>

int get_1st_weekday(int year){

int day;
day = (((year - 1) * 365) + ((year - 1) / 4) - ((year - 1) / 100) + ((year) / 400) + 1) % 7;
return day;
}

int main()
{
    system("COLOR 3F");
    int year, daysInMonth, day, weekDay = 0, startingDay;
    printf("Enter your desired year: ");
    scanf("%d", &year);
    char *months[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
    int monthDay[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    if(year % 4 == 0 && year % 100 != 0 || year % 400 ==0) // Year is leap
        monthDay[1] = 29;

      startingDay =  get_1st_weekday(year);
    for (int month = 0; month < 12; month++)
    {
         daysInMonth = monthDay[month];
         printf("\n\n----------------%s---------------\n", months[month]);
         printf("\n   Su   Mo   Tu   We   Th   Fr   Sa\n");


        for(weekDay = 0; weekDay < startingDay; weekDay++)
            printf("     ");

        for (day = 1; day <= daysInMonth; day++){
            printf("%5d", day);

        if(++weekDay > 6){
            printf("\n");
            weekDay = 0;
        }
        startingDay = weekDay;
        }

    }






    return 0;
}
