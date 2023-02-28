// * Check if a Number is Positive and Negative
// var no =-5
// if (no > 0) {
//   console.log("Positive");
// } else if (no == 0) {
//   console.log("Zero");
// } else {
//   console.log("Negitive");
// }

// * Program to Check Whether a Number is Even or Odd
// let no = 6;
// if(no % 2 == 0){
//     console.log("Even");
// }
// else{
//     console.log("odd");
// }

// * Find the Sum of the First N Natural Numbers
// let no = 5;
// let sum = 0;
// for (i = 0; i <= no; i++) {
//   sum += i;
// }
// console.log("sum is", sum);

// * Find the Sum of Numbers in a given Range
// let start = 3;
// let end = 5;
// let sum = 0
// for(i = start ; i <= end ; i++){
//  sum += i
// }
// console.log(sum);

// * Find the Greatest of the Two Numbers
// let num1 = 829;
// let num2 = 89;

// if (num1 < num2) {
//   console.log(num2);
// } else if (num1 > num2) {
//   console.log(num1);
// } else {
//   console.log("Equal");
// }

// * Find the Greatest of the Three Numbers
// let num1 = 8;
// let num2 = 8;
// let num3 = 8;

// if (num1 < num2 && num3 < num2) {
//   console.log(num2);
// } else if (num1 > num2 && num1 > num3) {
//   console.log(num1);
// } else if (num3 > num1 && num3 > num2) {
//   console.log(num3);
// } else {
//   console.log("Equal");
// }

// * Check Whether a Year is a Leap Year or Not
// let year = 2004;
// if (year % 400 == 0) {
//   console.log("leap year");
// } else {
//   console.log("Not leap year");
// }

// *Check Whether a Number is a Prime or Not
// let no = 6;
// let isPrime = true;
// for(i =2 ; i < no ; i++){
//     if(no % i ==0){
//         isPrime = false
//     }
//     break
// }
// if(isPrime){
//     console.log("Prime");
// }else{
//     console.log("Not Prime");
// }

// *Prime Numbers In A Given Range
let no = 17;
let isPrime = true;
const Prime = () => {
  for (i = 2; i < no; i++) {
    if (no % i == 0) {
      isPrime = false;
    }
    break;
  }
};
