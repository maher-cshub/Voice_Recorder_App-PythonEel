let record_btn = document.getElementById("record_btn")


function setValue(res) {
    console.log(res)
}

record_btn.addEventListener("click",(ev)=>{
    eel.Record("test")(setValue)
})