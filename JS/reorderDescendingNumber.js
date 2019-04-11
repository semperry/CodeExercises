// const assertEquals = num => {
//   let numArray = num.toString().split('')
//   numArray.sort().reverse()
  

//   return Number(numArray.join(''))
// }

// console.log(assertEquals(21445))

// function descendingOrder(n){
//   return parseInt(String(n).split('').sort().reverse().join(''))
//  }

// console.log(descendingOrder(21445))

function descendingOrder(n){
  let numArray = n.toString().split('')
    numArray.sort().reverse()
    return Number(numArray.join(''))
}
console.log(descendingOrder(21445))