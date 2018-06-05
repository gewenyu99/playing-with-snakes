const arr = [3, 2, 44, 2315, 12, 4, 8, 7, 0, -12];
const mergeSort = (arr) => {
        if (arr.length < 2) return arr;
        const mid = Math.floor(arr.length / 2);
        return merge(mergeSort(arr.slice(0, mid)), mergeSort(arr.slice(mid)));
}

const merge = (a, b)=>{
        let result = [];
        let i = 0;
        let j = 0;

        while(i < a.length && j < b.length) {
                if (a[i] < b[j]) {
                        result.push(a[i]);
                        i++;
                }
                else {
                        result.push(b[j]);
                        j++;
                }
        }
        while(i < a.length){
                result.push(a[i]);
                i++;
        }
        while(j < b.length){
                result.push(b[j]);
                j++;
        }
        return result;
}

console.log(arr);
console.log(mergeSort(arr));