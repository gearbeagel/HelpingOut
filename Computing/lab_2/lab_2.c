#include <stdio.h>
#include <omp.h>

int main() {
    int N;
    printf("Enter N: ");
    scanf("%d", &N);

    int A[N][N], B[N][N], C[N][N], total;

    printf("Enter values for matrix A:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    printf("Enter values for matrix B:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    double start_time = omp_get_wtime();

    #pragma omp parallel for schedule(static) shared(A, B) reduction(+:total) 
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("[%d]: calculation of the iteration number %d.\n", omp_get_thread_num(), i);
            int sum = 0;
            for (int k = 0; k < N; k++) {
                sum += A[i][k] * B[k][j];
            }
            C[i][j] = sum;
	    total = sum;
        }
    }
    double end_time = omp_get_wtime();

    printf("Total: %d\n", total);
    printf("Час виконання програми: %f секунд\n", end_time - start_time);

    return 0;
}
