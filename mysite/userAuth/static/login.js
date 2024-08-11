document.getElementById('login-form').addEventListener('submit',function(e) {
  e.preventDefault()  
  const formData = new FormData(this);
  fetch('/userProfile/login',{
    method:'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
        console.log('Data from login:', data);
        document.cookie = `access_token=${data.access_token}; path=/; Secure;`;
        document.cookie = `refresh_token=${data.refresh_token}; path=/; Secure;`;
        if (data.access_token && data.refresh_token) {
          console.log('[*] got tokens successfully');
          fetch('/userProfile/',{
            method: 'POST',
            body: JSON.stringify({
                access_token: data.access_token,
                refresh_token: data.refresh_token
            }),
            headers:{
                'Content-Type':'application/json'
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
        }else{
          console.log('no tokens in the request');
        }
        
    })
    .catch(error => console.error('Login Error:', error));
})