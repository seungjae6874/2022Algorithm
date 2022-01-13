import java.util.*;

public class Main{
    
    public static int[][] arr;
    public static int[] visited;
    public static int count=0;
    public static void dfs(int x){
        if(visited[x] == 1){
            return;
        }else{
            visited[x] = 1;
        }
        for(int i = 1; i < arr.length; i++){
            if(arr[x][i] == 1 && visited[i] != 1){
                //방문한 적이 없고, 두 노드는 이어져있다면
                dfs(i);
            }
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        //노드 갯수와 간선갯수 입력받기,
        int node = sc.nextInt();
        arr = new int[node+1][node+1]; //이어져있는지 확인할 이중배열
        visited = new int[node+1];
        int edge = sc.nextInt(); //간선의 갯수만큼 반복
        int t = edge;
        while(t-- > 0){
            int head = sc.nextInt();
            int tail = sc.nextInt();
            arr[head][tail] = 1;
            arr[tail][head] = 1;
        }
        for(int i = 1; i <= node; i++){
            if(visited[i]==0){
                dfs(i);
                count++;
            }
        }
        System.out.println(count);
    }
}