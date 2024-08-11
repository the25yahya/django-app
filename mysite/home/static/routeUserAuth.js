import { checkLoginState } from "./loginState.js"
console.log('user auth working')


let user = document.querySelector('.fa-user')
user.addEventListener("click",()=>{
    const loginState = checkLoginState()
    if (loginState) {
        window.alert('logged in')   
    }else{
        const url = window.location.origin+'/userAuth/signup'
        window.location.href = url   
        console.log(url);
        
    }
    
})
