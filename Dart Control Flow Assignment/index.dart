/*
Create a Dart program that prompts the user for a number and then prints a message to the 
console based on the following criteria:

If the number is greater than 10, print "Your number is greater than 10"
If the number is less than 10, print "Your number is less than 10"
If the number is equal to 10, print "Your number is equal to 10"
 */
import 'dart:io';


void main(){
    print("Enter your a number:");
 
   // Scanning number
    int? num = int.parse(stdin.readLineSync()!);
   // Here ? and ! are for null safety
   
   //using if statement to check it's equality
   if (num > 10){
    print('Your number is greater than 10');
   }
   else if(num < 10){
    print('Your number is less than 10');
   }
   else{
    print('Your number is equal to 10');
   }


}