console.log(isNaN('5')) // false
console.log(isNaN(3)) // false
console.log(isNaN('b3')) // true
console.log(isNaN('3b')) // true

console.log(Number.isNaN(undefined)) // false
console.log(Number.isNaN(null)) // false
console.log(Number.isNaN(NaN)) // true