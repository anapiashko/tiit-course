#include <stdio.h>
#include <string.h>
#include <time.h>
int main() {
    int r;
    int boolian = 1;
    while (boolian) {
        srand(time(0));
        r = rand() % 10 + 1;
        switch (r) {
            case 1:
                printf("I\n");
                break;
            case 2:
                printf("II\n");
                break;
            case 3:
                printf("III\n");
                break;
            case 4:
                printf("IV\n");
                break;
            case 5:
                printf("V\n");
                break;
            case 6:
                printf("VI\n");
                break;
            case 7:
                printf("VII\n");
                break;
            case 8:
                printf("VIII\n");
                break;
            case 9:
                printf("IX\n");
                break;
            case 10:
                printf("X\n");
                break;
        }
        int arab;
        printf("arabean view = ");
        scanf_s("%d", &arab);
        getchar();
        char toolongarr[4][255] = { "Tooooooooo long broo, r u kidding?",
                                    "My little brother even can do it faster",
                                    "Anastasia even can do it faster",
                                    "Even year didn't pass" };
        char mistakesarr[4][255] = { "Go to first form",
                                     "OMG YOU CAN'T EVEN SOLVE IT WHAT THE HEEEEEEEEL",
                                     "You are INVALID",
                                     "Pyfagor perevernulsya bi v grobu" };
        int phrases;
        phrases = rand() % 4 + 1;
        if (arab == r)
            printf("%s\n", toolongarr[phrases]);
        else
            printf("%s\n", mistakesarr[phrases]);
        printf("would you like to continue playing? (yes/no) \n");
        char answer[4];
        gets(answer);
        getchar();
        printf("%s\n", answer);
        if (answer == "no") {
//boolian--;
            break;
        }
    }
    system("pause");
    return 0;
}

Ещё
