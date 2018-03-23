
function getData(){
var posts;
fetch('https://jsonplaceholder.typicode.com/posts', {mode:'no-cors'}).then(function(response){
    return response.json();
}).then(function(pos){
posts = pos;
});
return posts;
}