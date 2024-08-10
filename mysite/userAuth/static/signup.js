document.getElementById("signup-form").addEventListener("submit",function(e){
    e.preventDefault();
    const formData = new FormData(this)
    fetch('/userProfile/register',{
        method:'POST',
        body:formData
    })
    .then(response => {
        if(response.redirected){
            window.location.href = response.url;
        }else{
            console.log(response.json());
            
        }
    })
    .catch(error=>{
        console.error('ERROR : ',error);
        
    })
})