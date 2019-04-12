function getSum(a, b) {
  let arr = [a, b]
  let sum = 0
  let min;
  let max;
  
  if(arr[0] < arr[1]){
    min = arr[0];
    max = arr[1];
  } else {
    min = arr[1];
    max = arr[0];
    }
  
  for (let i = min; i <= max; i++) {
    sum += i
  }

  if (a == b) {
    return a
  } else {
    return sum
  }
}


console.log(getSum(0, -1));
console.log(getSum(0, 1));
console.log(getSum(1, 1));
console.log(getSum(-1, 2));