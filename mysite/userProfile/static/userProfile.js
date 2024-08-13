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