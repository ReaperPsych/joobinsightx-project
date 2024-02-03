document.addEventListener("DOMContentLoaded", function() {
    var jobDescriptions = document.querySelectorAll(".job-description");
    var maxCharacters = 150;

    jobDescriptions.forEach(function(description) {
        var text = description.textContent.trim();
        if (text.length > maxCharacters) {
            description.textContent = text.slice(0, maxCharacters) + "...";
        }
    });
});