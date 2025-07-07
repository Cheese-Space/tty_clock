#include <time.h>
#include <stdlib.h>
#include <ncurses.h>
#include <signal.h>
char* get_time() {
	time_t t;
	struct tm *unformated_t;
	static char formated_time[8];
	time(&t);
	unformated_t = localtime(&t);
	strftime(formated_time, sizeof(formated_time), "%H:%M:%S", unformated_t);
	return formated_time;
}
void sigint_exit() {
	endwin();
	exit(0);
}
int main() {
	initscr();
	noecho();
	nodelay(stdscr, TRUE);
	attron(A_BOLD);
	curs_set(0);
	signal(SIGINT, sigint_exit);
	char quit;
	int x;
	int y;
	int center_x;
	int center_y;
	int begining = time(NULL);
	while(1) {
		quit = getch();
		if (quit == 'q') {
			break; 
		}
		erase();
		getmaxyx(stdscr, y, x);
                center_x = (x - 8) / 2;
		center_y = (y - 1) /2;
		mvaddstr(center_y, center_x, get_time());
		if (time(NULL) - begining <= 10) {
			mvaddstr(y - 1, (x - 15) / 2, "press q to quit");
		}
		refresh();
	}
	endwin();
	return 0;
}
