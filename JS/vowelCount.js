// Get the count of vowels (a,e,i,o,u) from a string
const getVowelCount = str => {
  newStr = str.split('').sort().join('')
  vowelsCount = newStr.match(/[aeiou]/gi);
  
  if (vowelsCount == null) {
    return 0;
   } else{
     return vowelsCount.length;
  }
}

console.log(getVowelCount('abracadabra'))
console.log(getVowelCount('pear tree'))
console.log(getVowelCount('my pyx'))