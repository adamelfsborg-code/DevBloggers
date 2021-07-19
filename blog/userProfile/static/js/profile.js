$("#username").focusout(function () {
  const username = $("#username").val();
  if (username !== $("input.username").attr("id")) {
    validate(
      "/auth/check-if-username-exists/",
      { username: username },
      "username",
      "Username",
      "Username does already exists"
    );
  }
});

$("#email").focusout(function () {
  const email = $("#email").val();
  if (email !== $("input.email").attr("id")) {
    validate(
      "/auth/check-if-email-exists/",
      { email: email },
      "email",
      "Email address",
      "Email does already exists"
    );
  }
});

$("#password").focusout(function () {
  const password = $("#password").val();
  validatePwd("/auth/validate-password/", password);
});

$(".save-profile-changes").on("click", function () {
  const password = $("#current_password").val();
  const id = $(".userid").attr("id");

  const isValid = $(".edit-profile").find(".text-danger");

  var isCorrectPassword;
  postData("/auth/check-correct-password/", {
    id: id,
    password: password,
  }).then((response) => {
    if (response === "200") {
      const username = $("#username").val();
      const fullname = $("#fullname").val();
      const email = $("#email").val();
      const newPassword = $("#password").val();
      const profileImage = $("#profile_image").val();
      const isblogger = $(".isblogger").attr("id");
      if (isValid.length === 0) {
        editProfile(
          id,
          newPassword,
          username,
          fullname,
          email,
          profileImage,
          isblogger
        );
      } else {
        showMessage("notvalid", "Not valid. Fix it and try again.");
      }
    } else {
      console.log(isCorrectPassword);
      showMessage("notvalid", "Current Password is incorrect.");
    }
  });
});

const editProfile = (
  id,
  newPassword,
  username,
  fullname,
  email,
  profileImage,
  isblogger
) => {
  postData("/auth/post-user/", {
    id: id,
    username: username,
    full_name: fullname,
    email: email,
    password: newPassword,
    profile_image: profileImage,
    is_blogger: isblogger,
  }).then((response) => {
    if (response === "Account Created") {
      showMessage("success", "Account updated");
    } else {
      showMessage("error", "Account not updated");
    }
  });
};
