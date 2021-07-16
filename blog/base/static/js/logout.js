const logout = () => {
  const userid = $(".userid").attr("id");
  if (userid) {
    postData("/profile/logout-user/", {
      id: userid,
    }).then((response) => {
      window.location.href = "/";
    });
  }
};
