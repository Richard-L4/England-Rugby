document.addEventListener("DOMContentLoaded", () => {
  // --- Utility: get CSRF token from cookie ---
  const getCookie = (name) => {
    const cookies = document.cookie.split(";");
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + "=")) {
        return decodeURIComponent(cookie.substring(name.length + 1));
      }
    }
    return "";
  };

document.querySelectorAll(".like-btn, .dislike-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    if (btn.disabled) return;  // ignore if already in progress
    btn.disabled = true;

    const url = btn.dataset.url;
    const comment = btn.closest(".comment");

    fetch(url, {
      method: "POST",
      headers: { "X-CSRFToken": getCookie("csrftoken") },
      credentials: "same-origin",
    })
      .then((res) => res.json())
      .then((data) => {
        comment.querySelector(".like-count").textContent = data.likes;
        comment.querySelector(".dislike-count").textContent = data.dislikes;
      })
      .catch(console.error)
      .finally(() => {
        btn.disabled = false;
      });
  });
});

});
