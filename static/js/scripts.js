function TogglePassword() {
    const passwordField = document.getElementById('floatingPassword');
    const togglePassword = document.getElementById('togglePassword');

    if (togglePassword.checked) {
        passwordField.type = 'text';
    } else {
        passwordField.type = 'password';
    }
}


function ToggleDeleteDialog(deleteRoute, csrfToken) {
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteDialog'));
    deleteModal.toggle();

    document.getElementById('deleteConfirm').addEventListener('click', () => {
        fetch(deleteRoute, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
        })
            .then(response => location.reload())
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error));

        deleteModal.toggle();
    });
}
