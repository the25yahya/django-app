console.log('index is working');


function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}


function checkLoginState(){
    let token = getCookie('access_token')
    return !!token
}

export {checkLoginState}