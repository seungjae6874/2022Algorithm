import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        int box=0;
        int book=0;
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        //상자 사이즈들을 합산
        for(int i =0; i < n; i++){
            box += Integer.parseInt(st2.nextToken());
        }
        StringTokenizer st3 = new StringTokenizer(br.readLine());
        for(int j =0; j <m; j++){
            book += Integer.parseInt(st3.nextToken());
        }
        //box 사이즈에서 book 사이즈를 뺀 것이 낭비 용량
        System.out.println(box-book);
        br.close();
    }
}