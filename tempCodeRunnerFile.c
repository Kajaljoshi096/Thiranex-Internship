#include <stdio.h>
int main() {
    int score = 0;
    
    for (int row = 1; row <= 3; row++) {
        for (int col = 3; col >= 1; col--) {
            // Pay close attention to the short-circuit behavior here!
            if ((row == col) || ((row + col) % 2 == 0 && ++score > 0)) {
                score += 2;
            } else {
                score -= 1;
            }
        }
    }
    printf("Final Score = %d\n", score);
    return 0;
}