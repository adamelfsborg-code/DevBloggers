const logout = () => {
  const userid = $(".userid").attr("id");
  if (userid) {
    postData("auth/logout-user/", {
      id: userid,
    }).then((response) => {
      window.location.href = "/";
    });
  }
};
