function descendingOrder(n){
  let numArray = n.toString().split('')
    numArray.sort().reverse()
    return Number(numArray.join(''))
}
console.log(descendingOrder(21445))