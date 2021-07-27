$(document).on("ready", function () {
  const date = getDateInText();
  const user_id = $(".userid").attr("id");
  getHomePageData(date, user_id);
});

const getHomePageData = async (date, user_id) => {
  const [categoriesData, categoriesError] = await getTrendingCategories(date);
  if (!categoriesError) {
    await drawTrendingCategories(categoriesData);
  }
  const [articlesData, articlesError] = await getTrendingArticles(date);
  if (!articlesError) {
    await drawTrendingArticles(articlesData);
  }
  const [visitsData, visitsError] = await getLastVisits(date, user_id);
  if (!visitsError) {
    await drawLastVisits(visitsData);
  }
};

const getTrendingCategories = async (date) => {
  try {
    const data = await postData("/get-trending-categories/", {
      date: date,
    });
    return [data.items, null];
  } catch (error) {
    return [null, error];
  }
};

const getTrendingArticles = async (date) => {
  try {
    const data = await postData("/get-trending-articles/", {
      date: date,
    });
    return [data.items, null];
  } catch (error) {
    return [null, error];
  }
};

const getLastVisits = async (date, user_id) => {
  try {
    const data = await postData("/get-last-visits/", {
      date: date,
      user_id: user_id,
    });
    return [data.items, null];
  } catch (error) {
    return [null, error];
  }
};

const drawTrendingCategories = async (data) => {
  var categories = [];
  $.each(data, function (key, val) {
    categories.push(
      `
      <div class="category_item" id=${
        val.name
      } onclick="javascript: navigate('/articles/?category=${
        val.name
      }&page=${1}')" >
        <i class="${val.icon}"></i>
        <div>
          <strong>${val.name}</strong>
          <span>
            ${val.count == 1 ? `${val.count} artilce` : `${val.count} artilces`}
          </span>
        </div>
      </div>
      `
    );
  });
  $(".trending-categories").find(".categories").append(categories.join(""));
};

const drawTrendingArticles = async (data) => {
  var articles = [];
  $.each(data, function (key, val) {
    console.log(val);
    articles.push(`
      <div class="article_item" id=${val.id}>
        <i class="${val.icon}"></i>
          <div>
          <strong class=${val.blocks[0].data.level} >
            ${val.blocks[0].type === "header" && `${val.blocks[0].data.text}`}
          </strong>
          <div class="footer" >
            <span>
              ${val.count == 1 ? `${val.count} reader` : `${val.count} readers`}
            </span>
            <small>
              ${val.publish_date}
            </small>
          </div>
        </div>
      </div>
    `);
  });
  $(".trending-articles").find(".articles").append(articles.join(""));
};

const drawLastVisits = async (data) => {
  var visits = [];
  $.each(data, function (key, val) {
    console.log(val);
    visits.push(`
      <div class="visit_item" id=${val.visit_id}>
        <img src=${
          val.profile_image ? `${val.profile_image}` : "/static/img/default.jpg"
        } />
        ${val.is_blogger && '<span class="badge bg-primary">Blogger</span>'}
        <strong>${val.username}</strong>
      </div>
    `);
  });
  $(".last-visits").find(".visits").append(visits.join(""));
};
