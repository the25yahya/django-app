document.addEventListener("DOMContentLoaded", function() {
    const searchTerm = document.querySelector("#searchTerm");
    const search = document.querySelector("#search")

    function handleEvent(event) {
        if (event.type === "click" || (event.type === "keydown" && event.key === "Enter")) {
            const term = searchTerm.value;  // Get the value from the input field
            document.location.href = `/search?query=${encodeURIComponent(term)}`;
        }
    }

    if (search) {
        // Trigger event on button click
        search.addEventListener("click", handleEvent);
    }

    if (searchTerm) {
        // Trigger event on Enter key press
        searchTerm.addEventListener("keydown", handleEvent);
    }
});
