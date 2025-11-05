// // Theme toggle functionality
// document.addEventListener('DOMContentLoaded', function() {
//     const themeToggle = document.getElementById('themeToggle');
//     const themeIcon = themeToggle.querySelector('i');
    
//     // Check for saved theme preference or default to light
//     const currentTheme = localStorage.getItem('theme') || 'light';
//     document.documentElement.setAttribute('data-bs-theme', currentTheme);
//     updateThemeIcon(currentTheme);
    
//     themeToggle.addEventListener('click', function() {
//         const newTheme = document.documentElement.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
//         document.documentElement.setAttribute('data-bs-theme', newTheme);
//         localStorage.setItem('theme', newTheme);
//         updateThemeIcon(newTheme);
//     });
    
//     function updateThemeIcon(theme) {
//         themeIcon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
//     }
    
//     // Mark complete functionality
//     const markCompleteButtons = document.querySelectorAll('.mark-complete-btn');
//     markCompleteButtons.forEach(button => {
//         button.addEventListener('click', function() {
//             const questionId = this.dataset.questionId;
//             markQuestionComplete(questionId, this);
//         });
//     });
    
//     // Search functionality
//     const searchInput = document.getElementById('searchInput');
//     if (searchInput) {
//         searchInput.addEventListener('input', function() {
//             const searchTerm = this.value.toLowerCase();
//             const questionCards = document.querySelectorAll('.question-card');
            
//             questionCards.forEach(card => {
//                 const questionText = card.querySelector('.card-title').textContent.toLowerCase();
//                 if (questionText.includes(searchTerm)) {
//                     card.style.display = 'block';
//                 } else {
//                     card.style.display = 'none';
//                 }
//             });
//         });
//     }
// });

// function markQuestionComplete(questionId, button) {
//     fetch(`/api/mark-complete/${questionId}`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         }
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.error) {
//             alert('Please login to track progress');
//             return;
//         }
        
//         if (data.completed) {
//             button.classList.add('completed');
//             button.innerHTML = '<i class="fas fa-check me-1"></i>Completed';
//         } else {
//             button.classList.remove('completed');
//             button.innerHTML = '<i class="fas fa-check me-1"></i>Mark Complete';
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// }

// // Smooth scrolling for anchor links
// document.querySelectorAll('a[href^="#"]').forEach(anchor => {
//     anchor.addEventListener('click', function (e) {
//         e.preventDefault();
//         const target = document.querySelector(this.getAttribute('href'));
//         if (target) {
//             target.scrollIntoView({
//                 behavior: 'smooth',
//                 block: 'start'
//             });
//         }
//     });
// });

// Simple main.js to avoid loading issues
document.addEventListener('DOMContentLoaded', function() {
    console.log('C Programming Portal loaded successfully!');
    
    // Basic theme toggle
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-bs-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-bs-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
    }
    
    // Initialize theme from localStorage
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-bs-theme', savedTheme);
});