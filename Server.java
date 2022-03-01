package Server;
import java.io.*;
import java.net.*;

public class Server {
    public Server() {
        System.out.println("Server is now listening ");
    }

    public static void main(String[] args) {
        try{
            ServerSocket ss = new ServerSocket(6666);
            Socket s = ss.accept();
            DataInputStream data = new DataInputStream(s.getInputStream());
            String stable = data.readUTF();
            System.out.println("Client"+stable);
    } catch (Exception e) {
            System.out.println(e);
        }
    }
}
