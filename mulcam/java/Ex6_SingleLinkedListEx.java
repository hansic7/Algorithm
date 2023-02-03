package mulcam.java;

import java.util.*;

public class Ex6_SingleLinkedListEx {
   static Scanner in = new Scanner(System.in);
   
   public static void main(String args[]){
	  ArrayList<String> list = new ArrayList<String>();
	  
      Sungjuk data;
      int menu;
      
      do
      {
         print_menu();
         System.out.printf("\n메뉴 선택 => ");
         menu = in.nextInt();
         if (menu == 5)
         {
            System.out.printf("\n프로그램 종료...\n");
            break;
         }

         switch (menu)
         {
            case 1:
               System.out.println();
               data = new Sungjuk();
               System.out.print("번호 입력 => ");
               data.setBunho(in.nextInt());
               System.out.print("이름 입력 => ");
               data.setIrum(in.next());
               System.out.print("점수 입력 => ");
               data.setJumsu(in.nextInt());
               L.insertLastNode(data);
               break;
            case 2:
               L.printList();
               break;
            case 3:
               System.out.println();
               data = new Sungjuk();
               System.out.print("검색할 번호 입력 => ");
               data.setBunho(in.nextInt());
               L.searchNode(data);
               break;
            case 4:
               System.out.println();
               data = new Sungjuk();
               System.out.print("삭제할 번호 입력 => ");
               data.setBunho(in.nextInt());
               L.deleteNode(data);
               break;
            default:
               System.out.printf("\n메뉴를 다시 입력하세요!!!\n");
               break;
         }

      }while(true);
   }
   
   static void print_menu()
   {
      System.out.printf("\n*** 메뉴 ***\n");
      System.out.printf("1. 데이터 입력\n");
      System.out.printf("2. 데이터 출력\n");
      System.out.printf("3. 데이터 검색\n");
      System.out.printf("4. 데이터 삭제\n");
      System.out.printf("5. 프로그램 종료\n");
   }
}

class LinkedList{
   private ListNode head;
   
   public LinkedList(){
      head = null;
   }
   
   public void insertLastNode(Sungjuk data){
      ListNode newNode = new ListNode(data);
      ListNode pre = null;
      Sungjuk obj = null;
      
      if(head == null){// 빈 리스트
         this.head = newNode;
         System.out.println("\n삽입 성공!!!");
         return;
      }
      
      ListNode temp = head;
      while(temp != null) // 번호 중복 데이터 체크
      {
         obj = temp.getData();
         if (data.getBunho() == obj.getBunho())
         {
            System.out.printf("\n입력 오류 - 존재하는 번호임!!!\n");
            return;
         }
         pre = temp;
         temp = temp.link;
      }
         
//      temp = head;
//      while(temp.link != null) //새노드를 삽입하기 위해 마지막 노드로 이동
//         temp = temp.link;
      
//      temp.link = newNode;
      pre.link = newNode;
      System.out.println("\n삽입 성공!!!");
   }
   
   public void printList(){
      ListNode temp = this.head;
      
      if(this.head == null)  
      {
         System.out.printf("\n리스트에 데이터가 없음!!!\n");
         return;
      }
      
      System.out.println();
      System.out.println("번호   이름   점수");
      System.out.println("===============");
      while(temp != null){
         Sungjuk data = temp.getData();
//         System.out.printf("%3d  %3s %4d %n", data.getBunho(), data.getIrum(), data.getJumsu());
         data.printData();
         temp = temp.link;      
      }
      System.out.println("===============");
   }
   
   public void searchNode(Sungjuk data){
      ListNode temp = this.head;
      Sungjuk obj = null;
      
      if(this.head == null)  
      {
         System.out.printf("\n리스트에 데이터가 없음!!!\n");
         return;
      }
      System.out.println();
      while(temp != null){
         obj = temp.getData();
         if(data.getBunho() == obj.getBunho())  
         {
            System.out.println("번호   이름   점수");
            System.out.println("===============");
//            System.out.printf("%3d  %3s %4d %n", obj.getBunho(), obj.getIrum(), obj.getJumsu());
            obj.printData();
            return;
         }
         else 
            temp = temp.link;
      }
      System.out.println("검색 오류-일치하는 번호가 없음!!!");
   }
   
   public void deleteNode(Sungjuk data){
      ListNode pre, temp;
      Sungjuk obj = null;
      
      if(this.head == null)  // 빈 리스트 일때
      {
         System.out.printf("\n삭제 오류-리스트에 데이터가 없음!!!\n");
         return;
      }
      
      if(this.head.link == null){ // ***리스트에 노드가 한 개만 있는 경우***
         temp = this.head;
         obj = temp.getData();
         if (data.getBunho() == obj.getBunho()) // 첫번째 노드의 번호와 일치하는 경우
         {
            System.out.printf("\n삭제 성공!!! \n");
            head = null; // 리스트 시작 포인터를 null로 설정한다.
            return;
         }
         else  // 노드가 하나밖에 없는데 번호가 일치하지 않는 경우
         {
            System.out.printf("\n삭제 오류-일치하는 번호가 없음!!!\n");
         }
      }
      else{  // ***리스트에 노드가 여러 개 있는 경우***
         temp = this.head;
         obj = temp.getData();
         if (data.getBunho() == obj.getBunho()) // 노드가 여러 개일때 첫번째 노드가 삭제할 노드인 경우
         {
            System.out.printf("\n삭제 성공!!!\n");
            this.head = this.head.link; // 후속 노드의 주소를 선행노드의 링크에 저장
            return;
         }
         else
         {
            pre = head; // 첫번째 노드의 주소 저장
            temp = head.link; // 두번째 노드의 주소 저장
            while(temp != null){
               obj = temp.getData();
               if (data.getBunho() == obj.getBunho()) 
               {
                  System.out.printf("\n삭제 성공!!!\n");
                  pre.link = temp.link; // 후속 노드의 주소를 선행노드의 링크에 저장
                  return;
               }
               else
               {
                  pre = temp;
                  temp = temp.link;
               }
            }
         }
         System.out.printf("\n삭제 오류-일치하는 번호가 없음!!!\n");
      }
   }
}

class ListNode{
   private Sungjuk data;
   public ListNode link;
   
   public ListNode(){
      this.data = null;
      this.link = null;
   }
   public ListNode(Sungjuk data){
      this.data = data;
      this.link = null;
   }
   
   public Sungjuk getData(){
      return  this.data;
   }
}

class Sungjuk {
   private int bunho;
   private String irum;
   private int jumsu;
   
   public int getBunho() {
      return bunho;
   }
   public void setBunho(int bunho) {
      this.bunho = bunho;
   }
   public String getIrum() {
      return irum;
   }
   public void setIrum(String irum) {
      this.irum = irum;
   }
   public int getJumsu() {
      return jumsu;
   }
   public void setJumsu(int jumsu) {
      this.jumsu = jumsu;
   }
   
   public void printData() {
      System.out.printf("%3d  %3s %4d %n", this.bunho, this.irum, this.jumsu);
   }
}
