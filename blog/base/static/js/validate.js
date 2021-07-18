const validate = (url = "", data, type, name, res) => {
  postData(url, data).then((response) => {
    console.log(response);
    $(".col").find(`.${type}`).empty();
    if (response === res) {
      $(".col").find(`.${type}`).append(response).addClass("text-danger");
    } else {
      $(".col").find(`.${type}`).append(`${name}`).removeClass("text-danger");
    }
  });
};

const validatePwd = (url,password) => {
  postData(url, {
    password: password,
  }).then((response) => {
    $(".col").find(".password").empty();
    if (response.is_valid !== true) {
      $(".col").find(".password").append(response.arg).addClass("text-danger");
    } else {
      $(".col").find(".password").append("Password").removeClass("text-danger");
    }
  });
};
