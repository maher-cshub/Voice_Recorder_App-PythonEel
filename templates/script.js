

function setValue(res) {
    console.log(res)
}

document.getElementById("record_btn").addEventListener("click",(ev)=>{
    
    let record_btn = document.getElementById("record_btn")
    const file_name = document.getElementById("voice_name")


    if(record_btn.getAttribute("state") == "False"){
        record_btn.setAttribute("state","True")
        eel.Record(file_name.value)(setValue)
    }
    else{
        record_btn.setAttribute("state","False")
    }
    
})


eel.expose(Check_Recording);
function Check_Recording() {
    let record_btn = document.getElementById("record_btn")
    if(record_btn.getAttribute("state") == "False"){
        
        return "false"
    }
    else{
        return "true"
    }

}

eel.expose(Set_Mics);
function Set_Mics(input_devices){
    let mic_select= document.getElementById('input_devices')
    const devices = Object.entries(input_devices)
    devices.forEach(element => {
        console.log(element)
        let new_el = document.createElement("option")
        new_el.setAttribute("item_id",element[0].toString())
        new_el.innerHTML = element[1]
        mic_select.appendChild(new_el)
    });
    return
}