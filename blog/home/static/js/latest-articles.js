$(document).on("ready", function () {
  getLatestArticlesData();
  $("#followers_only").on("change", function () {
    const followersOnly = $("#followers_only:checked").length > 0;
    getLatestArticlesData(followersOnly);
  });
});

const getLatestArticlesData = async (followersOnly = false) => {
  const [latestArticlesData, latestArticlesError] = await getLatestArticles(
    followersOnly
  );
  if (!latestArticlesError) {
    drawLatestArticlesData(latestArticlesData);
  } else {
    $(".latest-articles").empty();
    
  }
};

const getLatestArticles = async (followersOnly) => {
  try {
    const data = await postData("/get-latest-articles/", {
      followersOnly: followersOnly,
      user_id: $(".userid").attr("id"),
    });
    if (data.msg !== "no items") {
      return [data.items, null];
    }
    return [null, true];
  } catch (error) {
    return [null, error];
  }
};

const drawLatestArticlesData = async (data) => {
  $(".latest-articles").empty();
  var latestArticles = [];
  $.each(data, function (key, val) {
    latestArticles.push(`
        <div class="latest_article_item" id=${val.id}>
            <strong>${val.name}</strong>
            <div>
                <span id=${val.user_id}>${val.username}</span>
                <span>${val.publish_date}</span>
            </div>
        </div>
    `);
  });
  $(".latest-articles").append(latestArticles.join(""));
};
