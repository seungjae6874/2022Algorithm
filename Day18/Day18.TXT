import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        
        ArrayList<Integer>[] list = new ArrayList[n+1];
        for(int i =1; i<= n; i++){
            list[i] = new ArrayList<Integer>();
        }
        
        //연결하기
        for(int i =0; i<n-1; i++){
		//STRINGTOKENIZER를  반복문으로 호출해서 한줄씩 사용가능
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list[a].add(b);
            list[b].add(a); //서로 연결
            
        }
        int[] parents = new int[n+1]; //부모들을 담을 배열
        
        dfs(list, parents,n ,1, 0); //연결리스트, 부모배열, 전체 갯수, 시작번호, 부모번호
        
        for(int j =2; j<=n; j++) System.out.println(parents[j]);
        
    }
    private static void dfs(ArrayList<Integer>[] list, int[] parents, int n, int start, int parent){
        parents[start] = parent; 
	//처음에 start노드는 1이고 1의 부모는 0으로 설정
	//list[start]안에 start노드와 연결된 노드2개가 있을 것이다.
	// 그 2개를 item이라 하고, item이 parent가 아니면 다시 dfs로 부모를 찾는다.
        for(int item : list[start]){
            if(item != parent) dfs(list,parents,n,item,start);
/		//parent와 start를 계속 갱신해주면서
		//start노드의 부모노드를 찾아서 parents배열에 넣어준다.
        }
    }
}