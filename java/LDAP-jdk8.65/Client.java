import javax.naming.InitialContext;

public class Test {
    public static void main(String[] args) {
        try {
            new InitialContext().lookup("ldap://127.0.0.1:8888/a");
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
