package Server;

import java.io.*;
import java.net.*;
public class Client {
    public static void main(String[] args) {
        try{
        Socket s = new Socket("localhost", 6666);
        DataOutputStream os = new DataOutputStream(s.getOutputStream());
        os.writeUTF("How are Da server");
        os.flush();
        os.close();
        s.close();
        }
        catch (Exception e) {
            System.out.println(e);
        }
        
    }
}
