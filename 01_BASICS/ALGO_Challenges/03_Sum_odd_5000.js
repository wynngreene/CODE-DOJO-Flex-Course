//Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999)
// function sum_odd_5000() {
//     var sum = 0;
//     //your code here
//     let myOddArray = [];

//     for (i = 0; i = 10; i++){
//         if(i % 2 == 0){
//         myOddArray[i] = i;
            
//     }
    
//     return sum; 
// }

function sum_odd_5000() {
    var sum = 0;
    for(i = 1; i < 7; i++){
        if(i % 2 !==0){
            sum = i + sum;
        }
    }

    console.log(sum);
}

sum_odd_5000();