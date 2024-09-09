public class Pal {

    public static void main(String[] args) {
        String str = "s22s";
        
        int count = 0;
        int n = str.length();
        for (int i = 0; i < n; i++) {
            if (str.charAt(i) == str.charAt(n-i-1)) {
                count++;
            }
        }

        if (count == n) System.out.println("Yes");
        else System.out.println("No");

}
}