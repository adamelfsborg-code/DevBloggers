$(document).on("ready", function () {
  getHomePageData();
});

const getHomePageData = async () => {
  const [data, error] = await getTrendingCategories();
  if (!error) {
    await drawTrendingCategories(data);
  }
};

const getTrendingCategories = async () => {
  try {
    const data = await getData("/get-trending-categories/");
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
      <div class="category_item" id=${val.name}>
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
