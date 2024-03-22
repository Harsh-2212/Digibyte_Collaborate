document.addEventListener('DOMContentLoaded', function(){
    const sidebar = document.querySelector('.sidebar');
    const registeredEvent = document.querySelector('#registeredEvent');

    registeredEvent.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default behavior of the link
        sidebar.classList.remove('visible');
    });
});
