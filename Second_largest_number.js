var array=[10,20,30,40,50]
var set=new Set()
for(let num of array){
    if(Math.max(...array)>num){
        set.add(num)
    }
}
console.log(array)
console.log("This is Second Largest number in array:",Math.max(...set))