// Create a function that passes in a number and adds any other number to it (currying)
function add(n){
  return function Add(b) {
    let result = n + b
    return result
  }
}


console.log(add(1)(3))
console.log(add(3)(3))