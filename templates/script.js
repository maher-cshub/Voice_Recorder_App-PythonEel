

function setValue(res) {
    console.log(res)
}


eel.Start()

document.getElementById("record_btn").addEventListener("click",(ev)=>{

    let record_btn = document.getElementById("record_btn")

    if (record_btn.getAttribute("status") == "inactive"){
        let mic_select= document.getElementById('input_devices')
        let file_name = document.getElementById("voice_name")
        const chosen_mic = mic_select.options[mic_select.selectedIndex]
        eel.Set_Vars(file_name.value,chosen_mic.getAttribute("item_id"))    
    }
    
    eel.Record(record_btn.getAttribute("status"))

    
})


document.getElementById("save_btn").addEventListener("click",(evt)=>{
    eel.Save()
})

eel.expose(Change_Status);
function Change_Status(status) {
    let record_btn = document.getElementById("record_btn")
    record_btn.setAttribute("status",status)
    return record_btn.getAttribute("status")
}

eel.expose(Check_Status);
function Check_Status() {
    let record_btn = document.getElementById("record_btn")
    return record_btn.getAttribute("status")
}

eel.expose(Set_Mics);
function Set_Mics(input_devices){
    let mic_select= document.getElementById('input_devices')
    const devices = Object.entries(input_devices)
    devices.forEach(element => {
        let new_el = document.createElement("option")
        new_el.setAttribute("item_id",element[0].toString())
        new_el.innerHTML = element[1]
        mic_select.appendChild(new_el)
    });
    return
}