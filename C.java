import java.util.Scanner;
class  C {
	public static void main(String[] args) {
		System.out.println("Enter Any Two Values For Calculating Sum :");
		Scanner s=new Scanner(System.in);
		int a,b,c;
		a=s.nextInt();
		b=s.nextInt();

		c=a+b;
		System.out.println("The Sum Of a And b Value is :"+c);
	}
}
