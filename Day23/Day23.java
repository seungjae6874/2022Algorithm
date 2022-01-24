import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int[] amt = new int[3];
        amt[0] = a;
        amt[1] = b;
        amt[2] = c;
        ArrayList<Integer> aa = new ArrayList<Integer>();
        ArrayList<Integer> bb = new ArrayList<Integer>();
        ArrayList<Integer> cc = new ArrayList<Integer>();
        
        ArrayList<Integer> arr = new ArrayList<Integer>();
        int ac = 0;
        for(int i =0; i < 3; i++){
            StringTokenizer st2= new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st2.nextToken());
            int e = Integer.parseInt(st2.nextToken());
            arr.add(s);
            arr.add(e);
            if(i==0){
                aa.add(s);
                aa.add(e-1);
            }
            else if(i==1){
                bb.add(s);
                bb.add(e-1);
            }
            else if(i==2){
                cc.add(s);
                cc.add(e-1);
            }
        }
        Collections.sort(arr);
        int mint = arr.get(0);
        int maxt = arr.get(arr.size()-1);
        int[] check = new int[101];
        for(int ab = 0; ab< maxt+1; ab++){
            check[ab] = 0;
        }
        for(int i = mint; i<=maxt; i++){
            if((i >= aa.get(0)) & (i <= aa.get(1))){
                check[i]+=1;
            }
            if((i >= bb.get(0)) & (i <= bb.get(1))){
                check[i]+=1;
            }
            if((i >= cc.get(0)) & (i <= cc.get(1))){
                check[i]+=1;
            }
            
        }
        int sum = 0;
        for(int i =mint; i <=maxt; i++){
            if(check[i] == 1){
                sum += (check[i]*a);
            }
            else if(check[i] == 2){
                sum += (check[i]*b);
            }
            else if(check[i] == 3){
                sum += (check[i]*c);
            }
        }
        System.out.println(sum);
    }
}