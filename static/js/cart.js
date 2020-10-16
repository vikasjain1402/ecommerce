var updatebtn=document.getElementsByClassName("update-cart")


for (var i=0;i<updatebtn.length;i++){
updatebtn[i].addEventListener('click',function(){
    var productId=this.dataset.product
    var productAction=this.dataset.action
    console.log("productid:",productId,"Product action ",productAction )
    console.log(user)   
    if (user=='AnonymousUser'){console.log("User is not logged in ")}
    else{updateuserorder(productId,productAction)}

})
}

function updateuserorder(productId,action){
   
    var url='/updateitem/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productid':productId,'action':action})
    })
    .then(
        (response)=>{ return response.json()})
    .then(
        (data)=>{ console.log('data:',data)
        location.reload()
    })    
}

