checkBox = document.querySelector('#checkbox')


document.getElementById("signup-form").addEventListener("submit",function(e){
    e.preventDefault();
    const formData = new FormData(this)
    fetch('/userProfile/register',{
        method:'POST',
        body:formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Data from register:', data);
        fetch('/userProfile/',{
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
        })
        .catch(error=>console.error('ERROR: ',error))
    })
    .catch(error=>{
        console.error('ERROR : ',error);
        
    })
})