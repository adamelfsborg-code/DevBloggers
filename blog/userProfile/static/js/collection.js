$(document).on("ready", function () {
  const user_id = $(".userid").attr("id");
  getUserCategories(user_id);
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const slide = urlParams.get("slide");
  $(".current_page").attr("id", slide !== null ? slide : 1);
  getDateInText();
  getArticleSlide(user_id);
});

const getArticleSlide = (user_id) => {
  const slide = $(".current_page").attr("id");

  if (slide <= 1) {
    $("#prevslide").hide();
  } else {
    $("#prevslide").show();
  }

  postData(`/profile/get-user-articles/?slide=${slide}`, {
    user_id: user_id,
  }).then((response) => {
    if (response.msg === "200") {
      $(".articles-collection").find(".row").empty();
      $.each(response.items, function (key, val) {
        $(".articles-collection")
          .find(".row")
          .append(`<div class="col-12 article-card mb-2" id=${val.id}></div>`);

        $(".articles-collection")
          .find(`.article-card#${val.id}`)
          .append(
            `<div class="headline"><h6>${val.blocks[0].data.text}</h6><span>${val.publish_date}</span></div>`
          )
          .append(
            `<div class="category p-1" ><i class="${val.icon}"></i>${val.name}</div>`
          );

        $(".articles-collection")
          .find(`.article-card#${val.id}`)
          .find(".category")
          .css("backgroundColor", `${val.background_color}`)
          .css("color", `${val.text_color}`);
      });
    } else {
      console.log(response);
    }
  });
};

$(".changeSlide").on("click", function () {
  const user_id = $(".userid").attr("id");
  console.log($(this).attr("id"));
  $(".current_page").attr("id", $(this).attr("id"));
  getArticleSlide(user_id);
});

const nextSlide = () => {
  const user_id = $(".userid").attr("id");
  var current_slide = $(".current_page").attr("id");
  current_slide++;
  $(".current_page").attr("id", current_slide);
  getArticleSlide(user_id);
};

const prevSlide = () => {
  const user_id = $(".userid").attr("id");
  var current_slide = $(".current_page").attr("id");
  current_slide--;
  $(".current_page").attr("id", current_slide);
  getArticleSlide(user_id);
};

const getUserCategories = (user_id) => {
  if (user_id) {
    postData("/profile/get-user-categories/", {
      user_id: user_id,
    }).then((response) => {
      if (response.msg === "200") {
        $.each(response.items, function (key, val) {
          $(".categories-collection")
            .find(".grid-container")
            .append(`<div class="category-card" id=${val.id}></div>`);
          $(`.category-card#${val.id}`)
            .append(`<div class="icon"><i class="${val.icon}"></i></div>`)
            .append(`<span>${val.name}</span>`);
          $(`.category-card#${val.id}`)
            .css("backgroundColor", `${val.background_color}`)
            .css("color", `${val.text_color}`);
        });
      }
    });
  }
};

const getUserArticles = (user_id) => {
  if (user_id) {
    postData("/profile/get-user-articles/", {
      user_id: user_id,
    }).then((response) => {});
  }
};
