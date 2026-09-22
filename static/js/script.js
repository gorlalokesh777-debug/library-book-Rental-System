// ============================================
// Library Book Rental System - Frontend JS
// ============================================

document.addEventListener('DOMContentLoaded', function () {

    // Auto-hide alert messages after 4 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.transition = 'opacity 0.5s';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 4000);
    });

    // Extra client-side confirmation on delete links/buttons
    const deleteLinks = document.querySelectorAll('.btn-delete');
    deleteLinks.forEach(function (link) {
        link.addEventListener('click', function (e) {
            // Only intercept simple <a> links to the delete confirmation page,
            // not the actual delete form submit button.
            if (link.tagName === 'A') {
                return; // let it navigate to the confirmation page normally
            }
        });
    });

    // Highlight overdue rows in the table
    document.querySelectorAll('.status-overdue').forEach(function (badge) {
        const row = badge.closest('tr');
        if (row) {
            row.style.backgroundColor = '#fdecea';
        }
    });

    // Simple required-field check before submit (extra layer over Django validation)
    const rentalForm = document.querySelector('.form-wrapper form');
    if (rentalForm) {
        rentalForm.addEventListener('submit', function (e) {
            const requiredFields = rentalForm.querySelectorAll('[required]');
            let valid = true;
            requiredFields.forEach(function (field) {
                if (!field.value.trim()) {
                    valid = false;
                    field.style.borderColor = '#e74c3c';
                } else {
                    field.style.borderColor = '#ccc';
                }
            });
            if (!valid) {
                e.preventDefault();
                alert('Please fill out all required fields.');
            }
        });
    }
});
