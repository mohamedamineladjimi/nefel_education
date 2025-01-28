document.addEventListener('DOMContentLoaded', function () {
    const likeButtons = document.querySelectorAll('.like-button');
    likeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const likeCountElement = this.previousElementSibling;
            let likeCount = parseInt(likeCountElement.textContent, 10);
            likeCount++;
            likeCountElement.textContent = likeCount;
        });
    });
    const avatarInput = document.getElementById('avatarInput');
    const avatarImage = document.getElementById('avatar');
    const addAvatarLink = document.getElementById('addAvatarLink');
    addAvatarLink.addEventListener('click', function (e) {
        e.preventDefault(); 
        avatarInput.click(); 
    });
    avatarInput.addEventListener('change', function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                avatarImage.src = e.target.result; 
            };
            reader.readAsDataURL(file);
        }
    });
});
