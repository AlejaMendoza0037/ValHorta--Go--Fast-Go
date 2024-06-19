

const encabezadoTabla=document.getElementById('tablaPaciente')
const tablaPaciente=document.querySelector('tbody')

let btnCrear=document.getElementById('btnCrear')













async function traerDatosPaciente(){
    await fetch ('http://localhost:3000/pacientes')
        .then((res)=> res.json()
        )
        .then((pacientes)=>{
            pacientes.forEach((paciente,index) => {

                let tr=document.createElement("tr")

                let td=document.createElement("td")
                td.innerText=paciente.cedula
                tr.appendChild(td)

                td=document.createElement("td")
                td.innerText=paciente.nombre
                tr.appendChild(td)

                td=document.createElement("td")
                td.innerText=paciente.apellido
                tr.appendChild(td)

                td=document.createElement("td")
                td.innerText=paciente.fechaNacimiento
                tr.appendChild(td)

                td=document.createElement("td")
                td.innerText=paciente.telefono
                tr.appendChild(td)


               td=document.createElement("Button")   
               td.setAttribute("class", "btnActualizar ")  
               td.setAttribute("class", "btn btn-outline-success ")             
                td.innerText="Actualizar"
                tr.appendChild(td)


                td=document.createElement("Button")
                
                td.setAttribute("name", "btnBorrar");
                td.setAttribute("class", "btn btn-outline-danger");
                td.innerText="Eliminar"
                tr.appendChild(td)



                tablaPaciente.appendChild(tr)
         

            


               
                
            })

            function mensaje(message,cssClass){
                const div =document.createElement('div')
                div.className=`alert alert-${cssClass}`
                div.appendChild(document.createTextNode(message))
                const container=document.querySelector('.container-fluid')
                const divApp=document.querySelector('#divApp')
                container.insertBefore(div, app)




            }


            function btnDelete(element){
                if (element.name==='btnBorrar'){
                    element.parentElement.remove()
                    
                }
                
            }
            

           tablaPaciente.addEventListener('click',(e)=>{
           btnDelete(e.target)
            
        
        })

           
            

        }
        

        
        )
        

        
            
    }
       
    
 


traerDatosPaciente()