$("#category_name").on("input", function () {
  $(".category-card").find("span").html($(this).val());
});

$("#category_icon").on("change", function () {
  console.log($(this).val());
  $(".category-card")
    .find(".icon")
    .html(`<i class="${$(this).val()}"></i>`);
});

$("#background_color").on("input", function () {
  $(".category-card").css("backgroundColor", `${$(this).val()}`);
});

$("#text_color").on("input", function () {
  $(".category-card")
    .find("i,span")
    .css("color", `${$(this).val()}`);
});

$("#create_category").on("click", function () {
  const user_id = $(".userid").attr("id");
  const name = $("#category_name").val();
  const icon = $("#category_icon").val();
  const background_color = $("#background_color").val();
  const text_color = $("#text_color").val();
  const id = $(".category_id").attr("id");
  if (user_id) {
    postData("/profile/create-category/", {
      id: id,
      user_id: user_id,
      name: name,
      icon: icon,
      background_color: background_color,
      text_color: text_color,
    }).then((response) => {
      if (response.msg === "Category Created") {
        $(".category_id").attr("id", response.id);
        showMessage("success", response.msg);
        $("#create_category").html("Edit Category");
      } else if (response.msg === "Category Updated") {
        showMessage("success", response.msg);
      } else {
        showMessage("error", response.msg);
      }
    });
  }
});
