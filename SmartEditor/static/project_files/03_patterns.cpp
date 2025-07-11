#include <iostream>
using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     cout<< "enter a number n:";

//     for(int i = 1; i<=n; i++){

//         char ch = 'A';
//         for(int j =1; j<n; j++){
//             cout<<ch;
//             ch=ch+1;
//         }
//         // for(int j =1; j<=n; j++){
//         //     // cout<<j<<" ";
//         //     cout<<"*";
//         // }
//          cout<<endl;
//     }
//     return 0;

// }

//n=4         n=4          n=4
// 1234       ****          A B C D
// 1234       ****          A B C D
// 1234       ****          A B C D
// 1234       ****          A B C D


// triangle pattern//

// int main(){
//     int n=4;
//     for(int i=0; i<n; i++){
//         for(int j=0; j<i+1; j++){
//             cout<<"*";
//         }
//         cout<<endl;
//     }
//     return 0;
// }

/*
*
**
***
****
*/


//Reverse Triangle Pattern
/* 1
   21
   321
   4321
*/
    //  int main(){
    // int n=4;
    // for(int i=0; i<n; i++){
    //     for(int j=i+1; j>0; j--){
    //         cout<< j <<" ";
    //     }
    //     cout<<endl;
    // }
    // return 0;


// Floyd's Triangle Pattern//
/*  1
    23
    456
    78910*/

 int main(){
    int n=4;

    int num = 1;
    for(int i=0; i<n; i++){
        for(int j=i+1; j>0; j--){
            cout<< num <<" ";
            num++;
        }
        cout<<endl;
    }
    return 0;
 }



// Inverted Triangle Pattern
/* o/p
1 1 1 1
  2 2 2
    3 3
      4
*/

int main(){
    int n=4;

    int num = 1;
    for(int i=0; i<n; i++){

        //spaces
        for(int j=0; j<n-i; j++){
            cout <<" ";
        }

        //nums
        for(int j=0; j<n-i; j++){
            cout<<(i+1);
        }
        cout<<endl;
    }
    return 0;
 }


 // pyramid patter//
 int main(){
    int n=4;

    int num = 1;
    for(int i=0; i<n; i++){

        //spaces
        for(int j=0; j<n-i-1; j++){
            cout <<" ";
        }
        for(int j=1; j<i+1; j++){
            cout<<j;
        }
        for(int j=0; j<i-1; j++){
            cout<<j;
        }
        cout<<endl;
    }
    return 0;
 }