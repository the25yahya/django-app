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

//access token
const accessToken = document.cookie.split('; ').find(row => row.startsWith('access_token=')).split('=')[1];


//function to extract the user id from the jwt
function getUserIdFromToken(token) {
    const base64Url = token.split('.')[1]; // Extract the payload part of the JWT
    const base64 = base64Decode(base64Url); // Decode the base64
    const jsonPayload = JSON.parse(base64); // Parse the JSON

    return jsonPayload.user_id; // Adjust based on your JWT payload structure
}


 // Function to decode a base64-encoded string
 function base64Decode(str) {
        return decodeURIComponent(atob(str).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));
    }

document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.getElementById('file');
    const preview = document.getElementById('preview');
    const form = document.getElementById('profile-photo');
    const submitButton = document.getElementById('update-picture');


    // Function to extract the user ID from the JWT
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


        // Extract the user ID from the token
        const userId = getUserIdFromToken(accessToken);
        

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


console.log('name : ',document.querySelector('#user-name').innerHTML);

document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to the parent element
    document.body.addEventListener('click', function(event) {
        if (event.target && event.target.classList.contains('save-button')) {
            // Identify the parent info-container
            const container = event.target.closest('.info-container');
            
            // Determine which field is being edited
            const editInfo = container.querySelector('.edit-info');
            const fieldType = editInfo.classList
                .toString()
                .match(/edit-info-(\w+)/)[1]; // Extract the field type
            
            // Get the new value from the input field
            const input = container.querySelector('.edit-info input');
            const value = input.value;
            
            // Optionally, perform additional actions like sending the new value to a server
            const userId = getUserIdFromToken(accessToken);
            const data = {
                fieldType: fieldType,
                value: value,
                userId: userId
            };
        
            

            fetch('/userProfile', {
                method: 'PUT',
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.error(error);
            });
        }
    });
});
