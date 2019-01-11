/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Compose;
import java.util.Scanner;
/**
 *
 * @author Twins
 */
public class main {

    /**
     *
     */
    public static int i;

    /**
     * @param args the command line arguments
     */
    @SuppressWarnings("empty-statement")
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Number;");
        int number =sc.nextInt();
        System.out.println(number);
        System.out.println("Composite numbers:1");
        for( int i=2;i<= Math.sqrt(number);i++){
           if (number % i==0){
               if(i*i == number){
                   System.out.println(""+i);
               }
               else{
                   System.out.print(""+i);
                   System.out.print(""+number/i);
                   
               }
           }
        }
        System.out.println(""+number);
        // TODO code application logic here
    }
    
}
