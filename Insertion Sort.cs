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
            int i, j, atual;
            int [] vetor = new int[] { 9,5,2,1,41,0,1952,22,3,852,159,33,6};


            for (i = 1; i < vetor.Length; i++)
            {
                atual = vetor[i];
                j = i;
                while ((j > 0) && (vetor[j - 1] > atual))
                {
                    vetor[j] = vetor[j - 1];
                    j = j - 1;
                }
                vetor[j] = atual;
            }
            Console.WriteLine(String.Join(", ", vetor));
            Console.ReadLine();
        }
    }
}
