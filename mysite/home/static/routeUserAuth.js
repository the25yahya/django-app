import { checkLoginState } from "./index.js"
console.log('user auth working')


let user = document.querySelector('.fa-user')
user.addEventListener("click",()=>{
    const loginState = checkLoginState()
    if (loginState) {
        const url = window.location.origin+'/userProfile'
        window.location.href = url   
        console.log(url)     
    }else{
        const url = window.location.origin+'/userAuth/signup'
        window.location.href = url   
        console.log(url);
        
    }
    
})
