// Team Odin :: Yuqing Wu, Rachel Xiao
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.


var fact = (n) =>{
  if (n<=1){
   return 1;
  }else{
   return fact(n-1) *  n;
  }
};

var fib = (n) =>{
  if (n<=1){
   return n;
  }else{
   return fib(n-1) +  fib(n-2);
  }
};
