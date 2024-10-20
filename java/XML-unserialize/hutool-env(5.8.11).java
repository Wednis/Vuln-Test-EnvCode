import java.io.File;
import cn.hutool.core.util.XmlUtil;

public class Test {
    public static void main(String[] args)  throws Exception{
        File file = new File("1.xml");
        XmlUtil.readObjectFromXml(file);
    }
}
