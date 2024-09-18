public class file_24_7_4 {
	public static void main(String[]args){
	int[][] a =new int[5][5];
	int sum=0;
	for(int i =0;i<5;i++)
	{
		for(int j=0;j<5;j++)
		{
			a[i][j]=j+1;

		}

	}
	
	for(i=0;i<5;i++)
	{
		for(j=0;j<5;j++)
		{
			sum+=a[i][i];
			System.out.println(a[i][j]+" ");
		
		}
		System.out.println("\n");

	}

	System.out.println(sum);
	}

}
