using System;

namespace mergeSort
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			int[] array = new int[] { 1, 13, 4, 11, 34, 2, 14, 23, 34};
			mergeSort (array, 0, array.Length - 1);
			foreach (int i in array){
				Console.WriteLine (i);
			}
		}
		public  static void mergeSort(int[] array, int p, int r)
		{
			if (p < r) {
				int q = (p + r) / 2;
				mergeSort (array, p, q);
				mergeSort (array, q + 1, r);
				merge (array, p, q, r);
			}
		}

		public static void merge(int[] array, int p, int q, int r)
		{
			int[] tempA = new int[q-p+1];
			int[] tempB = new int[r-q];

			for (int i=0; i<q-p+1; i++) {
				tempA [i] = array [p + i];
			}
			for (int j=0; j<r-q; j++) {
				tempB [j] = array [q + j + 1];
			}

			int g = 0;
			int h = 0;

			for (int k=p; k<=r; k++) {
				if (g<tempA.Length && (h==tempB.Length || tempA [g] <= tempB [h])) {
					array [k] = tempA [g];
					g++;
				} else {
					array [k] = tempB [h];
					h++;
				}
			}
		}


	}
}
