function addGuest() {
    // Get the inputted guest name
    const guestName = document.getElementById("guestName").value;
    const guestList = document.getElementById("guestlist");

    // Create a new list item with the guest name
    let listItem = document.createElement("li");
    listItem.textContent = guestName;

    // Append list item to guest list
    guestList.appendChild(listItem); 
}

// Add event listener
document.querySelector('#addGuest').addEventListener('click', addGuest);

