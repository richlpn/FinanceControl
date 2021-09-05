let attemp = 3

function login(){
    if(attemp > 0 ){
    attemp--
    document.getElementById("username").disabled = true
    document.getElementById("username").disabled = true;
    document.getElementById("password").disabled = true;
    document.getElementById("submit").disabled = true;
    }
}