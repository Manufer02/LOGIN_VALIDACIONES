const registro = document.getElementById("registroForm")

if(registro){

registro.addEventListener("submit", async (e)=>{

e.preventDefault()

const data={
correo:document.getElementById("correo").value,
password:document.getElementById("password").value,
nombre_usuario:document.getElementById("nombre_usuario").value,
identificacion:document.getElementById("identificacion").value,
celular:document.getElementById("celular").value
}

try{

const response = await fetch("/registro",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify(data)
})

const result = await response.json()

// Si hay error de validación
if(result.error){

alert(result.error)

}else{

alert("✅ Usuario registrado correctamente")

// limpiar formulario
document.getElementById("registroForm").reset()

// redirigir a login
window.location.href="login.html"

}

}catch(error){

alert("Error conectando con el servidor")

}

})

}

const login=document.getElementById("loginForm")

if(login){

login.addEventListener("submit", async(e)=>{

e.preventDefault()

const correo=document.getElementById("correo").value
const password=document.getElementById("password").value

try{

const response=await fetch(`/login?correo=${correo}&password=${password}`,{
method:"POST"
})

const result=await response.json()

if(result.error){

alert(result.error)

}else{

alert("✅ Login exitoso")

// guardar nombre usuario
localStorage.setItem("usuario",result.usuario)

// ir al panel
window.location.href="dashboard.html"

}

}catch(error){

alert("Error conectando con el servidor")

}

})

}