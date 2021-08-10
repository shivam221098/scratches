const result = [];

const arr = ['a', 'b', 'c'];
for (const [index, elem] of arr.entries()){
    if (index > 1) break;
    result.push(elem);
}
console.log(result)