// JS Objects
// ------------------------------------
// key[string]:value pair - array[numbers] index:value
// for in loop

var my_obj = {'name': 'Phil', country: 'USA'};
// console.log(my_obj);

my_obj.location = 'Tulsa, OK'
// console.log(my_obj);
console.log(my_obj.name);

var my_arr = [2];
// console.log('my_arr[0]', my_arr[0])

for(k in my_obj) {
    console.log('k', k);
    console.log('my_obj[k]', my_obj[k])
    console.log('my_obj.k', my_obj.k)
    console.log(typeof(k));
}

my_obj['key']