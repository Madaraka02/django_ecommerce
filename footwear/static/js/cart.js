var updateBtns = document.getElementByClassName('update-cart')


for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function () {

        var productId = this.dataset.product
        var action = this.dataset.action

        console.log('USER', user)
        if(user == 'AnonymousUser'){

        }
        
    })
}