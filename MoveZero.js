var num=[0,2,0,3,0,5]
var newarray=[]
var zeroarray=[]
for(let i=0;i<num.length;i++){
    if(num[i]!==0){
        newarray.push(num[i])
    }
    else{
        zeroarray.push(num[i])
    }
}
console.log(newarray.concat(zeroarray))