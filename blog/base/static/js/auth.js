$(document).on("ready", function () {
  authSwitch();
});

const authSwitch = (val) => {
  switch (val) {
    case 1:
      renderLoginPage();
      break;
    case 2:
      renderRegisterPage();
      break;
    default:
      renderLoginPage();
      break;
  }
};

const renderLoginPage = () => {
  $(".authinformation").empty();

  $(".authinformation")
    .append(
      '<div class="col-12 header"><h4 class="text-center">Login</h4></div>'
    )
    .append('<div class="col-12 body"></div>')
    .append(
      '<div class="col-12 footer d-flex justify-content-between"><button type="button" onclick="authSwitch(2)" class="btn btn-sm btn-outline-primary">Register?</button><button type="button" class="btn btn-sm btn-primary auth-login "  >Login</button></div>'
    );

  const form = `
  <div className="row">
    <div class="col mt-3">
      <label for="email" class="form-label">Email address</label>
      <input type="email" class="form-control form-control-sm" id="email">
    </div>
    <div class="col mt-3">
      <label for="password" class="form-label">Password</label>
      <input type="password" class="form-control form-control-sm" id="password">
    </div>
  </div>`;

  $(".body").append(form);

  $(".auth-login").on("click", function () {
    const email = $("#email").val();
    const password = $("#password").val();

    postData("login-user/", { email: email, password: password }).then(
      (response) => {
        if (response === "Logged in") {
          window.location.href = "/";
        } else {
          showMessage("notvalid", response);
        }
      }
    );
  });
};

const renderRegisterPage = () => {
  $(".authinformation").empty();

  $(".authinformation")
    .append(
      '<div class="col-12 header"><h4 class="text-center" >Register</h4></div>'
    )
    .append('<div class="col-12 body mb-5"></div>')
    .append(
      '<div class="col-12 footer d-flex justify-content-between"><button type="button" onclick="authSwitch(1)" class="btn mr-2 btn-sm btn-outline-primary">Login?</button><button type="button" class="btn btn-sm btn-primary auth-register">Register</button></div>'
    );

  const form = `
  <div className="row">
    <div className="col-12">
      <div class="form-check form-switch mt-3">
        <input class="form-check-input" type="checkbox" id="is_blogger">
        <label class="form-check-label" for="is_blogger">Register as a blogger?</label>
      </div>
    </div>
    <div class="col mt-3">
      <label for="username" class="form-label username">Username</label>
      <input type="text" class="form-control form-control-sm" id="username">
    </div>
    <div class="col mt-3">
      <label for="fullname" class="form-label">Fullname</label>
      <input type="text" class="form-control form-control-sm" id="fullname">
    </div> 
    <div class="col mt-3">
      <label for="email" class="form-label email">Email address</label>
      <input type="email" class="form-control form-control-sm" id="email">
    </div>
    <div class="col mt-3">
      <label for="password" class="form-label password">Password</label>
      <input type="password" class="form-control form-control-sm" id="password">
    </div>
  </div>`;

  $(".body").append(form);

  $("#username").focusout(function () {
    postData("check-if-username-exists/", {
      username: $("#username").val(),
    }).then((response) => {
      $(".col").find(".username").empty();
      if (response === "Username does already exists") {
        $(".col").find(".username").append(response).addClass("text-danger");
      } else {
        $(".col")
          .find(".username")
          .append("Username")
          .removeClass("text-danger");
      }
    });
  });
  $("#email").focusout(function () {
    postData("check-if-email-exists/", {
      email: $("#email").val(),
    }).then((response) => {
      $(".col").find(".email").empty();
      if (response === "Email does already exists") {
        $(".col").find(".email").append(response).addClass("text-danger");
      } else {
        $(".col")
          .find(".email")
          .append("Email address")
          .removeClass("text-danger");
      }
    });
  });

  $("#password").focusout(function () {
    postData("validate-password/", {
      password: $("#password").val(),
    }).then((response) => {
      $(".col").find(".password").empty();
      if (response.is_valid !== true) {
        $(".col")
          .find(".password")
          .append(response.arg)
          .addClass("text-danger");
      } else {
        $(".col")
          .find(".password")
          .append("Password")
          .removeClass("text-danger");
      }
    });
  });

  $(".auth-register").on("click", function () {
    const is_blogger = $("#is_blogger").prop("checked");
    const username = $("#username").val();
    const fullname = $("#fullname").val();
    const email = $("#email").val();
    const password = $("#password").val();

    const isValid = $(".authinformation").find(".text-danger");
    if (isValid.length === 0) {
      postData("post-user/", {
        is_blogger: is_blogger,
        username: username,
        full_name: fullname,
        email: email,
        password: password,
      }).then((response) => {
        if (response === "Account Created") {
          showMessage("success", response);
          clearForms();
          authSwitch(1);
        } else {
          showMessage("error", response);
        }
      });
    } else {
      showMessage("notvalid", "Not valid. Fix it and try again :)");
    }
  });
};

function clearForms() {
  $(":input")
    .not(":button, :submit, :reset, :hidden, :checkbox, :radio")
    .val("");
  $(":checkbox, :radio").prop("checked", false);
}
