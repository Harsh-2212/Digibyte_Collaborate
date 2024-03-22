document.addEventListener('DOMContentLoaded', function(){
  const sidebar = document.querySelector('.sidebar');
  const dashboardIcon = document.querySelector('.dashboard-icon');
  const sidebarIcon = document.querySelector('.sidebar-icon');
  const registeredEvent = document.querySelector('#registeredEvent'); // Assuming registeredEvent is an ID
  const userGraduate = document.querySelector('#userGraduate'); // Assuming userGraduate is an ID

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
