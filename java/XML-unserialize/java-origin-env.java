import java.beans.XMLDecoder;
import java.io.FileInputStream;

public class Test {
    public static void main(String[] args)  throws Exception{
        FileInputStream file = new FileInputStream("1.xml");
        XMLDecoder d = new XMLDecoder(file);
        d.readObject();
    }
}
