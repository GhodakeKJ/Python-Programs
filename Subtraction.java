import java.util.Scanner;
class Subtraction {
	public static void main(String[]args){
		System.out.println("Enter Two Values For Substracting :");
		Scanner k=new Scanner(System.in);
		int x,y,z;
		x=k.nextInt();
		y=k.nextInt();
		z=x-y;
		System.out.println("Sub Of Two Values Are :"+z);
	}
}