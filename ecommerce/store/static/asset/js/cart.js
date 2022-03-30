var update_btns = document.getElementsByClassName('update-cart')

for (i=0; i<update_btns.length; i++){
    update_btns[i].addEventListener('click',function () {
        var product_id = this.dataset.product
        var action = this.dataset.action
        console.log('product_id',product_id,'action:',action)
        console.log('user',user)
        if (user === 'AnonymousUser')
        {
            console.log('Not logged in')
        }
        else{
            updateUserOrder(product_id, action)
        }

    })

}

function updateUserOrder(product_id,action){
    console.log('user if logged in')

    var url = '/update_item/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        mode: 'same-origin',
        body:JSON.stringify({'product_id':product_id,'action':action})
    })

        .then((response) => {
            return response.json()
        })
        .then((data) =>{
            console.log('data:',data)
            location.reload()
        })
}






















