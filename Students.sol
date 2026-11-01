
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {

    // Structure
    struct Student {
        uint rollNo;
        string name;
        uint age;
    }

    // Array
    Student[] public students;

    // Add student data
    function addStudent(uint _rollNo, string memory _name, uint _age) public {
        students.push(Student(_rollNo, _name, _age));
    }

    // Display student data
    function getStudent(uint index)
        public
        view
        returns (uint, string memory, uint)
    {
        Student memory s = students[index];
        return (s.rollNo, s.name, s.age);
    }

    // Display total number of students
    function getTotalStudents() public view returns (uint) {
        return students.length;
    }

    // Fallback function
    fallback() external payable {
    }
}