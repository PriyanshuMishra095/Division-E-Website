
function validate_password() {

    var pass = document.getElementById('password').value;
    var confirm_pass = document.getElementById('confirmpassword').value;
    if (pass != confirm_pass) {
        document.getElementById('wrong_pass_alert').style.color = 'red';
        document.getElementById('wrong_pass_alert').innerHTML
            = '☒ Use same password';
        document.getElementById('create').disabled = true;
        document.getElementById('create').style.opacity = (0.4);
    } else {
        document.getElementById('wrong_pass_alert').style.color = 'green';
        document.getElementById('wrong_pass_alert').innerHTML =
            '🗹 Password Matched';
        document.getElementById('create').disabled = false;
        document.getElementById('create').style.opacity = (1);
    }
}

function wrong_pass_alert() {
    var pass = document.getElementById('password').value;
    var confirm_pass = document.getElementById('confirmpassword').value;

    if(pass==confirm_pass)
    {
        alert("Your response is submitted");
    } 
    else 
    {
        alert("Passwords dont't match! Exiting the page.");
    }
}

function validate_email(mail) {
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(myForm.emailAddr.value)) {
        return (true)
    }
    alert("You have entered an invalid email address!")
    return (false)
}

function check() {
    if (document.getElementById('password').value != "")
        alert("Your responce is submitted");
    else
        alert("Please fill all the fields");

}

function sent(){
    alert("Your message was sent! You will be contacted shortly.")
}

function validate_prn()
{ 
var field = document.getElementById('prn').value; 
var mxlen = 11;

if(field.length<mnlen || field.length> mxlen)
{ 
alert("PRN should be of " +mxlen+ " digits");
return false;
}
else
{ 
return true;
}
}