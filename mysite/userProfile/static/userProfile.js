// edit name
editButtonName = document.querySelector('#edit-name').addEventListener("click",()=>{
    document.querySelector('.show-info-name').classList.add('hide');
    document.querySelector('.edit-info-name').classList.remove('hide');
})
cancelButtonName = document.querySelector('#cancel-name').addEventListener("click",()=>{
    document.querySelector('.show-info-name').classList.remove('hide');
    document.querySelector('.edit-info-name').classList.add('hide');
})
///////////////////////////////////////////////////////////////////////////
editButtonEmail = document.querySelector('#edit-email').addEventListener("click",()=>{
    document.querySelector('.show-info-email').classList.add('hide');
    document.querySelector('.edit-info-email').classList.remove('hide');
})
cancelButtonEmail = document.querySelector('#cancel-email').addEventListener("click",()=>{
    document.querySelector('.show-info-email').classList.remove('hide');
    document.querySelector('.edit-info-email').classList.add('hide');
})

///////////////////////////////////////////////////////////////////////////
editButtonPhone = document.querySelector('#edit-phone').addEventListener("click",()=>{
    document.querySelector('.show-info-phone').classList.add('hide');
    document.querySelector('.edit-info-phone').classList.remove('hide');
})
cancelButtonPhone = document.querySelector('#cancel-phone').addEventListener("click",()=>{
    document.querySelector('.show-info-phone').classList.remove('hide');
    document.querySelector('.edit-info-phone').classList.add('hide');
})

///////////////////////////////////////////////////////////////////////////
editButtonBirthday = document.querySelector('#edit-birthday').addEventListener("click",()=>{
    document.querySelector('.show-info-birthday').classList.add('hide');
    document.querySelector('.edit-info-birthday').classList.remove('hide');
})
cancelButtonBirthday = document.querySelector('#cancel-birthday').addEventListener("click",()=>{
    document.querySelector('.show-info-birthday').classList.remove('hide');
    document.querySelector('.edit-info-birthday').classList.add('hide');
})

///////////////////////////////////////////////////////////////////////////
editButtonTown = document.querySelector('#edit-town').addEventListener("click",()=>{
    document.querySelector('.show-info-town').classList.add('hide');
    document.querySelector('.edit-info-town').classList.remove('hide');
})
cancelButtonTown = document.querySelector('#cancel-town').addEventListener("click",()=>{
    document.querySelector('.show-info-town').classList.remove('hide');
    document.querySelector('.edit-info-town').classList.add('hide');
})

////////////// profile photo ////////////////////////////
document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.getElementById('file');
    const preview = document.getElementById('preview');
    const form = document.getElementById('profile-photo');
    const submitButton = document.getElementById('update-picture');

    // Function to decode a base64-encoded string
    function base64Decode(str) {
        return decodeURIComponent(atob(str).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));
    }

    // Function to extract the user ID from the JWT
    function getUserIdFromToken(token) {
        const base64Url = token.split('.')[1]; // Extract the payload part of the JWT
        const base64 = base64Decode(base64Url); // Decode the base64
        const jsonPayload = JSON.parse(base64); // Parse the JSON

        return jsonPayload.user_id; // Adjust based on your JWT payload structure
    }

    // Preview the selected image
    fileInput.addEventListener('change', function() {
        const file = fileInput.files[0];
        if (file) {
            const reader = new FileReader();

            reader.onload = function(e) {
                preview.src = e.target.result;
            };

            reader.readAsDataURL(file);
        }
    });

    // Prevent submit button from triggering file input click
    submitButton.addEventListener('click', function(e) {
        if (!fileInput.files.length) {
            e.preventDefault();
            alert("Please choose an image before updating.");
        }
    });

    // Handle form submission
    form.addEventListener("submit", function(e) {
        e.preventDefault();

        const file = fileInput.files[0];
        if (!file) {
            alert("Please select a file before submitting.");
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        // Get the JWT from the cookies
        const accessToken = document.cookie.split('; ').find(row => row.startsWith('access_token=')).split('=')[1];

        // Extract the user ID from the token
        const userId = getUserIdFromToken(accessToken);
        console.log(userId,accessToken);
        

        // Append the user ID to the form data
        formData.append('user_id', userId);

        fetch('/userProfile/profileUpload', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.success) {
                document.querySelector('.user-profile').src = data.new_img_url;
            }
        })
        .catch(error => {
            console.error(error);
        });
    });
});
