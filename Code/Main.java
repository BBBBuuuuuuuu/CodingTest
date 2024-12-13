package divisor_2501;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		
		int N = scn.nextInt();
		int K = scn.nextInt();
		
		int count = 0;
		for(int i=1; i<=N; i++) {
			if (N%i == 0) count++;
			
			if (count==K) {
				System.out.print(i);
				return;
			}
		}
		
		System.out.println(-1);
	}
}
