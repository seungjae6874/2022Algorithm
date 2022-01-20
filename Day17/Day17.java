import java.util.*;
import java.io.*;

class Node{
    char Data;
    Node Left,Right;
    public Node(char Data){
        this.Data = Data;
    }
}

class Tree{
    Node Root;
    
    public void Add(char Data, char Left_Data, char Right_Data){
        if(Root == null){
            //Data가 . 이 아니라면 루트는 data값을 가짐.
            if(Data != '.') Root = new Node(Data);
            //LeftData가 . 이아니면 Left_Data값을 가진 노드를 왼쪽에 생성
            if(Left_Data != '.') Root.Left = new Node(Left_Data);
            //Right Data가 .이 아니면 루트 오른쪽에 Right_Data 노드를 생성
            if(Right_Data != '.') Root.Right = new Node(Right_Data);
            
        }
        else{
            //루트가 널이 아니라면 탐색
            Search(Root, Data, Left_Data,Right_Data);
        }
    }
    
    public void Search(Node Root, char Data, char Left_Data, char Right_Data){
        if(Root == null) return; //루트가 널이면 종료
        
        else if(Root.Data == Data){
            //루트 데이터 값이 데이터와 같다면? 탐색
            //만약 루트의 왼쪽 노드가 .이 아니면 루트의 왼쪽노드를 생성
            if(Left_Data != '.') Root.Left = new Node(Left_Data);
            //루트의 오른쪽 노드가 .이 아니면 루트의 오른쪽노드를 생성
            if(Right_Data != '.') Root.Right = new Node(Right_Data);
            
        }
        else{
            //왼쪽의 왼쪽으로 계속 탐색
            Search(Root.Left, Data, Left_Data, Right_Data);
            //오른쪽의 오른쪽노드로 계속 탐색
            Search(Root.Right, Data, Left_Data, Right_Data);
        }
        
    }
    
    public void PreOrder(Node Root){
        //선위순회 -> 루트 -> 왼쪽 자식- > 오른쪽 자식
        System.out.print(Root.Data);
        if(Root.Left != null) PreOrder(Root.Left);
        if(Root.Right != null) PreOrder(Root.Right);
    }
    public void InOrder(Node Root){
        //중위 순회 -> 맨 왼쪽 -> 루트 -> 맨 오른쪽
        if(Root.Left != null) InOrder(Root.Left);
        System.out.print(Root.Data);
        if(Root.Right != null) InOrder(Root.Right);
    }
    public void PostOrder(Node Root){
        //후위 순회 -> 맨 왼쪽 -> 맨 오른쪽 -> 루트
        
        if(Root.Left != null) PostOrder(Root.Left);
        if(Root.Right != null) PostOrder(Root.Right);
        System.out.print(Root.Data);
    }
}

public class Main{
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Tree tree = new Tree();
        for(int i =0 ; i<n; i++){
            tree.Add(sc.next().charAt(0),sc.next().charAt(0),sc.next().charAt(0));
        }
        tree.PreOrder(tree.Root);
        System.out.println();
        tree.InOrder(tree.Root);
        System.out.println();
        tree.PostOrder(tree.Root);
        
    }
}