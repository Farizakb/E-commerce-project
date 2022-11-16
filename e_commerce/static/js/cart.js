document.addEventListener('readystatechange', event => { 

    if (event.target.readyState === "interactive") {   //does same as:  ..addEventListener("DOMContentLoaded"..
        get_fetch()

    }
    if (event.target.readyState === "complete") {
        remove_cartItem()
    }
})



var uptadeBtns = document.getElementsByClassName('update-cart')
console.log(uptadeBtns.length);
for(var i = 0; i < uptadeBtns.length; i++){
    uptadeBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log(productId,action)
        console.log(user)

        if (user === 'AnonymousUser' ){
            alert('Not logged in')

        }else{
            console.log('User is logged in')
            uptadeUserOrder(productId,action)
        }
    })
        
}

async function uptadeUserOrder(productId,action){
    console.log('post_fetch start');

    let Data = {
        'product_id':productId,
        'action':action,
        'user':user 
    }



    let response = await fetch('http://localhost:8000/api/baskets/',{
        method: 'POST',
        headers:{
            'Accept': '*/*',
            'Content-Type':'application/json'
            },
        body:JSON.stringify(Data)
    })

    let cart = await response.json()
    if(cart === 'ok'){
        console.log("burdan get");
    }
    console.log('post_fetch end');

}
            
            
            

async function  get_fetch(){
    console.log('get_fetch start');

    let response = await fetch('http://127.0.0.1:8000/api/baskets/');
    basket_list = await response.json();
    basket = basket_list[0]
    console.log(basket.items);
    console.log(basket);
    for(basket_item of basket.items) {
    document.querySelector('#basket').innerHTML += `
    <div class="sin-itme clearfix">
        <i data-product=${basket_item.id}  data-action="remove"" class="mdi mdi-close  update-cart"></i>
        <a class="cart-img" href="http://127.0.0.1:8000/az/orders/cart"><img src="http://127.0.0.1:8000/static/img/cart/1.png" alt="" /></a>
        <div class="menu-cart-text">
            <a href="#"><h5>${basket_item.product.title}</h5></a>
            <span>Color :  Black</span>
            <span>Size :     SL</span>
            <br>
            <b>$${basket_item.product.price}  x ${basket_item.count}</b>
            <strong>$${basket_item.get_total}</strong>
        </div>
    </div>
    `
    }
    document.querySelector('#total').innerHTML = `<span>total <strong>= $${basket.get_cart_total}</strong></span>`

    document.querySelector('#cart_show').innerHTML = `
    <i class="mdi mdi-cart"></i>
    ${basket.get_cart_items} items :  <strong>$${basket.get_cart_total}</strong>
    `
    console.log('get_fetch end');
    }


function remove_cartItem(){
    var btns = document.getElementsByClassName('update-cart')
    console.log(btns.length);
    for(var i = 0; i < btns.length; i++){
        uptadeBtns[i].addEventListener('click', function(){
            var productId = this.dataset.product
            var action = this.dataset.action
            console.log(productId,action)
            console.log(user)
    
            if (user === 'AnonymousUser' ){
                alert('Not logged in')
    
            }else{
                console.log('User is logged in')
                uptadeUserOrder(productId,action)
            }
        })
            
    }
    

}
