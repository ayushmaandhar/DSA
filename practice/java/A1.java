import java.util.*;

public class A1 {
    public static void main(String[] args) {

        ArrayList<Integer> list = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        while(true){
            String element = sc.nextLine();
            if(element.equals("exit")) {
                break;
            }
            list.add(Integer.parseInt(element));

        }

        // for(int i =0;i<list.size();i++){
        //     System.out.print(list.get(i)+ " ");
        // }

        System.out.print("Minimum is -> ");

        int minNum = list.get(0);
        for (int i=0; i<list.size(); i++) {
            minNum = Math.min(minNum, list.get(i));
        }

        System.out.println(minNum);

        // i want to find the minimum 
    }
}