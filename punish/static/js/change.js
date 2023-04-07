function validateform(x) {
    var pswrd = /^[A-Za-z ]+$/;

    if(x.old.value == ""){
        alert("please enter your old password");
        x.old.focus();
        return false;
    }
    if(x.password.value == ""){
        alert("please enter your new password");
        x.password.focus();
        return false;
    }
    if(x.newpassword.value == ""){
        alert("please re-enter your new password");
        x.newpassword.focus();
        return false;
    }
    if(x.password.value != x.newpassword.value){
        alert("passwords are not matching");
        x.newpassword.focus();
        return false;
    }
}