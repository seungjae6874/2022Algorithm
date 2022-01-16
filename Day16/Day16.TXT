import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st2.nextToken());
        
       
        long left = 1;
        long right = m;
        
        bs(left,right,m,n);
        br.close();
    }
    public static void bs(long left, long right, int m, int n){
        //임의의 찾을 값 x를 mid로 설정하고 index 위치로 나눠나간다.
        // min(Math.min(mid/idx, n))
        // arr의 한 행의 최대 길이가 n이므로 
        // 1 2 3인데 k=19이면 left = 1 이라 mid = 가 10이면 10/2는 5이다.
        //그래서 x보다 작은 갯수는 n을 못넘음.
        
        
        while(left < right){
            long mid = (left+right)/2;
            long count = 0;
            for(int i = 1; i <= n; i++){
                count += Math.min(mid/i,n); //한 행 길이n과 mid를/(i 단)으로 나누었을 때
			//i단에는 최소 mid/i인 갯수만큼 mid보다 작다는 뜻.
            }
            //count가 m보다 크다면?
            if (m <= count){ //Lower Bound를 쓰는 이유는?
                //k값에 대해 x보다 작은 수가 k값이랑 같은 경우의수가 발생
                //lower-bound : 찾고자하는 값과 같거나 큰수가 있는
                //첫번째 인덱스를 찾는다.
                //uppder-bound = 초과하는 첫번째 인덱스를 찾는다.
                //mid가 너무 크다는 뜻.
                right = mid;
            }
            else{
                left = mid+1;
            }
        }
        System.out.println(left);
    }
}