function sortedArr(array, target){
  
    for(let i = 0; i < array.length; i++){
        let j = i+1
        if(array[i] == target){
            return i
        }
        else if(target > array[i] && target < array[j]){
            return j
        }
    }
   
    let first_index_of_the_array = 0
    let last_index_of_the_array = array.length-1
    if(target < array[first_index_of_the_array]){
        return first_index_of_the_array
    }
   
    if(target > array[last_index_of_the_array]){
        return last_index_of_the_array + 1
    }
   
    if(array.length == 0){
        return 0
    }
 }
 
 module.exports = sortedArr;
