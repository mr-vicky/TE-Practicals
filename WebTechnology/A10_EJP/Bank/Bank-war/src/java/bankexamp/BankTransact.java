/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bankexamp;

import java.util.Date;
import javax.ejb.Schedule;
import javax.ejb.Stateless;

/**
 *
 * @author barta
 */
@Stateless
public class BankTransact implements BankTransactLocal {

    @Schedule(dayOfWeek = "Mon-Fri", month = "*", hour = "9-17", dayOfMonth = "*", year = "*", minute = "*", second = "0")
    @Override
    public void myTimer() {
        System.out.println("Timer event: " + new Date());
    }

    // Add business logic below. (Right-click in editor and choose
    // "Insert Code > Add Business Method")
    // default balance amount = 10000
    int balance = 10000;  
    @Override
    public void deposit(int amount) { 
        
        balance = balance+amount;
    }   
 
    @Override
    public int withdraw(int amount) { 
        
        balance = balance -amount;
        return balance; 
    }
    
    
}
