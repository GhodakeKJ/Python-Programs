import java.util.Scanner;
class  Add{
	public static void main(String[] args) {
		System.out.println("Enter Two Values For Calculating Sum :");
		Scanner s=new Scanner(System.in);
		int x,y,z;

		x=s.nextInt();
		y=s.nextInt();

		z=x+y;
		System.out.println("The Sum Of X And Y Values Is :"+z);
	}
}
