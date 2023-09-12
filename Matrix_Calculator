#include <stdio.h>
#define ROWS 3
#define COLUMNS 3

void printMatrix(int matrix[ROWS][COLUMNS]) {
    for(int i = 0; i < ROWS; i++) {
        for(int j = 0; j < COLUMNS; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

void addMatrices(int matrixA[ROWS][COLUMNS], int matrixB[ROWS][COLUMNS], int result[ROWS][COLUMNS]) {
    for(int i = 0; i < ROWS; i++) {
        for(int j = 0; j < COLUMNS; j++) {
            result[i][j] = matrixA[i][j] + matrixB[i][j];
        }
    }
}

int main() {
    int matrixA[ROWS][COLUMNS] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int matrixB[ROWS][COLUMNS] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int result[ROWS][COLUMNS];

    addMatrices(matrixA, matrixB, result);
    printMatrix(result);

    return 0;
}
