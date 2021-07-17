const ImageTool = window.ImageTool;

$(document).on("ready", function () {
  $("#upload_article").html("Upload Article");
  const user_id = $(".userid").attr("id");
  getCategories(user_id);
});

const getCategories = (id) => {
  postData("/profile/get-user-categories/", {
    user_id: id,
  }).then((response) => {
    if (response.msg === "200") {
      $("#category").prepend(
        '<option value="0" disabled selected >Select Category</option>'
      );
      $.each(response.items, function (key, val) {
        $("#category").append(`<option value=${val.id}>${val.name}</option>`);
      });
    } else {
      showMessage("error", response.msg);
    }
  });
};

const editor = new EditorJS({
  tools: {
    header: Header,
    raw: RawTool,
    image: SimpleImage,
    table: Table,

    quote: {
      class: Quote,
      inlineToolbar: true,
      shortcut: "CMD+SHIFT+O",
      config: {
        quotePlaceholder: "Enter a quote",
        captionPlaceholder: "Quote's author",
      },
    },

    checklist: {
      class: Checklist,
      inlineToolbar: true,
    },
    list: {
      class: List,
      inlineToolbar: true,
    },
  },
  autofocus: true,
});

$("#upload_article").on("click", function () {
  const date = getDateInText();
  const user_id = $(".userid").attr("id");
  const article_id = $(".codex-editor").attr("id");
  const category_id = $("#category").val();
  if (user_id && category_id != 0) {
    editor
      .save()
      .then((outputData) => {
        postData("/profile/upload-article/", {
          blocks: outputData.blocks,
          publish_date: date,
          user_id: user_id,
          article_id: article_id,
          category_id: category_id,
        }).then((response) => {
          if (response.msg === "Article Uploaded") {
            $(".codex-editor").attr("id", response.id);
            showMessage("success", response.msg);
            $("#upload_article").html("Update Article");
            $("#reset_addarticle").removeClass("d-none");
          } else if (response.msg === "Article Updated") {
            showMessage("success", response.msg);
          } else {
            showMessage("error", response.msg);
          }
        });
      })
      .catch((error) => {
        console.log("Saving failed: ", error);
      });
  } else {
    showMessage(
      "notvalid",
      "Not valid. Make sure you have selected a category."
    );
  }
});

$("#reset_addarticle").on("click", function () {
  window.location.reload();
});
