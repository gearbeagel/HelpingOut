#include <stdio.h>
#include <omp.h>

int main() {
    int n = 1000;
    int a, b;
    int k = 4;

#pragma omp parallel num_threads(n)
    {
        int thread_num = omp_get_thread_num();
        int num_threads = omp_get_num_threads();
        int num_procs = omp_get_num_procs();

        printf("I am thread %d out of %d threads! Number of processors: %d\n", thread_num, num_threads, num_procs);
    }

printf("\n");
#pragma omp parallel shared(b) private(a)
    {
        b = omp_get_thread_num();
        if (b == 0)
        {
            a = omp_get_num_threads();
            printf("Number of threads = %d\n", a);
        }

        printf("Thread %d starting...\n", b);
    }
   
printf("\n");
#pragma omp parallel num_threads(k)
    {
        int thread_num = omp_get_thread_num();
        int num_threads = omp_get_num_threads();

        printf("Thread %d out of %d threads executing parallel region\n", thread_num, num_threads);

        
#pragma omp sections
        {
            // Section 1
#pragma omp section
            {
                printf("Thread %d executing section 1\n", thread_num);
            }

            // Section 2
#pragma omp section
            {
                printf("Thread %d executing section 2\n", thread_num);
            }

            // Section 3
#pragma omp section
            {
                printf("Thread %d executing section 3\n", thread_num);
            }
        }
    }


    return 0;
}