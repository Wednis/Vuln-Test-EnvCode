package org.example;

import javax.naming.InitialContext;

public class Client {
    public static void main(String[] args) {
        try {
            new InitialContext().lookup("rmi://127.0.0.1:8888/A");
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
