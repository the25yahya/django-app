checkBox = document.querySelector('#checkbox')


document.getElementById("signup-form").addEventListener("submit",function(e){
    e.preventDefault();
    const formData = new FormData(this)
    fetch('/userAuth/register',{
        method:'POST',
        body:formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Data from register:', data.access_token , data.refresh_token);
          // Store tokens in cookies
        document.cookie = `access_token=${data.access_token}; path=/;`;
        document.cookie = `refresh_token=${data.refresh_token}; path=/;`;
        if (data.access_token && data.refresh_token) {
            fetch('/userProfile',{
                method: 'POST',
                body: JSON.stringify({
                    access_token: data.access_token,
                    refresh_token: data.refresh_token
                }),
                headers:{
                    'content-Type':'application/json'
                }
            })
            .then(response => response.text())
            .then(html => {
                document.open();
                document.write(html);
                document.close();
                history.pushState(null, '', '/userProfile?tab=personal');
            })
            .catch(error=>console.error('ERROR: ',error))
        }
    })
    .catch(error=>{
        console.error('ERROR : ',error);
        
    })
})