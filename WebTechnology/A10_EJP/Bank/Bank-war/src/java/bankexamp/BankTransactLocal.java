/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bankexamp;

import javax.ejb.Local;

/**
 *
 * @author barta
 */
@Local
public interface BankTransactLocal {
    
    public void myTimer();

    void deposit(int amount);

    int withdraw(int amount);
}
