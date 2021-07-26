$(document).on("ready", function () {
  $("#search")
    .on("input", function () {
      if ($(this).val().length >= 3) {
        getSearchData($(this).val());
      } else {
        resetSearchData();
      }
    })
    .on("change", function () {
      if ($(this).val().length >= 3) {
        getSearchData($(this).val());
      } else {
        resetSearchData();
      }
    });
});

const resetSearchData = () => {
  const bloggers = $(".bloggers-group").hasClass("d-none");
  if (!bloggers) {
    $(".bloggers-group").addClass("d-none");
  }
  const categories = $(".categories-group").hasClass("d-none");
  if (!categories) {
    $(".categories-group").addClass("d-none");
  }
  const articles = $(".articles-group").hasClass("d-none");
  if (!articles) {
    $(".articles-group").addClass("d-none");
  }
};

const getSearchData = async (param) => {
  const [bloggersData, bloggersError] = await getBloggersData(param);
  if (!bloggersError) {
    drawBloggersData(bloggersData);
  } else {
    $(".bloggers-group").addClass("d-none");
  }
  const [categoriesData, categoriesError] = await getCategoriesData(param);
  if (!categoriesError) {
    drawCategoriesData(categoriesData);
  } else {
    $(".categories-group").addClass("d-none");
  }
  const [articlesData, articlesError] = await getArticlesData(param);
  if (!articlesError) {
    drawArticlesData(articlesData);
  } else {
    $(".articles-group").addClass("d-none");
  }
};

const getBloggersData = async (param) => {
  try {
    const data = await postData("/get-bloggers/", {
      param: param.toLowerCase(),
    });
    if (data.msg !== "no items") {
      return [data.items, null];
    }
    return [null, true];
  } catch (error) {
    return [null, error];
  }
};

const getCategoriesData = async (param) => {
  try {
    const data = await postData("/get-categories/", {
      param: param.toLowerCase(),
    });
    return [data.items, null];
  } catch (error) {
    return [null, error];
  }
};

const getArticlesData = async (param) => {
  try {
    const data = await postData("/get-articles/", {
      param: param.toLowerCase(),
    });
    return [data.items, null];
  } catch (error) {
    return [null, error];
  }
};

const drawBloggersData = async (data) => {
  $(".bloggers").empty();
  var bloggers = [];
  if (data !== undefined) {
    $.each(data, function (key, val) {
      bloggers.push(`
        <div class="blogger_item" id=${val.id}>
            <img src="${val.profile_image}" />
            <div>
                <strong>${val.username}</strong>
                <span>${val.fullname}</span>
            </div>
        </div>
        `);
    });
    $(".bloggers-group").find(".bloggers").append(bloggers.join(""));
    $(".bloggers-group").removeClass("d-none");
  } else {
    $(".bloggers-group").addClass("d-none");
  }
};

const drawCategoriesData = async (data) => {
  $(".categories").empty();
  var categories = [];
  if (data !== undefined) {
    $.each(data, function (key, val) {
      categories.push(`
        <div class="category_item" id=${val.id}>
            <i class="${val.icon}"></i>
            <div>
                <strong>${val.name}</strong>
            </div>
        </div>
      `);
    });
    $(".categories-group").find(".categories").append(categories.join(""));
    $(".categories-group").removeClass("d-none");
  } else {
    $(".categories-group").addClass("d-none");
  }
};

const drawArticlesData = async (data) => {
  $(".articles").empty();
  var articles = [];
  if (data !== undefined) {
    $.each(data, function (key, val) {
      articles.push(`
            <div class="article_item" id=${val.id}>
                <strong>${val.name}</strong>
                <div>
                    <span id=${val.user_id} >${val.username}</span>
                    <span>${val.publish_date}</span>
                </div>
            </div>
          `);
    });
    $(".articles-group").find(".articles").append(articles.join(""));
    $(".articles-group").removeClass("d-none");
  } else {
    $(".articles-group").addClass("d-none");
  }
};
