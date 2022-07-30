/*Dark Mode*/
const toggleSwitch = document.querySelector('.dark_mode_switch input[type="checkbox"]');

function switchTheme(e) {
    if (e.target.checked) {
        alert("Checked")
        document.querySelector('body').classList.add("dark_mode");
    }
    else {
        alert("Not Checked")
        document.querySelector('body').classList.remove("dark_mode");
    }    
}

toggleSwitch.addEventListener('change', switchTheme, false);
