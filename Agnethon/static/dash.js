
document.addEventListener('DOMContentLoaded', function(){
    const sidebar = document.querySelector('.sidebar');
    const dashboardIcon = document.querySelector('.dashboard-icon');
    const sidebarIcon = document.querySelector('.sidebar-icon');

    dashboardIcon.addEventListener('click', function(){
        sidebar.classList.toggle('visible');
        dashboardIcon.querySelector('i').classList.toggle('active');
        sidebarIcon.querySelector('i').classList.toggle('active');
    });
    registeredEvent.addEventListener('click', function() {
        sidebar.classList.remove('visible');
        document.querySelector('.main').classList.remove('hidden');
      });
    
      userGraduate.addEventListener('click', function() {
        sidebar.classList.remove('visible');
        document.querySelector('.main').classList.remove('hidden');
      });
});