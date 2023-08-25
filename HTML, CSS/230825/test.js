const me = { name: "병헌", address: "고양" };
const newAddress = {address : "하남"};
const newMe = {...me, ...newAddress}

console.log(newMe);
// { name: '병헌', address: '하남' }