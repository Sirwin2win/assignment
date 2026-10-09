scores = [12, 15, 11, 18, 20, 14, 16, 13]
// count
const count = scores.length
// mean
let total = 0
for(let i = 0;i<scores.length;i++){
    total += scores[i]
}
let mean = total/count
console.log(count)
console.log(mean)
// std
let mean_squares = 0
let j = 0
while(j<scores.length){
    mean_squares += (scores[j]-mean)**2
    j++
}
let variance = mean_squares/(count-1)
const std = variance**0.5
console.log(std)
//minimum
let minNumber = scores[0]
let k = 1
while(k<scores.length){
    if(scores[k]<minNumber){
        minNumber = scores[k]
    }
    k++
}
console.log(minNumber)
// maximum
let maxNumber = scores[0]
let l = 1
while(l<scores.length){
    if(scores[l]>maxNumber){
        maxNumber = scores[l]
    }
    l++
}
console.log(maxNumber)