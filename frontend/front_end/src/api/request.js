//The static Promise.resolve function returns a Promise that is resolved.

const baseUrl = "http://127.0.0.1:5000"; 
const paths = { 
    loadUser: "/load", 
}

export default async function loadUser() {
    return await fetch(`http://127.0.0.1:5000/load`).then(response => response.json());
}