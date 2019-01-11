/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package arbitrary.bettingcalculator;
import java.util.Scanner;

/**
 *
 * @author BOBNATI
 */
public class ArbitraryBettingCalculator {
    //Arbing is the act of betting on all possible outcomes,thereby eliminating risk.

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
         System.out.println ("This Application eliminates risk by ensuring profit on all outcomes.");
         
         
        Scanner input = new Scanner (System.in);
        //Declaring all the variables im working with
        double odds1, odds2, stake,Return;
               double sd, cb, margin, Stake2,Stake3;
               
               //Accepting user inputs
               
                 System.out.println ("Input your odds ");
                 
                  System.out.print ("The lower odd here -----> ");
                odds1 = input.nextDouble();
                
                 System.out.print ("The higher odd here-----> ");
                odds2 = input.nextDouble();
                
                 System.out.print ("What's your stake ? ");
                 stake = input.nextDouble();
                 
                 //sd is the actual probability 
                 
                  sd = 100/odds1;
                  cb=100/odds2;
                  margin = sd + cb;
                 
                  
                 Stake2= (stake * sd)/margin;
                 Stake3= (stake * cb)/margin;
                 
                
                   System.out.println ("The stake at the lower odd is " + Stake2 );
                    System.out.println ("The stake at higher odd is " + Stake3);
                    
                    Return = Stake2 * odds1;
                            
                             System.out.println ("The total return despite any outcome is " + Return);
                  
                    
                  
    }
    
}
