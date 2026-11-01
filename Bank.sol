
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    uint public balance;

    // Deposit Ether
    function deposit() public payable {
        require(msg.value > 0, "Amount must be greater than zero");
        balance += msg.value;
    }

    // Withdraw Ether
    function withdraw(uint amount) public {
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= balance, "Insufficient balance");

        balance -= amount;

        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Show balance
    function showBalance() public view returns (uint) {
        return balance;
    }
}