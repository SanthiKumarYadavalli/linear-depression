const statusbtn1 = document.getElementById('c-status1');
const statusbtn2 = document.getElementById('c-status2');

const s1 = document.getElementById('sec1');
const s2 = document.getElementById('sec2');

s2.style.display="none"
statusbtn1.addEventListener('click', function() {
    s1.style.display = "block";  // Show section 1
    s2.style.display = "none";   // Hide section 2

    statusbtn1.classList.remove('btn-light');
    statusbtn2.classList.remove('btn-warning');
    statusbtn2.classList.add('btn-light');
    statusbtn1.classList.add('btn-warning');
});

statusbtn2.addEventListener('click', function() {
    s1.style.display = "none";   // Hide section 1
    s2.style.display = "block";  // Show section 2

    statusbtn2.classList.remove('btn-light');
    statusbtn1.classList.remove('btn-warning');
    statusbtn1.classList.add('btn-light');
    statusbtn2.classList.add('btn-warning');
});
