/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author barta
 */
class bankTransact { 
    
    static int balance = 10000;  

    static void deposit(int amount) { 
        
        amount = balance + amount;
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    static int withdraw(int amount) {  
        
        amount = balance -amount;
        
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
}
