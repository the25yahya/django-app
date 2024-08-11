import { checkLoginState } from "./loginState.js"
console.log('user auth working')


let user = document.querySelector('.fa-user')
user.addEventListener("click",()=>{
    const loginState = checkLoginState()
    if (loginState) {
        document.location.href = '/userProfile/'  
    }else{
        document.location.href = '/userAuth/signup'
    }
    
})
