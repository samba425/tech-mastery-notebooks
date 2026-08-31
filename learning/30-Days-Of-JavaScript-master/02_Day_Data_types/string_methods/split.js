// split(): The split method splits a string at a specified place.
let string = '30 Days Of JavaScript'
console.log(string.split())     // ["30 Days Of JavaScript"]
console.log(string.split(' '))  // ["30", "Days", "Of", "JavaScript"]
let firstName = 'Samba'
console.log(firstName.split())  // ["Samba"]
console.log(firstName.split(''))  // ["A", "s", "a", "b", "e", "n", "e", "h"]
let countries = 'India, Sweden, Norway, Denmark, and Iceland'
console.log(countries.split(',')) // ["India", " Sweden", " Norway", " Denmark", " and Iceland"]
console.log(countries.split(', '))   //  ["India", "Sweden", "Norway", "Denmark", "and Iceland"]