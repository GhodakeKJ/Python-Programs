import java.util.Scanner;
class Multiplay {
	public static void main(String[]args){
		System.out.println("Enter Two Values For Multiplication :");
		Scanner s=new Scanner(System.in);
		int a,b,c;
		a=s.nextInt();
		b=s.nextInt();
		c=a*b;
		System.out.println("The Multiplication Of Two Values Is :"+c);
	}
}