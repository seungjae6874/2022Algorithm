import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int t =1;
        int sumt=0;
        while(n>0){
            //n이 0될때까지 계속 빼기
            //n이 t보다 작아지면 t는 1로 변경
            if(n >= t){
                
                n -= t;
                
            }
            else{
                //n이 t보다 작아지면
                t = 1;
                n -=t;
            }
            sumt+=1;
            t+=1;
            
        }
        System.out.println(sumt);
    }
}