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
        if (response.ok) {
          console.log("User Logged In");
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
        <input class="form-check-input" type="checkbox" id="is_blogger" checked>
        <label class="form-check-label" for="is_blogger">Register as a DevBlogger?</label>
      </div>
    </div>
    <div class="col mt-3">
      <label for="username" class="form-label">Username</label>
      <input type="text" class="form-control form-control-sm" id="username">
    </div>
    <div class="col mt-3">
      <label for="fullname" class="form-label">Fullname</label>
      <input type="text" class="form-control form-control-sm" id="fullname">
    </div> 
    <div class="col mt-3">
      <label for="email" class="form-label">Email address</label>
      <input type="email" class="form-control form-control-sm" id="email">
    </div>
    <div class="col mt-3">
      <label for="password" class="form-label">Password</label>
      <input type="password" class="form-control form-control-sm" id="password">
    </div>
    <div class="col mt-3">
      <label for="profileimage" class="form-label">Profile image(URL)</label>
      <input type="text" class="form-control form-control-sm" id="profileimage">
    </div>
  </div>`;

  $(".body").append(form);

  $(".auth-register").on("click", function () {
    const is_blogger = $("#is_blogger").prop("checked");
    const username = $("#username").val();
    const fullname = $("#fullname").val();
    const email = $("#email").val();
    const password = $("#password").val();
    const profile_image = $("#profileimage").val();
    console.log(fullname, email, password, profile_image);
    postData("post-user/", {
      is_blogger: is_blogger,
      username: username,
      full_name: fullname,
      email: email,
      password: password,
      profile_image: profile_image,
    }).then((response) => {
      if (response.ok) {
        console.log("account created");
      }
    });
  });
};
