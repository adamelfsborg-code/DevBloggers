

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
