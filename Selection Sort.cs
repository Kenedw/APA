using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InsertionSort
{
    class Program
    {
        static void Main(string[] args)
        {
            int min, aux;
            int[] vetor = new int[] { 9, 5, 2, 1, 41, 0, 1952, 22, 3, 852, 159, 33, 6 };

            for (int i = 0; i < vetor.Length - 1; i++)
            {
                min = i;

                for (int j = i + 1; j < vetor.Length; j++)
                    if (vetor[j] < vetor[min])
                        min = j;

                if (min != i)
                {
                    aux = vetor[min];
                    vetor[min] = vetor[i];
                    vetor[i] = aux;
                }
            }
            Console.WriteLine(String.Join(", ", vetor));
            Console.ReadLine();
        }
    }
}
