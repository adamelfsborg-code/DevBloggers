const showMessage = (type, body) => {
  $("#showmessage-body").removeClass("text-success text-danger");

  if (type === "success") {
    $("#showmessage-body").addClass("text-success");
  } else if (type === "notvalid") {
    $("#showmessage-body").addClass("text-danger");
  } else if (type === "info") {
    $("#showmessage-body").addClass("text-primary");
  } else {
    $("#showmessage-body").addClass("text-warning");
  }
  $("#showmessage-body").html("");
  $("#showmessage-body").html(body);
  $("#showmessagemodal").modal("show");
};
