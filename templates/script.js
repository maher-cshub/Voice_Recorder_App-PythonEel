let record_btn = document.getElementById("record_btn")


function setValue(res) {
    console.log(res)
}

record_btn.addEventListener("click",(ev)=>{
    
    let record_btn = document.getElementById("record_btn")
    console.log(record_btn.getAttribute("status"))
    const file_name = document.getElementById("voice_name")
    
    if(record_btn.getAttribute("status") == "False"){
        eel.Record(file_name.value)(setValue)
    }
    else{
        record_btn.setAttribute.status = "True"
    }
    
    
})


eel.expose(Check_Recording);
function Check_Recording() {
    let record_btn = document.getElementById("record_btn")
    if(record_btn.getAttribute("status") == "False"){
        return false
    }
    else{
        return true
    }

}