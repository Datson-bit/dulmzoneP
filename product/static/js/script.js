const searchWrapper = document.querySelector(".search-bar");
const inputBox = document.querySelector("input");
const suggBox = document.querySelector(".search-btn");


inputBox.onkeyup=(e)=>{
    let userData = e.target.value;
    let emptyArray =[];
    if (userData) {
        emptyArray = suggestions.filter((data)=>{
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data)=>{
            return data ='<li>' + data +'<li>';
        });
         console.log(emptyArray);
    }else{
    }
    showSuggestions(emptyArray)
} 


function showSuggestions(list){
    let listData;
    if (!list.length) {
        userValue = inputBox.value;
        listData = '<li>'+ userValue +'</li>';
    }else{
        listData = list.join('');
    }
    suggBox.innerHTML= listData;
}