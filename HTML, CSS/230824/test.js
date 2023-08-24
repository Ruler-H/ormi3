const num = []

console.log(num.reduce((a, c) => {
	if (c % 2 === 1) {
		return a + c
	}else{
		return a
	}
})) // error