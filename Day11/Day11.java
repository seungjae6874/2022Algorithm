import java.util.*;

public class Main{
    public static int[][] arr; //전체 배열 
    public static int[] visited; //해당 노드를 방문했는지
    public static int count = 0;
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int t = in.nextInt(); //테스트케이스 갯수
        while(t-- > 0){ //테스트갯수만큼
            count = 0;
            int n = in.nextInt();
            arr = new int [n+1][n+1];
            visited = new int[n+1];
            
            for(int i = 1; i<= n; i++){
                int num = in.nextInt();
                
                arr[num][i] = 1;
                arr[i][num] = 1;
            }
            for(int i = 1; i <= n; i++){
                if(visited[i] ==0){
                    dfs(i);
                    count++;
                }
            }
            System.out.println(count);
        }
    }
    
    public static void dfs(int x){
        if(visited[x] == 1){
            return;
        }else{
            visited[x] = 1;
        }
        for(int i = 1; i < arr.length; i++){
            if(arr[x][i] == 1 && visited[i] != 1){
                dfs(i);
            }
        }
    }
}