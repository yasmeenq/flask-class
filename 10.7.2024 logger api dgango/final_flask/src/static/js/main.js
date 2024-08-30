function confirmDelete(){
    const ok = confirm("Are you sure ? ")
    if (!ok){
        event.preventDefault()
    }
}

const errorSpan = document.querySelector(".error");
if(errorSpan){
    setTimeout(() => {
        errorSpan.parentNode.removeChild(errorSpan);
    }, 40000);
}

function saveUser(){
    let email = document.getElementById("email").value;
    localStorage.setItem("email", email);
    alert("ok");
}