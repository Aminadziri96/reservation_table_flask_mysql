function handleSubmit () {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    // to set into local storage
    /* localStorage.setItem("NAME", name);
    localStorage.setItem("SURNAME", surname); */
    
    sessionStorage.setItem("name", name);
    sessionStorage.setItem("email", email);

    return;
}