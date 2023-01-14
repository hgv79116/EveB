const base_url = process.env.REACT_APP_SERVER_BASE_URL

export async function loadUser() {
    const response = await fetch(
        base_url + '/user/loadUser/', 
    )
    return [response.ok, (await response.json()).user]
} 

export async function login(params) { 
    console.log(params)
    const response = await fetch (
        base_url + '/user/login/', 
        { 
            method: "POST", 
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(params)
        }
    )
    return [response.ok, (await response.json()).user]
}

export async function logout(params) { 
    const response = await fetch (
        base_url + '/user/logout/'
    )
    return response.ok
}

export async function registerUser(params) { 
    const response = await fetch (
        base_url + '/user/registerUser/', 
        { 
            method: "POST", 
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(params)
        }
    )
    return response.ok
}

export async function deleteUser(params) { 
    const response = await fetch (
        base_url + '/user/deleteUser/', 
        { 
            method: "POST", 
            body: params
        }
    )
    return response.ok
}
