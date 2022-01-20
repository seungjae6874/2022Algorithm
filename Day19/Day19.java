import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        for(int i = 0; i < n; i++){
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int f = Integer.parseInt(st2.nextToken());
            int s = Integer.parseInt(st2.nextToken());
            combi(s,f);
        }
    }
    public static void combi(int s, int f){
        //조합은 순서가 존재하지 않으므로 다리가 겹치는 경우를 
        //신경쓰지 않아도 된다. 1,3,4랑 3,4,1, 4,3,1 이 모든 경우가 1가지이므로
        //1,3,4라고 생각하면 됨.
        long bunmo = 1;
        long bunja = 1;
        if(f > s-f){
            //뺀 값으로 나누는게 이득          
            for(int i = 0; i < (s-f); i++){
                bunmo *= (s-f-i);
                bunja *= (s-i);
            }
            System.out.println((long)(bunja/bunmo));
        }
        else{
            //그냥 빼기
            for(int i = 0; i < f; i++){
                bunmo *= (f-i);
                bunja *= (s-i);
            }
            System.out.println((long)(bunja/bunmo));
        }
    }
}