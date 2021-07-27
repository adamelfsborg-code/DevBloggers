$(document).on("ready", function () {
  let params = new URLSearchParams(document.location.search.substring(1));
  let category = params.get("category");
  let page = params.get("page");
  getArticlesByCategoryData(category, page);
});

let state = {
  artilcesCount: 0,
  articles_limit: 10,
};

const getArticlesByCategoryData = async (category, page) => {
  const [categoryData, categoryError] = await getCategoryBanner(category);
  if (!categoryError) {
    const banner = await drawCategoryBanner(categoryData);
    $(".category_banner").append(banner.join(""));
  }
  const [articlesCountData, articlesCountError] = await getArtilcesCount(
    category
  );
  if (!articlesCountError) {
    await drawPaginationTool(articlesCountData, page);
  }
  const [articlesData, articlesError] = await getArticlesPage(category, page);
  if (articlesError !== "Empty") {
    const page = await drawArticlesPage(articlesData);
    $(".articles").append(page.join(""));
  } else {
    const empty = await drawEmptyPage();
    $(".articles").append(empty.join(""));
  }
};

const getCategoryBanner = async (category) => {
  try {
    const data = await postData("/get-category-by-name/", {
      category: category,
    });
    return [data.items, null];
  } catch (error) {
    return [null, error];
  }
};

const getArtilcesCount = async (category) => {
  try {
    const data = await postData("/get-articles-count/", {
      category: category,
    });
    return [data.items[0].count, null];
  } catch (error) {
    return [null, error];
  }
};

const getArticlesPage = async (category, page) => {
  const offset = (page -= 1) * state.articles_limit;
  try {
    const data = await postData("/get-articles-page/", {
      category: category,
      limit: state.articles_limit,
      offset: offset,
    });
    if (data.msg !== "404") {
      return [data.items, null];
    } else {
      return [null, "Empty"];
    }
  } catch (error) {
    return [null, error];
  }
};

const drawCategoryBanner = async (data) => {
  const category = [];
  await $.each(data, function (key, val) {
    category.push(`
        <div class="banner_item" style="background-color: ${val.background_color}; color: ${val.text_color}">
            <div>
                <i class="${val.icon}"></i>
                <strong>${val.name}</strong>
            </div>
        </div>
    `);
  });
  return category;
};

const drawPaginationTool = async (data, page) => {
  state.artilcesCount = data;
  var newPage = parseInt(page);
  if ((newPage -= 1) === 0) {
    $(".prev-page").addClass("disabled");
  } else {
    $(".prev-page").removeClass("disabled");
  }
  if (state.articles_limit * page >= state.artilcesCount) {
    $(".next-page").addClass("disabled");
  } else {
    $(".next-page").removeClass("disabled");
  }
};

const drawArticlesPage = async (data) => {
  const articles = [];
  await $.each(data, function (key, val) {
    articles.push(`
        <div class="article_item" id=${val.id}>
            <strong>${val.name}</strong>
            <div>
                <span>${val.username}</span>
                <span>${val.publish_date}</span>
            </div>
        </div>
    `);
  });
  return articles;
};

const drawEmptyPage = async () => {
  const empty = [];
  empty.push(`
        <div class="empty_page text-center mb-5 mt-5 text-danger" >
            <h4>No more Content :(</h4>
        </div>
    `);

  return empty;
};

const prevPage = () => {
  let params = new URLSearchParams(document.location.search.substring(1));
  let page = params.get("page");
  let category = params.get("category");
  console.log(page--);
  window.location.href = `/articles/?category=${category}&page=${page--}`;
};

const nextPage = () => {
  let params = new URLSearchParams(document.location.search.substring(1));
  let page = params.get("page");
  let category = params.get("category");
  console.log(page++);
  window.location.href = `/articles/?category=${category}&page=${page++}`;
};
