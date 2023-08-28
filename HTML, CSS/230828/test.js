new Promise(function(res, rej){
	setTimeout(() => rej('에러'), 3000);
}).then(() => {
	console.log("에러 통과")
})