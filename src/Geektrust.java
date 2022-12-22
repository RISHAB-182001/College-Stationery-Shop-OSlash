import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;


public class Geektrust {
    public static void main(String[] args)  {
        try {
            // the file to be opened for reading
            FileInputStream fis = new FileInputStream(args[0]);
            Scanner sc = new Scanner(fis); // file to be scanned
            // returns true if there is another line to read
            while (sc.hasNextLine()) {
               String inputCommand = sc.nextLine();
               //Add your code here to process input commands.
               String output = ""; //process the input command and get the output
               //Once it is processed print the output using the command System.out.println()
               System.out.println(output);
            }
            sc.close(); // closes the scanner
        } catch (IOException e) {
        }
	}
}
